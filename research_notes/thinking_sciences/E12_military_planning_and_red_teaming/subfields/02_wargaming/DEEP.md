# Wargaming: deep document

*Subfield E12.02. Sources: evidence_a-d.jsonl, claims.jsonl (K01-K27), critique.md in this folder. Evidence ids (a01..d24) point to the evidence files. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested.*

## 1. What it is

A wargame tests a plan against an acting adversary. Someone plays the plan. Someone else plays the reply. A neutral party (umpire, control cell, rules) says what happens. Then the plan is changed. The core loop is action, reaction, counteraction. It exposes weak execution: the plan that looks fine on paper but fails when a reacting party moves.

Types, by level and format:
- By level: tactical (units, terrain), operational (campaigns, logistics), strategic (states, crises, escalation).
- By format: quantitative (discrete moves, rules and dice resolve them) and qualitative or open-ended (free moves, a moderator judges the outcome). Hogan and Brennen (a14) cite RAND's 1950s split between its mathematical and social-science games for this.
- By purpose (Goodman, Risi, Lucas 2020, a07): force testing, plan variation testing (run one plan many times to find branch points, such as a rare early loss in 2-5% of games), concept development, procurement.

Why it matters for our agent. In our schema it is a form of S4 TEST and a source of failures for S5. The adversary role asks "what would a reacting party do to this plan". The operator link is O5 work backwards: start from the bad end state and ask what moves lead to it.

What the evidence supports, in one paragraph. Three kinds of evidence exist and they do not mix.
1. Human forecasting studies (Green 2005, Armstrong 2002). Playing out the interaction forecast real conflict decisions about twice as accurately as unaided judgement. One research programme. Single-source.
2. Studies of LLMs as wargame players. They measure escalation, similarity to humans, and consistency. They do not measure whether the game found a real flaw.
3. Case history and one simulator study (Millennium Challenge 2002, Plan Orange 1933, IFPV 2026). No controlled test of "plan plus wargame step beats plan alone at equal tokens" exists (K18, K26). Practice is ahead of evidence (b26).

## 2. History and theories in depth

### 2.1 Origins (a05, a06, a01)
- Chess-like precursors: Hellwig (1780) and Venturini (1796) used grid games. One piece per square, removed when hit. Venturini added logistics and weather and is called the first operational-level game. Opiz 1806. Critics found them unrealistic (a05).
- Schuurman (2017, a06) treats twelve games from 1770-1830 as models. The central trade-off: more realism means more complexity and less playability. Designs differ in how they resolve it. Situational (asymmetric) games were the step toward modern wargames.
- Kriegsspiel (a01). Reisswitz Jr. showed a sand-table prototype in 1811, a wooden cabinet in 1812 (scale 1:2373) and the 1824 version on real 1:8,000 maps. Key inventions: the umpire, hidden information, dice-based partial losses. The umpire turns written orders into outcomes by judgment. Box set 30 thalers; every regiment was ordered to get one. This is the founding design of action, reaction, counteraction.

### 2.2 Rigid versus free (a02)
- Rigid Kriegsspiel used dice and loss tables. Meckel (1873/1875) gave four complaints: rules constrain umpire expertise, are too rigid, casualty maths is slow with minor effect, officers will not learn them. Verdy du Vernois (1876) dropped all rules.
- Free Kriegsspiel kept only the umpire, concealed information and delayed messages. It won, but by officer preference, not by a measured outcome.
- Lesson for an engineer. The split recurs in LLM work: rules adjudicate (stable, narrow) or a judge adjudicates (flexible, unstable). See Epstein 2026 in sections 4 and 5.

### 2.3 The 1870 claim and validation (a03, a04)
- Many credited Prussia's win in 1870 to wargaming. Prussia was the only army that practised it. One war, no control group. Correlation from one case.
- Validation in the wargame literature means the game can recreate a known battle. For forward-looking games the scenarios are hypothetical, so this is hard. No outcome numbers exist.

### 2.4 Modern practice and the cases
- Model kept a wargame going in November 1944 while the real US attack began, and fed its orders to the front (a06). The game became the reality; an early sign of the model-as-oracle risk.
- Plan Orange, 1933 (d22, Wikipedia citing Friedman, Miller, Holwitt, Vlahos). A Navy game of the Philippine relief plan ended in blue defeat: underwater damage, repair only at Pearl Harbor, stretched logistics. It led to a more gradual advance through the Marshalls. Pointer only; primary sources not opened.
- Millennium Challenge 2002 (d21, Zenko 2015). Cost $250 million, about 13,500 people. Van Riper's red force sank 19 US ships in minutes by his account. After free play was constrained, the JFCOM report itself says the end state was scripted. Van Riper was removed as commander after six days. Gen. Bell later called it a eureka moment for red teaming and reportedly directed at least 20 red teams. The weakness was documented and initially not acted on (K27). Secondary source; the 752-page report was not opened.
- Emery (2021, d10). Two early RAND games: the abstract mathematical MAD game (1954) went nuclear repeatedly; the realistic human-played SSD game never did. MIT games (Pauly 1958-1972): 2 of 26 crossed the nuclear threshold. 64.9% of n = 77 reported extreme or intense emotion. Emery blames abstraction and missing felt responsibility. He does not show a general "computer opponents escalate" effect, yet Lamparth and Rivera cite him that way (d11, K19 contested).
- RAND automated wargame (RSAS): escalation personas had to be built by hand (c29, secondhand).

