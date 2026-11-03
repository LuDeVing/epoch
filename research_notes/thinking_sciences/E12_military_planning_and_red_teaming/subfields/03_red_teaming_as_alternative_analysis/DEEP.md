# Red teaming as alternative analysis: deep document

*Subfield E12.03. Evidence files: evidence_a-d.jsonl (ids a01-a28, b01-b29, c01-c25, d01-d17). Claims: claims.jsonl (E12.03-K01 to K34). Cross-check: critique.md. Status marks: [E] established, [S] single-source, [C] contested. Read this first: the military core of this subfield (UFMCS handbook, ADSO, DSB 2003, Ipcha Mistabra outcomes) and the classic human-effect papers (Schwenk 1990, Nemeth 2001, Mitchell 1989, Lord 1984, Herzog and Hertwig 2009) were NOT opened. Numbers for them are not cited. The LLM evidence was opened and 10 key numbers were re-checked.*

## 1. What it is

Red teaming as alternative analysis is a group of methods that attack a plan or a judgment from the inside. The goal is to find faulty logic, hidden assumptions and missing views before an outside event does it.

Three related tools get mixed up. The CIA Tradecraft Primer (2009, a01-a03) keeps them apart.

| Tool | Use it when | What it does |
|---|---|---|
| Devil's advocacy | One dominant mind-set on a judgment you cannot afford to get wrong | One analyst builds the strongest case against the mainline view and its key assumptions. The product is labelled "Devil's Advocate". |
| Team A / Team B | Two strong competing views already exist | Two teams each build a full case. Costs "significant commitment of analytic time and resources". |
| Red team analysis | You must predict an adversary | Analysts model the target's culture, organisation and person to beat mirror-imaging. |

Heuer (1999, a04) defines the devil's advocate as someone who defends a minority view, even without believing it, as hard as possible. UFMCS (the US Army red team school; courses of 6 to 9 weeks per a05/b24) uses the term more broadly, as an "internal audit of thinking". Its handbook was not retrievable (a28, d17).

For our agent the question is narrow. Which parts of this human practice can be turned into a code-gated step that attacks the agent's own plan or answer, and does it pay at equal tokens? The honest answer from the evidence: most prompted self-attack does not pay. What pays is an attack tied to an external check, and a few cheap framing tricks.

## 2. History and theories in depth

### 2.1 Military and intelligence roots
- 1960s: RAND and the US military ran red/blue Cold War games (a05, secondary source).
- 1973: Israeli Military Intelligence failed before the Yom Kippur war. The Agranat Commission (set up 21 Nov 1973; 140 sessions, 58 witnesses, about 1,500-page report; four intelligence officers recommended for dismissal; a06) blamed "the concept". This was a fixed assumption that Egypt would not attack without air power to challenge Israel's air force, and Syria would not attack without Egypt. The assumption survived contrary warnings. Israel then formed a contrarian office, Ipcha Mistabra ("the opposite is likely"). The link from Agranat to Ipcha Mistabra is stated only on a Wikipedia page (a05); the Agranat page does not mention it (critique.md).
- 1976: Team B. The CIA let 16 outside experts in three teams review Soviet strategic policy. Team B (chair Richard Pipes) said the National Intelligence Estimates underrated Soviet aims. Later checks are mixed. Team B predicted about 500 Backfire bombers; about 235 existed by 1984. It said a 1970 NIE budget estimate was half the true figure. Garthoff and Pipes disagree on whether Team B was right on core intent. The panel was chosen one-sidedly, and Bush later wrote the approach could be manipulated for ends other than accuracy (a07). Lesson: an adversarial team with no grader and a known agenda can overstate.
- 2003: Defense Science Board report on DoD red teaming (a27, not read). 2004: the Army created the Army Directed Studies Office (the first service-level red team) and UFMCS (a28, a05).
- 2004: the Intelligence Reform and Terrorism Prevention Act mandated structured analytic techniques, including alternative analysis. Mandel and Tetlock (2018, b20-b23) say these spread by prestige, not by accuracy tests. Heuer argued testing was unnecessary, which they call the "goodness heuristic".

### 2.2 Psychological theory behind it
- Assigned dissent in groups. Devil's advocacy and dialectical inquiry were compared with consensus and expert-only approaches in lab studies (Schweiger et al. 1986; Schwenk 1990 meta-analysis). Recalled only: both dissent methods gave better quality, consensus groups were happier (a08, a09, b25; not read, d15 returned 403).
- Authentic vs role-played dissent. Nemeth et al. (2001) found role-played dissent stimulates thoughts that support the original position, while real minority dissent stimulates divergent thought (a10, b26; not read, d16 returned 403).
- Consider the opposite (Lord, Lepper, Preston 1984): "be fair" did not reduce biased reading, "consider the opposite" did (b27; not read).
- Prospective hindsight (Mitchell, Russo, Pennington 1989): imagining the event has happened raised correct reasons by about 30 percent. Basis of Klein's pre-mortem (a11, b28; recalled).
- Dialectical bootstrapping (Herzog and Hertwig 2009): a second estimate after "assume your first was wrong" is partly independent; averaging beats either alone (b29; gain size not retrieved).
- Warning on one-directional correctives: telling analysts to beware overconfidence may produce the mirror bias, underconfidence and endless second-guessing. Structured techniques are loosely defined and can add noise while claiming to remove bias (Mandel and Tetlock 2018; b22, b23). In an admiralty-code study, agreement among analysts fell as source-reliability and credibility ratings varied.

### 2.3 LLM-era lineage
1. Self-reflection and self-refine papers (2023) claimed gains from self-critique.
2. Huang et al. (ICLR 2024) showed those gains used oracle labels (section 3).
3. Debate (Du 2023, Liang 2023) was proposed as a fix. Later work re-tested it against vote baselines (Huang, Smit, Wang, Zhang, Choi, Ferreira).
4. LM red teaming for safety (Perez 2022, Ganguli 2022) is a different meaning of "red team": generate attacks against a model, graded by a classifier.
5. 2025-26 work asks when self-correction works (Stav, Tsui, Hu) and what makes a model cave (Yang, Huang 2026).

