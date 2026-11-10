# Automated wargaming: deep document

*Subfield E12.07. Simulated evaluation of plans: test a plan by running it against a simulated opponent and world, then read the result. Sources: evidence_a-d.jsonl, claims.jsonl (K01-K25), critique.md in this folder. Status marks as in SCHEMA.md: [E] established, [S] single-source, [C] contested. Evidence ids a01-d15 refer to the jsonl files.*

*Honest summary up front: almost all evidence is 2023-2026 LLM work, small N per cell (10-20 runs), author-built scenarios. The only human expert baseline is Lamparth 2024. The Cranfield/AIAA studies named in the subfield row were never read (HTTP 403), so no numbers exist for them. Only COA-GPT tests whether run-then-revise improves a plan against a real score.*

## 1. What it is

Automated wargaming means a machine plays some or all of the roles in a wargame: the players (blue, red), the controller or adjudicator who decides what happens, and the world. The aim for planners is to test a plan by running it, many times and cheaply, instead of convening a staff for days.

Three technical families exist.

1. **Rule-based or search-based automation.** Game theory, expert systems (RAND Strategy Assessment System, 1980s), search (MCTS), reinforcement learning (RL) with hierarchical agents. Strong where rules are rigid and results are checkable. Weak at open-ended, qualitative scenarios. (a10, a19, a20)
2. **LLM-driven simulation.** Language models play nations, teams or commanders in text, and often also write the consequences. Examples: Snow Globe, Rivera's escalation sim, WarAgent, Lamparth's Taiwan Strait game, Payne's nuclear-crisis tournament. (a01, a06, a10, a16, c16)
3. **Hybrid generate-then-run.** An LLM proposes plans (courses of action, COAs). A real simulator or rule engine scores them. COA-GPT and CADET are the cases. (a13, b15)

Matlin et al. (2026) sort the field into four quadrants by how open the player and the adjudicator are: Q-I both rule-based (chess, Go, StarCraft); Q-IV both open-ended (real serious wargames); Q-III language-rich but rule-resolved (many Diplomacy evaluations). Of 223 papers, only 20 (9%) give a language model both open roles. Validity of an LLM adjudicator is essentially untested. (a18, a19, b20)

For our agent the relevant question is narrow: can "test by running" (state S4 TEST, operator O6 in the schema) use a simulated opponent or simulated outcome, and when is that simulation trustworthy enough to move a decision? The evidence says: sometimes for comparing options, rarely for absolute prediction, and only with an external check that is not the same model's opinion.

## 2. History and theories in depth

**RAND 1950s.** Emery (2021) describes two RAND Cold War Games. The Mathematics Analysis Division version (1954-55, two weeks, 19 countries) was formal and quantified; players opened with H-bomb exchanges and the game ended in atomic war in the final round. The Social Science Division version (4 plays, Feb 1955 to Apr 1956; round 4 had 13 team members) was free-play with area experts and never went nuclear. Pauly's MIT study: 26 games 1958-72, only 2 crossed the nuclear threshold; 64.9% of 77 participants reported extreme or intense emotional involvement. Reading: formal, tabulated losses made nuclear use look cheap; free play with emotion kept it costly. (a09) Caution: the MAD game was a mathematical paper game, not a computer program. Rivera and Lamparth cite Emery for "computer models gave more rational play but more nuclear use". That reading is second-hand and loose. Status [C] (K18). Do not cite as hard evidence.

**RAND RSAS (1980s)** ran wargames with expert-system AI players. Known only from citation in Snow Globe; not read. (c28)

**Early planning aids.** CADET (Kott et al., 2016) turned a high-level COA into a detailed wargamed plan and synchronization matrix. Blind test: 5 brigade-level scenarios, 4 product types, 20 packages, 9 field-grade judges each grading 4 packages. Mean 4.2 (CADET) vs 4.4 (human staff), SD about 2.0; when judges knew which was which, 4.4 vs 3.9. Effort: under 2 minutes plus about 20 minutes editing, about 0.4 person-hours vs 16. A Battle Lab trial with two 8-officer teams found aided planning matched manual quality and was faster. Judges did not mark computer-looking products down. (b15, b16, b17)

**Cranfield and AIAA line.** Yuksek et al. (2023) propose an MDMP-based approach rating a plan by operational success and asset survivability, with automated agents and a fleet composer algorithm. Schwartz et al. (2020, SPIE) describe a tool that takes friendly and enemy COAs, proposes changes, and runs the DAVINCI combat simulation to evaluate each change. Both are search-summary only; no numbers. (b22, b23, d11, a26)