### 2.5 Theory of why role-play should work (Green, Armstrong; b01-b07)
Role thinking: people placed in a role and made to interact use information about the parties that experts' abstract analysis ignores. Game theory needs the right payoffs and rational choice; real conflicts have messy objectives. Armstrong's audit points to interaction between parties as the active ingredient (b06, b07).

### 2.6 AI and wargaming (a07, a08, a14, a23)
- Goodman et al. (2020): reinforcement learning agents overfit to the training scenario and generalise poorly to small changes. Self-play fails in asymmetric games because Blue's learned policy does not model a different Red. Costs: about $250,000 or more per AlphaZero run, several million dollars for StarCraft II.
- LLM-era systems: Snow Globe (control, player and team agents), WarAgent (country agents plus a secretary checker), COA-GPT (LLM proposes courses of action, simulator scores), Richelieu (Diplomacy agent with opponent model and reflection).
- Scoping review (Matlin 2026, a23, b20): 223 studies to 1 May 2026. Only 20 (9%) let the language model both play and adjudicate. Among 63 core military studies, 4 (6.3%); among 160 adjacent, 16 (10.0%). 152 (68%) fully autonomous, 19 (8.5%) human in the loop. 155 (70%) touch a safety theme; deception 29%, escalation 11%, bias 5%; 68 none. Single coder with LM help; no reliability reported.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Role-play (simulated interaction) beats game theorists and unaided judgement on real conflicts | 8 conflicts. Game theorists 31% (101 forecasts, 23 theorists). Unaided students 31% (354). Simulated interaction 62% (105). Error cut 47%. Permutation P = 0.004 | Green 2005 (b01, b02) | [S] one programme |
| Gain does not depend on conflict difficulty | Four easiest (49% by game theorists): error cut 49%. Four hardest (13%): error cut 45% | Green 2005 (b02) | [S] |
| Expertise and effort did not help | Theorists 31% = novices 31%. Predictions before data (n = 77): novices 30%, simulated 40%, theorists 50% | Green 2005 (b03) | [S] |
| Combining several role-play runs is more accurate than one | Combined forecast accurate in 7 of 8 conflicts; single runs 62%; modal theorist forecast right in 3 of 8 | Green 2005 (b04) | [S] |
| Earlier audit shows the same on 6 situations | Excluding the non-interactive case: chance, unaided, game theory about 28% each; role playing 61%. Wilcoxon one-tailed P = 0.03. Over 1100 participants | Armstrong 2002 (b06) | [S], same programme |
| Gain needs interaction between parties | Game theory beat role playing in 1 of 6 situations: the non-interactive one (Panalba) | Armstrong 2002 (b07) | [S] |
| Usefulness ratings track accuracy | Simulated interaction 6.6, game theorists 4.3, random 4.1 (10-point). kappa 0.249, 5 raters | Green 2005 (b05) | [S] weak |
| Same-model LLM crisis sims escalate | 5 models, 3 scenarios, 10 runs each, 8 nations, 27 actions. None de-escalated significantly. GPT-3.5 neutral score 10.15 to 26.02 (+256%). Some turns jumped over 50% | Rivera 2024 (b08, c01, c02) | [S] |
| Untuned base model is worst | GPT-4-Base nuclear actions 7.08% / 7.09% / 6.71% (neutral / invasion / cyber); mean score 17.6-20.0. GPT-4: 0.00% violent and nuclear in neutral | Rivera 2024 (c04, c03) | [S] |
| Arms-race pattern despite disarmament options | All models raised military capacity; reasons cited deterrence and first strike | Rivera 2024 (a10, b10) | [S] |
| Escalation is a sampling and prompt dial in a small model | Mistral-7B, 10 runs per cell. Score 6.37 at T=1.0; 3.96 at T=0.5 (-38%); 3.33 at T=0.01 (-48%). Planning prompt 4.61 (-28%); de-escalation prompt 2.76 (-57%); context prompt about -8%. Final-day 11.1 vs 6.7 and 6.5 | Elbaum and Panter 2025 (b11, b12) | [E] with Rivera prompt variants (K06) |
| Rivera's own prompt variants moved severe actions | GPT-3.5 No-Goals and Low-Stakes variants significantly reduced severe actions; most other variants did not | Rivera appendix (critique fix 2) | [E] (K06) |
| LLM teams match human experts on about half of actions | 214 experts, 48 teams, 21 actions, 2 moves. LLM = 80 simulated games per configuration. Matched on 16 (GPT-3.5), 10 (GPT-4), 9 (GPT-4o) | Lamparth 2024 (b14, c05) | [S] |
| Treatment effects mostly reproduced | 2x2 AI weapon accuracy (70-85% vs 95-99%) x crew training, plus China posture; LLM conclusions mostly agreed with humans | Lamparth 2024 (b15) | [S] |
| Persona labels do nothing | Pacifist vs sociopath, age, gender, background: no significant change for any action, any model | Lamparth 2024 (b16, c06) | [S] |
| Simulated team dialogue is thin and changes the answer | "Farcical harmony"; about 350 words per chunk, 3 chunks used. More dialogue raised aggression toward human level for GPT-3.5/4 but raised action count away from humans; GPT-4o overshot | Lamparth 2024 (b17, c07, c08) | [S] |
| Escalation persistence | P(aggressive move 2 given aggressive move 1): humans 0.94, GPT-3.5 0.98, GPT-4 0.99, GPT-4o 1.00. Given de-escalatory move 1: humans 0.65, GPT-3.5 0.85, GPT-4 0.73, GPT-4o 0.86 | Lamparth 2024 (c10) | [S] |
| Free-form advice is inconsistent in meaning | 5 LMs, 20 responses per simulation at T=1.0, BERTScore. GPT-4 worst; Claude 3.5 Sonnet and GPT-4o mini best. Anonymising countries did not remove it | Shrivastava 2024 (b18, c11) | [S] |
| Prompt rewrites vs sampling | At T=0, meaning-preserving rewrites give inconsistency comparable to T=0.2 sampling (GPT-4 lower). Inconsistency above rewording noise at T>0.2 | Shrivastava 2024 (b19, c12) | [S] (K04) |
| Giving the adversary's counter-move lowers inconsistency | Lower in both continuations for Claude 3.5 Sonnet, GPT-4o, GPT-4o mini | Shrivastava 2024 (c13) | [S] (K20) |
| Opponent modelling gap | Professional humans 85.7, elite 85.5, general 77.9; DeepSeek R1 49.1, Qwen3 47.9, V3 45.9 | WGSR-Bench (c22) | [S] |
| Complex situation analysis gap | Humans 85.9% vs best model 37.5% (48.4 points); humans average 79.9% over six tasks | WGSR-Bench (b23, c24) | [S] |
| Long-term vs short-term prediction | R1 long-term reward 84.0 (human 83.3); short-term 45.2 (human 87.8). High-risk strategy prediction R1 31.1 | WGSR-Bench (a22, c23) | [S] |
| Plan length and mid-game pivots hurt | Accuracy 60-70% at 50-100 step sequences, 35-40% for campaign-level; best models 45% of expert performance at a mid-game pivot. GPT-4.1 about 60 points on policy generation; elite humans 92.3 | WGSR-Bench (b24, a21) | [S]; LLM judge scores policies |
| Induction easier than deduction | Trait attribution better than predicting actions from a trait; ambiguous wording ("moderately high risk") lowers accuracy | WGSR-Bench (a22) | [S] |
| LLM umpire is unstable when free | 378 actions, 9 games. Re-run self-disagreement 3-6% (Semi-Rigid), 14-16% (Free). Judge swap +3 points. Panel changed 40 of 378 outcomes, pass count by only 8. Variance split: submission 34.0%, method 0.2%, judge AI 1.0%, method x judge 5.6%, residual 59.2% | Epstein 2026 (d01) | [S] |
| Judges differ in how much they anchor | Under same Semi-Rigid instruction: Gemini kept rulebook difficulty on 92.9% of rulings, Opus 16.4%. Mean pass probability: players' stated 0.585, rulebook 0.743, panel 0.754 | Epstein 2026 (d02) | [S] |
| An adversarial verification step raised simulator success | Mission success 61.0% (IFPV/MPHA) vs 49.3% (Gemini 3.1 Pro), 48.7% (DeepSeek-V3), 13.3% (GLM-5), 2.7% (Qwen3-Max-Thinking). Abstract: +19.4% success, -41.7% cost | Huang 2026 IFPV (d04) | [S]; same adversary scores and selects; compute not matched |
| Prompted LLM opponent finds fewer flaws than scripted | Suppression rate: No_Brain 93.33 / GLM-5 33.33 / ACSE 96.00 (one set); 41.33 / 0.00 / 52.00; 34.67 / 0.00 / 46.67. ACSE +31.8% over rule-based validator | IFPV (d05) | [S] (K23) |
| One adversary reply overstates plan strength | BLUE advantage for 1, 2, 4, 8, 16 RED samples: .516, .498, .490, .485, .479. Win rate .920 (1 sample) vs .820 (best of 8) | COA-Bench (d06) | [S]; synthetic scores |
| Strategic comparisons need many seeds | Pairwise separability stabilises at about 150 seeds; 5 games, 10 LLMs | d08 | [S] |
| Code-space opponent recovery feasible | 75 policies, 5 environments, 12 LLMs; recovery closed 34-72% of distance; probing helped in 16 of 20 model-game pairs; raw traces best input | RevengeBench (d09) | [S] |
| LLM proposes, simulator scores | 5 COAs x 10 sims. Best variant 3.4% below human expert; RL baseline 112 thousand battles (70 million timesteps) | COA-GPT (a15) | [S]; scripted enemy |
| History fit is weak evidence | WarAgent WWI, 7 runs: Britain-France, Germany-Austria, Serbia-Russia alliances 100%; Austria-Serbia, Austria-Russia, Germany-Russia declarations 100%; France-Germany 71.4%; Britain-Germany 14.3%; no peace agreement | Hua 2023 (c15) | [S] |
| Reflection and opponent model help Diplomacy | Vs Cicero table: win 6.83% vs 6.03%; Most SC 8.63 vs 6.90; Survived 39.95 vs 41.87; Defeated 44.60 vs 45.20. Vs AutoGPT table: win 9.10% vs 1.63%; Most SC 18.33 vs 4.10; Defeated 34.30 vs 61.37 | Richelieu (c19, critique fix 1) | [S]; small edge over Cicero, no test |
| 2026 frontier models still escalate model-vs-model | 21 games, 329 turns, 3 models. No de-escalating or surrender choice. Strategic-threat level reached: Claude 64%, GPT-5.2 36%, Gemini 29%. Strategic war: GPT-5.2 14%, Gemini 7%, Claude 0%. Return to start line used 45 times (6.9%) | Payne 2026 (d12) | [S]; with d13-d16 [E] (K25) |
| But cooperative against graduate students | Round 1 (n = 63) agreement 0.254-0.540 (Gemini .540, Claude .533, Mistral .476, ChatGPT .460, Qwen .317, Grok .254); round 2 (n = 45) 0.156-0.333. Alpha among models .41, with humans .39 | Solopova 2026 (d13) | [S] |
| One-line framing shifts escalation | 3,604 games. 10.7% baseline vs 28.6% under coercion prime (2.7x). Rights-based prime 10.9%. Claude Opus 4.7 8.4% to Kimi K2.6 31.7% (3.8x) | Adl and Williams 2026 (d14) | [S]; preprint |
| Reasoning language changes launch advice, only for hesitant models | Claude Sonnet launch 40% to 0% (unnecessary strike), 93% to 17% (contested); Gemini Pro 3.1 53% to 13%. Five other models launched almost always | Touchent 2026 (d15) | [S] |
| Fog of war breaks state tracking | 54 matches, 5,258 actions, 15 models. 58% of illegal actions were fog or state errors. Nuclear rush 78% of rules-coherent games | Ricci 2026 (d16) | [S]; exploratory |
| Models leak hindsight | Behavioural cutoffs span 22 months across vendors, precede stated dates by up to 8 months. Leakage with hint prompt 5.2%, 2.7%, 1.0%; date-filtered retrieval 13.1%, 8.9%, 4.7% | HindsightBench (d18), Zhang 2026 (d19) | [S]; general, not wargame-specific |
| Humans beat LLMs at resource-allocation conflict | >200 humans vs LLM tournaments; LLM strategies simpler and more stereotyped | Dagaev 2026 (d17) | [S] |
| Wargaming has no outcome-level proof | Prussia 1870 confounded; rigid vs free settled by preference; MC 2002 and Plan Orange are secondary-source cases | a03, a02, a04, d21, d22 | [E] that evidence is absent (K18) |
| Umpire separated from players in every design | Kriegsspiel umpire; Snow Globe control; WarAgent secretary | a01, a13, c14, c27 | [E] as design practice (K21) |