## 3. Core findings with exact numbers

Evidence ids in brackets. Status is the claim-level status after the gap search.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Intrinsic self-critique (no label, no tool) lowers accuracy on older chat models | GPT-3.5 CSQA 75.8 to 38.1 (3 calls), 41.8 (5); GSM8K 75.9 to 75.1 to 74.7; HotpotQA 26.0 to 25.0. GPT-4 GSM8K 95.5 to 91.5 to 89.0; CSQA 82.0 to 79.5 to 80.0; HotpotQA 49.0 to 49.0 to 43.0. GPT-4-Turbo GSM8K 91.5 to 88.0 to 90.0. Llama-2 GSM8K 62.0 to 43.5 to 36.5 [a14, b02, b03, c01] | Huang 2024 (2310.01798) | [C] (see section 5.2) |
| Earlier gains came from oracle labels | With oracle: GPT-3.5 GSM8K 75.9 to 84.3, CSQA 75.8 to 89.7, HotpotQA 26.0 to 29.0; GPT-4 HotpotQA 49.0 to 59.0, GSM8K 95.5 to 97.5 [b01, c03] | Huang 2024 | [E] |
| Why it fails: right answers flip to wrong | GPT-3.5 kept 74.7% of GSM8K answers; correct-to-incorrect flips exceeded the reverse [b04, c02] | Huang 2024 | [E] |
| Debate loses to a vote at equal responses | GSM8K standard 76.7; self-consistency 82.5 (3), 85.3 (6), 88.2 (9); debate (3 agents, 2 rounds) about 83 at 6 to 9 responses [b05] | Huang 2024 | [E] |
| Original debate gains (against own baselines) | Arithmetic 67.0 single / 72.1 reflection / 69.0 majority / 81.8 debate; GSM8K 77.0 / 75.0 / 81.0 / 85.0; MMLU 63.9 / 57.7 / 71.1. Counter-intuitive arithmetic (200 Q): 26.0, CoT 28.0, self-consistency 29.5, reflect 27.5, MAD 37.0; GPT-4 51.0 [c06, c08] | Du 2023; Liang 2023 | [C] |
| Debate protocols vs simple baselines | Debate no reliable win; Medprompt best and cheaper; Multi-Persona about 7% below Medprompt on MedQA; Multi-Persona (devil told to disagree) lowered accuracy vs first agent's answer on medical sets [b06, c07] | Smit 2024 | [E] with K05 |
| Disagreement intensity is a large moderator | On a 376-question USMLE subset, higher prompted agreement gave about +15% (Multi-Persona), +5% (Society of Mind); lower agreement helped a counter-intuitive set [b07] | Smit 2024 | [S] (+15 not re-found, critique item 9) |
| Strong single prompt matches discussion | ChatGPT-3.5 avg (ECQA, GSM8K, FOLIO-wiki). No demo: single 67.41, MAD 63.42, Debate(3) 71.67. With demo: single 75.63, MAD 70.04, Debate(3) 73.88, CMD(6) 74.46 [b08] | Wang 2024 (2402.18272) | [E] with K05 |
| Debate vs stronger baselines | GPT-4o-mini: Society of Mind below CoT on 9 of 9 sets; ChatEval and AgentVerse above CoT on 1 of 9. Claude-3.5-haiku MMLU: only AgentVerse above CoT (+0.85); others at least 3.60 lower. AgentVerse beats CoT in about 15% of cases [c10] | Zhang 2025 (2502.08788) | [C] |
| Debate can lower accuracy over rounds | Correct-to-incorrect flips exceed the reverse in later rounds; flip chance rises with number of disagreeing peers; a weak agent drags strong ones down (GPT-4o-mini, Llama-3.1-8B, Mistral-7B; values in figures) [b09, c11] | Wynn 2025 (2509.05396) | [E] |
| Debate is a martingale; voting gets the gain | Qwen2.5-7B, 7 benchmarks, 5 agents: single 0.7205; MAD T=2 0.7377, T=5 0.7050; sparse T=2 0.7330; centralised T=2 0.6551; majority vote 0.7691. Arithmetic: vote 0.99 vs best MAD 0.84. Biased updates T=2: vanilla 0.7332, Conformist 0.7625, Follower 0.7629, oracle 0.8236 [d02] | Choi 2025 (2508.17536) | [S] |
| Mixed-model debate loses to the roster's own vote | 23 models, 11 families, 5,500+ runs. Debate +3.3 to +6.6 pts over single agent where headroom exists; at matched generations it ties or loses at 1.6x time and 3.4x tokens. 80 mixed triples: debate 88.4 vs roster vote 89.4, delta -1.04 pp, CI [-1.61, -0.52]; debate won 83 of 320 cells. One round 84.6%, two 87.2, flat to five. Mixed teams fix 63.7% of wrong round-one majorities vs 42.9% homogeneous [d03] | Ferreira 2026 | [S] |
| Random-noise placebo matches self-correction | GSM-Hard: noise placebo c=0.33, alpha=0.27 vs self-correction c=0.34, alpha=0.25 (Qwen2.5-32B c=0.45 both). Debate N_eff about 1.8 at N=30. Heterogeneous teams c 0.85 to 0.54. Qwen3-8B thinking: 87.2% solo, debate N_eff=1.02 [d04] | Bertalanic and Fortuna 2026 | [S] |
| Self-correction works with external feedback | CRITIC EM/F1: AmbigNQ 50.0/64.9 vs 42.0/58.3 without tool; TriviaQA 72.7/80.6 vs 67.3/74.7; HotpotQA 38.7/50.5 vs 34.9/46.1 (second block 59.8, 77.0, 43.1 EM) [c14]. Survey: no prior prompted self-feedback success on general tasks [a15, b16, c05] | Gou 2024; Kamoi 2024 | [E] |
| Finding the error is the weak step | BIG-Bench Mistake, 2186 traces: GPT-4 locates the mistake 52.87%; GPT-3.5 as low as 1.67 to 19 on some tasks. Backtracking at true location: multistep arithmetic +43.92 on wrong traces, -6.67 on right traces, +20.39 at a random location [b17, c04, critique] | Tyen 2024 | [S] |
| Self-correction blind spot | 14 open non-reasoning models: 64.5% average (62.8% logic/tracking); Haiku-class 52.5%, Sonnet 4 41.4%. SFT on 5,306 traces cuts 76.0%. Appending "Wait" cuts 89.3%, raises mean accuracy 156%. Accuracy base / +Wait / reasoning model: Qwen3-32B 0.045/0.793/0.894; Qwen3-14B 0.117/0.868/0.843; DeepSeek-V3 0.567/0.902/0.908. Reasoning models show about no blind spot [d01] | Tsui 2026 (2507.02778) | [E] by claim count, open models only |
| Self-correction depends on verifiability | 5 models 2025-26, 6 benchmarks, temp 0. SAT removes 65.66% of baseline errors; correct-to-wrong flips at most 2.1% on SAT vs up to 13.25% on BBEH and HLE. BBH gains: Zebra +16.2%, Web of Lies +13.4%, Time arithmetic +12.7%, NYCC +0.3%. Spearman with verifiability 0.65 (p<0.001), with reasoning load 0.54 (p=0.007). Haiku 4.5 changed its Codenames clue in about 99% of turns and lost accuracy [d05] | Stav 2026 (2606.23196) | [S] |
| Structured critique without a verifier | Blocksworld 3-5: Gemini 1.5 Pro 49.8 to 89.3; 3-7: 57.2 to 79.5; Claude 3.5 Sonnet 68 to 89.5; Logistics hard 18.9 to 32.8; Gemma-2 27B no gain [b15] | Bohnet 2025 (2512.24103) | [S] |
| Verifier value is bounded by oracle gap and fidelity | LiveCodeBench: public-test verifier (MCC 0.825) +8.14 pp; generated-test (MCC 0.248) +2.70 pp with near-zero harm vs LLM selector 4.69% harm. MATH L5: symbolic equivalence beats self-consistency +4.67 pp; LLM selectors negative. GPQA-Diamond recoverable mass 3.03%; 87.54% of pools answer-identical [d06] | Hu 2026 (2607.17531) | [S] |
| Independent verification beats joint | Llama 65B FACTSCORE: few-shot 55.9, joint 60.8, factored 63.7, factored+revise 71.4. Wikidata list precision 0.17, joint 0.29, two-step 0.36, factored 0.32 [c13] | Dhuliawala 2024 | [S] |
| Two-sided debate helps a weak judge with source access | Model judges 76% vs 48% naive; humans 88% vs 60% (QuALITY) [a22, b11] | Khan 2024 | [S] |
| Sycophancy under challenge | After "Are you sure?" Claude 1.3 wrongly admitted mistakes on 98% of right answers (GPT-4: 42). Accuracy fell up to 27% under "Are you sure" (Claude 1.3). A user-suggested wrong answer cut accuracy up to 27% (LLaMA 2) [a24, b10, c12; corrected in critique item 5] | Sharma 2024 | [S] |
| Wording of the push matters little | 103,939 replies, 8 LLMs, 200 items, 13 pressure conditions, 4 turns. McFadden R2: task 0.485, model family 0.139, tactic 0.009. Plain repetition 15.0% adoption; fallacy 12.9%; emotion 13.2%. Anchored facts conceded 1.3%; personal choices 77.0%. 84.0% of 2,453 final-turn adoptions follow the first push. Deep puzzles 19.2% and 12.5% fall to 0% at max reasoning [d07] | Yang 2026 (2610.08840) | [S] |
| But wording changes who flips | 11 frontier models, about 760,000 replays; lines asserting the opposite verdict vs lines that only challenge rank models almost unrelatedly; a planted derivation lowers release of the argued answer, a bare value does not; a wrong answer is corrected far more often than the true one is abandoned [d08] | Huang 2026 (2610.06522) | [S] |
| Self-judging bias | GPT-3.5, GPT-4, Llama 2 beat 50% at recognising their own summaries; fine-tuning on 500 examples gave over 90%; self-preference rose linearly with self-recognition [b18] | Panickssery 2024 | [S] |
| Anticipatory reflection (in-agent pre-mortem) | WebArena after 7 episodes: 23.5% vs LATS 22.7% vs Plan+Act 19.8%; plan revisions down 45%; "+3.5 points" over prior zero-shot [a23, b13, c15] | Wang 2024 (2405.16334) | [S] |
| Pre-mortem for safety | Up to 32% less harm vs zero-shot, 16% vs safety prompt; judge agreement 76.7% [d12] | InvThink 2026 | [S], not planning |
| Different models keep dissent alive without a right answer | 120 deliberations: first-choice concentration 70.9% to 46.1% (child welfare), 46.0% to 22.9% (housing); no ground truth [d13] | Sela 2026 | [S] |
| LM red teaming finds failures, needs a grader | Zero-shot: 3.7% offensive of 0.5M cases (18,444). RL: over 40%, but 78% contained the word "invisible" [a12, c18]. Human red teaming: 324 workers, 38,961 attacks, 3 sizes x 4 types [a13] | Perez 2022; Ganguli 2022 | [E] |
| LLM wargames differ from experts | 214 experts vs 80 simulated games per cell; LLMs more aggressive, scenario-sensitive; persona prompts ("pacifist", "aggressive sociopath") made no significant difference; all 5 LLMs escalated [c19, c20] | Lamparth 2024; Rivera 2024 | [E] |
| Multi-agent systems fail often | Failure rate 41% to 86.7% across 7 frameworks, 1600+ traces [b19] | Cemri 2025 | [S] |
| Human-facing devil's advocate | 48 people, 12 groups: process satisfaction 5.10 to 5.55 (p<0.01), outcome 5.31 to 5.89 (p<0.01), psychological safety not significant [b14]. GPT-4o facilitator, 1,475 people, 281 groups: more information shared, no effect on decision [c17] | Lee 2025; Alsobay 2026 | [C] |
| Physical red teams | TSA red-team agents got weapons or fake explosives through 67 of 70 times (2015) [a05, b24] | Wikipedia (secondary) | [S], not cognitive |

