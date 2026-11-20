# Coordination and common ground: deep document

*Subfield E13.03 of cognitive systems engineering. Relevance to our agent: background only. Sources: evidence_a-d.jsonl (a01-a33, b01-b26, c01-c30, d01-d19), claims.jsonl (K01-K28), critique.md in this folder. Status marks follow SCHEMA.md: [E] established (two or more independent sources), [S] single source, [C] contested; extra tags [H] human-only, [O] older models only.*

## 1. What it is

Common ground is what two or more parties mutually take to be known, believed or agreed, so that they can act together. Klein, Feltovich, Bradshaw and Woods (2005) say it is a process, not a stored state. People communicate, test, update, tailor and repair mutual understanding all the time (a07). The quality needed depends on the purpose. Chit-chat needs little. Handing off a patient needs a lot.

The field has three layers.

1. **Psycholinguistics of grounding** (Clark and colleagues, 1986 to 1996). How two people reach "understood well enough". Measured in lab referring tasks.
2. **Cognitive systems engineering of joint activity** (Klein, Woods, Bradshaw and colleagues, 2004 to 2005). What a machine must do to be a team member: enter a "Basic Compact", be predictable, be directable, show status and intent. Mostly conceptual, built on field incidents.
3. **LLM studies, mostly 2023 to 2026.** Do language models build common ground, track what others believe, ask when unsure, and coordinate with partners? Measured with benchmarks, simulated users and a few human-subject studies.

Why it is background only for us. Our agent is one model working on a task with a scaffold. It has no human partner in most runs. The parts that touch it are narrow:

- Whether the agent should ask or check when a task is ambiguous (a clarify gate).
- Whether it should keep written slots for what has been agreed, what is assumed, and what terms mean.
- Whether it should stay wary of multi-agent structure (it should; see G9 in SCHEMA.md).

Most of the evidence is human-team or human-LLM dialogue. Transfer to a single agent solving a bench item is by analogy. The critique file states that no study tests a grounding or clarification step inside a scaffold at equal tokens. Everything pointing at our schema is inference.

## 2. History and theories in depth

### 2.1 Grounding theory (Clark and Brennan 1991)

Source: a01-a05 (opened; a book chapter, so theory, no new data).

- **Definition.** Common ground is mutual knowledge that must be updated. The updating is grounding. The stop rule is the *grounding criterion*: the partners mutually believe the message was understood "to a criterion sufficient for current purposes" (a01). The bar is "good enough", not perfect.
- **Least collaborative effort.** Partners try to minimise the total effort of both, not the speaker's alone. A speaker may offer a rough description, let the partner repair it, and still spend less overall (a02). Example from Clark and Wilkes-Gibbs 1986: "the person ice skating that has two arms?" said with rising intonation, offering the description for acceptance.
- **Media change the price.** The chapter lists eight constraints and eleven costs, and Table 1 rates seven personal media. It is qualitative, not an empirical scale (a04).
- **Installments.** People split long items into chunks and wait for acknowledgement. Geluykens (1988), cited in the chapter: 29% of left-dislocated noun phrases in the London-Lund corpus are followed by a partner move, another 52% by a pause where the partner could nod (a03). Second-hand figures.
- **Medium effects.** Cohen (1984), read only second-hand through the chapter: many more separate identification requests by phone than face to face. Counts not given (a05). Small lab study; explanation post hoc.

### 2.2 Referring as a collaborative process (Clark and Wilkes-Gibbs 1986)

Opened this run (d07).

- Design: tangram figures. A director describes, a matcher places. Experiment 1: 8 pairs, 12 figures, 6 trials. That is 576 figure placements and 9,792 transcribed words. Error rate 2%.
- Director words per figure fell from 41 in trial 1 to 8 in trial 6, F(1,35)=44.31, p<.001. Director turns per figure fell from 3.7 to about 1, F(1,35)=79.59, p<.001. The hardest figure averaged 26.5 words per trial.
- Model: a referring act has a presentation, a judgment (accept, reject, postpone) and, if needed, refashioning by replacing or expanding the description. Heeman and Hirst (1995) made this the first computational model, using discourse plans (a15, opened; no human numbers).
- Precursor: Krauss and Weinheimer (1964) found that reference phrases get shorter with repetition (a32, not opened).

### 2.3 Conceptual pacts (Brennan and Clark 1996)

Opened this run (d08).

- Speakers who refer to an object repeatedly settle on a term with a specific partner. That term is a *conceptual pact*.
- With the same matcher, directors reused the last term in trial C1 48% of the time. After switching to a new matcher, 18%. F1(1,18)=5.18, p<.05 (by items p=.08).
- After a firm pact over four B trials, directors kept an over-informative term (for example "pennyloafer") 46% of the time in the first C trial.
- Replication record: Metzing and Brennan (2003) is the usual follow-up (a new partner using an old term cost comprehension time). It was not opened (d09). Treat as background recall only.

### 2.4 Mutual knowledge and perspective use (Keysar and colleagues)

- Keysar, Barr, Balin and Brauner (2000), opened (a13, b20). Exp 1: 20 addressees, a 4x4 shelf with some slots hidden from the director. Fixations on the hidden object: 1.01 (test) vs 0.65 (control). Total time 420 ms vs 178 ms. Addressees reached for the hidden object in 23% of test trials (none in control). Exp 2: 40 addressees; fixations 0.90 vs 0.33; time 452 vs 106 ms; reached or grabbed in about 20%.
- Reading: addressees use mutual knowledge late, as a correction, not as a first filter.
- Horton and Keysar (1996), not opened (a33): speakers under time pressure also design messages less for the partner.
- **Rival account.** Santiesteban et al. (2015), opened (b21): accuracy was .79 with a human director and .80 with a camera (F(1.01,36.51)=0.034, p=.86; N about 38). So the "egocentric error" may be object-centred spatial coding, not failed perspective-taking.
- **Moderator.** Samuel et al. (2019), opened (b22): 40 participants; faster with an informed director than an ignorant one; switch cost mainly when returning to own perspective. People are egocentric by default and flexible when cued.

### 2.5 Joint activity and the Basic Compact (Klein, Feltovich, Bradshaw, Woods 2005)

Opened (a06-a11).

- Three requirements of joint activity: **interpredictability**, **common ground**, **directability**.
- Common ground has three parts: initial common ground, public events so far, current state of the activity.
- Five kinds of mutual knowledge: roles, routines, skills, goals and commitment, stance (time pressure, fatigue, competing priorities).
- **Basic Compact.** A usually tacit agreement to coordinate, align goals, stay predictable, repair faulty beliefs when detected, and signal if one drops out.
- **Fundamental Common Ground Breakdown.** A believes B has some knowledge. B lacks it and does not know he should have it, so he does not ask. Incidents: *Viennese Waltz* (the word "presentation" meant the whole talk to the speaker and only a slide file to the assistant; handouts almost not sent), *Fuel Leak* (pilot asked "Are you having any trouble?", answer "No", leak diagnosis took another ten minutes), *Handing off an Airplane* (a08).
- **Joint action ladder** (after Clark 1996): attend, perceive, understand, act. A message can fail at any rung. A relevant reply is "downward evidence" that the lower rungs worked (a09).
- **Coordination costs.** The effort of choreographing joint work is itself a cost. Shared scripts and one-word signals cut it (relay hand-off, "stick") (a10).
- **Software as team member** (section 6 of the paper, a11): design automation to the Basic Compact; make it predictable, directable, and show status and intent.
- **Ten challenges** (Klein, Woods, Bradshaw, Hoffman, Feltovich 2004, a12): enter a basic compact, model others, be predictable, be directable, reveal status and intentions, interpret signals, negotiate goals, support collaborative planning, and more. Only titles were read.
- No numbers in these two papers. They are conceptual, built on incidents.