**RL era.** Black and Darken (2023): hierarchical RL agents. A multi-model framework with several state abstractions beat the best single model by 62.6%, even when added models were worse abstractions. Preliminary, 1,000 games, 10x10 board, 30 phases. Mean scores: scripted 813.750 (sd 6.253), RL-global 1095.601 (sd 62.972), RL-local 7x7 1070.512 (sd 24.992). (a20)

**Diplomacy line.** CICERO (Meta FAIR 2022) pairs a language model with a planning engine; Diplodocus (Bakhtin 2022) regularizes RL toward a human-imitation policy (abstract only: 200-game tournament, 62 humans, two Diplodocus agents first and third on Elo). Neither was opened. (a22, a23) Welfare Diplomacy (Mukobi 2023) shows LLM agents reach high welfare by mutual demilitarising but one scripted defector exploits them. (b12, d09) Richelieu (Guan 2024) adds memory, reflection, forward simulation, self-play; it beat AutoGPT agents far more often (win 9.10% vs 1.63%) but against Cicero was only marginally better (win about 0.7% higher; authors say not significant). (c26, c27)

**LLM wargaming wave, 2023-2026.** Hua et al. WarAgent (WWI/WWII/Warring States), Rivera et al. escalation, Lamparth et al. human comparison, Hogan and Brennen Snow Globe, Goecks and Waytowich COA-GPT, Shrivastava et al. inconsistency, Elbaum and Panter escalation control, Jensen et al. CFPD benchmark, Payne 2026 nuclear tournament, Matlin 2026 review, Riedl and Matlin 2026 position paper. Detail in sections 3 to 6.