## 4. Mechanisms and models

### 4.1 Role thinking and why interaction matters
Mechanism (Green, Armstrong). A forecaster who imagines the other party alone anchors on own goals. A role player has to produce the other side's reply in time and in character, then the first side must answer it. The extra steps expose reactions that a single judgement skips. The effect vanished in the one case with no interacting parties (b07).
Implementation. Trigger the adversary step only when the task has a reacting party. Otherwise skip (saves tokens, K02). Each role is a separate call with its own brief. Roles do not see each other's reasoning, only each other's moves.

### 4.2 The action-reaction-counteraction cycle (code skeleton)
```
state = plan, world facts (held in code)
for turn in 1..K:
    blue_move = BLUE(state)                          # short, structured
    code_validate(blue_move)                         # reject illegal or invented moves (K21)
    red_move = RED(state_visible_to_red, brief_red)  # separate call
    code_validate(red_move)
    outcome = ADJUDICATE(state, blue_move, red_move) # rules first, judge bounded
    state = code_update(state, outcome)
collect: failure events from state (code-detected), not from model opinion
```
Design choices backed by evidence:
- Umpire separate from players and state held by code (K21; fog errors in d16 show models mis-track hidden state).
- Short steps with code-held state rather than one long imagined campaign (K11; plan quality falls with length in b24).
- Bounded adjudication: let the judge adjust a rulebook number rather than free-set difficulty (3-6% vs 14-16% re-run change, d01).