### 2.6 Team cognition in organisational psychology

- DeChurch and Mesmer-Magnus (2010), measuring shared team mental models, opened (b26): similarity ratings, concept mapping and questionnaires differ in how well they predict outcomes (section 3).
- DeChurch and Mesmer-Magnus (2010), team cognition meta-analysis: 231 correlations from 65 studies (b23; abstract via a search summary only, not opened).
- Mesmer-Magnus et al. (2017), opened (b24, b25): 128 independent studies. See section 3.

### 2.7 Coordination without a shared language in AI

- Hu et al. (2020) Other-Play, opened (c28): self-play agents invent private conventions that fail with new partners.
- LLM-era multi-agent work (2023 to 2026) is in sections 3 and 6.

## 3. Core findings with exact numbers

Status key: [E] established, [S] single source, [C] contested, [H] human-only, [O] older models only. "Recheck OK" means the critique re-opened the number.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Referring converges with repetition | director words per figure 41 to 8 over 6 trials; turns 3.7 to about 1; error 2%; 8 pairs, 576 placements | Clark and Wilkes-Gibbs 1986 (d07) | [E] [H] |
| Partner-specific conceptual pacts | same partner 48% term reuse vs new partner 18%; over-informative term kept 46% | Brennan and Clark 1996 (d08) | [E] [H]; replication not opened |
| Addressees do not filter by mutual knowledge first | hidden-object fixations 1.01 vs 0.65 (Exp 1, N=20); 0.90 vs 0.33 (Exp 2, N=40); reached for hidden object 23% | Keysar et al. 2000 (a13, b20) | [C] |
| Same effect may be spatial coding, not mentalising | accuracy .79 (director) vs .80 (camera), p=.86, N about 38 | Santiesteban et al. 2015 (b21) | [C] |
| Egocentric default is flexible | N=40; switch cost mainly on returning to own view | Samuel et al. 2019 (b22) | [S] |
| Shared team cognition predicts team performance | rho=.35, 95% CI .31 to .39, k=107, 7,775 teams; with process k=44 | Mesmer-Magnus et al. 2017 (b24) | [E] [H] |
| Emergence type moderates | performance: compositional rho=.39 (k=55), compilational rho=.29 (k=62); process: .32 (k=31) vs .44 (k=14, CI .02 to .86) | same (b25) | [S] |
| Shared mental models and outcomes; measurement matters | process r=.20 (k=17, N=1,238); performance r=.29 (k=19, N=1,363); process by method: similarity .24 (k=6), questionnaire .04 (k=5); performance: similarity .20 (k=9), concept mapping .28 (k=6) | DeChurch and Mesmer-Magnus 2010 (b26) | [E] [H] |
| Self-play conventions fail with humans | other-play bot 15.75 (sem 1.23), 45% bombed out; self-play bot 9.15 (sem 1.18), 85% bombed out; 20 players | Hu et al. 2020 (c28) | [S] [O] |
| LLMs presume common ground | 77.5% fewer grounding acts than humans; follow-ups -64.3%; acknowledgements -83.4%; clarifications -84.8% on TSCC; classifier macro-F1 0.89 | Shaikh et al. 2024 (a17, b01, c01); recheck OK | [E] (partial independence) |
| Timing of grounding is also wrong | human-LM kappa mostly below 0.3; ChatGPT-3.5 ESConv clarification base rate 0 | Shaikh 2024 (b02, c02) | [S] |
| Preference tuning lowers grounding | DPO kappa vs steps R about -0.79; PPO base rate -7.0%, kappa -39.0%; DPO -12.1%, -42.5%; SFT no trend (p>0.1); questions in 13.77% of preferred vs 18.35% of dispreferred answers; 11.83% in UltraChat | Shaikh 2024 (a18, b02, b03, c03) | [S] [O] |
| Prompting to ground overshoots | follow-ups 10.76 to 42.32; acknowledgements 1.05 to 2.54; clarification kappa 0 to -1.65 | Shaikh 2024 (a19, c04) | [S] [O] |
| Real-log gap persists in 2024 models | 3x less likely to clarify, 16x less likely to follow up; RIFTS accuracy 23.9 to 27.0 (chance 33); no-grounding-needed items 96.09% correct, other items 2.22% correct initiative | Shaikh et al. 2025 Rifts (d04) | [E] with Shaikh 2024 |
| Gated grounding prompt repairs timing | Llama 3.1 8B + GROUND (trained forecaster) 54.48 vs about 24 | Rifts (d04) | [S] |
| Multi-turn loss | mean -39%, 200,000+ conversations, 6 tasks; aptitude -15%; unreliability +112%; two turns already enough | Laban et al. 2025 (b09, c22); recheck OK | [S] |
| Recap recovers part | GPT-4o-mini: full 86.8, sharded 50.4, recap 66.5, snowball 61.8; GPT-4o: full 93.0, concat 90.9, sharded 59.1, recap 76.6, snowball 65.3 | Laban 2025 (c23, d05) | [S] |
| Reasoning models also lose | o3, R1, Gemini 2.5 Pro degrade like others; replies 33% longer with more assumptions | Laban 2025 (d05) | [S] |
| Ask-gate on coding tasks | N=500, Claude Sonnet 4.5: full spec 70.8; never ask 54.8; forced ask 70.4; one agent self-check 61.2; separate checker 69.4 (p<0.001 vs self-check; p=0.458 vs full). Checker asked on 344 tasks; forced on 496 | Edwards and Schuster 2026 (d01) | [S] |
| Same, second backbone | Kimi K2.6: full 72.8; never ask 55.4; forced ask 47.2 (instruction failures); self-check 61.6; checker 69.4; 8.71 queries per task | same (d01) | [S] |
| Detection is the bottleneck | interaction lifts resolve rate by up to 74%; detection accuracy 89% and 84% (best two); some at 50% chance; one model never asks | Ambig-SWE (d02) | [E] with d04, d16 |
| Structured question choice | 39% higher coverage than prompting baselines; When2Call 36.5 to 65.2 (3B), 36.7 to 62.9 (7B) after GRPO | SAGE-Agent (d03) | [S] |
| Over- and under-asking | one policy asks in 98.5% of episodes needing no question; Ask F1 0.245 vs 0.931 | BACE (d16) | [S] (number mapping uncertain) |
| Clarifying questions can raise false trust | N=180, six scenarios; more perceived understanding, less review, more erroneous answers accepted | Is That Clear? (d17) | [S] |
| No conceptual pacts in LLMs | agents verbose from round one; label overlap same for real and shuffled dyads | Aligned but not partner-specific (d12) | [E] with d13 (abstract level) |
| No spontaneous shortening | MLLMs understand shorter partner language but do not shorten their own | Hua et al. 2024 ICCA (d13) | [S] (abstract) |
| Explicit belief text helps | ToM probes (introspection / 1st / 2nd order): ChatGPT 79.0 / 41.9 / 11.6; GPT-4 80.0 / 60.0 / 64.3; GPT-4 + belief 97.2 / 80.1 / 69.4 | Li et al. 2023 (a20, c06) | [E] with Hypothetical Minds, Grounding Layer |
| Round-count gain from belief state | 12.3 vs 28.3, or 12.3 vs 11.0: unresolved | Li 2023 (c05, a20, d06) | [C] do not use |
| Status ledger helps a single agent | sensitivity 0.06 to 0.56 (DeepSeek), 0.13 to 0.49 (Qwen); 71% of errors at action selection with full history | Grounding Layer (d15) | [S] |
| ToM brittleness | original 99% chocolate; altered variants still 95% and 98% on the wrong answer | Ullman 2023 (b14, c13); recheck OK | [E] [O] |
| ToM in conversation | human 87.5 vs GPT-4 CoT 26.6 (June) and 14.8 (Oct); ChatGPT CoT 3.7; fine-tuned Flan-T5 XL 53.7; answerability: human 90.6 vs GPT-4 CoT 40.2 / 57.7 | FANToM (b15, c15); not re-opened | [E] [O] |
| Higher-order ToM | Hi-ToM GPT-4 58.11 vanilla, 59.88 CoT; GPT-3.5 27.50 / 35.50 | Hi-ToM (c14) | [S] [O] |
| Multimodal ToM | human 93.5; best model 56.4 (Gemini 1.5 Pro); GPT-4o 50.6 | MuMA-ToM (c16) | [S] (table garbled) |
| Coordination from world state strong, partner modelling weak | Hanabi mean: RL 23.92 to 24.10; GPT-4-turbo 13.33; without ToM step 10.33; without ToM and verification 4.33; GPT-4o 8.33; GPT-3.5 1.33; CoordQA 198 items | LLM-Coordination (b13, c11) | [E] |
| Modular LLM agent cooperates | C-WAH steps 57 (CoELA pair) vs 75 (MHP pair); TDW-MAT 0.71 vs 0.61; trust 6.3 vs 4.7 without talk, p=0.0003 | CoELA (c08, c09) | [S] |
| Teammate-intention verifier | over 10% gain; success 20% over 100 steps without the Verificator | ProAgent (c10) | [S] |
| Hypotheses-about-partner scaffold | beats baselines in all environments, 30 scenarios; hypothesis testing and refinement are the key parts | Hypothetical Minds (b19, c17) | [S] |
| Human-AI teams underperform best single party on average | g=-0.23, CI -0.39 to -0.07; 106 experiments, 370 effect sizes; decision g=-0.27 (CI -0.44 to -0.10); creation g=+0.19 (CI -0.09 to 0.48, n=34); moderator F(1,104)=7.84, p=.006 | Vaccaro et al. 2024 (b06-b08) | [E] for the sign; mixes AI types |
| Human-agent beats autonomous | win rates 86% / 74% / 66% (travel, tabular, related work); communication failures 65%, situational awareness 40% in real use | Collaborative Gym (a23, c20) | [S] |
| Free interleaving beats strict turns | travel performance 0.84 vs 0.81; satisfaction 3.95 vs 3.55, p=0.012; win 70% | same (a24, c21) | [S] |
| Multi-agent LLM failure taxonomy | 1,642 traces, 7 frameworks, failure rates 41% to 86.7%; shares: design 41.8%, misalignment 36.9%, verification 21.3%; clarification failure 6.80%, ignoring input 1.90%, reasoning-action mismatch 13.2%; kappa 0.88 | MAST (a21, b04, c18); recheck OK | [S] |
| Fixes | +9.4% ChatDev (cause named two ways in the paper); +15.6% ProgramDev from a verification step | MAST (a22, b05, c19) | [S] |
| Task structure decides if agents help | 260 configurations, 6 benchmarks, 5 architectures: +80.8% to -70.0%; negative returns above about 45% single-agent accuracy (beta=-0.236, p=0.004); error amplification single 1.0, centralised 4.4, decentralised 7.8, hybrid 5.1, independent 17.2 (coefficient p=0.658 after controls) | Kim et al. 2026 (b16, b17, d10); recheck OK | [S] |
| Debate does not beat sampling | 5 methods, 9 benchmarks, 4 models | Stop Overvaluing MAD (b18, c25) | [E] with SCHEMA G9 |
| Blackboard design | +4.33% over CoT, +5.02% over static multi-agent | Han and Zhang 2025 (c26) | [S] |
| Common-ground tracking is hard | move F1 0.61; common ground annotation F1 0.54; action F1 0.67; Dice with axiomatic common ground 0.219 to 0.382 | Khebour 2024, Zhu 2026 (a25, a26, c27) | [E] |
| Seeing partner's view inflates assumed understanding | 13,077 expressions; recall on aligned .590 to .822, on not-aligned .677 to .518; yes-rate .515 to .727 | Li, Gatt, Poesio 2026 (a27) | [S] |
| Sycophancy corrupts common ground | violations in more than 40% of conversations; steering 45.3 to 31.3 and 47.1 to 39.1; guardrail prompt only to 44.0 and 44.1 | Sarkar et al. 2026 (a28) | [S] |
| Models communicate too literally | literal clues 60% of the time; explicit common ground cuts literal clues 30% to 50% | Ahuja et al. 2026 (a29) | [S] |
| Referential-task collapse | PARLEY N=400, success 60.5%; Tangram 34.0%; grounding failures 17.4% of instances; failure-taxonomy prompt 60.5 to 70.5 (+10.0 pp, p=.019, N=200) | Hernandez and Wilson 2026 (d11) | [S] |
| Training for multi-turn rewards | +18.5% task performance, +13.3% efficiency, +46.3% interactivity (LLM judge); N=201 user study: satisfaction +17.6%, time -10.4% | CollabLLM (b11, c30) | [S] |
| Teamwork-theory scaffold | 49.4% average over 8 medical sets vs 48.4 to 51.6% for four MAS baselines; lower token cost | TeamMedAgents (a31) | [S] |
| Roles act through a submission gate | forcing submission: recovery 0.198 to 0.613 (400 Omni-MATH problems); role-free minus role-structured +0.009, CI -0.014 to +0.033 | Beyond Division of Labor (d19) | [S] |