**Theories competing in the field.**
- *Hallucination as feature* (Snow Globe): plausible invention of consequences is the point of open-ended adjudication. Authors report failures as repeated output and drift from stated plans. This conflicts with our G3/G8 (grounded, checked outcomes). (a12)
- *Stress test, not oracle* (Riedl and Matlin): LM wargames should be treated as stress tests of the model, not safe previews of real conflict. Five failure modes: decision laundering, adjudication opacity, role collapse, escalation-through-adjudication, failure of strategic imagination. Argument only. (b21)
- *Escalation is a model artefact* (Elbaum and Panter vs Rivera): escalation moves with sampling and reflection prompts, so it reflects settings as well as "what LLMs do". (b18, c15)
- *Recall confound* (Hua): matching history may be recall, not simulation. (a16, a17)

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| LLM teams match human experts on only about half of 21 action frequencies, and fewer with newer models | Humans 214 experts, 48 teams; matches 16/21 (GPT-3.5), 10/21 (GPT-4), 9/21 (GPT-4o); LLM arm 80 games per configuration | Lamparth 2024 (a01, b05, c08) | [S] K01 |
| Scenario-variable effects mostly agree in direction between LLM and humans, with exceptions | China posture: effect in humans and all LLMs; AI accuracy: none anywhere; crew training: none in humans, effect in GPT-4 and GPT-4o | Lamparth 2024 (a02, c09) | [S] K02 |
| Simulated team dialog is shallow ("farcical harmony") and shifts aggressiveness and action count | about 350 words per chunk, 1050 words per move used | Lamparth 2024 (a03, b07, c10) | [S] K03 |
| Background persona labels do nothing in a menu game; goal-stating hawk/dove personas change outcomes in free text | Lamparth: no significant effect, 3 models, both moves. Snow Globe armed conflict in 20 runs: dove-dove 1/20, dove-hawk 4/20, hawk-hawk 14/20 | a04, a11, b09 | [C] K04 |
| All tested LLM nation agents escalate; none showed significant de-escalation; level depends on model | 10 runs x 8 nations per cell, 3 scenarios, 14 days, 27 actions. GPT-3.5 neutral 10.15 to 26.02 (+256%). Table 2 ranges: GPT-4 9.8-11.8, GPT-3.5 17.8-21.9, Claude-2.0 3.4-6.7, Llama-2 4.4-5.8, GPT-4-Base 17.6-20.0. Nuclear share: GPT-4-Base 6.7-7.1%, GPT-3.5 0.13-0.21%, GPT-4 and Claude 0% | Rivera 2024 (a06, a07, b01, b02) | [E] K05 |
| Escalation comes as heavy-tailed spikes | Some GPT-3.5/GPT-4 runs rose more than 50% in one turn; military capacity rose steadily in all models | a06, b03, c07 | [S] K08 |
| Rivera's eight prompt variants mostly did not change escalation | 10 sims per group, 8 agents; most differences not significant | b04 | part of [C] K06 |
| Escalation falls with lower temperature and reflection prompts (Mistral-7B) | 10 runs each, 14 days: T 1.0 to 0.5 -38%, to 0.01 -48%; planning reflection -28%; de-escalation reflection -57%; final-day -40% and -42% | Elbaum and Panter 2025 (b18, c15) | [C] K06 |
| Free-form crisis answers are inconsistent across samples; rewording moves answers as much as temperature | 5 models, 20 samples, 20 simulations per model/experiment; rewording at T=0 about as inconsistent as T=0.2; meaning-changing edits about T=0.6-0.8; 0.25 or more counts as semantic variation | Shrivastava 2024 (a14, a15, b19, c21, c22) | [S] K07 |
| Generate-then-run with a real score works in one game | 5 COAs x 10 sims = 50 rollouts per variant; beat RL baselines on mean reward; best variant 3.4% below one human expert (15 trials); RL needed 112 thousand battles (70M timesteps, 35 workers) | COA-GPT (a13, b11, c04, c05) | [S] K09 |
| Staged domain prompt multiplies win rate against harder opponents | Prompt 1 vs 2: L1 87.5 vs 100; L2 66.7 vs 100; L3 25 vs 100; L4 12.5 vs 84; L5 0 vs 50; L6 0 vs 8.3 | Ma 2024 (c24) | [S] K10 |
| Selecting by measured outcome beats using all attempts | Fine-tune on wins from top 25% by utilisation 54/100 vs full data 28/100 | Ma 2024 (c25) | [S] K19 |
| Same-model opposing sides are not independent adversaries | One scripted exploiter beats LLM Diplomacy players; no de-escalation option chosen in 21 games/329 turns (8 options, -5 to -95); Richelieu gain over Cicero not significant | b12, c16, c27, d09 | [E] K11 |
| Verdicts depend on framing | Deadline: Claude 100% to 33% win, GPT-5.2 0% to 75%; GPT-5.2 median escalation 175 to 900; tactical nuclear line crossed in 17% of open games vs 100% of deadline games; CFPD actor swap changes advice (less escalatory for China/Russia than US/UK, all 7 models) | Payne 2026 (c17), Jensen 2025 (c19, c20) | [E] K12 |
| Historical-match tests are confounded by recall | De-anonymised WWI: alliance 97.43%, mobilisation 100%, war declaration 13-19%; war in every run, also after counterfactual fine-tuning (108 points, 3 epochs) | Hua 2024 (a16, a17, b13, c12-c14) | [S] K13 |
| Stated reasoning is a poor record of cause | Stated signals matched later actions about 70%; one model acted more aggressively than announced in 70% of mid and 60% of high-level moves | Payne 2026 (c18), Rivera (a08) | [E] K14 |
| LLM adjudicator validity is untested | 20 of 223 papers (9%) give LMs both roles; 17 of 223 (7.6%) under stricter filter; 4 of 63 (6.3%) core military | Matlin 2026 (a18, b20) | [E] K15 |
| LLMs lose to plain search on exact games | NRA -1 against MCTS in Tic-Tac-Toe, Connect-4, Breakthrough, Nim, all LLMs and reasoning methods; all beat random | GTBench (b14) | [S] K16 |
| Plan generation plus wargaming matches staff at far less effort | 4.2 vs 4.4, 9 judges, 20 packages; 0.4 vs 16 person-hours | CADET (b15) | [S] K17 |
| Self-revision without external signal does not help | Llama-2 GSM8K 62.0 to 43.5 then 36.5; CommonSenseQA 64.0 to 37.5; GPT-4-Turbo flat or down (GSM8K 91.5 to 88.0-91.0) | Huang 2024 (d01), CRITIC (d05) | [E] K21 |
| More samples help only with an exact check | SWE-bench Lite 15.9% to 56% at 250 samples; CodeContests Gemma-2B 0.02% to 7.1% at 10,000; MATH majority vote 40.50% to 41.41% from 100 to 10,000; adaptive allocation over 4x efficiency | Brown 2024, Snell 2024 (d03, d04) | [E] K22 |
| LLM judges agree with humans over 80% but carry position, verbosity, self-enhancement bias | over 80% on MT-Bench and Chatbot Arena | Zheng 2023 (d06, d13) | [S] K23 |
| Personas do not add factual accuracy and explain little variance | 162 personas, 2,410 questions, 4 model families, no gain; persona variance under 10% | Zheng 2024, Hu and Collier 2024 (d07, d08) | [S] K24 |
| Mixed-family debate beats same-family debate, no equal-call baseline | GSM-8K 91% (Gemini-Pro, Mixtral 8x7B, PaLM 2-M) vs 80-82% for three Gemini-Pro copies; singles 78, 64, 70 | Hegazy 2024 (d10) | [S] K25 |
| Debate gain equals majority voting at equal responses | GSM8K gpt-3.5: standard 76.7; self-consistency 82.5 (3), 85.3 (6), 88.2 (9); debate round 2 83.2 at 6 responses | Huang 2024 (d02) | [E] with G9 |