### 4.3 Adjudication models (Epstein 2026, Kriegsspiel)
- Rigid: rules and dice only. Stable, narrow.
- Semi-rigid: rulebook gives base difficulty, judge adjusts within bounds. Self-disagreement 3-6%.
- Free: judge alone. Self-disagreement 14-16%.
- Panel: several judges. Moved 40 of 378 outcomes but the pass count by 8, so aggregate rates hide ruling-level change.
- 59.2% of outcome variance was residual (unexplained noise); method explained 0.2%. The submitted action explained 34.0%.
Implementation. Log adjudicator verdicts, re-run twice, and treat verdicts that flip as unreliable.

### 4.4 The adversary is a parameterised sampler
Its output depends on frame, model, temperature and prompt wording, not on persona:
- Frame: one line moved escalation from 10.7% to 28.6% (d14).
- Temperature: 6.37 to 3.33 (b11).
- Reflection prompt: 6.37 to 2.76 (b12).
- Model: 3.8x range across eight models (d14).
- Personas: no effect (b16). Role-play emphasis: no effect (c07).
So a red team measures the brief as much as the plan (K06). Implementation: treat the adversary brief as an experimental variable, fix it per run and log it.

### 4.5 Repeat and aggregate (G5)
- One adversary reply overstates plan strength; most of the drop occurs in the first 2-4 samples (.516 to .490 by 4, then .479 by 16, d06).
- Green: combined role-play runs were right in 7 of 8 conflicts vs 62% single (b04).
Implementation. Run N adversary samples at fixed total budget. Code extracts each weakness as a normalised tag, clusters, counts. Stop when new tags per run is near zero. A weakness flagged in a single run is a hint only (G4).