## 4. Mechanisms and models

Each model below is written so an engineer could build it. All are conceptual models of human or agent behaviour; none is validated as a single-agent scaffold at equal tokens.

### 4.1 Contribution cycle with a grounding criterion (Clark and Brennan)

State per shared item (a fact, a referent, a plan step): `{content, status, evidence}`.

1. Speaker presents the item.
2. Partner gives evidence: continued attention, relevant next turn, acknowledgement, demonstration, display of understanding, or repeat-back.
3. Speaker checks the evidence against a *criterion* set by the purpose and the cost of error.
4. If the criterion is met, status becomes "grounded". If not, repair: rephrase, expand or ask.

Implementation notes:
- The criterion is a threshold per task, not a constant. High stakes raise it.
- Cost matters. Where checking is cheap, check more; where each exchange is costly, accept weaker evidence (least collaborative effort).
- For a single agent without a partner, "evidence" can be external: a tool result, a test, a re-read of the task text.

### 4.2 Joint action ladder (Clark 1996; Klein 2005)

Four levels: attend, perceive, understand, act. A message fails if any rung fails. Evidence at a higher rung implies the lower ones. Use as a debugging checklist for failed exchanges: was the thing seen, read correctly, understood as intended, then done? MAST's misalignment share (36.9%) can be mapped to rungs.

### 4.3 Perspective use as late correction (Keysar) and the rival

Default-and-correct process: resolve a reference from own knowledge, then check against the partner's view, then repair. The rival account (Santiesteban 2015) predicts the same errors from spatial coding with no mentalising. Practical point for an agent: its first interpretation may use information the partner does not have. A written "who knows what" slot with a check before committing makes the correction explicit.

### 4.4 Common ground tracking as banks (Khebour et al. 2024)

Three stores: **FBank** (facts the group accepted), **EBank** (evidence for and against), **QBank** (open questions under discussion). A classifier labels each utterance as a move (statement, accept, doubt). Accepted statements move from QBank to FBank. Result: move F1 0.61, common-ground F1 0.54 (a25, c27). A 2026 follow-up shows prompted LLMs reach Dice 0.219 to 0.382 against the axiomatic common ground (a26).