Data note: Huang's GPT-4 GSM8K baseline is 95.5 in b02 (series 95.5 to 91.5 to 89.0). The 91.5 start belongs to GPT-4-Turbo in b03. critique.md item 1 quotes "GPT-4 GSM8K 91.5 to 89.0", which mixes the two. Use the b02 series for GPT-4 and the b03 series for GPT-4-Turbo.

## 4. Mechanisms and models

Each model below can be coded as a small component.

### 4.1 Oracle gap and signal fidelity (Hu 2026, d06)
Net gain of any critic, selector or verifier = (share of items where a better answer exists in the pool) x (how well the signal finds it) minus (harm to items that were already right).
- Step 1: estimate the oracle gap on the task class. On GPQA-Diamond it is 3.03%, and 87.54% of pools are answer-identical, so a challenger has almost nothing to find.
- Step 2: measure signal fidelity. Public tests MCC 0.825 gave +8.14 pp. Generated tests MCC 0.248 gave +2.70 pp but near-zero harm. An LLM selector gave harm 4.69%.
- Implementation: before enabling a challenger for a task class, log (a) pool diversity under k plain samples and (b) a held-out check's pass rate. If the pool is answer-identical on most items, skip the challenge (matches G1, G12).

### 4.2 Flip accounting (Huang 2024, Wynn 2025, Huang 2026)
A revision is a transition from answer A to answer B. Log two counts: right-to-wrong and wrong-to-right. A challenge step is kept only if the second exceeds the first at equal tokens. A bare flip rate hides this (d08), so a matched no-challenge control is required to separate "corrected" from "capitulated".
- Implementation: for each item run arm P (plain) and arm C (challenge). Store both final answers and the gold label. Report net = (wrong-to-right) minus (right-to-wrong), plus the share of answers left unchanged.