Note on derived ratios: "about 33% as often" for GPT-4-Base nuclear strikes (2.48 vs 7.38 messages) is a derived ratio, not reported. Payne tactical-nuclear table is column-garbled in text; only Claude 86% is confirmed from prose. The 79% (Gemini) and 64% (GPT-5.2) figures are likely, unverified. The 21 Payne games include a seventh match of a model against a copy of itself.

## 4. Mechanisms and models

Each mechanism is written so it can be built.

**4.1 Generate-then-run loop (COA-GPT).** Inputs: mission text, doctrine excerpts, optional image. The LLM writes several named COAs in one call. Code translates each into simulator commands and runs it (10 rollouts per COA). Code reads the simulator's reward (friendly and enemy losses, objectives). A human may give feedback (1 to 2 rounds), and the LLM revises. Selection is by simulator score, never by the LLM. Observed: feedback raised mean and cut variance. Failure: one command at the start, low control resolution, high friendly casualties. Build: `plans = gen(task); scores = [mean(run(p) for _ in range(10)) for p in plans]; best = argmax`. Needs an executable simulator. (a13, c04, c05)

**4.2 Multi-agent LLM wargame (Rivera).** Eight nation agents, one model per run; each turn each agent picks from 27 actions in six severity classes (de-escalation, status quo, posturing, non-violent escalation, violent escalation, nuclear) with an optional message. A separate world-model LLM writes consequences. Code scores escalation by fixed weights. Agents were not told it is a simulation. Bootstrap CIs over 10 runs. Independence flaw: nations in one run share a model and world state. Build the scoring in code; log per-turn score and flag spikes above 50% in one turn. (a06, a25)

**4.3 Controlled human-vs-LLM comparison (Lamparth).** Same fictional scenario, 2 moves, 21 actions, treatment factors (AI weapon accuracy, crew training, China posture). For each action, compare frequency in human teams and LLM teams with bootstrap CIs; count how many match. Use treatment-effect significance patterns as a second validity test. This is the cheap way to validate any simulator: does it move the same way as humans when one factor changes? (a01, a02)

**4.4 Open-ended adjudication (Snow Globe).** Roles: players with personas, a controller/adjudicator agent, optional human seats. Each of 3 persona combinations was run 20 times with one one-year move. "Include unexpected consequences" makes the adjudicator add events nobody ordered. Known faults: repeated output across moves, drift from stated plans. Code check: parse the plan's stated actions and verify the adjudicated outcome references them; count drift rate. (a10, a12)

**4.5 Counterfactual sensitivity check (WarAgent).** De-anonymise or anonymise countries; change one key fact; require the outcome to change. If war breaks out in every run regardless, the simulator cannot tell plans apart. Seven runs per setting, round 6 evaluation, Jaccard overlap to history for alliances, declarations, mobilisation. Each country has a secretary agent that checks proposed actions for format and logical consistency, a simple code-plus-LLM validity gate. (a16, c12)

**4.6 Inconsistency metric (Shrivastava).** Sample 20 responses at T about 1.0, embed with BERTScore (DeBERTa-xlarge-MNLI), compute 1 minus rescaled F1 over all unique pairs, average. Calibrate with ablations: lexical 0.08, syntactic 0.17, semantic shift 0.37; 0.25 or more counts as semantic variation. Use as a stability gate on a plan verdict: if spread is above 0.25, do not trust one sample. (a14)

**4.7 Escalation control (Elbaum and Panter).** Run the same scenario at T=1, 0.5, 0.01 and with an added reflection slot ("consider the planning" or "consider de-escalation") before each action. Compare the escalation score. Caution: a de-escalation reflection also tells the agent what answer is wanted, so it may reduce validity as well as bias. (b18, critique gap 10)

**4.8 External-signal revision (CRITIC).** Critique then revise, but with a tool that returns real output (code interpreter, search, scorer). Without the tool the gain disappears. Build: revision step may only fire on a tool-returned failure. (d05, d01)