### 4.6 Opponent variety
- Code enumerator or scripted opponent exposed more flaws than a prompted LLM opponent on the same plans (35-93% vs 0-33% suppression, d05). A world-model opponent exposed the most.
- An RL no-press policy exploited prompted LLM agents far more than LLM exploiters did (c17).
- RevengeBench (d09): an LLM can write an executable opponent policy from behaviour traces; probing helped strong models.
Implementation. Where the domain allows, use a code adversary that enumerates options (legal-move search, edge-case generator, fuzzer) alongside a model adversary.

### 4.7 Give the adversary structure
- Supplying the counter-move lowered inconsistency (c13).
- Opponent goals are hard to infer: best model 49.1 vs 77.9 for general humans (c22). Models are better at induction than deduction (a22), and ambiguity hurts.
Implementation. Build the adversary's goal and option list in code from the task, and give them, instead of asking the model to guess intent. Untested (see UNKNOWNS).

### 4.8 Work backwards (O5) from the failure
Wargame plan variation testing (a07) finds rare branches. A backward version: name a bad end state, ask which reply sequence reaches it, then check each step with code. A sketch only; no study tests it.

## 5. What holds up

### 5.1 Holds, with qualifications
- Role-play beats game theory and unaided judgement on interactive conflict forecasts: 62% vs 31% (Green 2005), 61% vs 28% (Armstrong 2002). One research programme; Armstrong audited Green's earlier 6-situation study, so these are not independent replications (critique fix 5). No outside-lab replication or LLM-role-player test was found (gap 2).
- Same-model LLM crisis games drift toward escalation, and tone is set by frame, temperature, prompt and model (K05, K06, K25). Direction is stable. Size is not.
- Persona labels and background do not move simulated players (Lamparth, one group).
- Umpire/validator separation is a stable design practice (K21).
- The absence of outcome evidence for wargaming is itself established (K18).

### 5.2 Failures and boundary conditions
- Non-interactive problems: game theory beat role-play on Panalba (b07).
- Rivera vs Elbaum and Panter: the 7B model's escalation depended heavily on temperature and prompt. The direction held; the stability did not.
- Lamparth: newer models matched human action frequency on fewer actions (16, 10, 9 of 21). "Better model" did not mean "closer to human wargame behaviour".
- 2026 models are more cooperative than graduate students in menu games (d13) yet never de-escalate in model-vs-model games (d12). Task structure matters.
- Hindsight: WarAgent fit to history may reflect memory. No anonymised test.
- Emery 2021 is misquoted in two LLM papers as a general computer-opponent effect (K19, contested).
- A claimed LLM-adjudicator kappa of about 0.89 versus three human adjudicators came from a withdrawn paper (d03). Do not use.
- Richelieu's edge over Cicero is small and untested for significance; Richelieu survived slightly less often (39.95 vs 41.87).
- RL does not transfer across small scenario changes or asymmetric sides (a08).
- IFPV's gain holds only inside its own simulator; its compute was not matched.

### 5.3 Moderators
Interaction between parties (needed). Model and tuning (base model worst). Frame and language (large). Temperature (large in a small model). Adjudication freedom (3-6% vs 14-16%). Plan length (accuracy falls). Opponent type (scripted and world-model beat prompted LLM). Number of adversary samples (diminishing after 2-4).

### 5.4 Interventions that worked and did not
Worked: lower temperature (-48%), de-escalation reflection (-57%), rights-based frame (back to baseline), supplying the counter-move (less inconsistency), bounded adjudication, code-held state, scripted or world-model opponents, repeated adversary sampling (diminishing), reflective memory plus opponent model in Diplomacy (small).
Did not: personas, role-play emphasis, "players must discuss" instruction, anonymising countries (inconsistency stayed), 50-word context summary (-8%), temporal hint prompts for leakage, panels (moved rulings, not totals), written summaries for opponent recovery.

### 5.5 Independence warning
Lamparth and Shrivastava share an author group. Most LLM numbers rest on Rivera, Lamparth, Shrivastava, Yin. Only Green and Armstrong test accuracy against real outcomes.

## 6. Language models