### 4.3 Locate then fix (Tyen 2024, b17)
Split audit into two functions: find the first bad step, then repair from that step. The model is weak at finding (52.87% for GPT-4) and strong at fixing once told. So location must come from code: a failing test, a unit mismatch, a retrieved fact that disagrees. Control: a random-location backtrack arm. Tyen's random location also gained +20.39, so about half of the +43.92 may be plain resampling.

### 4.4 Martingale view of debate (Choi 2025, d02)
If agents update toward peers without a bias toward truth, expected belief stays put. Voting gets the gain from independent samples. Only a bias toward correction (updates that favour evidence) helps. Implementation: let a challenge change an answer only when it brings new evidence (a tool output, a retrieved line, a failed check). Otherwise keep the first answer.

### 4.5 Correlation ceiling (Bertalanic and Fortuna 2026, d04)
Team accuracy saturates at an effective size N_eff set by error correlation c. Homogeneous teams: c about 0.85; dense debate collapses diversity (N_eff about 1.8 at N=30). Random-noise revision matched real self-correction (c 0.33 vs 0.34), so in homogeneous teams the gain is re-evaluation, not content. Only mixing architectures lowered c (0.85 to 0.54). Implementation: every challenge test needs a noise-placebo arm (an irrelevant revision prompt of equal length).

### 4.6 Self-correction blind spot (Tsui 2026, d01)
Models fix an identical error when it is attributed to a user and fail when it is attributed to themselves. Post-training data lacks error-correction sequences. Appending "Wait" reduced the blind spot 89.3%. Reasoning-trained models have about none. Implementation: in the audit slot show the draft as "another agent's answer" and, for non-reasoning models, append a Wait cue. Caveat: injected errors are synthetic; natural own-errors caught when shown externally are only 4.3 to 10.8%.

### 4.7 Verifiability gate (Stav 2026, d05; Yang 2026, d07)
Self-correction benefit tracks how checkable the task is (Spearman 0.65) and reasoning load (0.54). Concession to pressure also tracks task verifiability (R2 0.485), not wording (0.009). Implementation: S0 computes a verifiability score for the class (is there a code check, a symbolic equivalence, a constraint list?). Challenge is on only above a threshold.

### 4.8 Anticipatory reflection / pre-mortem (a23, d12)
Before an action, the agent writes the likely failure and a backup; after acting it checks alignment and backtracks on mismatch; at the end it reviews the plan. Gain is small (23.5 vs 22.7). Gate it to high-stakes irreversible steps.

### 4.9 Independent verification (Chain-of-Verification, c13)
Generate verification questions from the draft, answer each in a fresh context that does not see the draft, then reconcile in code. Factored beat joint (63.7 vs 60.8).

### 4.10 Role separation (a01-a03)
Three operators, not one: (1) challenge the dominant view's assumptions, (2) build two full competing cases, (3) model the adversary from its own constraints. LLM wargames show personas do not change outcomes (c19), so the adversary must be driven by scenario facts, not a role name.

## 5. What holds up

### 5.1 Replications and consistent results
- Prompted intrinsic self-critique does not help older chat models: Huang 2024, Kamoi 2024 (partly summarising Huang), Zhang 2025 (debate side). That the earlier gains came from oracle labels is solid [E].
- External feedback helps: CRITIC (tool vs no tool, about 4 to 8 EM points), Kamoi's survey, Hu 2026 (tests). [E]
- Debate does not reliably beat a vote or a strong single prompt at equal compute: Huang, Smit, Wang, Zhang, Choi, Ferreira, Bertalanic. Five or more sources. [E]
- Debate flips right answers to wrong: Wynn 2025, Choi 2025 (martingale proof). [E]
- LLM wargames are more aggressive and less varied than experts: Lamparth, Rivera. [E]