### 4.5 Status ledger for proposals (Grounding Layer, d15)

Keep each proposal with a status: accepted, unacknowledged, revised, scoped. The agent acts only on accepted items. Sensitivity rose from 0.06 to 0.56 (DeepSeek) and 0.13 to 0.49 (Qwen). With full history, 71% of errors still happened at action selection although status was visible. So the ledger has to gate the action, not just sit in context.

### 4.6 Belief-state and hypothesis scaffolds (Li 2023; Hypothetical Minds; ProAgent)

- Li et al.: add an explicit text block of what each agent believes about the world and about the other agent; update each round.
- Hypothetical Minds: generate hypotheses about the partner's strategy, score each by how well it predicts observed behaviour, refine (b19, c17).
- ProAgent: infer the teammate's intention, check it with a verifier module, correct from observed behaviour (c10).
All three assume a partner whose behaviour is observed. Without a partner, only the write-down-and-check part transfers.

### 4.7 Ask-or-assume gate (Edwards and Schuster; BACE; SAGE-Agent)

Pipeline from d01:
1. A separate checker call reads the task and the proposed plan.
2. It decides whether key slots are missing. It does not solve the task.
3. If yes, the agent asks; the (simulated) user answers; the agent continues.
4. If no, proceed.

The separate checker asked on 344 of 500 tasks (3.06 questions per task); forced-ask asked on 496 (1.02 per task). One agent self-checking asked on 369 but reached only 61.2. So separating the detector from the solver mattered. The paper reports no equal-token comparison.

BACE (d16) uses a small belief-tracking chooser (27.7M parameters) on a frozen model to pick how many questions to ask. SAGE-Agent picks which question by expected value of information over tool parameters (d03).

### 4.8 Coordination cost and task structure (Kim et al. 2026)

A regression over 260 configurations predicts the best architecture in 87% of held-out cases (cross-validated R2 0.373). Key terms: task decomposability (helps multi-agent), tool count (hurts), and a single-agent baseline above about 45% (more agents give negative returns, beta=-0.236, p=0.004). Centralised verification contains error propagation (4.4x vs 17.2x for independent). The error amplification coefficient itself is not significant after controls (p=0.658), so the causal story is weak.

### 4.9 Basic Compact as a requirement list (Klein 2004, 2005)

For a software teammate: enter and keep the compact; model others; be predictable; be directable; show status and intent; read signals; negotiate goals; support planning. No one has measured these as separate variables on LLM teammates (K27). Descriptive failure taxonomies exist: 695 incidents in 12 failure modes (all at both low and high autonomy), and 163,487 Reddit posts in 23 categories in 7 groups (d18).

## 5. What holds up

### 5.1 Replications and rival accounts

| Claim | Check | Result |
|---|---|---|
| Referring shortens with repetition (Clark and Wilkes-Gibbs) | Krauss and Weinheimer 1964 found the same direction (a32, not opened); d07 numbers read | Holds for humans. Large, 41 to 8 words. |
| Conceptual pacts are partner-specific (Brennan and Clark) | Same vs new partner 48% vs 18%; by-items p=.08 | The by-subjects effect is significant, the by-items test is not. Follow-up (Metzing and Brennan 2003) not opened. Treat as likely but not fully checked. |
| Addressees ignore mutual knowledge early (Keysar 2000) | Santiesteban 2015: director vs camera .79 vs .80 | Contested. The same pattern can come from spatial coding. Samuel 2019 shows the default flips after a cue. |
| Shared mental models predict performance | Two meta-analyses, 65 then 128 studies; rho=.35 | Holds in humans. Depends on how the model is measured (questionnaire r=.04 for process, similarity r=.24). Moderated by compositional vs compilational emergence. |
| LLMs do not ground (Shaikh 2024) | Rifts 2025 on real logs; Laban 2025; Ambig-SWE | Holds for 2024 to 2025 models. Same research group for the first two; independence partial. No 2026 frontier test. |
| Belief-state text helps LLM teams | Li 2023 probes; Hypothetical Minds; Grounding Layer | Holds for probe accuracy and valid actions. The round-count gain cannot be tied to the belief condition. |
| LLM theory of mind is robust | Ullman 2023; FANToM; Hi-ToM; MuMA-ToM | Fails. Trivial changes flip answers. Humans 87.5 vs GPT-4 CoT 14.8 to 26.6 on FANToM. All tested models are 2023 to 2025. |
| Multi-agent debate adds value | Stop Overvaluing MAD, 5 methods x 9 benchmarks x 4 models | Fails against CoT and self-consistency. Agrees with SCHEMA G9. |
| Role prompts fix multi-agent failure (MAST +9.4%) | Later work (d19) | No replication found. The paper itself names the cause two ways (role specification or CEO final say). Later work shows roles act through a submission gate. |

### 5.2 Failures and null results worth keeping

- Supervised instruction tuning does not raise grounding (p>0.1 on 10 checkpoints). Preference tuning lowers it (a18).
- A prompt telling the model to ground gave 10.76 to 42.32 follow-ups and made timing worse (clarification kappa 0 to -1.65). Frequency is easy to change. Timing is not (a19).
- A guardrail prompt against sycophantic deference barely helped (45.3 to 44.0, 47.1 to 44.1). Activation steering did (to 31.3 and 39.1) (a28). Steering is not available to a scaffold.
- Telling a model to encourage asking changes behaviour unevenly. One model got worse with stronger encouragement (d02).
- Forced asking is not safe. On Kimi K2.6 it scored 47.2, below never-ask (55.4), from instruction-following errors (d01).
- Clarifying questions can raise false trust: users reviewed less and accepted more wrong answers (N=180, d17).
- Seeing the partner's view raised accuracy and also over-predicted shared understanding (yes-rate .515 to .727, a27).
- Multi-agent coordination hurts on sequential tasks (-70.0%) and above about 45% single-agent accuracy (Kim 2026).

### 5.3 Moderators

- **Medium and cost** (Clark and Brennan): what is cheap to check gets checked.
- **Task structure** (Kim 2026): decomposable tasks gain (+80.8%), sequential tasks lose (-70.0%).
- **Relative skill** (Vaccaro 2024): when the human beats the AI alone, the combination gains. When the AI beats the human, it loses. Task type: decisions lose (g=-0.27), creation tends to gain (g=+0.19, not significant).
- **Interaction mode** (Collaborative Gym): free interleaving with notifications beat strict turns (satisfaction 3.95 vs 3.55, p=0.012).
- **Task completeness**: the same content given all at once (CONCAT 84.4 / 90.9) beats the sharded version (50.4 / 59.1) by about 30 points. So the loss is from delivery in pieces, not from capacity (Laban).
- **Model size**: CONCAT degradation is larger for smaller models (b10).
- **Partner view visibility** (a27): more shared view, more assumed agreement.
- **Measurement method** for shared mental models (b26).

### 5.4 Interventions that worked

- Separate ambiguity checker before acting: 69.4 vs never-ask 54.8 (d01). Detection by a second call, not self-check.
- Forecaster-gated grounding prompt: about 24 to 54.48 (d04). Needs a trained forecaster.
- Recap of earlier turns in the final message: 66.5 and 76.6 vs sharded 50.4 and 59.1. Recovers about 52% of lost points for GPT-4o. Snowball (repeat all every turn) about 18% (d05). Costs extra tokens.
- Explicit belief or status text: probe gains (Li 2023), sensitivity 0.06 to 0.56 (d15).
- Failure-taxonomy prompt on PARLEY: +10.0 points (60.5 to 70.5, p=.019), longer prompt not controlled (d11).
- Verification step: +15.6% ProgramDev (a22); Hanabi without ToM step 10.33, without ToM and verification 4.33 vs 13.33 with both (c11).
- Training for multi-turn reward (CollabLLM): +18.5% task, +46.3% interactivity (training, not a scaffold).

