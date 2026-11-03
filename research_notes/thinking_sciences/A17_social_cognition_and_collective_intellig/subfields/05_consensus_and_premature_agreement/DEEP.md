# Consensus and premature agreement: deep document

*Subfield A17.05. Writer pass, 2026-11-03. Built from evidence_a-d.jsonl (a01-a35, b01-b31, c01-c26, d01-d18), claims.jsonl (K01-K32) and critique.md in this folder. Evidence ids in brackets. Status marks follow SCHEMA.md: [E] established, [S] single source, [C] contested. Items marked "unverified" were not read in full and must not be quoted as exact.*

---

## 1. What it is

Groups that seek agreement can end up less accurate than their best members, or than the plain average of their members. Three things happen together:

1. **Concurrence-seeking.** The group wants to agree. It treats silence as assent and treats a dissenter as a problem (Janis 1972) [a01].
2. **Pooling failure.** Members talk about what they all know and leave out what only one of them knows. The best option never surfaces (hidden profile; Stasser and Titus 1985; Lu et al. 2012) [a04, a05, b25].
3. **Conformity.** An individual drops a correct private view when others disagree (Asch 1951-56) [a09].

For a language model agent the same three failures appear in a new form:

- **Correct-to-incorrect flips.** A model that was right changes its answer after reading peers who were wrong [a24, a27, c13].
- **Disagreement collapse.** Agents converge on one answer before anyone checks it. The answer is often wrong [a26, b17, b16].
- **Hidden-profile failure in panels.** Agents that each hold part of the evidence do not share it. The panel reaches 30.1% against 80.7% for one agent that sees everything [d01].
- **Speaker-free conformity.** A bare repeated wrong answer, with no speaker at all, causes most of the measured flips [d12].

**Why it matters for our agent.** The schema bans debate (G9), bans treating same-model samples as independent (G4), and puts selection in code (G5). This document is the evidence base for those rules. It also lists what could be added: a premature-consensus signal, commit-before-sharing, an unused-evidence step and a grounded dissent step. All of these are untested at equal tokens and sit in UNKNOWNS.md.

**Scope.** Not covered here (sibling subfields): crowd wisdom and estimate averaging (Lorenz 2011 only noted), the surprisingly popular method, red teaming, distributed cognition, debiasing by structure.

---

## 2. History and theories in depth

### 2.1 Asch conformity (1951-56)

- Asch used 7 confederates and 1 real participant judging line lengths. N=50 experimental and 37 control. 35.7% of critical answers followed the wrong majority. 74% gave at least one wrong answer over 12 critical trials. 12% conformed nearly always and 26% never. Control error was under 0.7% [a09].
- One true dissenting partner cut following to about 5% (9% if the dissenter was extreme). One opponent leaves independence high. Two or three raise conformity. Four or more add little [a09].
- The iconic rate is 36.8% of 123 subjects in the 1955 report. Later replications are lower. Bond and Smith (1996) pooled 44 strict replications and found about 25% mean error. This number is second-hand [a08].
- Franzen and Mader (2023) replicated with five confederates. 202 analysed (210 recruited). Error 33% against Asch's 36.8% (t(16)=0.59, p=0.57). A small payment of 1 CHF per correct answer cut it to 25%. Mean wrong answers over 6 critical trials: 1.97 vs 1.47 (t(208)=2.24, p=0.03). Opinion statements showed 38% mean conformity [a07, b24].

Lesson for agents: the effect is real, moderate, shrinks with incentive but does not vanish, and one honest dissenter is the strongest known cure.

### 2.2 Groupthink (Janis 1972)

- Janis named eight symptoms in three clusters: overestimating the group, closed-mindedness, pressure toward uniformity (self-censorship, illusion of unanimity, direct pressure on dissenters, mindguards). Three antecedents: cohesion, structural faults, stressful context. Cases: Pearl Harbor 1941, Bay of Pigs 1961, Vietnam 1964-67 as failures; the Cuban Missile Crisis 1962 as success [a01].
- Proposed cures (1972 book, pp. 209-215): a critical-evaluator role for every member, leader states no opinion first, several independent groups on one problem, outside experts, rotating devil's advocate [a02].
- Tests gave only partial support. Park (1990) found 16 empirical studies. Turner and Pratkanis (1998) found fewer than two dozen in 26 years. Cohesion alone had no main effect. Structural faults (homogeneity, insulation) predicted poor decisions better than stress or cohesion. Kramer (1998) argued Janis overstated closed-mindedness in his cases. Baron (2005): Janis's antecedents are neither necessary nor reliably amplifying [a03, b30].
- Source weakness: all of this is from Wikipedia summaries. The Mullen (1994) meta-analysis and Esser (1998) review were not opened [a35].

### 2.3 Hidden profiles (Stasser and Titus 1985 onward)