### 5.2 Failures and contested points
- Du 2023 and Liang 2023 gains were real against their own baselines (arithmetic 67.0 to 81.8; counter-intuitive 26.0 to 37.0) but vanish against CoT or a vote at equal compute (Zhang: 9 of 9 sets below CoT for Society of Mind). Counted as contested [C], not refuted.
- "Self-critique cannot work" (K01) is now contested. Tsui 2026: reasoning models have no blind spot. Stav 2026: SAT removes 65.66% of errors. Bohnet 2025: Blocksworld 49.8 to 89.3 with no verifier. Reconciliation (untested): rule-checkable, structured tasks vs open reasoning; reasoning-trained vs chat models.
- Smit's own numbers conflict across settings: Multi-Persona was worse on medical sets (b06; c07 says about 7% below Medprompt) yet best with high agreement (b07). The moderator is disagreement intensity.
- Team B is both a cautionary case and a partly vindicated one (a07).
- Cross-family: helps as extra votes, not as debaters (Ferreira: mixed debate -1.04 pp vs roster vote). Sela: helps keep dissent alive when there is no ground truth. Bertalanic: lowers correlation. [C]
- Human LLM devil's advocate: satisfaction up, safety and decisions unchanged (b14, c17). [C]

### 5.3 Moderators
- Task verifiability and reasoning load (Stav). The strongest moderator seen.
- Model class: non-reasoning vs reasoning (Tsui). Max reasoning removed concessions on hard puzzles (Yang: 12.5% to 0%).
- Disagreement intensity in a devil agent (Smit).
- Presence of a source text for a debater (Khan).
- Prompt strength: discussion helps only without a demonstration (Wang b08).
- Decision boundary: flip effects grow several-fold near it (Huang 2026).
- Number of disagreeing peers (Wynn).

### 5.4 Interventions that worked
- Tool or test feedback in the loop (CRITIC; Hu).
- Located flaw plus repair (Tyen, with the resampling caveat).
- Factored verification (Dhuliawala).
- Appending "Wait" for non-reasoning models (Tsui).
- Cap debate at one round (Ferreira: 84.6% at round 1, 87.2 at two, flat to five).
- Majority vote over the same budget (Choi, Huang, Ferreira).
- Source-grounded two-sided debate for a weak judge (Khan).

### 5.5 Interventions that did not work
- "Review and correct" prompts with no signal (Huang).
- Red-team-style prompts: "Assume this answer could be either correct or incorrect" did not fix the self-correction loss (b03).
- Persona prompts in wargames (c19).
- More debate rounds (Choi T=5 0.7050 below T=2 0.7377).
- Fallacy or emotional pressure as a stronger challenge (no better than repetition; d07).
- A weak agent added to strong agents (Wynn).
- Single-model RL red teaming without diversity terms (Perez: 78% "invisible").

## 6. Language models

### 6.1 Self-critique
- 2023-24 chat models: GPT-3.5 CSQA fell from 75.8 to 38.1. GPT-4 GSM8K fell 95.5 to 89.0. Llama-2 GSM8K fell 62.0 to 36.5. Weaker models are hurt more (b03).
- Cause: plausible wrong options draw edits (CSQA), so correct answers get flipped.
- With oracle label: HotpotQA 49 to 59. The label, not the critique, did the work.
- 2025-26 models: gains depend on the task. SAT errors removed 65.66%. Flip harm at most 2.1% on SAT vs 13.25% on BBEH/HLE. Claude Haiku 4.5 changed its Codenames clue in about 99% of turns and lost accuracy.
- Reasoning-trained models: blind spot about zero. DeepSeek-R1 and QwQ-32B traces show perspective diversity, conflict and reconciliation which account for part of the accuracy advantage (Kim 2026, d11; abstract only). This is an internal red team learned by RL, not prompted.
- Appending "Wait": Qwen3-32B 0.045 to 0.793 (reasoning model 0.894).

### 6.2 Challenge and sycophancy
- Claude 1.3 admitted mistakes on 98% of cases; GPT-4 on 42% (Sharma). These are old models.
- 2026 data: concession depends on task verifiability (R2 0.485), not tactic (0.009). 84% of concessions come after the first push, so more rounds add little. Anchored facts conceded 1.3%.
- A planted derivation lowers release of the argued answer; a bare stated value does not (Huang 2026).
- Training-free attention steering cut pressure following by 18.8 pp and raised evidence updating 5.5 pp (He 2026, d09; abstract only).

### 6.3 Debate and multi-agent
- Du 2023: arithmetic 67.0 to 81.8 for GPT-3.5-class models.
- At equal budget: debate ties or loses to voting (Ferreira 1.6x time, 3.4x tokens; Choi 0.7377 vs 0.7691; Huang about 83 vs 88.2).
- Homogeneous debate collapses diversity (N_eff about 1.02 for a thinking model).
- A noise placebo tracks self-correction (c 0.33 vs 0.34).
- Heterogeneous teams lower correlation (0.85 to 0.54) and fix more wrong majorities (63.7% vs 42.9%), but the best use is as a vote.
- Multi-agent systems fail 41 to 86.7% in practice (Cemri).

### 6.4 Self-preference and judge bias
Models recognise and prefer their own output (Panickssery). A same-model challenger shares the blind spot. This is the base of G5 and G9.

### 6.5 Agent-level pre-mortem
Anticipatory reflection raised WebArena success to 23.5% from 19.8% (Plan+Act). InvThink cut harm 32% vs zero-shot. No planning-accuracy test exists beyond resampling.

### 6.6 Simulating adversaries
LLM nation agents escalate (5 of 5 models). Simulated teams were more aggressive than 214 experts and had "farcically harmonious" dialogue. Personas did not change outcomes. An LLM adversary needs scenario constraints and an external judge.

### 6.7 LM red teaming (safety)
Zero-shot attack generation found 3.7% failures; RL found over 40% but narrow. Human crowd attacks (38,961) showed RLHF models get harder to attack with scale (a13). Attack generators need a diversity term and an external grader.

### 6.8 Caveats
Nearly all 2025-26 sources are preprints, often single-author, on 7-9B open models. Wynn and Choi use small models. Bohnet used October 2024 checkpoints. The Tyen random-location control shows a resampling confound. No source tests a frontier cross-family challenger on tasks like ours.