**4.9 Staged domain prompt (Ma).** Prompt 2 asks for situation overview, analysis, planning, decision in order. Gain was biggest where plain prompt had a foothold and smallest at the hardest tier (L6 0 to 8.3%). Chain of Summarization compresses single and multi-frame observations before acting. (c23, c24)

**4.10 Multi-view evaluators (Black).** Several state abstractions of the same simulation give diverse cheap evaluators; ensemble beat single best by 62.6%. Works only if views really differ. (a20)

## 5. What holds up

**Replications and agreement between sources**
- Escalation of LLM nation agents: Rivera 2024 (5 models, 3 scenarios) and Payne 2026 (3 frontier models, 21 games) agree directionally. Different designs, so not a direct replication. [E] (K05)
- Same-model opposition is weak: Welfare Diplomacy exploit, Payne's zero de-escalation choices, Richelieu's non-significant self-play gain, Lamparth's farcical harmony. Three independent lines. [E] (K11)
- Verdicts flip with framing: Payne deadline, CFPD actor swap, Shrivastava rewording. [E] (K12)
- Self-revision without external check fails: Huang 2024 plus CRITIC. [E] (K21)
- Exact-check scaling: Large Language Monkeys and Snell agree. [E] (K22)

**Failures and contradictions**
- Persona effect: Lamparth null (menu game, background text) vs Snow Globe effect (goal-stating personas, 7B model). Different manipulation types may explain it. Zheng and Hu and Collier support the null for background personas. Goal-stating personas never tested in a wargame across models. [C] (K04)
- Temperature and prompt: Elbaum large effects (Mistral-7B) vs Rivera's own eight prompt variants mostly null (GPT-class). Shrivastava: wording matters as much as temperature. [C] (K06)
- Newer models match humans on fewer actions (16, 10, 9). More capable does not mean more human-like. (a01)
- Historical fidelity: strong match on alliances and mobilisation but weak on war declarations (13-19%), and war broke out in every run. Recall plus bias. (a16)
- Richelieu: large gain over AutoGPT but not significant over Cicero. Gains over weak baselines do not show real strength. (c26, c27)
- Emery claim: thin base, second-hand. [C] (K18)

**Moderators**
- Model: safety-tuned chat models escalate less than base models (GPT-4-Base 6.7-7.1% nuclear vs 0-0.21%).
- Sampling: temperature and reflection (Mistral-7B).
- Framing: deadline pressure reverses winners.
- Dialog length: more simulated dialog raised aggressiveness and total action count.
- Commitment: adding wargame continuations lowered inconsistency for every model. Early choices drive variance. (a15)
- Difficulty: staged prompt gains fell as opponent difficulty rose.

**Interventions that worked**
- Run the plan against a real simulator and score by its output (COA-GPT).
- Select by measured outcome (top-25% fine-tune 54 vs 28).
- Human feedback rounds (higher mean, lower variance).
- External-signal revision (CRITIC), many samples with exact verifier (Brown).
- Lower temperature and reflection (single small model).

**Interventions that did not work**
- Self-critique revision without external signal (Huang).
- Persona labels on a menu game; extreme pacifist or sociopath prompts (Lamparth).
- Debate among copies of one model (equal to voting).
- Rivera's eight prompt variants.
- T=0 as a fix for instability (rewording still moves answers).
- Fine-tuning on counterfactual history to stop the war outcome (Hua).

**Independence caveat.** Bootstrap intervals over runs of 8 nations that share a model and world state are optimistic. (a25, critique)

## 6. Language models

**Behaviour.**
- Escalate by default, with spikes; the base model also uses nuclear options readily. Written justifications cite deterrence and first-strike logic; "A lot of countries have nuclear weapons... We have it! Let's use it." (GPT-4-Base, a07)
- Over-consistent and over-harmonious in simulated teams: p(agg2|agg1) 0.94 to 1.00 across LLMs. (a05, a03)
- Ignore player background in menu games. (a04)
- Across samples: semantically inconsistent in free text for all five models; GPT-4 worst, Claude 3.5 Sonnet and GPT-4o mini least. (a14)
- Actor-name bias: less escalatory advice for China and Russia than US and UK. (c20)
- Frontier 2026 models (GPT-5.2, Claude Sonnet 4, Gemini 3 Flash): all games had nuclear signalling; 95% mutual nuclear signalling; tactical nuclear use 86% for Claude (others likely 79% and 64%, unverified); none of eight de-escalatory options chosen; mildest action "Return to Start Line" 45 times (6.9%). Under a deadline, win rates flipped. Stated signals matched actions about 70%. (c16-c18)
- Lose to plain search (MCTS) in deterministic complete-information games. (b14)
- Hallucinate at adjudication: repeated output, drift from the stated plan. (a12)