- Task design: information is split so the best option looks worse to every member before discussion. Standard layout: candidate A has 6 positive and 3 negative attributes, candidate B has 3 positive and 6 negative. The shared subset favours B (3 positive, 2 negative against A's 2 positive, 3 negative) [a12].
- The founding paper (four-person groups choosing a student president) is paywalled. The remembered 18% vs 83% was never recovered from any source and must not be cited [a04, d18].
- Meta-analysis (Lu, Yuan and McLeod 2012): 65 studies, 101 independent effects, 3,189 groups. Hidden-profile groups were about eight times less likely to find the solution than full-information groups. Groups mentioned shared information about two standard deviations more than unique information. Information coverage predicted decision quality more than discussion focus. Abstract-level only, via search snippet [b25, d17].
- Modern anchor (Faulmueller et al. 2010, Exp 2, N=95): hidden-profile groups 1 of 15 correct (7%) against 100% in full-information groups. Hidden-profile individuals 4 of 16 (25%). So the failure starts before talking: each member forms a wrong preference from their partial list [d16].
- Oxytocin study (19 groups per arm): placebo groups solved a murder-mystery hidden profile 47% of the time against 74% for oxytocin groups. Pre-discussion individual correct 32% (chance 33.3%). Used here only as a clean unaided baseline [a15].

Two accounts of the failure:

1. **Shared-information bias.** Shared facts get mentioned and repeated more because several people hold them, and mentioning them earns social reward [a12].
2. **Preference-consistency bias.** People believe arguments that fit their current preference [a12].

Fiedler et al. (2018) added a third: **metacognitive myopia.** People cannot correct for the repetition of shared arguments even when warned, even when repetition comes from one speaker, and even after blatant debriefing. Frequency of mention biases evaluation by simple learning [a13].

Moderators of shared-information bias [a05, a06]:
- Stronger under closure-seeking, time pressure, ambiguous judgment tasks, and when members protect their reputation.
- Weaker with more discussion time, opinion diversity, explicit expertise labels, and tools that catalogue information.
- Stewart and Stasser (1998): stronger in judgment tasks than in demonstrable intellectual tasks. Mesmer-Magnus and DeChurch (2009): sharing matters most on intellectual tasks.
- Reimer et al. (2010) meta-analysis title says decision-making groups attenuate the bias. Not opened [b28].

### 2.4 Preference disclosure and dissent

- Mojzisch and Schulz-Hardt (2010): telling members others' preferences before discussion hurt hidden-profile solving across four experiments (the fourth face-to-face with three-person groups). The effect ran through less attention to exchanged information. Abstract-level only [b26].
- Schulz-Hardt et al. (2006): initial dissent in the group helped hidden-profile solving. Title and recalled finding only; no numbers [a34, b27].
- Nemeth (1986): minority dissent, even when wrong, stimulates divergent thinking; majority influence gives convergent thought. Recalled, not opened [a10].
- Pescetelli et al. (2022): a bot trained to support under-represented opinions in teams of 10 humans (bot = 10% of team) changed opinion dynamics but gave only a small team gain [a14].

### 2.5 Group polarization

Discussion pushes members to a more extreme version of their lean. Two mechanisms, both real (Isenberg 1986): persuasive arguments and social comparison. Walker and Main (1973): federal judges alone took extreme action 35% of the time, three-judge panels 65% [a11]. Kept as human context only.

### 2.6 LLM debate as a modern version

- Du et al. (2023) started the line. Several ChatGPT agents see each other's answers and revise [a16, c01]. Debate beat a single agent, reflection and majority vote. The authors saw that agents converge to one answer, and that confident agents resist change [a17, b16].
- Liang et al. (2023/24) named Degeneration-of-Thought: once confident, a model keeps its answer. They added a tit-for-tat debate with a judge [a18, b22].
- Sceptical wave 2024-25: Wang et al. (a single agent with a demonstration matches discussion), Smit et al., Zhang et al., Choi et al.
- Failure-mode wave 2025-26: Wynn et al., Yao et al., Wu et al., Kaesberg et al., and a cluster of 2026 preprints on sycophancy, speaker-free conformity and hidden-profile benchmarks.

---

## 3. Core findings with exact numbers

Status key: [E] established, [S] single source, [C] contested. "Human" = human study.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Asch conformity, original | 35.7% of critical answers followed the wrong majority; 74% wrong at least once in 12 trials; control under 0.7%; N=50 (+37 control); one true partner cuts to about 5% | Asch 1951 via Wikipedia [a09] | [E] human |
| Asch replications are lower | 33% (N=202) vs 36.8% (p=.57); 25% with 1 CHF incentive; Bond and Smith mean about 25% over 44 replications (second-hand) | Franzen and Mader 2023 [a07, a08, b24] | [E] human |
| Groupthink antecedents only partly supported | cohesion no main effect; 16 studies (Park 1990); under two dozen in 26 years | Turner and Pratkanis 1998 etc. via Wikipedia [a03, b30] | [E] human |
| Hidden profile: pooling failure | about 8x less likely to find the solution; 65 studies, 3,189 groups (abstract only) | Lu et al. 2012 [b25, d17] | [E] human |
| Hidden profile, modern lab anchor | 1/15 (7%) hidden vs 100% full information; individuals 4/16 | Faulmueller 2010 [d16] | [S] human |
| Hidden profile, unaided groups | placebo 47% vs oxytocin 74% (19 groups per arm) | Sci Rep 2017 [a15] | [S] human |
| Knowing others' preferences hurts pooling | 4 experiments, sample sizes not read | Mojzisch and Schulz-Hardt 2010 [b26] | [S] human |
| LLM panels fail hidden profiles | 30.1% distributed vs 80.7% single agent with full info; 15 LLMs; 65 tasks; pre-discussion 0.008; best model Gemini-2.5-Pro 0.671 | HiddenBench [d01] | [E] |
| LLM hidden-profile failure is surfacing, not reasoning | Reveal-All: GPT-4.1 0.037 to 0.926; Gemini-2.5-Flash 0.173 to 0.982 (18 tasks) | HiddenBench Table 6 [d04] | [E] |
| More rounds, bigger groups, tone do not fix pooling | rounds 5/10/15/20: 0.108/0.200/0.233/0.133; group size N=3..7 gain +0.348 to +0.006; "share all information" 0.467; conflictual 0.017 (GPT-4.1, 3 tasks) | HiddenBench Tables 2-4 [d02] | [S] tiny task count |
| Debate beat single and vote (original) | arithmetic 67.0 / 69.0 vote / 81.8 debate; GSM8K 77.0 / 81.0 / 85.0; chess 91.4 / 102.2 / 122.9; biographies 66.0 to 73.8; MMLU 63.9 to 71.1 | Du et al. 2023 [a16, b15, c01] | [S] not reproduced |
| Debate does not beat vote at matched compute | Qwen2.5-7B, 7 benchmarks: single 0.7205, vote 0.7691, debate T=2 0.7377, T=3 0.7112, T=5 0.7050, sparse 0.7330, centralized 0.6551 | Choi et al. 2025 [b05, c07] | [E] |
| Llama3.1-8B same pattern | single 0.6203, vote 0.7242, decentralized T=2 0.6929, centralized T=5 0.5670 | Choi et al. 2025 [c07] | [E] |
| Debate rarely beats CoT | beats CoT in about 15% of 36 configs; Multi-Persona 0%; GPT-4o-mini SoM below CoT on all 9 sets | Zhang et al. 2025 [a21, b10] | [E] |
| Medical QA | MedQA: Medprompt 0.65, SoM 0.64, ER 0.64, ChatEval 0.60, SC 0.60, single 0.60, Multi-Persona 0.58 | Smit et al. 2024 [a19] | [E] |
| Debate is a martingale | expected belief in the correct answer does not change from talk alone; flat belief curves | Choi et al. 2025 Theorem 2 [b06] | [S] theory, homogeneous case |
| Correct-to-incorrect flips outnumber the reverse | MMLU 40.0 to 28.0 (-12.0); CSQA 53.4 to 46.8; GSM8K 61.0 to 64.8 (up); 100 questions x 5 seeds | Wynn et al. 2025 [a24, b01, c09] | [S] small models |
| Weak member can hurt | CSQA 58.2 to 50.2; MMLU 51.8 to 43.6 (2+1 mix) | Wynn et al. 2025 [b03] | [S] |
| Heterogeneous mixes help | Heter-SoM +6.4%; Heter-EoT +8.2%; up to +5.8% over CoT average | Zhang et al. 2025 [b12] | [C] vs Wynn |
| Wrong-majority resistance, strong models | inside a wrong majority self-correction 34.4% (gemini-2.5-flash), 30.0% (gpt-5-mini), 3.6% (flash-lite); inside a correct majority above 97% hold | Wu et al. 2025 [a27, c13] | [E] one puzzle family |
| Disagreement collapse | DCR up to 86.36% (Llama3.3-70B, 2-agent CSQA); r=0.902 debaters' negative agreement vs sycophancy | Yao et al. 2025 [a26, b17] | [E] |
| Judge cuts collapse | Qwen-Qwen CSQA acc 83.62 to 86.65, DCR 81.71 to 41.27; Qwen-Llama 81.00 to 86.49, DCR 80.41 to 35.51 | Yao et al. 2025 [c12] | [E] |
| Peacemaker personas worst | 45 homogeneous persona mixes 81.98 to 83.87, lowest when both peacemakers; hetero 78.95 to 82.06; 3 agents MMLU-Pro 72.10 (DCR 31.66) vs single 66.46 | Yao et al. 2025 [b18] | [S] 2-3 point effects |
| Prompted agreement level | Multi-Persona +15 points, SoM +5 on 376 USMLE items at about 90% agreement; reverse on CIAR | Smit et al. 2024 [a19, b09] | [E] dataset dependent |
| Forced disagreement is not best | disagreement 0.988 not best; moderate best; MAD 37.0 vs GPT-3.5 26.0 on counter-intuitive arithmetic | Liang et al. 2024 [a18, b22] | [S] |
| No transferable dissent optimum | GPT-4.1 0.233 to 0.492 at 25% adversarial then worse; GPT-5-mini 0.000 at 0%, peaks 0.556-0.583 at 50-100%; Gemini-2.5-Flash 0.889 at 0%, 0.306 with one dissenter | HiddenBench Table 5 [d03] | [S] few tasks |
| Consensus vs voting | voting +13.2% on reasoning (MuSR +26.4, SQuAD2 +13.1); consensus +2.8% on knowledge (MMLU +2.3, MMLU-Pro +4.9, GPQA +1.3); approval voting fails in 59%; consensus 1.42 rounds vs voting 3.38 | Kaesberg et al. 2025 [a28, c08] | [S] |
| More rounds before voting lowers accuracy | slight drop over rounds 1-10 (oddity at 10); more agents raise it | Kaesberg et al. [c24] | [S] |
| History lowers challenge rate | challenge rate fell 10% overall and 60% on StrategyQA; wrong solutions challenged 75%, irrelevant 99% when shown alone | Kaesberg et al. [a29] | [S] |
| Payoff prompt does not stop flips | no significant reduction; often more flips | Wynn et al. [a25, b04, c11] | [S] |
| Sycophancy from user pushback | Claude 1.3 wrongly admits a mistake 98%; wrong user suggestion cuts accuracy up to 27% (LLaMA 2, main text); GPT-4 most robust | Sharma et al. [a31, c03] | [S] 2023 models |
| Conformity grows with group size | open 7-9B models, 2 to 10 participants; devil's advocate on TriviaQA Llama-3-8B base 63.20% to 41.37% sycophantic; instruct 25.18% to 12.37% | Zhu et al. 2025 [b19, b20] | [S] |
| Yield is not just RLHF | base models yield too; yield 44 to 98%; patching restores 96% of gap; one correct dissenter cuts yield 54-73 points | "Not Just RLHF" 2026 [c15, c16] | [S] anonymous preprint |
| Many flips are not conformity | 37% change with no peer info; strict conformity 29.30% (n=960/3277); vote 77.35% vs individual 42-46%; 57% more tokens for full reasoning | "Not All Flips Are Conformity" 2026 [c17] | [S] GPT-4o |
| Cost of debate | 2.1 to 3.4x tokens of isolated self-correction; modal adoption up to 85.5%; vulnerability up to 70.0%; oracle gap up to 32.3 pp | "Cost of Consensus" 2026 [c18] | [S] abstract only |
| Speaker-free floor | harmful revision 66.5% no-source vs 10.3% plain re-ask vs 79.4% expert panel (+12.9) | Hu and Qu 2026 [d12] | [S] small open models |
| Resistance-receptivity frontier | unanimous wrong group reverses 22.8% MMLU, 54.8% GPQA, 71.0% SimpleQA; reflection +7.9 resistance, -15.3 receptivity; R-squared 0.80-0.90 | Hussain and Nielbo 2026 [d13] | [S] 23 open models |
| Attribution tags hurt | removing or shuffling tags +13-24 points; full transcript below no notes; relevance filter loses 23-31 to rarest-first | CrossProfile 2026 [d08] | [S] |
| Structured deliberation vs one agent | single 8.84 vs DCI 8.62; DCI about 62x tokens; hidden-profile 9.56 | Prakash 2026 [d09] | [S] |
| Equal-budget scaling | MMLU-Pro: CoT 64.3, SC 68.7, debate 70.0, MoA 71.4 at up to 20x CoT budget | Wunderlich et al. 2026 [d10] | [S] |
| Effective team size saturates | R(N)=Neff/N=1/(1+c(N-1)N^-alpha), R-squared above 0.99; SC has alpha=0; noise placebo tracks self-correction | Bertalanic and Fortuna 2026 [d14] | [S] |
| Premature-consensus controller | 0.83 avg vs 0.26 round-robin vs 0.285 unstructured vs 0.731 full-info reference | Consilience 2026 [d07] | [S] |
| Minority overturn | 39.1% of samples are 2:1; minority right in 25.5%; flip precision 81.2% (39 right, 9 wrong); net +1.71%; LLM judge 42.7%, -1.37% | Minority Sentinel 2026 [c19, d11] | [S] |
| Withholding model | gain falls as withholding rises; c=1 nearly removes gain; reasoning off raises gain | Mansuri et al. 2026 [d05, d06] | [S] |
| Group polarization | judges alone 35% extreme action, panels 65% | Walker and Main 1973 [a11] | [S] human |

---

## 4. Mechanisms and models

Each model is written so it can be coded. Variable names are ours.

### 4.1 Hidden profile (the pooling failure)

Setup: option set O. Evidence set E split across agents. Each agent i holds a private set P_i plus a shared set S. The best option b has support only in the union of the P_i. Each agent's own view favours a wrong option.

Failure chain:
1. Each agent forms a preference from its partial set (Faulmueller: 25% of individuals right, 7% of groups) [d16].
2. Agents mention shared items first because more of them hold the same item [a12].
3. Repetition biases evaluation with no social cause and cannot be corrected by warning [a13].
4. A stated preference lowers attention to the others' facts [b26].
5. The group commits. In LLMs this takes 1-2 rounds [d01].

What breaks the chain in LLMs:
- **Forced disclosure.** Every agent writes all its facts before anyone judges. GPT-4.1 0.037 to 0.926 [d04]. This is oracle-like, but it shows the reasoning step is fine.
- **Exchange-then-Decide.** Two rounds. Each agent shares 1-2 decision-relevant facts and one reason the current front-runner may be wrong. Then one Decide pass. Helped across three model families (numbers not extracted) [d04].
- **Share-all prompt.** 0.467 against a baseline of about 0.1-0.2 (GPT-4.1, 3 tasks) [d02].
- **Rarest-first memory.** When the decider sees notes, ordering by how few agents hold the fact beats a perfect relevance filter by 23-31 points in the classic layout [d08].

Implementable rule for one agent: in S3 write the evidence as a list of atomic items, each tagged with the attempt that raised it. In S4 code counts items that appeared in only one attempt (the "unique" set). Before commit, require a pass that tests each option against the unique set first.

### 4.2 Debate as a martingale (why talk alone adds nothing)

Choi et al. model each agent's belief as a Dirichlet-compound-multinomial over answers. When an agent updates by seeing peers, the expected belief in the correct answer stays constant across rounds. So:
- Expected accuracy after talk equals expected accuracy before talk.
- Majority vote over independent first answers does help: success probability is lower-bounded by 1 - exp(-N(...)) and approaches 1 as N grows, even when the correct answer holds under 50% share [a22].
- Only a bias toward correct signals can add gain. Oracle (lock in correct answers): 0.8236 at T=2, 0.8364 at T=5. Conformist (keep your answer if it matched last round's majority): 0.7625 at T=2, 0.7439 at T=5. Follower (adopt the majority with 30% probability): 0.7629 at T=2, 0.7527 at T=5. Vanilla: 0.7332 at T=2, 0.7160 at T=5 [a23, b07, critique item 1]. Always quote T.
- Limits: homogeneous or clique topologies. Heterogeneous fully connected debate need not be a martingale (paper appendix) [b06].

Code sketch:
```
votes = [answer_i for i in range(N)]        # N independent samples, no sharing
final = argmax(count(votes))                # code, not a model
```
Compare with debate at the same total tokens. The Choi result says the vote line wins.

### 4.3 Disagreement collapse rate (DCR)

Yao et al. definition: among cases where at least one agent held the right answer at the start, the share where the group did not keep it. Use it as a log metric.
```
DCR = |{q : any(initial_i == gold) and final != gold}| / |{q : any(initial_i == gold)}|
```
Measured: 86.36% (Llama3.3-70B homogeneous, 2-agent CSQA); 81.71% (Qwen-Qwen decentralized) falling to 41.27% with a centralized judge [b17, c12]. Three-agent debates collapse less than two-agent ones [b18].

### 4.4 Flip rate as a function of peer agreement (Asch in models)

Wynn et al. measure the chance that a correct agent flips as a function of how many peers agree with it (0, 1, 2). The chance is highest when it stands alone and falls with each agreeing peer. Resistance is lower in round 2 than in round 1 [c10, b02]. Zhu et al. find the same shape: conformity rises with the number of confederates (2 to 10) and with lower initial confidence [b19]. Bellina et al. (2026) report social-impact-theory scaling in multimodal agents (abstract only) [d15].

Probe to build into our bench:
```
for k in 0,1,2,3:
    prompt = question + k confident wrong peer answers (written by a different model)
    flip_rate[k] = P(final != gold | own_initial == gold)
    fix_rate[k]  = P(final == gold | own_initial != gold, one peer correct)
```
Report both. Hussain and Nielbo show a fix that lowers flips usually lowers acceptance of correct peers too [d13].

### 4.5 Resistance-receptivity frontier

Resistance = P(keep correct answer under wrong pressure). Receptivity = P(accept correct peer answer when own answer is wrong). Six mitigations lie on one line (R-squared 0.80-0.90). Reflection: +7.9 resistance, -15.3 receptivity on MMLU. Only reasoning on self-derivable subjects moved both up (+7.2, +9.6) [d13]. Rule: any anti-conformity operator is scored on both numbers.

### 4.6 Withholding model (Mansuri et al. 2026)

Agents in discussion either state or hide a private view, and may or may not internalise the group view. Mean-field result: discussion can overturn a wrong initial majority only if the withholding rate c is below a critical value c* set by the net correction rate and the internalisation rate [d05].
```
gain_discussion > 0  iff  c < c*(net_correction, internalisation)
```
Measurements: nine LLMs, three instructions (A honest, B none, C value cohesion). Gain falls as (c - c*) grows, clearly on HiddenBench and MedEInst, unclear on MuSiQue. Fixing c=1 externally nearly removed the gain (causal). Reasoning off raised the gain by lowering internalisation, with no consistent change in c [d06]. Implication: log the private answer and the stated answer as separate fields. Never instruct "value agreement".

### 4.7 Effective team size

R(N) = Neff / N = 1 / (1 + c(N-1) N^-alpha), fit with R-squared above 0.99 in every condition. Independent sampling has alpha=0, so Neff=N. Thirty dense debating agents gave no more diversity than one on MMLU-Hard. Only different-architecture teams lowered c. A noise placebo matched the gain of self-correction, so much of the debate gain is re-evaluation, not peer content [d14]. Caution: same-model samples still correlate (G4). The claim is only that dense debate adds more correlation than independent sampling.

### 4.8 Minority overturn classifier (Minority Sentinel)

Not a verifier. LightGBM on 22 debate-log features: 10 dynamics, 4 voting, 8 semantic audit features from GPT-4o. Applied only to 2:1 splits among 3 heterogeneous agents after 2 rounds. 39.1% of samples are 2:1. In 25.5% of those the minority is right. Majority vote 74.3%, oracle 84.3%. Flips: 39 correct, 9 wrong, precision 81.2%, net +1.71% (20 seeds mean +1.65, std 0.19, min +1.31, max +2.00). An LLM judge: 70 correct, 94 wrong, precision 42.7%, net -1.37%. Removing all audit features cost only 0.29 pp [d11]. Gain is small, author-only, and needs training data.

### 4.9 Premature-consensus controller (Consilience)

A controller tracks uncertainty, disagreement, evidence gain, redundancy and a premature-consensus signal, and picks the next move: challenge, clarify, seek evidence, route. 0.83 average vs 0.26 for round-robin. A rules controller scored 0.843, above the full-information reference of 0.731 [d07]. Tuned on the same task family as the benchmark; no token-matched single-agent baseline.
```
state = {uncertainty, disagreement, new_evidence_rate, redundancy, premature_flag}
premature_flag = agreement_high AND new_evidence_rate_low AND unseen_facts_remain
move = challenge if premature_flag else seek_evidence if new_evidence_rate_low else clarify
```
Our version would live in code (G5), not in a model. The pseudocode is our reading, not the paper's exact rule.

### 4.10 Typed epistemic acts (DCI)

Prakash's structure: typed moves, a minority report, reopen conditions. Wrote minority reports in 98% of runs. Non-routine tasks (n=40): DCI minus unstructured debate +0.95 (CI +0.41 to +1.54). A single agent still beat DCI overall (8.84 vs 8.62; difference 0.60, CI 0.15 to 1.06) with about 62x fewer tokens (3,809 per task) [d09]. Only on hidden-profile tasks did DCI (9.56) win.

### 4.11 Speaker-free conformity

Hu and Qu: a bare repeated wrong answer causes 66.5% harmful revision in initially correct cases (six open instruction-tuned models, seven datasets). A plain re-ask gives 10.3%. The strongest expert-panel frame gives 79.4%. The effect holds off-ceiling (77.3%), with options hidden (75.4%) and with paraphrase. Flipped models are usually confidently wrong, and temperature rescaling did not recover the original answer in 42 of 42 cells [d12]. So the main driver is in-context repetition of an answer, not social framing. Parallel result: 37% of GPT-4o answers change with no peer info at all [c17].

### 4.12 Sycophancy: training product, but not only that

Preference data favour agreeable answers [c03]. But base models yield too, at a higher average yield than instruct models. Patching mid layers (L14-L18, Llama-3.1-8B-Instruct) restores 96% of the clean-to-pressured gap [c15]. Message role matters: user-role framing needs unanimity, assistant or tool role flips at majority (47.5-point yield gap at majority consensus) [c15]. Zhu et al. found instruction tuning lowers conformity [b20]. So RLHF is not the sole cause (see section 5.5).

---

## 5. What holds up

### 5.1 Replications and failed replications

| Claim | Outcome |
|---|---|
| Asch effect | Replicates but smaller: 33% (Franzen and Mader), mean about 25% (Bond and Smith). Incentive lowers it to 25% in one study [a07, a08]. |
| Groupthink antecedents | Partial support only. Cohesion alone fails [a03, b30]. |
| Hidden-profile failure | Replicates across 65 studies (abstract-level) and in a 2026 LLM benchmark [b25, d01]. |
| Debate beats vote (Du 2023) | Not reproduced at matched compute (Choi, Smit, Zhang, Wang). Du's own majority control was 69.0 vs debate 81.8 on arithmetic, so the gap is not wholly explained by baseline choice [c07, a19, a21, a20, critique]. |
| Heterogeneity helps debate (Zhang) | Conflicts with Wynn's weak-member harm. Unresolved [K10]. |
| Debate hurts everywhere (Wynn) | Not so. GSM8K went up in the 1+1+1 mix (61.0 to 64.8; up to +4.4) while CSQA and MMLU fell [c09]. |
| Dissent helps | Humans: a single true dissenter is the strongest cure (Asch, 5%) [a09]. LLMs: one correct dissenter cuts yield 54-73 points [c16]; devil's advocate cuts TriviaQA sycophancy 63.2 to 41.4 [b20]; but instructed adversaries hurt Gemini-2.5-Flash (0.889 to 0.306) [d03]. |
| Sentinel | No non-author replication [d11]. |
| MAST failure percentages | Garbled in extraction. Do not use [c14]. |

### 5.2 Moderators that matter

- **Who is in the majority.** Wynn's flip rate is highest when the agent stands alone [c10]. Wu: inside a correct majority above 97% hold; inside a wrong majority 30-34% self-correct for strong models [a27].
- **Model strength.** Debate success is governed mainly by the strongest participant [a27]. A weak, stubborn partner can pull a strong one down (Xiong 2023; six pre-2024 LLMs; summary only) [b21].
- **Task type.** Voting wins on reasoning, consensus on knowledge (Kaesberg) [a28]. Debate better on math than programming (Zhang) [a21]. MedQA and PubMedQA like high agreement, CIAR likes disagreement (Smit) [b09].
- **Group size.** More independent agents help; more rounds do not [c24]. Three-agent debates collapse less than two-agent [b18]. The hidden-profile gain from group size falls from +0.348 to +0.006 [d02].
- **Prompt framing.** Friendly vs hostile instructions: strong-agreement share 70.7-96.3% vs 9.5-19.3% [c21]. The Smit "agree X%" instruction gives +15 points for Multi-Persona. Agreement level is largely a prompt property.
- **Demonstrations.** A demonstration closes the gap between single agent and discussion [a20].
- **Reasoning on or off.** Reasoning models stay above the withholding threshold because internalisation is high; reasoning off raised gain in one set of four models [d05, d06]. Reasoning on self-derivable questions improved both resistance and receptivity [d13].
- **Role of the message.** User-role vs assistant-role framing changes how many agreeing peers are needed to flip [c15].

### 5.3 Interventions that worked

- Independent sampling plus a code vote (Choi, Kaesberg, Zhang, Wunderlich) [E].
- A centralized judge in debate: DCR 81.71 to 41.27, accuracy 83.62 to 86.65 [c12]. Choi found a central aggregator agent clearly worst (0.6551) [c07]. The protocols differ, so the direction (judge reduces collapse) is established for Yao's setting only. Treat the general claim with care.
- Forced evidence disclosure (oracle) and Exchange-then-Decide in panels [d04].
- Rarest-first ordering and stripping attribution tags in decision memory [d08].
- One correct dissenter (54-73 points yield cut) [c16].
- Biasing updates toward the majority (Conformist/Follower) beats vanilla debate but not majority vote at T=2 (vote 0.7691 vs Follower 0.7629) [a23, b05].
- Heterogeneous teams lower correlation [d14].
- Typed deliberation on hidden-profile tasks [d09].

### 5.4 Interventions that did not work, or came with a cost

- Correctness-payoff prompt: no significant drop in flips [a25].
- Answer-agnostic interventions: cut both harmful and beneficial adoption, no net gain [c17].
- More rounds, more agents beyond a point, tone prompts for hidden profiles [d02].
- Reflection: +7.9 resistance, -15.3 receptivity [d13].
- Showing confidence: negligible effect for weak teams [c13]. Self-reported confidence was uniformly high and uninformative [a17].
- LLM judge for minority overturn: -1.37% [d11].
- Persona control in homogeneous debates: 2-3 points only [b18].
- DEAR notes that individual confidence or perplexity scores do not detect blind conformity and can worsen it (abstract only; needs RL training) [c20].
- Human cures with weak support: staged devil's advocacy may be weaker than authentic dissent (Nemeth, not opened) [a10, b31]; the Pescetelli bot gain was small [a14].

### 5.5 Competing explanations for the LLM effects

1. **Training (RLHF sycophancy)** [c03].
2. **Base-model prior** (yield in base models too) [c15].
3. **In-context repetition** (speaker-free floor) [d12].
4. **Re-evaluation noise** (placebo matches self-correction; 37% change with no peer) [d14, c17].
5. **Correlated errors** (majority suppresses a correct minority) [c19, d14].
6. **Information not surfaced** (hidden profiles) [d04].
7. **Withholding of dissent** [d05].

No study separates all seven. The 2026 work shifts weight from 1 toward 3 and 4.

---

## 6. Language models

### 6.1 Baseline behaviour

- **Single sample vs vote.** Qwen2.5-7B: 0.7205 vs 0.7691 (+4.9 points). Llama3.1-8B: 0.6203 vs 0.7242 (+10.4) [c07]. GPT-4o on a selected set of MMLU-Pro disagreement questions: individual accuracy 42.17-45.87%, majority vote 77.35% [c17].
- **Debate vs vote.** Debate T=2 0.7377 (vote 0.7691). Longer debate decays: T=5 0.7050. Centralized worst: 0.6551. Arithmetic: vote 0.99 vs decentralized T=5 0.67 [b05].
- **Debate vs CoT / SC.** Debate beats CoT in about 15% of 36 configurations [a21]. GPT-4o-mini SoM below CoT on all 9 datasets [b10]. Self-consistency scales with tokens; debate does not [b11].
- **Equal budget on MMLU-Pro.** CoT 64.3, SC 68.7, debate 70.0, MoA 71.4 at up to 20x CoT [d10]. This is the one source where debate edges SC. Same lab as Kaesberg. The 1.3 vs 1.4 figures disagree inside the paper. Treat as contested against Choi and Zhang.
- **Cost.** Debate uses 2.1-3.4x the tokens of isolated self-correction for equal or lower accuracy [c18]. DCI uses about 62x the tokens of a single agent [d09].

### 6.2 Conformity measurements

| Model set | Pressure | Measure | Result | Source |
|---|---|---|---|---|
| Claude 1.3 | "Are you sure?" | wrong admit | 98% | [a31] |
| LLaMA 2 | wrong user suggestion | accuracy drop | up to 27% | [a31] |
| 6 open instruct models | bare repeated wrong answer | harmful revision | 66.5% (plain re-ask 10.3%; expert frame 79.4%) | [d12] |
| 23 open models (14B+) | unanimous wrong group | reversal of correct | 22.8% MMLU, 54.8% GPQA, 71.0% SimpleQA | [d13] |
| Gemma-2-9B, Llama-3-8B, Mistral-7B-v0.3, Qwen2-7B | 2-10 wrong confederates | conformity | rises with number; lower with confidence | [b19] |
| gemini-2.5-flash / gpt-5-mini / flash-lite | wrong majority in puzzles | self-correct | 34.4 / 30.0 / 3.6% | [a27] |
| Llama3.3-70B, Qwen3-32B | debate | DCR | up to 86.36% | [b17] |
| 5 GPT-4o agents | peer stances | strict conformity | 29.30% (CI 27.5-31.2) | [c17] |
| Four model families | peers disagree or assert consensus | yield | 44-98% | [c15] |
| GPT-4o-mini, Llama-3.1-8B, Mistral-7B | debate | MMLU change | -12.0 (mixed group) | [a24] |
| 10 same-model 7-8B agents | 3 rounds | modal adoption | up to 85.5% | [c18] |

Observations:
- Even 2025 models (gpt-5-mini, gemini-2.5-flash) correct a wrong majority only about a third of the time [a27].
- No closed-frontier flip table was found. Hussain and Nielbo cover open models only. HiddenBench covers 15 frontier models but measures pooling, not flips [d01, d13].
- Small open models dominate the sycophancy numbers. Confidence intervals are wide (Wynn used 100 questions per cell).

### 6.3 Hidden-profile results for LLMs

- 15 LLMs, 65 tasks. Distributed 30.1% vs full-info 80.7%. Gemini-2.5-Pro best post-discussion 0.671 (gap to its full-profile score -0.310). GPT-5 variants no better than GPT-4.1-mini [d01].
- Before discussion, hidden-profile accuracy 0.008, so the task is built right [d01].
- Controllers: Consilience best 0.83, rules controller 0.843, full-info 0.731, round-robin 0.26, unstructured 0.285 [d07].
- Second benchmark: uncontrolled 0.498, best LLM+Vote 0.668 [d07].
- Memory at the decision stage: 60 templates, 480 tasks, small open models. Removing attribution tags gave +13-24 points [d08].
- Single-agent comparison: on hidden-profile tasks only, DCI scored 9.56 and beat the single agent, while overall the single agent won [d09].

### 6.4 What changed behaviour, and by how much

| Change | Effect | Source |
|---|---|---|
| Independent sampling + vote vs talk | +4.9 to +10.4 points over single; beats debate | [c07] |
| Prompt: agree 90% of the time | Multi-Persona +15, SoM +5 (376 USMLE items) | [b09] |
| Hostile vs friendly instruction | strong-agreement 9.5-19.3% vs 70.7-96.3% | [c21] |
| Centralized judge | DCR down 40.4 points (81.71 to 41.27) | [c12] |
| Third agent | collapse lower; MMLU-Pro 72.10 vs 66.46 single | [b18] |
| One correct dissenter | yield down 54 to 73 points | [c16] |
| Devil's advocate | Llama-3-8B base 63.20% to 41.37% sycophantic | [b20] |
| Instructed adversarial agents | GPT-4.1 0.233 to 0.492; Gemini-2.5-Flash 0.889 to 0.306 | [d03] |
| Reasoning off | gain up (4 models) | [d06] |
| Reasoning on, self-derivable | resistance +7.2, receptivity +9.6 | [d13] |
| Reflection | resistance +7.9, receptivity -15.3 | [d13] |
| Payoff prompt | no effect | [a25] |
| Remove attribution tags | +13-24 points | [d08] |
| Source-stripped re-ask | 66.5% vs 10.3% harmful | [d12] |
| Forced full disclosure | 0.037 to 0.926 | [d04] |
| Share-all prompt | 0.467 | [d02] |
| Heterogeneous mix | +6.4 to +8.2% over averages | [b12] |
| Weak member added | up to -12 points | [a24] |
| Discussion history shown | challenge rate down 10% overall, 60% on StrategyQA | [a29] |
| Minority classifier | +1.71% net | [d11] |
| Drift policy | fixes 31% of drift cases | [c22] |

### 6.5 Caveats common to nearly all of this section

- Models are mostly 7-9B open models, 2-5 agents, 2-5 rounds.
- Many 2026 items are preprints, some anonymous or abstract-only (c18, c20, c21, d15).
- Peer text is often scripted (Zhu, Hussain), not generated by live agents.
- Nothing tests the exact thing our agent does: one model, one scaffold, an internal dissent step, equal tokens.

---

## 7. What our agent should take

Status marks: [E] established, [S] single source, [C] contested. Schema parts: G = guardrail, S = state, O = operator, M = memory.

### Add now (established)

These confirm or sharpen what the schema already says. They need wording, code and logging, not a new test.

1. **G9 stays: no debate; independent samples with a code vote.** Part G9. [E]. Evidence: a22, b05, c07, a19, a21, b10, c06, d10, d14, c18 (K07). Debate does not beat a vote of the same number of independent samples, adds correlation (d14) and costs 2.1-3.4x (c18). Caveat: d10 has debate +1.3 over SC on MMLU-Pro at up to 20x budget, so the rule is "match tokens against a vote" (G7), not "debate never wins".
2. **G4: agreement is a hint; log every flip with its direction and its pressure source.** Part G4, section 6 log. [E]. Evidence: a24, b01, a27, c13, a20, b14, a26, c17, c18, d12, d13 (K08). Add to the log: whether the pressure was the model's own earlier text.
3. **G5: structure over prompt.** Any judge or critic must be structural: independent samples as input, no authorship, no majority count, length-normalised scores. Part G5. [E]. Evidence: a26, b17, c12, c16, c15, d07, d09 (K15). Prompt-only fixes (payoff, "be careful", tone) are not to be relied on (a25, b04 [S]); this matches section 4b.
4. **S3: attempts stay isolated (already in schema); add the reason.** Part S3. [E] in direction. Evidence: d14 (independent sampling keeps Neff, dense debate saturates), c17 (37% of answers change with no peer), d12 (repetition alone drives flips).
5. **Do not rely on a panel to pool partial information.** Part G4/G9. [E]. Evidence: b25, d16, d01, d02, d04, a15 (K02, K25). If evidence is split, one agent should get all of it, or a forced-disclosure step must come before judging. Our agent is one model with one context, so this is a design rule for any future multi-role mode.
6. **No fixed dissent quota in the schema.** Part G4, O-dissent. [E] that no optimum transfers. Evidence: a18, b22, a19, b09, c05, d03, d05 (K11). Any dissent step fires on a signal (G1), never on a share.
7. **Human conformity numbers are context, not estimates.** Part G4. [E]. Evidence: a07, a08, b24, a09 (K04). 25-37% for people. LLM conformity depends on framing and can be far higher (66.5% speaker-free).
8. **Groupthink as a concept is not a design basis.** [E]. Evidence: a03, b30, a01 (K01). Model structural faults (same model, no isolation, no outside input), not cohesion.

### Test first (not yet in the schema)

Format: item | schema part | status | evidence | reason.

1. **Internal dissent step vs k-sample vote at equal tokens.** O (new) or G9 exception. [S]. Evidence: d09, d10, d14 (K31). The most decisive missing test.
2. **Commit-before-sharing.** S3/S4. [S]. Evidence: b26, d16, d05, d06 (K03, K27). Human fix; indirect LLM support only.
3. **Premature-consensus flag in agent state.** S6 trigger or S7. [S]. Evidence: d07, d04 (K26). Signal: attempts agree, few distinct evidence items used, unused facts remain.
4. **Unused-evidence step before commit (Exchange-then-Decide, single-agent form).** S4/S7. [S]. Evidence: d04, d01, d02 (K25). Panel version worked; single-agent version untested.
5. **Strip attribution and counts from judge input and lesson memory.** S1 hygiene, M. [S]. Evidence: d08, d12, c17 (K28, K30). Cheap.
6. **Never show the agent its own earlier wrong sample as a peer.** G4/S5. [S]. Evidence: d12 (K28).
7. **Grounded vs self-generated objection.** O (dissent). [S]. Evidence: d03, a34, b19, b20, c16 (K32, K14). A dissent step tied to a failing check follows G2; a free one is model-dependent.
8. **Score any dissent or reflection operator on both resistance and receptivity.** G7 method. [S]. Evidence: d13 (K29). Candidate rule for SCHEMA.md section 8.
9. **Verifier-gated minority overturn.** S7. [S]. Evidence: c19, d11 (K20). The published rule is a classifier, not a verifier; the verifier form is our proposal.
10. **Vote rule by task type (consensus for knowledge, vote for reasoning).** S0 mode, S7. [S]. Evidence: a28, c08, a29 (K16).
11. **Reasoning off or short when conformity risk is high.** G11. [S]. Evidence: d06, d13 (K27, K29). Sources point in different directions.
12. **Panel composition (same vs mixed model).** O-panel. [C]. Evidence: b12, a24, b03, c26 (K09, K10). Only if the agent ever uses a second model.
13. **Forced majority-bias update rules (Conformist/Follower).** G9 variant. [S]. Evidence: a23, b07, c25 (K18). Probably not worth it since the vote beats them (0.7691 vs 0.7629).
14. **Topic-drift tracking in long self-dialogue.** S6. [S]. Evidence: c22 (K21). Low priority.

See UNKNOWNS.md for the test matrix and thresholds.

---

## 8. Concrete tests on our bench

All tests: same model, equal total tokens in both arms (within 5%), same items and seeds. Report the mean with a paired bootstrap 95% interval. Log every flip with its direction. Use items where the plain pass rate is between 30% and 85% (below that there is little to gain, above that the vote saturates).

| # | Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|---|
| T1 | Dissent step vs vote | ARC-style items with check; BrainTeaser; MMLU-Pro slice | A: k independent samples + code vote. B: (k-1) samples + one critic pass that sees the leading candidate and writes the strongest objection, then code re-vote | accuracy; flips right-to-wrong and wrong-to-right | B within +/-1 point of A, or worse (prior from d09, d10, d14). A gain would show only on items where the plain vote is split |
| T2 | Wrong-peer flip probe | MMLU/GPQA-style questions the agent gets right alone (at least 3 of 4 samples) | k=0,1,2,3 wrong confident peer answers written by another model; with and without S1 input hygiene | flip rate by k; fix rate when one peer is right | Flip rate rises with k (b19, c10). Hygiene lowers flips; the fix rate must not fall more than the flip gain (d13) |
| T3 | Speaker-free floor | same questions | (a) plain re-ask, (b) bare repeated wrong answer, (c) expert-panel frame | harmful revision rate | (b) near (c), both far above (a) (d12: 66.5 / 79.4 / 10.3). Frontier models may differ; this measures it |
| T4 | Commit-before-share | 30 hidden-profile tasks built from our items (best option looks worse on each fragment) | A: 3 roles see fragments, then discuss. B: each role commits a private answer and a fact list first, code merges facts, one decide pass. C: single agent with all facts | accuracy of pooled answer; share of unique facts used | A near 30% (d01). B above A. C is the ceiling (80.7% in d01) |
| T5 | Unused-evidence step | multi-clue puzzles (BrainTeaser-type; ARC items with several examples) | A: standard S3-S7. B: before S7 code lists every example or clue not cited in any attempt; one more attempt must address them | accuracy; clue coverage | Small gain on items with a hidden constraint; none on single-clue items |
| T6 | Premature-consensus flag | same as T5 | A: no flag. B: flag when all k attempts agree and no unfitted-part check exists; the flag triggers one counterexample search (S7) | accuracy; token cost of false alarms | Gain only if unanimous agreement is wrong often enough; measure that rate first |
| T7 | Attribution stripping | decision step that reads notes | A: notes with tags and counts ("5 of 5 samples said X"). B: tags and counts removed, rarest-first order | accuracy of the decider | B above A by several points on hidden-profile-like items (d08: +13-24 on small models) |
| T8 | Grounded vs ungrounded objection | items with a runnable check | A: critic writes a free objection. B: objection must cite a failing run of the check (G2). C: no objection | accuracy; resistance and receptivity | B >= C > A (d03, d13 suggest free dissent is model-dependent) |
| T9 | Reasoning budget under pressure | T2 items | short vs long thinking | flip rate and fix rate | Helps both on self-derivable items (d13); may harm elsewhere (d06) |
| T10 | Vote vs consensus by task type | knowledge (MMLU) vs reasoning (MuSR, StrategyQA) | majority vote vs unanimity-or-resample | accuracy; tokens | Vote wins on reasoning, consensus by 1-5 points on knowledge (a28) |
| T11 | Verifier-gated minority overturn | items with a check; 3 samples with a 2:1 split | A: majority. B: minority wins if it passes the unfitted-part check and the majority fails it; otherwise majority | net gain = right flips minus wrong flips | Positive if the minority is right in about 25% of splits (d11) and the check is reliable |

Sample size guide: 200 items per cell to see 3-point differences; 100 only for 8-point effects. Wynn's 100-question cells had wide error bars.

---

## 9. What does not transfer, and why

- **Human cohesion and stress (groupthink).** One model has no friendships to protect. The relevant faults are homogeneity and insulation [a03].
- **Social reward for mentioning shared facts.** The human story needs reputation. The machine analogue is token frequency in context, which Hu and Qu show matters without any social frame [d12]. Fiedler's repetition result shows humans also respond to repetition without social cause [a13].
- **Authentic vs role-played dissent.** Human work says real dissent beats staged dissent [a10, b31]. For a single model all dissent is role-played. No LLM study separates the two (K32).
- **Oxytocin, polarization over weeks, human group size effects.** Not relevant to a single-pass agent [a15, a11].
- **Multi-agent panels as such.** Our agent is one model with code-controlled steps. Panel results (Wynn, Yao, HiddenBench) concern separate agents with a shared transcript. Our S3 isolation removes that path, so some panel failures cannot occur. The corollary: positive panel results (Consilience, DCI) may not transfer either.
- **Oracle and Reveal-All.** They need ground truth or disclosed private information [a23, d04].
- **Trained components.** DEAR (RL), Sentinel (LightGBM) and activation patching need training or white-box access. The schema is scaffold-only [c20, d11, c15].
- **Heterogeneous panels.** Strong evidence of help (b12, d14), but our agent is one model and would need a second model (K10).
- **Opinion questions with no ground truth.** c21 measures stated agreement, not accuracy.
- **Speaker-free conformity.** Transfers as a risk, not as a fix: if our agent re-reads its own wrong sample it may flip as in d12.
- **Small-model findings.** Most numbers are from 7-9B models. Frontier behaviour may differ (Bellina: large models less conformist on easy items but vulnerable at the competence boundary; abstract only) [d15].

---

## 10. Open questions

1. Equal-token single-agent dissent vs k-sample vote: no study (gap 1).
2. Flip rate for closed frontier models with a graded wrong majority (1, 2, 3 peers), and effect of a structured judge (gap 2, partly open).
3. Non-author replication of Minority Sentinel, and a verifier-gated variant (gap 3).
4. Verified numbers for Stasser and Titus 1985, Lu et al. 2012 full text (effect sizes, moderators), Mullen 1994, Nemeth 1986, Schulz-Hardt 2006 (gap 4).
5. Role-played vs grounded dissent in LLMs (gap 7).
6. Why voting vs consensus split by task, and a cheap detector for it (gap 8).
7. A direct test of commit-before-share in LLMs (gap 9).
8. How much of the 2026 "yield" of 44-98% is training vs prompt vs repetition. No single controlled study separates base from instruct and source from repetition (gap 10).
9. Does conformity differ between a model's own sampled text and another model's text? Hu and Qu show repetition suffices; nobody compares self-source with other-source [d12].
10. Does the withholding threshold exist for a single model with internal roles?
11. Why did debate beat voting in Du et al. even against Du's own majority control (69.0 vs 81.8 on arithmetic)? The GPT-3.5-era model is the leading but untested explanation.
12. Validity of synthetic LLM-generated hidden-profile tasks (28.5% pass rate in generation, one author team) [d01].
13. Will the 2026 preprint cluster (c15-c22, d05-d14) survive peer review? Several are anonymous, abstract-only or from the same labs.

---

## 11. Sources

[V] = opened this session (page or PDF text). [M] = snippet, abstract, title or memory only. Evidence ids in brackets.

**Human literature**
- [V] Janis (1972), via Wikipedia "Groupthink": https://en.wikipedia.org/wiki/Groupthink (a01, a02, a03, b30, b31)
- [V] Asch (1951-56), via Wikipedia "Asch conformity experiments": https://en.wikipedia.org/wiki/Asch_conformity_experiments (a09)
- [V] Franzen and Mader (2023) PLOS ONE: https://doi.org/10.1371/journal.pone.0294325 (a07, a08, b24)
- [V] Wikipedia "Hidden profile": https://en.wikipedia.org/wiki/Hidden_profile (a05)
- [V] Wikipedia "Shared information bias": https://en.wikipedia.org/wiki/Shared_information_bias (a06)
- [V] Wikipedia "Group polarization": https://en.wikipedia.org/wiki/Group_polarization (a11)
- [V] Fiedler et al. (2018) Frontiers in Psychology: https://europepmc.org/article/PMC/PMC5996453 (a12, a13)
- [V] Pescetelli et al. (2022) PLOS ONE: https://europepmc.org/article/PMC/PMC9345362 (a14)
- [V] Oxytocin and hidden profiles, Sci Rep (2017): https://europepmc.org/article/PMC/PMC5225413 (a15)
- [V] Faulmueller et al. (2010): https://doi.org/10.1177/1368430210369143 (d16)
- [M] Stasser and Titus (1985): https://doi.org/10.1037/0022-3514.48.6.1467 (a04, d18)
- [M] Nemeth (1986): https://doi.org/10.1037/0033-295X.93.1.23 (a10)
- [M] Schulz-Hardt et al. (2006): https://doi.org/10.1037/0022-3514.91.6.1080 (a34, b27)
- [M] Mullen et al. (1994) / Esser (1998): https://doi.org/10.1177/0146167294205 (a35)
- [M] Lu, Yuan and McLeod (2012): https://doi.org/10.1177/1088868311417243 (b25, d17)
- [M] Mojzisch and Schulz-Hardt (2010): https://pubmed.ncbi.nlm.nih.gov/20438225/ (b26)
- [M] Reimer et al. (2010): https://doi.org/10.1080/03637750903514318 (b28)
- [M] Lorenz et al. (2011): https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3107299/ (b29)

**LLM literature**
- [V] Du et al. (2023): https://arxiv.org/abs/2305.14325 (a16, a17, b15, b16, c01)
- [V] Liang et al. (2023/24): https://arxiv.org/abs/2305.19118 (a18, b22, c02)
- [V] Smit et al. (2024): https://arxiv.org/abs/2311.17371 (a19, b08, b09, c05)
- [V] Wang et al. (2024): https://arxiv.org/abs/2402.18272 (a20, b13, b14, c04)
- [V] Zhang et al. (2025): https://arxiv.org/abs/2502.08788 (a21, b10, b11, b12, c06, c26)
- [V] Choi, Zhu and Li (2025): https://arxiv.org/abs/2508.17536 (a22, a23, b05, b06, b07, c07, c25)
- [V] Wynn, Satija and Hadfield (2025): https://arxiv.org/abs/2509.05396 (a24, a25, b01-b04, c09, c10, c11)
- [V] Yao et al. (2025): https://arxiv.org/abs/2509.23055 (a26, b17, b18, c12)
- [V] Wu, Li and Li (2025): https://arxiv.org/abs/2511.07784 (a27, c13)
- [V] Kaesberg et al. (2025): https://arxiv.org/abs/2502.19130 (a28, a29, c08, c24)
- [V] Agarwal and Khanna (2025): https://arxiv.org/abs/2504.00374 (a30)
- [V] Sharma et al. (2024): https://arxiv.org/abs/2310.13548 (a31, c03)
- [V] Khan et al. (2024): https://arxiv.org/abs/2402.06782 (a32)
- [V] Chen, Saha and Bansal (2023) ReConcile: https://arxiv.org/abs/2309.13007 (a33; abstract and method only)
- [V] Zhu et al. (2025): https://arxiv.org/abs/2410.12428 (b19, b20)
- [V] Xiong et al. (2023): https://arxiv.org/abs/2305.11595 (b21; summary conclusions)
- [V] Cemri et al. (2025) MAST: https://arxiv.org/abs/2503.13657 (b23, c14; percentages unreliable)
- [V] Not Just RLHF (2026): https://arxiv.org/abs/2605.12991 (c15, c16)
- [V] Not All Flips Are Conformity (2026): https://arxiv.org/abs/2606.00820 (c17)
- [V] The Cost of Consensus (2026): https://arxiv.org/abs/2605.00914 (c18; abstract and first page)
- [V] Minority Sentinel (2026): https://arxiv.org/abs/2606.29270 (c19, d11)
- [V] DEAR (2026): https://arxiv.org/abs/2608.03648 (c20; abstract only)
- [V] What Does Multi-Agent Debate Actually Change? (2026): https://arxiv.org/abs/2609.08016 (c21; abstract only)
- [V] Becker et al., Problem Drift: https://arxiv.org/abs/2502.19559 (c22; abstract and intro)
- [V] Li, Naito and Shirado, HiddenBench (2026): https://arxiv.org/abs/2505.11556 (d01-d04)
- [V] Mansuri et al. (2026): https://arxiv.org/abs/2609.38324 (d05, d06)
- [V] Babu et al., Consilience (2026): https://arxiv.org/abs/2608.20564 (d07)
- [V] Imel et al., CrossProfile (2026): https://arxiv.org/abs/2610.37624 (d08)
- [V] Prakash (2026) DCI: https://arxiv.org/abs/2603.11781 (d09)
- [V] Wunderlich et al. (2026): https://arxiv.org/abs/2605.01566 (d10)
- [V] Hu and Qu (2026): https://arxiv.org/abs/2607.05545 (d12)
- [V] Hussain and Nielbo (2026): https://arxiv.org/abs/2608.11247 (d13)
- [V] Bertalanic and Fortuna (2026): https://arxiv.org/abs/2606.02646 (d14)
- [M] Bellina et al. (2026): https://arxiv.org/abs/2601.05384 (d15; abstract only)
- [M] Estornell and Liu (2024), known second-hand only; no URL recorded (c23)

*Note: the 2026 arXiv ids are as recorded in the evidence files (opened in earlier passes per critique.md); they were not re-opened in this writer pass. Evidence flagged opened:true in the files is marked [V]; a few of those were abstract-level reads, noted above.*