## 7. What our agent should take

Schema part key: G = guardrail, S = state, O = operator, memory = S9 look-back store.

### Add now (established)

1. **Keep G9 (no debate) and G4.** Debate does not beat a vote at equal tokens; Ferreira and Choi agree with Huang. Part: G9 / G4. [E] K05, K07. Evidence a19, a20, b05, b08, c10, c11, d02, d03.
2. **Keep G2 (revise only from real output) and make it concrete.** A revision step runs only when code supplies a failing output, a retrieved line or a test result. Without it, keep the first answer. Part: G2 / S5. [E] K02, K03. Evidence a14, a15, b01, c03, c05, c14.
3. **Log right-to-wrong and wrong-to-right flips for every revision.** Net must be positive over a no-revision arm. Part: G2 / S5, S9 memory. [E] K07. Evidence b04, b09, c11, d08.
4. **Require every challenge-driven change to cite new evidence.** Pressure from peers or self moves nothing in expectation. Part: G2 / G4. [E] K07, [S] K33. Evidence c11, d02.
5. **Attack generators need an external grader and a diversity term.** Perez: 78% of RL attacks used one word. If we generate attacks (mutated inputs, adversarial cases for S4), code must grade and de-duplicate them. Part: G3 / S4. [E] K28. Evidence a12, c18, a13, c22.
6. **Adversary models must be constrained by scenario facts and checked.** Personas changed nothing in wargames. Part: O-challenge / G4. [E] K18. Evidence c19, c20, a25, a26.
7. **Do not import effect sizes from military practice.** No published accuracy metric exists; the only numbers (TSA 67 of 70) are physical tests. Treat red-team tools as unvalidated. Part: G7. [S] K19, K20; kept as a rule against adoption, not as an operator. Evidence b20-b24.

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Verifiability gate: enable any challenge step only when S0 finds a code check or symbolic equivalence; skip when the oracle gap is small | G1, G12 / S0 | [C] K01, [S] K31 | d05, d06, d07 |
| T2 | Audit slot presents the draft as another agent's output; for non-reasoning models append a "Wait" cue | G2 / S5 | [E] K29 (open models, synthetic errors) | d01, d11 |
| T3 | Locate-then-fix with code-chosen failing step vs model-chosen step vs random step | G2 / S4-S5 | [S] K04 | a16, b17, c04, c24, d06 |
| T4 | Cross-family challenger used as an extra independent vote, not as a debater | G4 / S7 | [C] K12 | d03, d04, d13, c10 |
| T5 | Cap any challenge at one exchange | G4 / S5 | [S] K32 | d03, d07 |
| T6 | Factored verification: check each claim in a fresh context that cannot see the draft | G2 / S8 | [S] K15 | c13 |
| T7 | Pre-mortem step before irreversible plan steps, gated by a high-stakes signal | O-premortem / S6 | [S] K13, K24 | a23, b13, c15, a11, d12 |
| T8 | Structured self-critique on rule-checkable planning with no tool (Bohnet-style) | G2 | [S] K14 | b15, d05 |
| T9 | Challenge intensity by task type (knowledge vs counter-intuitive) | G4 | [S] K17 | b07, b06 |
| T10 | Consider-the-opposite / dialectical bootstrapping: second estimate after "assume the first wrong", averaged | O-challenge | [S] K25 | b27, b29 |
| T11 | Assumption-listing step (Agranat): name the key assumption and search for disconfirming evidence | S1 / S6 | [S] K22 | a06 |
| T12 | Separate operators for devil's advocate, competing cases, and adversary model | O-challenge | [S] K23 | a01-a03 |
| T13 | Noise-placebo arm in every challenge test | G7 | [S] K30 | d04 |
| T14 | Authentic vs assigned dissent: challenger given independent evidence vs an assigned-opposite persona | G4 | [C] K10 | a10, b26 (not read), d16 |

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens (count prompt plus output across all calls), same items, three seeds, paired comparison. Report net flips (wrong-to-right minus right-to-wrong), accuracy delta with a 95% bootstrap interval, and harm rate on already-correct items. Include a plain self-consistency arm at equal tokens in each test.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 verifiability gate (T1) | Mixed set: code-checkable (ARC-style grid check, SAT-like constraints) and uncheckable (word puzzles, open QA) | A plain; B challenge always; C challenge only where S0 finds a check | Accuracy, harm on correct items, by verifiability stratum | B beats A on checkable items, loses on uncheckable (flip harm up to 13.25% in Stav); C gets the gain without the loss |
| B2 framing (T2) | Items where the model gives a wrong first answer | A "review your answer"; B draft shown as another agent's; C B plus "Wait" | Fix rate on wrong drafts, break rate on right drafts | B and C raise fix rate for non-reasoning models; reasoning models show about none |
| B3 locate-then-fix (T3) | Multi-step traces with a known first error (arithmetic, code with tests) | A model-located; B code-located; C random-located; D resample only | Fix rate on wrong traces, break rate on right traces | B above C and D; gap B minus C is the true location value (Tyen: 43.92 vs 20.39) |
| B4 cross-family vote vs debate (T4) | Single-answer set with headroom | A same-family vote of k; B mixed-family vote of k; C mixed debate, one round | Accuracy at equal tokens | B above A through lower correlation; C at or below B (Ferreira -1.04 pp) |
| B5 one-round cap (T5) | Items with an initial split | A 1 round; B 3 rounds | Net flips | B equal or worse (84.6 vs 87.2 pattern is flat) |
| B6 factored verification (T6) | Long answers with many claims | A joint critique; B factored; C none | Claim-level precision | B above A (63.7 vs 60.8 on FACTSCORE) |
| B7 pre-mortem gate (T7) | Multi-step planning with irreversible steps | A plain; B always pre-mortem; C gated pre-mortem; D resample at equal tokens | Plan success, extra steps | C at or above D; small effect (about 3 points) |
| B8 structured critique (T8) | Blocksworld-style planning, no verifier | A single pass; B critique x N; C vote | Plan validity | B gains on structured tasks, none on small models |
| B9 intensity (T9) | Knowledge vs counter-intuitive sets | A mild challenge; B hard challenge | Accuracy by set | Mild wins on knowledge, hard on counter-intuitive |
| B10 opposite estimate (T10) | Numeric estimation | A one estimate; B two estimates averaged; C two independent resamples averaged | Absolute error | B gain small; C may match it (resampling confound) |
| B11 assumption listing (T11) | Plans with a hidden premise | A plan; B plan plus assumption list plus disconfirming search | Premise-failure detection | B finds more only if the search returns real evidence |
| B12 dissent type (T14) | Decision items with a correct answer | A assigned-opposite persona; B challenger with independent evidence | Net flips | B above A |