How they behave:
- As adversary: tone depends on frame and settings, not on a stable "character" (K06, K25). Free-form output varies in meaning across samples (K04). Prompted LLM opponents find fewer flaws than scripted ones in a simulator (K23).
- As team: simulated discussions are thin, unanimous and do not object (K08). Persona prompts do nothing (K07).
- As analyst: far below humans in opponent modelling (49.1 vs 77.9-85.7) and complex situation analysis (37.5% vs 85.9%). Good at long-term reward (84.0 vs 83.3), poor at short-term moves (45.2 vs 87.8) (K10, K11).
- As planner: plan quality falls with plan length (60-70% at 50-100 steps; 35-40% at campaign level); mid-game pivots are weakest.
- As umpire: 3-6% verdict change on re-run when bounded, 14-16% when free; no accuracy measure (K12, K22). Only 9% of AI-wargame studies let the LM both act and adjudicate.
- State tracking under hidden information: 58% of illegal actions were fog or state errors (d16).
- Escalation: all five 2023 models escalated, base model worst (nuclear 6.7-7.1%); 2026 models never chose de-escalation in 21 games; one-line framing shifted escalation 2.7x; reasoning language changed launch advice for hesitant models (93% to 17%).

What changed it, by how much:

| Lever | Change |
|---|---|
| Temperature 1.0 to 0.01 | escalation -48% (7B) |
| De-escalation reflection prompt | -57% (7B) |
| Planning reflection prompt | -28% (7B) |
| Coercion frame | 10.7% to 28.6% |
| Rights-based frame | back to 10.9% |
| Japanese reasoning (Claude Sonnet) | launch 93% to 17% |
| Counter-move supplied | lower inconsistency (3 models) |
| No safety tuning (GPT-4-Base) | 7% nuclear vs 0-1% tuned |
| Newer model | matches fewer human action frequencies |
| Expert documents (Sun 2023) | higher win rate; figures not extracted |

The measurable use for our purpose (a plan tested by an adversary at equal tokens) has one near-case: IFPV 61.0% vs 49.3%. It is simulator-only, scored by the design adversary, and compute-unmatched (K26). At equal compute on reasoning QA, debate beat self-consistency by 1.3 points and mixture-of-agents by 2.7 (d07). G9 already says debate does not beat voting for single-answer problems; this is a different task and does not override G9.

## 7. What our agent should take

Schema part key: G guardrail, S state, O operator, M memory.

### Add now (established [E])
1. **Log the adversary setting on every wargame call: model, temperature, frame, brief.** Part: logging (SCHEMA section 6) and G4. [E] K06, K25. Evidence a20, b11, b12, d12-d16. Reason: findings depend on the brief.
2. **A separate, code-validated adversary step: code checks that adversary moves are legal and not invented before they enter the state; the umpire is never the planner.** Part: G5 / G8. [E] as design practice, K21. Evidence a01, a13, c14, c27. This does not claim the step improves plans.
3. **No persona or discussion voters for the adversary.** Part: G4 / G9. [E] already in schema; consistent with K07, K08 [S] on this side.
4. **Do not add the wargame step as a default.** Part: G7. [E] K18: no outcome evidence. It must pass the equal-token test first.

### Test first (single-source or contested)

| Item | Part | Status | Evidence ids |
|---|---|---|---|
| Separate-call adversary at S4 when a reacting party exists | S4 | [S] | K01, K26; b01, b06, d04 |
| Skip adversary when no counter-actor | S0 / S4 trigger | [S] | K02; b07 |
| Repeat adversary N times, cluster weaknesses in code, stop at diminishing returns | G5, S4 | [S] | K03, K24; b04, d06, d08 |
| Adversary given code-built goals and option list | S4 / O5 | [S] | K10, K20; c13, c22 |
| Code-enumerator or different-model adversary vs same-model prompt | G4 | [S] | K15, K23; d05, c17 |
| Short rollout steps with code-held state | S4 | [S] | K11; b24, d16 |
| Bounded vs free adjudication; run twice, log flips | G8 | [S] | K22; d01, d02 |
| LLM proposes, code scores COAs vs model-opinion ranking | S4 / G8 | [S] | K16; a15 |
| Backward step from a named bad end state | O5 | [S] | a07; no direct test |
| Store lessons from verified simulated runs | M | [S] | K17; c19, c20 |
| Log overrides of adversary findings, count later errors | G5 | [S] | K27; d21 |
| Anonymised or post-cutoff scenarios for history-based tests | G7 | [S] | K14; d18-d20 |

Contested: the claim that computer opponents escalate more than humans (K19) [C]. Do not use.

## 8. Concrete tests on our bench