**What changed behaviour, and by how much.**
| Lever | Effect |
|---|---|
| Temperature 1.0 to 0.5 / 0.01 (Mistral-7B) | escalation -38% / -48% |
| De-escalation reflection / planning reflection | -57% / -28% |
| Deadline framing (Payne) | Claude 100% to 33% win; GPT-5.2 0% to 75% |
| Safety tuning (Rivera Table 2) | Claude-2.0 3.4-6.7 vs GPT-3.5 17.8-21.9 |
| Simulated dialog length | more aggressive, more actions |
| Staged prompt, StarCraft | L3 25 to 100, L5 0 to 50 |
| Human feedback, COA-GPT | higher mean reward, lower variance |
| Goal-stating personas (7B) | armed conflict 1/20 to 14/20 |
| Mixed-family debate (GSM8K) | 91% vs 80-82% |

**Not demonstrated.** Any LLM adjudicator validated against a human adjudicator. Any 2026 frontier replication of the Rivera or Lamparth protocol. Counterfactual sensitivity across simulators. (K23, d12)

## 7. What our agent should take

Part codes: G guardrail, S state, O operator, M memory.

### Add now (established)

1. **Score a plan by running it, not by the model's opinion; revise only from the tool's real output.** G2, S4/S5, O6. [E] Evidence: d01, d05, d03, a13 (K21, K09 partly). Note: COA-GPT supports the generate-then-run form in one game only; the revise-needs-external-signal part is established.
2. **Same-model simulated opponents and same-model simulated dialog are not independent opposition; do not count their agreement.** G4, G9. [E] Evidence: a03, b12, c16, c27, d02, d09, d13 (K11, K03).
3. **Spend extra samples only where the check is exact or the item is hard; without an exact check, voting plateaus.** G12, O6. [E] Evidence: d03, d04, d12 (K22).
4. **Score verdicts under reframing and actor swaps; treat a flip as "not stable".** G3. [E] Evidence: c17, c19, c20, a14, c22 (K12).
5. **Never take a simulated agent's written reasoning as the cause; compare stated plan with executed action in code.** G10. [E] Evidence: a08, c18 (K14).
6. **Do not treat an LLM as a validated adjudicator of plan outcomes; use code adjudication for any checkable part and flag the rest unvalidated.** G3, G8. [E] Evidence: a18, b20, a12, b10, b21 (K15).
7. **Treat each simulated run as one noisy draw from a heavy-tailed distribution; do not stop at one.** G12. Evidence: a06, b03 (K08 single-source; consistent with item 3 so used as a rule, not as a claim).

### Test first

- Compare options (A vs B) in simulation rather than predicting absolute scores. O6. [S] Evidence: a02, c09 (K02).
- Median or agreement of k simulated verdicts vs one run, at equal tokens, with paraphrase variants. G12. [S] Evidence: a14, c22 (K07, K08).
- Counterfactual sensitivity gate: change one key fact, require the outcome to move. G3. [S] Evidence: a16, a17 (K13).
- Different-model or code-built adversary vs same-model adversary for finding flaws. G4. [S] Evidence: d09, d10 (K11, K25).
- Goal-stating adversary roles vs background personas. G4. [C] Evidence: a04, a11, d07, d08 (K04, K24).
- Reflection slot or lower temperature on the simulated opponent. O6. [C] Evidence: b18, b04 (K06).
- Staged domain prompt for the plan test, with gain tracked per difficulty. S4. [S] Evidence: c24 (K10).
- Select by code-computed score vs random sample. G5. [S] Evidence: c25 (K19).
- Code adjudicator vs LLM adjudicator drift rate. G3. [S] Evidence: a12, d06 (K15, K23).
- Several state abstractions as diverse cheap evaluators. S4/S7. [S] Evidence: a20.
- Memory: store past plan verdicts with their simulator seeds and the tool outputs, not narratives. M. [D] Design choice; no direct evidence.

## 8. Concrete tests on our bench