Placebo (T13): add a noise-revision arm to B1, B2, B4 and B10. If a real challenge does not beat noise at equal tokens, it does not stay.

## 9. What does not transfer, and why

- Group dynamics. Psychological safety, satisfaction, status and groupthink (Schweiger, Lee, Alsobay) need several humans. A solo agent has none.
- Authentic minority dissent. Nemeth's mechanism needs a real second mind. A same-model persona is not one (K09, G4).
- Institutional design. Ipcha Mistabra, ADSO and UFMCS depend on the independence of a standing office. We have no analogue except a different model or a code check.
- Adversary modelling from culture. Red team analysis (a03) needs deep knowledge of a human opponent. Our tasks are puzzles and benchmarks.
- Physical penetration testing figures (TSA 67 of 70). Different goal.
- Human effect sizes (30% from prospective hindsight, dialectical bootstrapping gains) came from people reasoning about real events. They were not read here and LLMs may respond differently to imagining a failure.
- Debate gains from Du and Liang. They were against weak baselines and older GPT-3.5-class models.
- Findings on 7-9B open models (Choi, Ferreira, Bertalanic, Sela) may not hold for frontier models. Findings on 2023-24 chat models (Huang, Sharma) may not hold for reasoning models.
- LM safety red teaming (Perez, InvThink) concerns harm, not answer accuracy.
- Team B as a lesson in motive: a one-sided panel is a governance problem, not a reasoning mechanism.

## 10. Open questions

1. Does a frontier different-family challenger, at equal tokens, beat a same-model challenger and a plain vote on our tasks? (Ferreira says no for small models as debaters.)
2. After the random-location control, how much of Tyen's +43.92 is true location? Does a code-located fix beat model-located critique?
3. Have reasoning-trained 2025-26 models fully overcome the Huang loss, or does it return on low-verifiability tasks? Stav: still negative on BBEH and HLE (up to 13.25% flips).
4. What are the real pooled effects in Schwenk 1990 and Nemeth 2001, and does authentic vs assigned dissent replicate with LLMs? No LLM study found.
5. What does the UFMCS handbook list as tools, and has any been measured? No outcome data for Ipcha Mistabra or ADSO was found.
6. Does a pre-mortem raise planning accuracy beyond resampling? Only the safety result (InvThink) exists.
7. Does a "neutral evidence request" differ from "Are you sure?" as a challenge wording? Not isolated; Huang 2026 says wording changes who flips.
8. Does Bohnet's no-verifier gain hold beyond Blocksworld and Logistics, and for which model class?
9. Can disagreement intensity be set from a cheap signal such as pool diversity or verifiability?
10. Team A / Team B vs a single devil's advocate on forecasting: no LLM test found.
11. Does Kim 2026 (reasoning models grow internal "societies of thought") mean an explicit challenge step is redundant for reasoning models?
12. Is the Smit +15% (USMLE 376 questions, high agreement) real? Not re-located.

## 11. Sources

[V] = opened and read this session (as recorded in the evidence file; some only abstract and introduction, noted). [M] = snippet or memory only. Evidence-line ids in parentheses.

**Military and intelligence**
- [V] CIA (2009) Tradecraft Primer: devil's advocacy, Team A/B, red team analysis (a01-a03). https://www.cia.gov/resources/csi/static/Tradecraft-Primer-apr09.pdf
- [V] Heuer (1999) Psychology of Intelligence Analysis (a04). https://www.cia.gov/resources/csi/static/Pyschology-of-Intelligence-Analysis.pdf
- [V] Wikipedia, Red team (a05, b24). https://en.wikipedia.org/wiki/Red_team
- [V] Wikipedia, Agranat Commission (a06). https://en.wikipedia.org/wiki/Agranat_Commission
- [V] Wikipedia, Team B (a07). https://en.wikipedia.org/wiki/Team_B
- [V] Mandel and Tetlock (2018) Correcting judgment correctives in national security intelligence (b20-b23). https://doi.org/10.3389/fpsyg.2018.02640
- [M] Defense Science Board (2003) Role and Status of DoD Red Teaming Activities (a27). https://apps.dtic.mil/sti/pdfs/ADA430100.pdf (fetch failed)
- [M] UFMCS Red Team Handbook / ADSO (a28, d17). https://usacac.army.mil/ (seven URLs failed)

**Human psychology (not read)**
- [M] Schwenk (1990) Effects of devil's advocacy and dialectical inquiry. https://doi.org/10.1016/0749-5978(90)90051-A (a08, b25, d15; HTTP 403)
- [M] Schweiger, Sandberg and Ragan (1986). https://doi.org/10.5465/255859 (a09)
- [M] Nemeth, Brown and Rogers (2001). https://doi.org/10.1002/ejsp.58 (a10, b26, d16; HTTP 403)
- [M] Mitchell, Russo and Pennington (1989). https://doi.org/10.1002/bdm.3960020103 (a11, b28)
- [M] Lord, Lepper and Preston (1984). https://doi.org/10.1037/0022-3514.47.6.1231 (b27)
- [M] Herzog and Hertwig (2009). https://doi.org/10.1111/j.1467-9280.2009.02487.x (b29)