All arms at equal total tokens. Seeded-flaw items: plans, programs, schedules or policies where code knows the planted flaws. Score by flaw recall and false-alarm rate, plus final task success where a check exists.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Core A/B | Plans with seeded flaws that appear only when a counter-actor reacts | (a) plan alone; (b) plan plus self-critique; (c) plan plus separate-call adversary | flaw recall, false alarms, final success | (c) beats (b) by 10+ points recall; false alarms up under 5 |
| T2 Trigger | Mixed items, half with no counter-actor | adversary always vs only when counter-actor present | accuracy, tokens | no accuracy loss on no-actor items; tokens down |
| T3 Repetition | Same plan, 3 paraphrases of the brief | 1, 3, 5, 10 adversary runs | share of runs naming same top weakness; new flaws per extra run | most new flaws in first 3-4 runs |
| T4 Opponent type | Seeded-flaw plans | same-model persona, different model, code enumerator | flaw recall | enumerator and different model beat persona |
| T5 Goals supplied | Opponent-modelling items | model infers goal vs code-built goals and options | recall, run agreement | supplied goals raise recall and agreement |
| T6 Rollout steps | Long plans | one long imagined campaign vs short steps with code state | flaw recall, illegal-state rate | steps lower illegal state and raise recall |
| T7 Adjudication | Moves with known rule outcomes | code rules vs bounded judge vs free judge | agreement with rules, invented-consequence rate, flip rate on re-run | bounded between code and free; free flips 10%+ |
| T8 Role collapse | Same items | one model in all roles vs different models | error correlation across planner, adversary, judge | different models lower correlation |
| T9 Score by running | Plan generation with a simulator | rank by code rollout vs model opinion | rank agreement with ground truth | rollout wins |
| T10 Hindsight | Historical crisis items | well-known vs anonymised vs post-cutoff | accuracy | accuracy drops on anonymised |

## 9. What does not transfer, and why

- Human forecast gains (62% vs 31%) came from people playing roles with real knowledge, across many participants. No evidence that a single model call reproduces them (K01).
- Escalation scores measure crisis-game behaviour, not plan-flaw finding. Our tasks are mostly not nuclear crises.
- Match to human experts (Lamparth) is about behaviour similarity, not correctness.
- Simulator success (IFPV, COA-GPT) uses scripted enemies and same-adversary scoring.
- Group dynamics (rank, fear, felt responsibility, Emery) are missing in one-model teams.
- The Kriegsspiel umpire is human judgement built from experience; an LLM umpire has 14-16% self-disagreement when free.
- Real red-team cases (Millennium Challenge) turned on organisational override, not model quality. Our agent has no commander to overrule; the equivalent is the planner ignoring the adversary (G5).
- Persona and debate effects from human teams do not transfer: LLM personas had no effect and dialogue is unanimous.
- RL wargame agents need huge training budgets and do not generalise (a08); we do not train.

## 10. Open questions

1. Does a separate adversary step improve plans at equal tokens? No study tests it.
2. Does Green's role-play advantage replicate outside the lab, and with LLM role-players?
3. How accurate is LLM adjudication against humans? Only self-consistency is measured. The 0.89 kappa is from a withdrawn paper.
4. Does a code or different-model opponent find more flaws than a persona on seeded-flaw plans?
5. How many adversary runs make a flagged weakness stable; does clustering help?
6. Does giving explicit goals close the opponent-modelling gap?
7. How much of historical-wargame fit is memory?
8. Do experts replicate Lamparth with 2026 models?
9. What do Brewer and Blair 1979, Perla 1985, Naval War College 1894 records, RAND and Army red-team reports show? Not opened.
10. Is the framing sensitivity (10.7% to 28.6%) also true of red-team findings on plans?

## 11. Sources

[V] = opened and read this session. [M] = snippet or secondhand only.