All arms use equal total tokens (setup counted, G7). Every metric scored against ground truth by code where possible.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Items with an executable checker (ARC-style programs, puzzles with a verifier) | (a) propose once; (b) propose-run-revise from the checker's output; (c) revise from own critique | accuracy vs ground truth | c above a; b at or below a for c (K21); b gains largest where plain pass rate is non-zero |
| T2 | Plan-verdict items with a seeded flaw (plan with a known hidden failure) | simulate k=1, 3, 5, 10 verdicts at equal tokens; median vs single; with and without paraphrase | verdict accuracy and stability (agreement across reruns) | plateau after k about 3-5 without exact check; log-linear only with exact check |
| T3 | Seeded-flaw plans | red-team by (a) same model, (b) other family, (c) rule or code adversary | number of seeded flaws found; false alarms | b and c above a; size unknown |
| T4 | Scenario items with one key fact changeable | verdict before and after the fact flips | share of verdicts that move in the expected direction | at least 80% moves; lower means discard the simulator |
| T5 | Plan pairs with known ranking | simulated A-vs-B ordering vs simulated absolute score | accuracy of order vs accuracy of absolute value | order more accurate (K02) |
| T6 | Same item under 3 framings plus anonymised actors | single run vs 3-framing agreement requirement | flip rate; accuracy of accepted verdicts | agreement gate lowers errors at equal tokens |
| T7 | Items with stated plans and adjudicated outcomes | code check vs LLM adjudicator vs human | drift rate (outcome not following the plan); agreement with human | LLM drift above code drift |
| T8 | Simulated-opponent items | background persona vs goal-stating persona, two model families | behaviour shift and plan accuracy, separately | goal-stating shifts behaviour; accuracy gain unlikely (K24) |
| T9 | Simulated-opponent items | T=1 vs T=0.3 vs reflection slot | plan-verdict accuracy and escalation-like bias | bias down; validity may fall |
| T10 | Mixed difficulty | staged prompt vs plain at each tier | win or pass rate per tier | gain shrinks at hardest tier (K10) |
| T11 | Any multi-sample item | best of N by code score vs random sample | accuracy | best-of-N above random (K19) |

## 9. What does not transfer, and why

- **Escalation levels.** Rivera and Payne measure how language models behave as nations. Our agent solves single-answer problems; escalation rates do not transfer. What transfers is the method: log per-step score, flag spikes in code.
- **Open-ended adjudication by LLM.** Snow Globe's "hallucination as feature" is for qualitative exploration, not for scoring a plan. Our G3/G8 require checked outcomes.
- **Persona-driven diversity.** Background persona results are null (Lamparth, Zheng, Hu and Collier). Schema section 4b already says no persona voters on single-answer problems.
- **Historical-match scoring.** WarAgent's accuracy is confounded with recall. Our bench needs items the model cannot have memorised.
- **Debate-style team dialog.** Farcical harmony; equal to voting at best (G9).
- **StarCraft and COA-GPT numbers.** One game, partly deterministic, RL baselines copied from earlier work. The loop transfers; the numbers do not.
- **RL and MCTS agents.** Strong in rigid-rule games (GTBench NRA -1 for LLMs). Relevant only where the sub-problem is exactly checkable, where code should do the work anyway (G5).
- **Cranfield/AIAA numbers.** None exist in this document.
- **RAND 1950s.** Thin, second-hand, human players. Illustrates that formal scoring can hide costs not in the model; that is a design note, not a measured effect.

## 10. Open questions

1. Does simulate-then-revise raise accuracy against ground truth for plan-like tasks at equal tokens outside StarCraft? Only COA-GPT tests it.
2. How many samples of a simulated verdict give a stable and correct answer; does median of k beat one run at equal tokens?
3. Does an LLM adjudicator with code checks match a human adjudicator on outcomes? No validation found.
4. Does a different-model or code-built adversary find more real flaws than a same-model adversary, against an equal-call baseline?
5. Do the escalation and agreement results hold under the Rivera and Lamparth protocols on 2026 frontier models (replications)?
6. What do Yuksek 2023 and Schwartz 2020 measure, with numbers?
7. Do goal-stating personas change outcomes across models, versus background personas?
8. Does changing one fact (or anonymising actors) make the outcome move across simulators?
9. What is the real base of the RAND 1950s and RSAS evidence?
10. Does a reflection slot reduce bias but also validity?
11. How independent are agents in one run? Is the bootstrap interval too narrow, and by how much?
12. Is Payne's escalation ladder (author design) a valid measure?

## 11. Sources

Marks: [V] opened (full text this session), [M] snippet or summary only.