### 5.5 Interventions that did not work

- Prompting to ground (overshoot, bad timing).
- Single-agent self-check for ambiguity (61.2 vs 69.4 for a separate checker).
- Always-ask (forced) on poorly calibrated models.
- Anti-sycophancy guardrail prompt.
- Multi-agent debate.
- Temperature 0 for sharded unreliability (d05).
- Reasoning models for the multi-turn loss (o3 and R1 degrade like others).

## 6. Language models

### 6.1 Do they ground?

No. Off-the-shelf models make 77.5% fewer grounding acts than humans in the same dialogue context (Shaikh 2024, GPT-3.5 and older open models). On real logs they are 3x less likely to clarify and 16x less likely to follow up (Rifts, WildChat, MultiWOZ, Bing Chat). On the Rifts test, GPT-4o 25.26, 4o-mini 24.48, o3-mini 25.26, Claude 3.5 Sonnet 26.95, Opus 3 24.57, Llama 3.1 8B 24.22 and 70B 23.88, all below the 33% chance level. The benchmark was built from cases where GPT models failed, so absolute scores are biased low. Models are good where no grounding is needed (96.09%) and near zero where it is (2.22% correct initiative).

Cause. Preference tuning. DPO kappa falls with training steps (R about -0.79); preferred answers contain fewer questions (13.77% vs 18.35%). Not proven for 2026 RLHF pipelines.

### 6.2 Do they notice that a task is underspecified?

Rarely. Ambig-SWE: detection accuracy 89% (Claude Sonnet 4) and 84% (Claude Sonnet 3.5) were the only good ones, others near 50%, one never asked. Once they ask, they use the answer well (resolve rate up to +74%). On BACE one policy asked in 98.5% of episodes that needed no question. Detection is the bottleneck, not use (K24).

### 6.3 Gating when to ask

Edwards and Schuster (N=500, SWE-bench Verified, simulated oracle user, Claude Sonnet 4.5): never ask 54.8, forced ask 70.4, single-agent self-check 61.2, separate checker 69.4, full spec 70.8. The separate checker is statistically level with the full spec (p=0.458) and beats the self-check (p<0.001). The result is one benchmark and two backbones. Token cost is not matched (3.06 questions per task vs 1.02).

### 6.4 Do they lose the thread over turns?

Yes. Laban 2025: -39% mean over 6 tasks, 15 models, 200,000+ simulated conversations. Aptitude falls about 15%, unreliability rises 112%. The loss shows even with two turns. Mechanisms: early wrong assumptions, premature full answers, over-reliance on the model's own earlier answer, bloated later answers. Reasoning models (o3, R1) lose similarly and write 33% longer replies with more assumptions. Recap helps part way (GPT-4o 59.1 sharded to 76.6, full 93.0).

### 6.4a What a scaffold can do about it

A rule such as "hold assumptions open; do not give a full answer until slots are filled" is suggested by the mechanisms, but no paper tests it at equal tokens. The recap result is the closest measured intervention.

### 6.5 Do they track what others believe?

Poorly and brittly.
- Ullman 2023: GPT-3.5 gives 99% chocolate on the original false-belief item and still 95% and 98% on altered versions where the answer should change.
- FANToM (information asymmetry in conversations): human 87.5 vs GPT-4 CoT 26.6 (June) and 14.8 (Oct). Models answer from the full view, not the person's limited view.
- Hi-ToM: GPT-4 58.11 vanilla and 59.88 with CoT; accuracy falls with belief order.
- MuMA-ToM: human 93.5; best model 56.4.
- Li 2023 (bomb game): GPT-4 80.0 / 60.0 / 64.3 (introspection / first / second order) vs ChatGPT 79.0 / 41.9 / 11.6. Writing the belief state down raised GPT-4 to 97.2 / 80.1 / 69.4.
All are 2023 to 2025 models. No 2026 frontier model was tested in these four benchmarks.

### 6.6 Coordination games

LLMs match or beat RL when coordination is solved from visible world state (Overcooked) and trail when they must model a partner (Hanabi GPT-4-turbo 13.33 vs RL 23.92 to 24.10). In Hanabi, dropping the ToM step cut GPT-4-turbo to 10.33 and dropping ToM and verification to 4.33. Environment comprehension correlates strongly with success; ToM only moderately (c12; column mapping unverified). LLM agents adapt to unseen partners, unlike self-play RL (b13). CoELA (modular memory, communication, planning) gave over 40% efficiency gain and human trust 6.3 vs 4.7 without talk (p=0.0003).

### 6.7 Do they form conventions with a partner?

No. Humans compress descriptions over rounds and raise label overlap with a specific partner. Agents stay verbose from round one, and their label overlap is the same for real and shuffled dyads (d12, abstract level). ICCA (Hua 2024): no spontaneous efficiency gain over rounds; some models adapt only with heavy prompting (d13, abstract level). LLMs succeed by verbose description, not shared shorthand.

### 6.8 Sycophancy and deference

Qwen3-VL-32B as Player 2 deferred to a partner against its own private image in more than 40% of conversations (45.3% and 47.1%). Anti-sycophancy steering cut it to 31.3% and 39.1%. A guardrail prompt barely moved it (44.0%, 44.1%) (a28). PARLEY authors report excessive compliance, not egocentric bias (d11). So the human egocentric default (Keysar) is not the main LLM failure mode.

### 6.9 Understanding vs sharing

Giving a vision-language model both maps raised macro-F1 from .591 to .671 but also raised the share of "aligned" answers from .515 to .727, over-predicting shared understanding (a27). Frontier models give literal clues 60% of the time and cannot infer whether common ground exists when it is not stated (a29).

### 6.10 Multi-agent LLM systems

- MAST: 41% to 86.7% failure across 7 frameworks, 1,642 traces; 41.8% design, 36.9% misalignment, 21.3% verification.
- Scaling: gains +80.8% on decomposable work, losses -70.0% on sequential planning; independent agents amplify errors 17.2x, centralised 4.4x (trace level; coefficient not significant after controls).
- Debate: no consistent gain over CoT or self-consistency at higher cost.
- Blackboard: +4.33% over CoT and +5.02% over static multi-agent (one source).
- Human-agent: win rates 86 / 74 / 66%, communication failures 65%.
- Real-world failure reports: 695 coded incidents (12 failure modes), 163,487 Reddit posts (23 categories).

### 6.11 Human-AI teams

Meta-analysis of 106 experiments: g=-0.23 on average (CI -0.39 to -0.07). Decision tasks g=-0.27; creation tasks g=+0.19 (not significant). Most studies predate LLM chat agents; the "AI" mix is mostly not LLM. The abstract lists publication bias as a limit.

## 7. What our agent should take

Relevance is background only. Status marks: [E] established, [S] single-source, [C] contested. Nothing below is a measured result for our agent. Evidence ids refer to the evidence files; K ids to claims.jsonl.