- [V] Wikipedia, Kriegsspiel. https://en.wikipedia.org/wiki/Kriegsspiel (a01-a03)
- [V] Wikipedia, Wargame. https://en.wikipedia.org/wiki/Wargame (a04, a05)
- [V] Schuurman (2017) Models of war 1770-1830. https://repub.eur.nl/pub/101998/REPUB_101998-OA.pdf (a06)
- [V] Goodman, Risi, Lucas (2020) AI and Wargaming. https://arxiv.org/abs/2009.08922 (a07, a08)
- [V] Rivera et al. (2024) Escalation Risks. https://arxiv.org/abs/2401.03408 (a09, a10, b08-b10, c01-c04)
- [V] Lamparth et al. (2024) Human vs. Machine. https://arxiv.org/abs/2403.03407 (a11, a12, a25, b14-b17, c05-c10)
- [V] Hogan and Brennen (2024) Snow Globe. https://arxiv.org/abs/2404.11446 (a13, a14, b25, c27)
- [V] Goecks and Waytowich (2024) COA-GPT. https://arxiv.org/abs/2402.01786 (a15)
- [V] Hua et al. (2023) WarAgent. https://arxiv.org/abs/2311.17227 (a16, a17, c14-c16)
- [V] Shrivastava, Lamparth, Hullman (2024) inconsistency. https://arxiv.org/abs/2410.13204 (a18, a19, b18, b19, c11-c13)
- [V] Elbaum and Panter (2025) Managing Escalation. https://arxiv.org/abs/2508.01056 (a20, b11-b13)
- [V] Yin et al. (2025) WGSR-Bench. https://arxiv.org/abs/2506.10264 (a21, a22, b23, b24, c22-c25)
- [V] Matlin et al. (2026) Shall We Play a Game? https://arxiv.org/abs/2509.17192 (a23, b20, b21)
- [V] Sun et al. (2023) Self-Generated Wargame AI. https://arxiv.org/abs/2312.01090 (a24; win-rate figures not extracted)
- [V] Green (2005) Game theory, simulated interaction. https://www.professionalwargaming.co.uk/Role-Play-Works.pdf (b01-b05)
- [V] Armstrong (2002) Assessing game theory, role playing. https://faculty.wharton.upenn.edu/wp-content/uploads/2012/04/Assessing-Game-Theory.pdf (b06, b07)
- [V] Riedl and Matlin (2026) AI Is Not Ready for Strategic Conflicts. https://arxiv.org/abs/2609.16189 (b22)
- [V] On LLMs in National Security Applications (2024). https://arxiv.org/abs/2407.03453 (b26)
- [V] Mukobi et al. (2023) Welfare Diplomacy. https://arxiv.org/abs/2310.08901 (c17, c18)
- [V] Guan et al. (2024) Richelieu. https://arxiv.org/abs/2407.06813 (c19-c21)
- [V] Ma et al. (2024) TextStarCraft II. https://arxiv.org/abs/2312.11865 (c26)
- [V] Epstein (2026) Thumb on the scale. https://arxiv.org/abs/2610.32066 (d01, d02)
- [V] Laitinen Imanov et al. (2026) sdLM, withdrawn. https://arxiv.org/abs/2601.14862 (d03; do not use)
- [V] Huang et al. (2026) IFPV. https://arxiv.org/abs/2605.14851 (d04, d05)
- [V] Vidra et al. (2026) COA-Bench. https://arxiv.org/abs/2609.26059 (d06)
- [V] Wunderlich et al. (2026) Multi-agent test-time scaling. https://arxiv.org/abs/2605.01566 (d07)
- [V] Choosing LLMs for Strategic Agent Interactions (2026). https://arxiv.org/abs/2610.18354 (d08)
- [V] RevengeBench (2026). https://arxiv.org/abs/2606.26094 (d09)
- [V] Emery (2021) Moral Choices without Moral Language. https://tnsr.org/2021/09/moral-choices-without-moral-language-1950s-political-military-wargaming-at-the-rand-corporation/ (d10, d11)
- [V] Payne (2026) AI Arms and Influence. https://arxiv.org/abs/2602.14740 (d12)
- [V] Solopova et al. (2026). https://arxiv.org/abs/2603.02128 (d13)
- [V] Adl and Williams (2026) Greenland Sovereignty Game. https://arxiv.org/abs/2605.22841 (d14)
- [V] Touchent (2026). https://arxiv.org/abs/2608.12373 (d15)
- [V] Ricci (2026) Age of LLM. https://arxiv.org/abs/2606.24391 (d16)
- [V] Dagaev et al. (2026) Colonel Blotto. https://arxiv.org/abs/2605.22095 (d17)
- [V] Jia (2026) HindsightBench. https://arxiv.org/abs/2607.18867 (d18)
- [V] Zhang, Chen, Stadie (2026). https://arxiv.org/abs/2602.17234 (d19)
- [V] ExAnte (2025). https://arxiv.org/abs/2505.19533 (d20)
- [V] Zenko (2015) Millennium Challenge. https://warontherocks.com/2015/11/millennium-challenge-the-real-story-of-a-corrupted-military-exercise-and-its-legacy/ (d21)
- [V] Wikipedia, Plan Orange. https://en.wikipedia.org/wiki/Plan_Orange (d22)
- [V] Crossref record of Bolton (2002). https://api.crossref.org/works/10.1016/s0169-2070(02)00027-4 (d23)
- [V] Lin-Greenberg, Pauly, Schneider (2022), abstract only. https://dspace.mit.edu/handle/1721.1/148672 (b27, d24)
- [M] Green and Armstrong (2011) Role thinking. https://doi.org/10.1016/j.ijforecast.2010.05.001 (a26, not opened)
- [M] Lin-Greenberg, Pauly, Schneider (2022) EJIR. https://doi.org/10.1177/13540661211064090 (a27)
- [M] Lin-Greenberg (2022) Wargame of Drones. https://doi.org/10.1177/00220027221106960 (a28)
- [M] Brewer and Blair (1979) War games and national security with a grain of salt (secondhand via d11)
- [M] Davis and Stan (1984) RAND R-3235 (c29, via Snow Globe)
- [M] Bakhtin et al. (2022) Cicero (c30, via Richelieu)
- [M] Jensen et al., actor-identity effects (b13, via Elbaum and Panter)

## Source audit (2026-10-27)

Fresh auditors re-opened the sources of 3 established claims: 2 confirmed as written, 1 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E12.02-K25** (reworded: the sources support less). Payne (21 games, 29-64%) and Adl & Williams (3,604 games, 10.7% to 28.6%) verified, but Solopova et al. does not show models pick more cooperative actions than graduate students (only their explanations are cooperative in framing; some models were more coercive on economic choices), and Payne's models did sometimes reduce violence (return to start line) though never chose accommodation or withdrawal. Corrected claim: In Payne's 21 model-vs-model nuclear-crisis games no model ever chose accommodation or surrender (only de-escalation as far as returning to the start line) and strategic-threat level was reached in 29-64% of games depending on the model; in Solopova et al.'s menu simulations models' explanations were cooperative in framing but their actions were mixed against graduate-student players (some more coercive); one-line framing moved escalation from 10.7% to 28.6% in 3,604 games (Adl and Williams). No Lamparth replication with experts was found.
- **E12.02-K06** (now single-source: only one opened source, code check).