- Lamparth et al. (2024) Human vs. Machine: Behavioral Differences between Expert Humans and Language Models in Wargame Simulations. [V] https://arxiv.org/abs/2403.03407 (a01-a05, a24, b05-b08, c08-c11)
- Rivera et al. (2024) Escalation Risks from Language Models in Military and Diplomatic Decision-Making. [V] https://arxiv.org/abs/2401.03408 (a06-a08, a25, b01-b04, c06, c07)
- Hogan and Brennen (2024) Open-Ended Wargames with Large Language Models (Snow Globe). [V] https://arxiv.org/abs/2404.11446 (a10-a12, b09, b10, c01-c03)
- Goecks and Waytowich (2024) COA-GPT. [V] https://arxiv.org/abs/2402.01786 (a13, b11, c04, c05)
- Shrivastava, Hullman and Lamparth (2024) Measuring Free-Form Decision-Making Inconsistency. [V] https://arxiv.org/abs/2410.13204 (a14, a15, b19, c21, c22)
- Hua et al. (2024) War and Peace (WarAgent). [V] https://arxiv.org/abs/2311.17227 (a16, a17, b13, c12-c14)
- Matlin et al. (2026) Shall We Play a Game? Language Models for Open-ended Wargames. [V] https://arxiv.org/abs/2509.17192 (a18, a19, b20)
- Riedl and Matlin (2026) Position: AI Is Not Ready for Strategic Conflicts. [V] https://arxiv.org/abs/2609.16189 (b21)
- Black and Darken (2023) Scaling Intelligent Agents in Combat Simulations for Wargaming. [V] https://arxiv.org/abs/2402.06694 (a20)
- Black (2024) NPS thesis. [M] cover only. https://arxiv.org/abs/2408.13333 (a21)
- Emery (2021) Moral Choices without Moral Language. [V via page summary] https://tnsr.org/2021/09/moral-choices-without-moral-language-1950s-political-military-wargaming-at-the-rand-corporation/ (a09)
- Meta FAIR et al. (2022) CICERO. [M] https://www.science.org/doi/10.1126/science.ade9097 (a22)
- Bakhtin et al. (2022) Diplodocus / DiL-piKL. [M abstract only] https://arxiv.org/abs/2210.05492 (a23)
- Mukobi et al. (2023) Welfare Diplomacy. [V] https://arxiv.org/abs/2310.08901 (b12, d09)
- Duan et al. (2024) GTBench. [V] https://arxiv.org/abs/2402.12348 (b14)
- Kott et al. (2016) CADET. [V] https://arxiv.org/abs/1601.06108 (b15-b17)
- Elbaum and Panter (2025) Managing Escalation in Off-the-Shelf LLMs. [V] https://arxiv.org/abs/2508.01056 (b18, c15)
- Payne (2026) AI arms and influence. [V] https://arxiv.org/abs/2602.14740 (c16-c18)
- Jensen et al. (2025) Critical Foreign Policy Decisions benchmark. [V] https://arxiv.org/abs/2503.06263 (c19, c20)
- Ma et al. (2024) LLMs play StarCraft II. [V] https://arxiv.org/abs/2312.11865 (c23-c25)
- Guan et al. (2024) Richelieu. [V, numbers not re-opened] https://arxiv.org/abs/2407.06813 (c26, c27)
- Yuksek et al. (2023) Intelligent wargaming approach. [M] https://dspace.lib.cranfield.ac.uk/handle/1826/19164 and .../items/e85b68bd-5d62-4d85-a4d8-91566e13622b/full (b22, d11, c29)
- Schwartz et al. (2020) AI-enabled wargaming in MDMP (SPIE). [M] https://ui.adsabs.harvard.edu/abs/2020SPIE11413E..0HS/abstract (b23)
- Huang et al. (2024) LLMs Cannot Self-Correct Reasoning Yet. [V] https://arxiv.org/abs/2310.01798 (d01, d02, d15)
- Brown et al. (2024) Large Language Monkeys. [V] https://arxiv.org/abs/2407.21787 (d03, d14)
- Snell et al. (2024) Scaling LLM Test-Time Compute Optimally. [V] https://arxiv.org/abs/2408.03314 (d04)
- Gou et al. (2024) CRITIC. [V] https://arxiv.org/abs/2305.11738 (d05)
- Zheng et al. (2023) Judging LLM-as-a-Judge. [V] https://arxiv.org/abs/2306.05685 (d06, d13)
- Zheng et al. (2024) Personas in System Prompts. [V] https://arxiv.org/abs/2311.10054 (d07)
- Hu and Collier (2024) Quantifying the Persona Effect. [V] https://arxiv.org/abs/2402.10811 (d08)
- Hegazy (2024) Diversity of Thought in Multi-Agent Debate. [V] https://arxiv.org/abs/2410.12853 (d10)
- RAND Strategy Assessment System (1980s). [M, via Hogan and Brennen] (c28)
- Status note: arXiv, Semantic Scholar and OpenAlex returned rate-limit errors in the gap pass (d12).