**LLM self-correction and critique**
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (a14, b01-b05, c01-c03)
- [V] Kamoi et al. (2024) When can LLMs actually correct their own mistakes. https://arxiv.org/abs/2406.01297 (a15, b16, c05, d10)
- [V] Tyen et al. (2024) LLMs cannot find reasoning errors, but can correct them. https://arxiv.org/abs/2311.08516 (a16, b17, c04, c24; d14 not re-opened)
- [V] Gou et al. (2024) CRITIC. https://arxiv.org/abs/2305.11738 (c14)
- [V] Dhuliawala et al. (2024) Chain-of-Verification. https://arxiv.org/abs/2309.11495 (c13)
- [V] Bohnet et al. (2025) Intrinsic self-critique for planning. https://arxiv.org/abs/2512.24103 (b15)
- [V] Panickssery, Bowman and Feng (2024) LLM evaluators favor their own generations. https://arxiv.org/abs/2404.13076 (b18)
- [V] Tsui (2026) Self-Correction Bench. https://arxiv.org/abs/2507.02778 (d01)
- [V] Stav et al. (2026) When does intrinsic self-correction help. https://arxiv.org/abs/2606.23196 (d05)
- [V] Hu (2026) Oracle gap and signal fidelity. https://arxiv.org/abs/2607.17531 (d06)
- [V] Kim et al. (2026) Reasoning models generate societies of thought (abstract only). https://arxiv.org/abs/2601.10825 (d11)

**Debate and multi-agent**
- [V] Du et al. (2023) Multiagent debate. https://arxiv.org/abs/2305.14325 (a18, c06)
- [V] Liang et al. (2023) Encouraging divergent thinking through multi-agent debate. https://arxiv.org/abs/2305.19118 (a17, c08, c25)
- [V] Smit et al. (2024) Should we be going MAD. https://arxiv.org/abs/2311.17371 (a19, b06, b07, c07)
- [V] Wang et al. (2024) Rethinking the bounds of LLM reasoning. https://arxiv.org/abs/2402.18272 (a20, b08, c09)
- [V] Zhang et al. (2025) Stop overvaluing multi-agent debate. https://arxiv.org/abs/2502.08788 (c10, c23)
- [V] Wynn, Satija and Hadfield (2025) Talk isn't always cheap. https://arxiv.org/abs/2509.05396 (a21, b09, c11)
- [V] Khan et al. (2024) Debating with more persuasive LLMs. https://arxiv.org/abs/2402.06782 (a22, b11)
- [V] Choi, Zhu and Li (2025) Debate or vote. https://arxiv.org/abs/2508.17536 (d02)
- [V] Ferreira, Liu and Zheng (2026) Beyond symmetric agents. https://arxiv.org/abs/2609.35875 (d03)
- [V] Bertalanic and Fortuna (2026) The Ringelmann effect in multi-agent LLM systems. https://arxiv.org/abs/2606.02646 (d04)
- [V] Sela (2026) Preserving disagreement. https://arxiv.org/abs/2604.26561 (d13)
- [V] Cemri et al. (2025) Why do multi-agent LLM systems fail. https://arxiv.org/abs/2503.13657 (b19)

**Sycophancy and challenge**
- [V] Sharma et al. (2024) Towards understanding sycophancy. https://arxiv.org/abs/2310.13548 (a24, b10, c12)
- [V] Yang et al. (2026) Beyond the sycophancy score. https://arxiv.org/abs/2610.08840 (d07)
- [V] Huang (2026) Anatomy of LLM sycophancy (SycoLens), abstract and introduction. https://arxiv.org/abs/2610.06522 (d08)
- [V] He et al. (2026) Suppressing pressure, amplifying evidence, abstract. https://arxiv.org/abs/2610.04329 (d09)

**Pre-mortem and agent planning**
- [V] Wang et al. (2024) Devil's advocate: anticipatory reflection for LLM agents. https://arxiv.org/abs/2405.16334 (a23, b13, c15)
- [V] Kim et al. (2026) InvThink. https://arxiv.org/abs/2510.01569 (d12)

**Red teaming of models and wargames**
- [V] Perez et al. (2022) Red teaming language models with language models. https://arxiv.org/abs/2202.03286 (a12, b12, c18)
- [V] Ganguli et al. (2022) Red teaming language models to reduce harms. https://arxiv.org/abs/2209.07858 (a13)
- [V] Rivera et al. (2024) Escalation risks from language models. https://arxiv.org/abs/2401.03408 (a25, c20)
- [V] Lamparth et al. (2024) Human vs machine wargames. https://arxiv.org/abs/2403.03407 (a26, c19)

**Human-LLM groups**
- [V] Lee et al. (2025) Conversational agents as catalysts for critical thinking. https://arxiv.org/abs/2503.14263 (b14, c16)
- [V] Alsobay et al. (2026) Bringing everyone to the table. https://arxiv.org/abs/2508.08242 (c17)
- [M] Lee et al. (2025) Amplifying minority voices. https://arxiv.org/abs/2502.06251 (c21, snippet only)

**Links to parallel subfields (not covered here):** Debiasing by training; Debiasing by structure (pre-mortem, reference class); Analysis of competing hypotheses; Good Judgment Project; Consensus and premature agreement; Dialectical reasoning; Falsificationism; Confidence and metacognition; Learned refinement and self-verification; Scenario planning; Surprisingly popular method.

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 7 established claims: 6 confirmed as written, 1 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E12.03-K03** (number corrected). Kamoi's survey supports the external-feedback point, but CRITIC with tools beats CRITIC w/o Tool by 1.6 to 8.0 EM points across tasks and backbones (text-davinci-003: +8.0, +5.4, +3.8; ChatGPT: +6.8, +1.6, +7.2), not a uniform 4 to 8. Corrected claim: Self-correction works when feedback comes from a reliable external tool (code, search, tests); CRITIC with tools beats the same loop without tools by about 2 to 8 EM points (text-davinci-003 and ChatGPT, AmbigNQ/TriviaQA/HotpotQA).