### Add now (established)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Do not trust fluent statements about what another party believes or knows. Treat a model's own claim about a partner's view as unverified. | G (matches G10) | [E] | K16: b14, c13, b15, c15, c14 |
| Do not add debate or a multi-role internal split for sequential single-answer work. | G9 (already in schema) | [E] | K11: b18, c25, b16; K10 |
| When a task is ambiguous, the main failure is not noticing. Put the ambiguity check at the start (S0/S1), and make it a separate step from solving. | S0/S1 | [E] for "detection is the bottleneck" | K24: d02, d04, d05; gated version is [S] (K23) |
| Assume common ground is missing until shown. Do not treat "the user saw the same material" as "the user understood". | G | [E] | K04: a17, b01, c01, d04; K18 (a27, a29, d17) is [S] |
| Do not rely on the model to form shared shorthand with a partner; any agreed term must be written down explicitly. | memory | [E] that LLMs do not form pacts (the ledger's benefit is untested, see T3) | K25: d07, d08, d12, d13 |

Note. The "Add now" list is short on purpose. These items state what models do not do. None is a measured gain for our agent; those are in Test first. The G7 rule applies: each addition must win at equal tokens before it is kept.

### Test first

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Ambiguity-gated clarify step: a separate check call decides whether slots are missing; ask only then; else act with assumptions written down | G / S1 | [S] | K23: d01, d02, d03, d16; K06: a19, d04 |
| Written agreement ledger (accepted, unacknowledged, revised, scoped) that gates which items the agent acts on | S / memory | [S] | K28: d15 |
| "What the other party believes" slot (only if tasks involve a simulated user or asymmetric information) | S | [E] for probe accuracy, round-count gain [C] | K15: a20, c06, b19, c17, d15 |
| Hold assumptions open; no full answer until needed slots are filled; recap of collected constraints before answering | S/O | [S] | K07: b09, c22, c23, d05 |
| Final verification step before submit | S8 (existing) | [S] for multi-agent | K09: a22, d19; c11 |
| Scratch ledger (shared-board design in one context) | memory | [S] | K21: c26 |
| Own conventions check: re-read own labels as a fresh reader | S9 / memory | [S] | K20: c28 |
| Treat having asked as not aligned (do not lower guard after a clarifying answer) | G | [S] | K26: d17 |

## 8. Concrete tests on our bench

All tests use both arms at equal total tokens (count setup, calls, and extra questions). The baseline arm gets spare tokens as extra samples with code selection (G4, G5). Items are from our existing bench unless noted.

| ID | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Underspecified items: take solvable items and delete one needed slot (a number, a referent, a format); keep the full item as a ceiling. | (a) plain, never ask; (b) always ask once; (c) separate ambiguity check then ask only if flagged; oracle answers from the removed slot. Equal tokens. | Accuracy; questions per item; false-ask rate on complete items; detector accuracy alone | (c) near full-item accuracy with fewer questions than (b). Based on d01: 69.4 vs 70.4 vs 54.8. Expected benefit smaller than in coding because bench items are short. |
| T2 | Sharded items: split each item into 3 to 5 turns of facts | plain vs recap-before-answer vs "no answer until all slots filled" vs one-turn concat (ceiling) | Accuracy; premature-answer rate; tokens | Recap recovers part of the gap (Laban: about 52% for GPT-4o). Check whether a slot-filled rule adds beyond recap. |
| T3 | Ambiguous-term items (word with two readings, as in the "presentation" example) | plain vs gloss-the-referent step vs term ledger across a session of 10 to 20 items | Wrong-referent rate; re-description length | Fewer wrong-referent actions with a gloss step. Ledger benefit only appears in long sessions. |
| T4 | Asymmetric-information items (FANToM style: someone leaves the room) | plain vs belief ledger (who knows what) vs CoT | Belief-choice accuracy; strict all-question score | Ledger raises accuracy over plain; CoT alone small gain. Probe numbers from Li 2023 suggest large gains on 1st and 2nd order, but only for GPT-4-class models. |
| T5 | Items where the user proposes then revises a plan | plain vs agreement ledger (accepted, unacknowledged, revised) | Action-selection accuracy; execution of unacknowledged items | Fewer actions on unacknowledged items (d15: sensitivity 0.06 to 0.56). |
| T6 | Sequential vs decomposable items | single agent vs internal role split at equal tokens | Accuracy per class | Role split loses on sequential, may gain on decomposable (Kim 2026). Only needed if we consider splitting. |
| T7 | Items with a confirming clarifying question | ask and proceed vs ask and then verify the reply against the original text | Accept-wrong-answer rate | Tests the false-trust effect (d17) on the agent's own handling of answers. |

Also run a detector check: label 100 items ambiguous or complete and measure the checker's accuracy alone. Ambig-SWE shows some models near chance.

## 9. What does not transfer, and why

- **Partner-specific pacts and shortening.** Our agent has no stable partner across a session in most runs. Pacts need repeated rounds with one person.
- **Mutual knowledge and perspective-taking.** The agent has no partner view to mismodel in single-agent bench items.
- **Team mental model meta-analyses.** Human teams, correlational, with different measurement methods. Mesmer-Magnus and DeChurch results say nothing about one model.
- **Human-AI team synergy.** The meta-analysis mixes AI types and mostly predates LLM agents. Hand-off design is not our problem.
- **Multi-agent failure taxonomies and scaling laws.** They describe multi-agent frameworks. Our rule is single agent, so they serve as a checklist and a warning, not as a design to adopt. The regression's causal term is not significant (p=0.658).
- **Training-side fixes** (CollabLLM, DPO analysis, GRPO question choosers). We do not train.
- **Trained forecaster for when to ask** (Rifts GROUND, BACE chooser). Requires training a small model. Only the idea of a separate gate transfers.
- **Klein et al.'s Basic Compact for software teammates.** Conceptual, for long-lived human-machine teams. No measurements on LLMs.
- **Egocentric bias.** For LLMs the reported failure is over-compliance, not egocentrism (d11, a28).
- **Simulated users.** Several results use LLM-simulated users. A real person's answers are noisier and costlier.

## 10. Open questions

1. Does an ambiguity-gated clarify step beat never-ask and always-ask at equal tokens on single-turn items? (d01 has no equal-token test.)
2. Do 2026 frontier and reasoning models still show the grounding gap? Rifts covers only o3-mini as a reasoning model.
3. Is the Li 2023 round-count gain real? The table text is garbled; 28.3 vs 12.3 and 12.3 vs 11.0 conflict.
4. Does recap, snowball or a slot-filled rule at equal tokens recover the Laban loss?
5. Replication record for conceptual pacts (Metzing and Brennan 2003 not opened).
6. Any measured test of predictability and directability on LLM teammates (K27: none found).
7. Cause of MAST +9.4%: role specification, CEO final say, or a submission gate (d19 suggests a gate). No replication found.
8. Does the DPO grounding drop show in current RLHF models, and can a prompt repair timing without a trained forecaster?
9. Does the spatial-coding account hold for LLM referential errors? (PARLEY points to over-compliance instead.)
10. Does a single agent with an internal verifier show the 17.2x vs 4.4x pattern? Kim 2026 never ran it.
11. Is the 77.5% gap an artifact of comparing to human supporters in therapy-like corpora (ESConv, TSCC, P4G)?
12. How much of the clarifying-question gain on benchmarks survives with real users, given the false-trust result (N=180)?

## 11. Sources

[V] = opened and read this run (page or PDF text); [M] = snippet, abstract skim or not opened.

- [V] Clark & Brennan (1991) Grounding in communication (a01,a02,a03,a04) https://collablab.northwestern.edu//CollabolabDistro/nucmc/ClarkAndBrennan-GroundingInCommunication-1991.pdf
- [V] Cohen (1984), as reported in Clark & Brennan (1991) (a05) https://collablab.northwestern.edu//CollabolabDistro/nucmc/ClarkAndBrennan-GroundingInCommunication-1991.pdf
- [V] Klein, Feltovich, Bradshaw, Woods (2005) Common ground and coordination in joint activity (a06,a07,a08,a09,a10,a11) https://raw.githubusercontent.com/papers-we-love/papers-we-love/refs/heads/main/software_engineering_orgs/common-ground-and-coordination-in-joint-activity.pdf
- [V] Klein, Woods, Bradshaw, Hoffman, Feltovich (2004) Ten challenges for making automation a team player in joint human-agent activity (a12) https://fermatslibrary.com/s/ten-challenges-for-making-automation-a-team-player-in-joint-human-agent-activity
- [V] Keysar, Barr, Balin, Brauner (2000) Taking perspective in conversation: the role of mutual knowledge in comprehension (a13,b20) https://www.coli.uni-saarland.de/~masta/WS13/Keysar_etal_00.pdf
- [M] Clark & Wilkes-Gibbs (1986) Referring as a collaborative process (a14) https://web.stanford.edu/~clark/1980s/Clark.Wilkes-Gibbs.86.pdf
- [V] Heeman & Hirst (1995) Collaborating on referring expressions (a15) https://arxiv.org/pdf/cmp-lg/9504003
- [M] Brennan & Clark (1996) Conceptual pacts and lexical choice in conversation (a16) https://typeset.io/pdf/conceptual-pacts-and-lexical-choice-in-conversation-2zo2x2dwcx.pdf
- [V] Shaikh, Gligoric, Khetan, Gerstgrasser, Yang, Jurafsky (2024) Grounding gaps in language model generations (NAACL) (a17,a18,a19) https://arxiv.org/pdf/2311.09144
- [V] Li, Chong, Stepputtis, Campbell, Hughes, Lewis, Sycara (2023) Theory of mind for multi-agent collaboration via large language models (EMNLP) (a20) https://arxiv.org/pdf/2310.10701
- [V] Cemri, Pan, Yang et al. (2025) Why do multi-agent LLM systems fail? (MAST) (a21,a22) https://arxiv.org/pdf/2503.13657
- [V] Shao et al. (2026) Collaborative Gym: a framework for enabling and evaluating human-agent collaboration (ICLR) (a23,a24,c20,c21) https://arxiv.org/pdf/2412.15701
- [V] Khebour, Lai, Bradford, Zhu, Brutti, Tam, Tu, Ibarra, Krishnaswamy, Pustejovsky (2024) Common ground tracking in multimodal dialogue (LREC-COLING) (a25) https://arxiv.org/pdf/2403.17284
- [V] Zhu, Bradford, Lai, Obiso, Venkatesha, Pustejovsky, Krishnaswamy (2026) Distributed Partial Information Puzzles: examining common ground construction under epistemic asymmetry (a26) https://arxiv.org/pdf/2603.05450
- [V] Li, Gatt, Poesio (2026) Seeing is not sharing: some vision-language models overestimate common ground in asymmetric dialogue (a27) https://arxiv.org/pdf/2606.31719
- [V] Sarkar, Srikanth, Gupta, Bonial, Resnik, Rudinger (2026) Sycophancy undermines epistemic vigilance in cooperative vision-language tasks (a28) https://arxiv.org/pdf/2607.29585
- [V] Ahuja, Li, Lampinen (2026) Beneath the surface: investigating LLMs' capabilities for communicating with subtext (a29) https://arxiv.org/pdf/2604.05273
- [V] Chen, Sun, Lu, Wang, Wang, Yao (2026) CollabSim: a CSCW-grounded methodology for investigating collaborative competence of LLM agents (a30) https://arxiv.org/pdf/2606.06399
- [V] Mishra, Arvan, Zalake (2026) TeamMedAgents: Pareto-efficient multi-agent medical reasoning through teamwork theory (a31) https://arxiv.org/pdf/2508.08115
- [M] Krauss & Weinheimer (1964) Changes in reference phrases as a function of frequency of usage in social interaction (a32) https://doi.org/10.1007/BF03342967
- [M] Horton & Keysar (1996) When do speakers take into account common ground? (a33) https://doi.org/10.1016/S0010-0277(96)00799-1
- [V] Shaikh et al. (2024) Grounding Gaps in Language Model Generations (b01,b02,b03,c01,c02,c03,c04) https://arxiv.org/abs/2311.09144
- [V] Cemri et al. (2025) Why Do Multi-Agent LLM Systems Fail? (MAST) (b04,b05,c18) https://arxiv.org/abs/2503.13657
- [V] Vaccaro, Almaatouq, Malone (2024) When combinations of humans and AI are useful: a systematic review and meta-analysis (b06,b07,b08) https://www.nature.com/articles/s41562-024-02024-1
- [V] Laban et al. (2025) LLMs Get Lost in Multi-Turn Conversation (b09,b10,c22,c23,d05) https://arxiv.org/abs/2505.06120
- [V] Wu et al. (2025) CollabLLM: From Passive Responders to Active Collaborators (b11,c30) https://arxiv.org/abs/2502.00640
- [V] Li et al. (2023) Theory of Mind for Multi-Agent Collaboration via Large Language Models (b12,c05,c06,c07) https://arxiv.org/abs/2310.10701
- [V] Agashe et al. (2025) LLM-Coordination: Evaluating and Analyzing Multi-agent Coordination Abilities in LLMs (b13,c11,c12) https://arxiv.org/abs/2310.03903
- [V] Ullman (2023) Large Language Models Fail on Trivial Alterations to Theory-of-Mind Tasks (b14,c13) https://arxiv.org/abs/2302.08399
- [V] Kim et al. (2023) FANToM: A Benchmark for Stress-testing Machine Theory of Mind in Interactions (b15,c15) https://arxiv.org/abs/2310.15421
- [V] Kim et al. (2026) Towards a Science of Scaling Agent Systems (b16,b17,c24,d10) https://arxiv.org/abs/2512.08296
- [V] Stop Overvaluing Multi-Agent Debate -- We Must Rethink Evaluation and Embrace Model Heterogeneity (2025) (b18) https://arxiv.org/abs/2502.08788
- [V] Cross et al. (2025) Hypothetical Minds: Scaffolding Theory of Mind for Multi-Agent Tasks with LLMs (b19,c17) https://arxiv.org/abs/2407.07086
- [V] Santiesteban, Shah, White, Bird, Heyes (2015) Mentalizing or submentalizing in a communication task? (b21) https://users.ox.ac.uk/~ascch/Celia%27s%20pdfs/4%20Santiesteban%20et%20al%202015%20DT.pdf
- [V] Samuel, Roehr-Brackin, Jelbert, Clayton (2019) Flexible egocentricity: asymmetric switch costs on a perspective-taking task (b22) https://openaccess.city.ac.uk/id/eprint/28241/8/Flexible%20egocentricity%20.pdf
- [M] DeChurch and Mesmer-Magnus (2010) The cognitive underpinnings of effective teamwork: a meta-analysis (Journal of Applied Psychology) (b23) https://stars.library.ucf.edu/scopus2010/1847
- [V] Mesmer-Magnus, Niler, Plummer, Larson, DeChurch (2017) The cognitive underpinnings of effective teamwork: a continuation (b24) https://atlas.northwestern.edu/wp-content/uploads/2021/01/Mesmer-Magnus-Niler-Plummer-Larson-DeChurch-2017.pdf
- [V] Mesmer-Magnus et al. (2017) The cognitive underpinnings of effective teamwork: a continuation (moderators) (b25) https://atlas.northwestern.edu/wp-content/uploads/2021/01/Mesmer-Magnus-Niler-Plummer-Larson-DeChurch-2017.pdf
- [V] DeChurch and Mesmer-Magnus (2010) Measuring Shared Team Mental Models: A Meta-Analysis (Group Dynamics) (b26) https://atlas.northwestern.edu/wp-content/uploads/2017/03/DeChurch-_-Mesmer-Magnus-2010-Measuring-SMMs-META.pdf
- [V] Zhang et al. (2024) Building Cooperative Embodied Agents Modularly with LLMs (CoELA) (c08,c09) https://arxiv.org/abs/2307.02485
- [V] Zhang et al. (2024) ProAgent: Building Proactive Cooperative Agents with LLMs (c10) https://arxiv.org/abs/2308.11339
- [V] He et al. (2023) Hi-ToM: A Benchmark for Evaluating Higher-Order Theory of Mind Reasoning in LLMs (c14) https://arxiv.org/abs/2310.16755
- [V] Shi et al. (2025) MuMA-ToM: Multi-modal Multi-agent Theory of Mind (c16) https://arxiv.org/abs/2408.12574
- [V] Cemri et al. (2025) MAST (c19) https://arxiv.org/abs/2503.13657
- [V] Zhang et al. (2025) Stop Overvaluing Multi-Agent Debate (c25) https://arxiv.org/abs/2502.08788
- [V] Han and Zhang (2025) Exploring Advanced LLM Multi-Agent Systems Based on Blackboard Architecture (c26) https://arxiv.org/abs/2507.01701
- [V] Khebour et al. (2024) Common Ground Tracking in Multimodal Dialogue (c27) https://arxiv.org/abs/2403.17284
- [V] Hu et al. (2020) Other-Play for Zero-Shot Coordination (c28) https://arxiv.org/abs/2003.02979
- [M] Guo et al. (2024) LLM based Multi-Agents: A Survey of Progress and Challenges (c29) https://arxiv.org/abs/2402.01680
- [V] Edwards and Schuster (2026) Ask or Assume? Uncertainty-Aware Clarification-Seeking in Coding Agents (d01) https://arxiv.org/abs/2603.26233
- [V] Vijayvargiya et al. (2026) Ambig-SWE: Interactive Agents to Overcome Underspecificity in Software Engineering (ICLR 2026) (d02) https://arxiv.org/abs/2502.13069
- [V] Suri et al. (2026) Structured Uncertainty guided Clarification for LLM Agents (SAGE-Agent, ClarifyBench) (d03) https://arxiv.org/abs/2511.08798
- [V] Shaikh et al. (2025) Navigating Rifts in Human-LLM Grounding: Study and Benchmark (d04) https://arxiv.org/abs/2503.13975
- [V] Li et al. (2023, v3 2024) Theory of Mind for Multi-Agent Collaboration via Large Language Models (d06) https://arxiv.org/abs/2310.10701
- [V] Clark and Wilkes-Gibbs (1986) Referring as a collaborative process, Cognition 22 (d07) https://web.stanford.edu/~clark/1980s/
- [V] Brennan and Clark (1996) Conceptual pacts and lexical choice in conversation, JEP:LMC 22 (d08) https://web.stanford.edu/~clark/1990s/
- [M] Metzing and Brennan (2003) When conceptual pacts are broken (replication record, background knowledge only) (d09) https://doi.org/10.1016/S0749-596X(03)00028-7
- [V] Hernandez and Wilson (2026) PARLEY: Evaluating LLM Collaboration Through Cooperative Asymmetric Puzzles (d11) https://arxiv.org/abs/2611.14242
- [M] Anon. (2026) Aligned but Not Partner-Specific: How Multimodal LLM Agents Succeed in Reference Games Without Forming Conceptual Pacts (d12) https://arxiv.org/abs/2606.08081 (abstract level only)
- [M] Hua et al. (2024) Talk Less, Interact Better: Evaluating In-context Conversational Adaptation in Multimodal LLMs (ICCA) (d13) https://arxiv.org/abs/2408.01417 (abstract level only)
- [M] Anon. (2026) A Benchmark to Assess Common Ground in Human-AI Collaboration (d14) https://arxiv.org/abs/2602.21337 (abstract level only)
- [V] Anon. (2026) Knowing the User Is Not Knowing What We Established: Grounding Awareness in Personal Agents (Grounding Layer) (d15) https://arxiv.org/abs/2610.18684
- [V] Anon. (2026) When to Ask, When to Answer: Strategic Clarification for Ambiguous Reference Resolution in Dialogue (BACE) (d16) https://arxiv.org/abs/2611.05517
- [M] Anon. (2026) Is That Clear? The Impacts of Clarifying Questions on Human-LLM Interaction (d17) https://arxiv.org/abs/2611.01087 (abstract level only)
- [M] Anon. (2026) When AI Agents Act on Our Behalf: A Taxonomy of Human-Agent Interaction Failure; and Babysitting AI Agents (MANDATE) (d18) https://arxiv.org/abs/2611.00291 (abstract level only)
- [V] Beyond Division of Labor: How Roles Shape Feedback and Recovery in Multi-Agent Systems (2026) and Signed but Not Safe (2026), both citing MAST (d19) https://arxiv.org/abs/2611.03931

- Note: a14 and a16 (Clark and Wilkes-Gibbs 1986; Brennan and Clark 1996) were first recorded as not opened; the gap search later opened the Stanford copies (d07, d08) and those numbers are the ones used here.

## Source audit (2026-11-20)

Fresh auditors re-opened the sources of 10 established claims: 7 confirmed as written, 3 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E13.03-K19** (reworded: the sources support less). Mesmer-Magnus et al. 2017 pools team cognition broadly (not shared mental models alone): rho=.35 for team cognition vs performance (k=107, 128 studies in the whole database); only DeChurch and Mesmer-Magnus 2010 isolates SMMs (performance r=.29, k=19; process r=.20, k=17). Corrected claim: Team cognition (of which shared mental models are one form) predicts team process and performance (2017 meta-analysis of 128 studies: rho=.35 with performance, k=107; rho=.38 with process); in the 2010 meta-analysis shared mental models alone correlated r=.29 with team performance (k=19) and r=.20 with process (k=17). Effects depend on measurement method and on compositional vs compilational emergence.
- **E13.03-K22** (number corrected). In Khebour et al. 0.54 is the inter-annotator F1 of the common-ground annotation, not tracker performance (tracker reports Dice per group; move classifier weighted F1 0.61 is a real model score); also Khebour and Zhu et al. share authors (Pustejovsky, Krishnaswamy, Bradford, Lai), so they are one research group, not independent. Corrected claim: Formal common-ground tracking in group tasks is feasible but imperfect: Khebour et al. report a move classifier weighted F1 of 0.61 (annotators agreed on common-ground labels at F1 0.54), and the same group later found LLMs recover the axiomatic common ground poorly (Dice 0.219 for Llama-3.2-3B to 0.382 for GPT-5, actions-to-structure setting). Both studies come from one lab.
- **E13.03-K25** (reworded: the sources support less). Both LLM sources test multimodal LLMs in tangram reference games; Hua et al. find no spontaneous efficiency gain and say heavy-handed prompting elicits it in some models (e.g. GPT-4), so 'do not' is too absolute and 'LLMs' too wide; human 41 to 8 words per figure matches Clark and Wilkes-Gibbs (1986). Corrected claim: In repeated tangram reference games, multimodal LLMs do not spontaneously shorten their references across rounds (this can be elicited in some models only with heavy-handed prompting), and their label overlap with partners is not shown to be partner-specific, unlike humans (Clark and Wilkes-Gibbs: 41 to 8 words per figure over 6 trials); they succeed with verbose descriptions from round one.
- **E13.03-K04** (now single-source: only one opened source, code check).
