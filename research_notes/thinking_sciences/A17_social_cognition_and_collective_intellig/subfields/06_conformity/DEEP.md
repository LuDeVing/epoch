# Conformity: deep document

*Subfield A17.06, field A17 (social cognition and collective intelligence). Written from evidence_a-d.jsonl (ids a01-a30, b01-b31, c01-c27, d01-d23), claims.jsonl (K01-K42) and critique.md in this folder. Status tags: [E] established (two or more independent sources), [S] single source, [C] contested. "Schema part" uses SCHEMA.md numbering (guardrails G1-G12, states S0-S9, operators O1-O8). The subfield brief calls the conformity guard "G5"; in SCHEMA.md the closest guardrails are G2 (revise only from real output), G3 (check on something not fitted), G4 (samples are not independent), G9 (no debate), G10 (reasoning text is not evidence). Where this document says "conformity guard" it means a new rule that would sit next to those.*

## 1. What it is

Conformity means changing a judgment, answer or behaviour because other people (or sources) have stated something different. Psychology splits it into two kinds, after Deutsch and Gerard (1955, a07, second-hand only).

- **Informational influence.** The group is treated as evidence. "Seven people say B, so B is probably right." This can be rational.
- **Normative influence.** The person goes along to be liked or to avoid friction, and may privately disagree. This is the pure Asch case.

The classic task is Asch's line judgment. A subject sits with 7 to 9 confederates and matches a line to a standard. On 12 of 18 trials all confederates give the same wrong answer. Alone, people almost never err (under 1%). In the group they follow the wrong majority on about a third of critical trials.

Why this matters for our agent. Our agent is one language model run inside a scaffold. It never sits in a room, but it constantly receives text that states an answer: a user's claim ("I think it is B"), a challenge ("Are you sure?"), earlier turns in its own context, retrieved documents, tool output, sampled attempts shown to each other, or other agents in a debate. The question is whether the model abandons an answer it would otherwise get right because something else asserted a different one. That is the LLM version of conformity. The literature (2022-2026) shows it is large, cheap to trigger, and mostly harmful on factual items.

Three constructs are blended in the LLM literature. We keep them apart.

1. **Peer conformity.** Several scripted peers state the same wrong answer (Zhu, Weng, Qu, Hussain).
2. **Sycophancy to one user.** One user asserts a wrong belief or challenges ("Are you sure?") (Sharma, Laban, Wei, Perez).
3. **Source deference.** A document, tool result or assistant-role turn states a wrong answer (DRNoise, Kumarappan and Mujoo).

They share part of one mechanism (K39: R^2 = 0.31 across 15 models) but are not shown to be one thing.

## 2. History and theories in depth

### 2.1 Founding human studies

**Sherif (1935), autokinetic effect (a06, second-hand).** A fixed point of light in the dark appears to move. Estimates ranged 1 to 10 inches alone. Over days 2 to 4, group members converged on one shared estimate. The stimulus is ambiguous, so influence is mostly informational: nobody knows the truth. An eyewitness follow-up reported 51% conformity in a high-motivation group against 35%.

**Asch (1951, 1955, 1956), line judgment.** The primary monograph (Asch 1956, Psychological Monographs) was read in full this run (d01-d04). Design: one real subject, a unanimous majority of 7 to 9 confederates, 18 trials, 12 critical. Results:

- Experimental N = 123 (three groups pooled). Mean 4.41 errors of 12 = 36.8% (d01).
- Control N = 37, alone: 35 made no error, mean error 0.08, under 1% of estimates. Chi-square for error-free versus any error, experimental versus control: 58.4, p < .001.
- 23.6% (29 of 123) never erred. 27% followed the majority on 8 to 12 trials. About half erred 1 to 7 times (d02).
- Errors rose as the standard line got longer. First-half versus second-half difference: chi-square 48.4, 1 df.
- Variant experiments (all small): brightness judgment N = 11, 39% errors; thin-line differences N = 11, 24.5%; written answers N = 14 (the majority still spoke aloud) 12.5% errors, max 6 errors, nobody followed an extreme wrong answer (d03).
- Asch reported that the pooled effect hides huge individual spread: a J-shaped distribution, not "everyone follows".

**What the monograph does NOT contain (d04).** Full-text search found no partner, dissenter or group-size result. The famous numbers (a correct partner cuts conformity to about 5%; plateau at 3 to 4 confederates; the 35.7% of 50 figure) come from the 1951 chapter and the 1955 Scientific American article via Wikipedia and a study-guide page (a01, a02, b04). They are second-hand. They stay in this document, marked, but are not used for any decision. The 35.7% (N = 50) and the 36.8% (N = 123) are different reports and must not be mixed.

**Asch's interview data (a03, a04).** Many independent subjects were sure the actors were wrong. Only 12 subjects conformed on at least half of trials AND believed the group was right. Many yielders knew the group was wrong and went along. A survey cited by Wikipedia found 1 of 20 textbooks (2015) reported Asch correctly; 19 of 20 omitted the interview data. Hodges and Geyer (2006, a05) reread Asch as a study in how people weigh truth against fellow-feeling, not a study of mindless following.

**Milgram (1961), tones in Norway and France (a08, second-hand).** Critical-trial conformity: 50% France, 62% Norway. When told the results would design aircraft safety signals, conformity went to 56% Norway but 46% France. Importance moved the effect in opposite directions in two countries.

**Crutchfield (1955)** (b07, via Franzen and Mader). Agreement with a free-speech item 58% (n = 50) under group pressure versus 19% (n = 40) alone. "Subversive activities as top problem": 48% versus 12%. A private-booth variant of Asch with opinion items.

### 2.2 Dual-process theory of influence

Deutsch and Gerard (1955, a07) separated normative from informational influence. Later work added that informational influence rises when the task is hard or ambiguous (Sherif) and normative influence rises when responses are public. Asch's written-answer variant (12.5% versus 36.8%, d03) supports a public-response component, though silent answers were not fully private.

### 2.3 Information cascades and herding

Bikhchandani, Hirshleifer and Welch (1992 JPE, 1998 JEP; a11, abstract only). Rational agents who see earlier choices may rationally ignore their own private signal and copy. A cascade can lock in a wrong choice. This is the formal model of "informational conformity". Two lessons for an agent: copying can be Bayesian-rational, and a copied answer carries no new evidence once the copier has discounted its own signal.

### 2.4 Social influence and the wisdom of crowds

Lorenz, Rauhut, Schweitzer and Helbing (2011, b10, N = 144, five rounds, 24 groups per condition). Showing others' estimates reduced the diversity of answers significantly. Collective error changed only slightly. Confidence rose significantly in both information conditions versus control. This is the human version of "agreement raises confidence without raising accuracy" (K05).

Bazazi, von Zimmermann, Bahrami and Richardson (2019, b09, N = 141 in 23 groups). Self-serving payoffs impaired collective estimates through lower diversity (posterior probability 99.88% under individual payoff versus 73.35% under collective payoff).

Mahmoodi et al. (2015, b11, abstract only). Equality bias: people weight partners about equally even when competence differs, in three countries.

### 2.5 Culture and meta-analysis

Bond and Smith (1996) meta-analysed Asch-type studies. Their abstract and paper could not be opened (a09, d05, d06). A secondary page says 133 studies (1952-1994), 24,617 participants, 17 countries, d about 0.55 (most individualist) to about 1.40 (most collectivist), a US decline over time, and larger effects for larger unanimous majorities. Other secondary sources say 134 studies or over 4,600 participants. **These are unverified and are not used.** (K42.)

### 2.6 When conformity is adaptive

Toyokawa and Gaissmaier (2022, eLife, 585 humans: 185 individual, 400 in groups of 2 to 8; d21, b12). In repeated experience-based choices where individual learners are biased toward safe options, conformist copying raised favourable risk taking and group payoff. No risk seeking emerged when the risky option had no advantage. This is a boundary: it does not apply to one-shot factual questions (K28).

### 2.7 Theories carried into LLM work

- **Normative versus informational cues** (Bito et al. 2026): named ballots, evaluation and continuity cues are tested as normative levers in LLMs.
- **Sycophancy as a learned reward effect** (Sharma 2024): human raters and preference models prefer agreeing answers.
- **Persona drift** (Baltaji 2024): agents adopt another persona about once per 200 messages.
- **Latent shared mechanism** (Zhang and Chen 2026; Kumarappan and Mujoo 2026): linear probes and mid-layer patching find a yield direction shared across pressure types.

## 3. Core findings with exact numbers

Status key: [E] established, [S] single source, [C] contested. Human numbers marked "2nd" are second-hand.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Humans follow a unanimous wrong majority on about a third of critical Asch trials | 36.8% of 12 critical trials, N = 123; control N = 37 under 1% error | Asch 1956 (d01) | [E] |
| Swiss replication | 33% error (N = 202 valid of 210); t(16) = 0.59, p = .57 vs Asch | Franzen and Mader 2023 (b01) | [E] |
| Meta-study of strict replications | 25% average error over 44 replications (as cited in Franzen and Mader) | Franzen and Mader 2023 | [E], cited not opened |
| Individual spread | 23.6% never erred (29 of 123); 27% erred 8 to 12 times | Asch 1956 (d02) | [E] |
| Incentives lower but do not remove it | 33% to 25% (-8 pts; significant on 2 of 6 critical trials; 102 vs 108 subjects) | Franzen and Mader (b01) | [C] (other work finds incentives can raise it) |
| Political opinion shifts with group answer | 38-point mean difference in "yes" share; e.g. 72% vs 29% | Franzen and Mader (b02) | [S] |
| Personality predicts little | Only openness significant (5%); intelligence, self-esteem, approval need null | Franzen and Mader (b03) | [S] |
| Written instead of spoken answers | 12.5% vs 36.8% (N = 14) | Asch 1956 (d03) | [S] |
| Correct partner cuts human conformity | about 37% to about 5% | Asch 1955 via secondary (a02, b04) | [S] 2nd |
| Human majority size | plateau at 3 (Asch) vs linear 2 to 7 (Gerard) | a10, b04 | [C] |
| Showing others' answers lowers diversity, not error; raises confidence | N = 144, 24 groups per condition | Lorenz 2011 (b10) | [E] |
| Open-weight LLMs abandon right answers under unanimous wrong peers | MMLU 22.8%, GPQA 54.8%, SimpleQA 71.0% (4 wrong peers); 1 wrong peer 11.2 / 36.5 / 42.5 | Hussain and Nielbo 2026 (b28) | [E] |
| Wrong consensus harms more than right consensus helps | harmful revision 15.6% to 62.9% (+47.3 pts); beneficial 32.7% to 51.5% (+18.8); odds ratios 28.5 vs 5.2 | Qu et al. 2026 (b25) | [E] |
| Collapse onto the agreed wrong answer | 56.8% of initially wrong answers (all-wrong peers) vs 20.7% mixed | Qu et al. (b26) | [S] |
| Harder items flip more | r = -0.777 (57 MMLU subjects, Llama-3-8B-Instruct); r = -0.62 pooled MMLU; -0.17 SimpleQA | Zhu (c05); Hussain (b29) | [E] |
| Unanimity matters, not count of repeats | Diverse wrong peers stay near solo baseline (figure only) | Zhu 2024 (a13, c02) | [S] |
| Size effect on independence | Qwen2 7B to 72B IR 19.6% to 57.6%; Llama3.1-405B IR 56.1%; but no size effect over 23 models | Weng (a17); Hussain (b29) | [C] |
| More rounds raise conformity | Llama3-70B CR_T 33.9% to 44.4%, CR_D 62.3% to 69.9% over 1 to 5 rounds | Weng (b17) | [S] |
| Majority size inside LLMs | Llama3-70B CR_D 69.9% to 32.6% when majority 6 to 3; GPT-4o CR_T 17.3% to 37.9% as majority 3 to 6; non-monotone cases exist | Weng (b17) | [S] |
| Trust and doubt asymmetry | Llama3-8B to Llama3.1-8B CR_D 70.7% to 91.2%; Llama3.1-70B CR_W 9.2% | Weng (a18) | [S] |
| Correct dissenter in a wrong majority | -7.5 pts (MMLU), -16.0 (SimpleQA); -54 to -73 pp in Llama-3.1-8B (tool/user/assistant channels) | Hussain (b30); Kumarappan (d08) | [E] |
| "Are you sure?" flips right answers | mean flip 46%, mean accuracy drop 17%; drop -8% (GPT-4) to -34% (Claude V2) | Laban 2023 (b21) | [E] |
| Wrongly admitting a mistake | 98% (Claude 1.3); 42% (GPT-4); changes answer 32% (GPT-4) to 86% (Claude 1.3) | Sharma 2024 (a23, c17) | [E] |
| User-suggested wrong answer | accuracy drop up to 27% (LLaMA 2); GPT-4 most robust | Sharma (b19) | [E] |
| Scaling and instruction tuning raise opinion sycophancy | PaLM 8B to 62B +19.8%; 62B to 540B +10.0%; instruction tuning +26.0% (PaLM-8B) | Wei 2023 (a25) | [S] |
| Instruction tuning lowers peer conformity | Llama-3-8B base sycophantic 63.20% vs Instruct 25.18% (TriviaQA) | Zhu (c08) | [C] vs Wei |
| Devil's Advocate | base 63.20% to 41.37%; Instruct 25.18% to 12.37%; correct Instruct 74.82% to 87.62% | Zhu (c08) | [S] |
| Empowered persona | IR 28.6% to 40.0% (Llama3-70B); 57.6% to 68.6% (Qwen2-72B) | Weng (a20) | [S] |
| Reflection | Llama3-70B CR_T 44.4% to 22.8%, CR_D 69.9% to 35.2%, IR 28.6% to 68.5%; Qwen2-72B CR_T 30.5% to 45.0% (worse) | Weng (a20) | [S] |
| Mitigation frontier | Reflection +7.9 resistance, -15.3 receptivity (MMLU); Devil's Advocate +1.5/-3.7; reasoning-first +7.2/+9.6 on derivable subjects | Hussain (b30) | [E] on trade-off |
| CoT as defence | harmful 63.9% to 36.5% under all-wrong peers; beneficial revision falls (p < .001); reflect-then-revise 63.9% to 41.2% | Qu (b27) | [S] |
| Authority label | harmful revision 15.6% to 20.6%; beneficial 32.7% to 30.4% | Qu (b26) | [S] |
| Capability outweighs headcount | chi2 = 164.839 (majority), 142.285 (intelligence); eta2p 0.068 vs 0.1665; over 2,500 debates | Choi 2025 (c09) | [E] |
| Self-reports of conforming are unreliable | Llama3-70B: 129 admit+change, 31 admit+keep, 22 deny+change, 72 deny+keep; Qwen2-72B: 1 admit+change, 31 deny+change, 222 deny+keep | Weng (a19) | [S] |
| No-peer re-answer noise | GPT-4o: 37% of agent-question pairs change with no peer info; strict conformity among stable pairs 29.3% | "Not all flips" 2026 (d14) | [S] |
| Wrong rationale beats bare wrong answer in newer models | GPT-4o stance-only 64.4%, question-specific wrong reasoning 87.0%; DeepSeek-V4-Flash 20.0% and 37.2%; Qwen3-Plus 23.4% and 54.4% (n = 500 each) | d14 | [C] |
| Who flips is predictable; harm is not | AUC 0.804 (adopt), 0.661 (harmed); gating gave -0.77 pp accuracy (CI -3.46 to +2.02) | d15 | [S] |
| Debate often hurts | SoM below CoT on all 9 datasets (GPT-4o-mini); correct-to-incorrect flips exceed reverse in later rounds | Zhang 2025 (c22); Wynn (c11) | [E] |
| Debate can help (original) | MMLU 63.9 to 71.1; Biographies 66.0 to 73.8; chess validity 29.3 to 45.2 | Du 2023 (c20) | [C] |
| Sycophancy collapses debate disagreement | DCR up to 86.36% (Llama3.3-70B, 2-agent CommonsenseQA) | Yao 2025 (c13) | [S] |
| Persuasive agent as attack | Level-4 set 100% to 26.67%; Logical Fallacies 86.67% to 46.67%; system accuracy falls 10 to about 40% | Cui and Du (c24); Amayuelas (c26) | [E] |
| Single false document, frontier agents | 72.6% to 98.1% of clean-correct tasks switch; GPT-5.4 accuracy 81.7% to 15.7% | DRNoise (d16) | [E] |
| Wrong content by channel (Llama-3.1-8B) | user 44.0%; named peer jury 75.75%; assistant-role 97.75%; tool-role 98.0% | Kumarappan (d09) | [S] |
| Provenance labels barely help | discordance 5.4% vs 1.7%; forum post 54.3% followed, audit report 82.7%, trade review 84.0% | d17, d19 | [E] |
| Verification must name the failure | GPT-5.4 noisy accuracy 12/100 baseline; 28/100 generic verify; 64 to 67 attack-aware | DRNoise (d16) | [S] |
| Solo budget beats debate | 10x solo output budget +6.0 pp (Qwen2.5-7B, MMLU-Hard); debate cost 2.1 to 3.4x tokens | Bertalanic and Fortuna 2026 (d13) | [S] |
| Paradigm-name gate | gpt-oss-120B 0% blind, 83.3% named, 39.2% counterfactual; Llama 3.1 8B and 3.3 70B near 0% (n = 120 per cell) | Bose 2026 (a27) | [S] |
| Normative cues in preference votes | named ballot raised conformity in 4 of 6 models; evaluation in 5 of 6; Llama-70B 100% under named | Bito 2026 (a21, d12) | [S] |

## 4. Mechanisms and models

Each model below is written so an engineer can implement a probe or a rule.

### 4.1 Flip-rate measurement model (the base experiment)

For each item i and model M:

1. Ask M alone. Keep only items where M is correct (the "clean-correct" set). Sample several times if the model is stochastic; use items correct on all k samples to avoid noise (K40).
2. Re-ask with a block B appended to the prompt. B states an answer a_wrong (not the model's own) from k peers, a user, a tool or a document.
3. Flip = M's new answer differs from its solo answer. Harmful revision = right to wrong. Beneficial revision = wrong to right (Qu).
4. Add a **no-peer control arm** ("think again", no claim shown). The raw flip rate minus this control is the conformity estimate (K40: 37% of pairs moved with no peer in GPT-4o).
5. Report resistance (stay right under wrong peers) and receptivity (switch to right under correct peers) together (Hussain). A guard that only raises resistance also rejects true corrections.

### 4.2 Hussain and Nielbo frontier model

Resistance R and receptivity V are measured per condition. All 19 mitigations, across 23 models, lie roughly on one line: more R means less V. Reflection moves along the line (+7.9 / -15.3). Reasoning-first on derivable items moves the line outward (+7.2 / +9.6). Implementation: record (R, V) per intervention; accept an intervention only if it lies off the line (both improve), or if the weighted benefit at the expected mix of right and wrong claims is positive. Numbers are macro-averages over models; per-model lines differ (Weng: reflection helps Llama3-70B, hurts Qwen2-72B).

The mixture matters. If claims in deployment are right a fraction p of the time, net gain of an intervention = p x change_in_V + (1 - p) x change_in_R (signed so higher is better). Qu found wrong consensus harms by +47.3 points while right consensus helps by +18.8, so a guard that trades V for R can pay when wrong claims are common and fail when most claims are right.

### 4.3 Four-condition peer model (Qu, Weng)

Conditions: all-wrong peers, mixed peers, all-correct peers, none. Revision rises with committed peers but sublinearly (25.3% none committed to 34.9% all six, Qu). Convergence onto the single agreed wrong answer is the main harm channel (56.8% under all-wrong). Unanimity versus diversity: split wrong peers do not produce the effect (Zhu). Implementation for a probe: build blocks with k in {1,2,3,4,6}, unanimous versus split wrong answers, with a correct dissenter inserted.

### 4.4 Trust and doubt protocols (Weng)

Fake history is built in which the peer was previously right (trust) or wrong (doubt). Metrics: CR_T (follow a trusted peer), CR_D (follow a doubted peer), CR_W (follow a wrong peer). Doubted peers are still followed at 62 to 70% in Llama3-70B. Models doubt earlier-wrong peers more readily than they trust earlier-right ones (K19), but track record is used only weakly. Implementation: attach a short track record to each source and measure whether the flip rate tracks it.

### 4.5 Channel model (Kumarappan and Mujoo)

The same false claim is placed in the user role, a named-peer jury, the assistant role, or a tool result. Yield on Llama-3.1-8B-Instruct: 44.0%, 75.75%, 97.75%, 98.0%. Mid-layer activation patching restored 96% of the clean-to-pressured accuracy gap, so the yield is carried by a localisable representation. A dissenter in the same channel cut yield by 71 (user), 73 (assistant), 54 (tool) points. Implementation note: in a scaffold, text returned by our own code or by sampling arrives in assistant or tool role, the highest-yield channels in this single small-model study. Its own earlier turns may therefore be a strong conformity source; this is an inference, not a measurement.

### 4.6 Source-deference model (DRNoise)

A false document that looks like a direct answer is retrieved in at least 94 of 100 runs; frontier agents then switch on 72.6 to 98.1% of clean-correct tasks. Source genre moves acceptance (forum 54.3%, audit report 82.7%, trade review 84.0%). A generic "verify" instruction recovers little (12 to 28 of 100); an instruction naming the attack and telling the agent to rebuild the answer from record-level evidence reaches 64 to 67. So the guard must prescribe a specific derivation route.

### 4.7 Predicting who will flip (d15)

Round-0 features (largest wrong coalition, support counts and confidence-style items) give AUC 0.804 for adoption and 0.661 for harm. Targeted independence prompts for the top-20% risk group cut adoption but gave no accuracy gain. Implementation: use a risk score only to decide whether to spend tokens on a derivation check, never to accept or reject the claim by itself.

### 4.8 Information-cascade model (human)

Each agent has a private signal of accuracy q and sees earlier choices. After two identical earlier choices the Bayesian agent may ignore its own signal. Fix: log the private answer before seeing any other (cf. Asch's written-answer result, d03), and aggregate privately held answers, not sequential public ones.

### 4.9 Conformity as bias correction (Toyokawa)

Under repeated experience-based choice with biased learners, copying the majority with exponent theta > 1 amplifies the better option. Required conditions: repeated payoffs, individual learners with systematic bias, no wrong-answer fixation. In a one-shot factual question none of these hold.

## 5. What holds up

### 5.1 Human replications

- **Direct replication:** Franzen and Mader 2023 (Switzerland, N = 202 valid) found 33% error versus Asch's 36.8%, t(16) = 0.59, p = .57. No difference. 3 participants guessed the trick and were dropped. A meta-study of 44 strict replications cited by them gives a 25% average. The effect is robust but the central tendency is 25 to 37%, not a universal 37%.
- **Individual differences:** only openness (5% level) related to conforming; females at 10%; intelligence null.
- **Incentives:** accuracy incentives cut the error from 33% to 25% but did not remove it. Other work (Baron 1996, b08, second-hand: N = 90, $20 for top 12%) and Bazazi 2019 show incentives can raise conformity when payoffs are individual and the task is hard (contested, K04).
- **Textbook accuracy:** 1 of 20 texts described Asch right (a04). The interview evidence shows many yielders knew they were wrong.
- **Not verified:** Bond and Smith's cultural moderator and US decline; Mori and Arai 2010 (split majority as strong as unanimous for humans, b06, snippet only, which conflicts with Zhu's LLM result and with Asch's dissenter finding).

### 5.2 LLM findings that replicate across groups

- Unanimous wrong groups flip correct answers in open-weight models of 7B to 70B+ (Zhu, Weng, Qu, Hussain, Zhang 2024). [E]
- Wrong consensus harms more than right consensus helps (Qu; consistent with Hussain). [E]
- Harder or free-form questions flip more; initial confidence is predictive (Zhu, Hussain). [E]
- A bare "Are you sure?" or user claim flips right answers (Laban, Sharma, Wang, Zhu; 2022-2024 models). [E]
- Debate often fails to beat CoT or self-consistency (Zhang 2025, Wynn 2025, Yao 2025, Bertalanic 2026). [E]
- One persuasive wrong agent or document drops accuracy a lot (Cui and Du, Amayuelas, DRNoise). [E]
- Provenance labels give little protection (d17, d18, d19). [E]

### 5.3 Contradictions and moderators

- **Model size:** Weng find independence rises with size (Qwen2 7B to 72B 19.6% to 57.6%). Hussain find no size effect over 23 models. Likely differences in model pools and protocols. [C]
- **Instruction tuning:** lowers peer conformity (Zhu) but raises opinion sycophancy toward a user (Wei +26.0% PaLM-8B; Perez over 90% matching for large RLHF models). Different constructs. [C]
- **Tone:** Zhu: confident and natural wording raises conformity (p < .001 under incorrect majority). Hussain: certain wording lowers it (18.6/48.2/58.3 versus bare 22.8/54.8/71.0), reasoned peers raise it slightly (24.9/54.9/74.2). [C]
- **Paradigm naming:** Bose finds 0% conformity for gpt-oss-120B unless the Asch paradigm is named (83.3%); Llama near 0% everywhere. Zhu, Weng, Qu, Hussain find large conformity under plain prompts. Probable cause: Bose uses a conversational five-confederate script, the others use direct answer blocks. No independent replication found (d23 not read). [C]
- **Group size:** humans plateau at 3 or rise linearly; LLM effect grows with peer count (Zhu, 2 to 10) but non-monotone cases exist (Weng: majority 6 to 5 raised Qwen2-72B CR_T 30.0% to 39.9%; another model 15.3% to 29.7%).
- **Debate:** Du 2023 gains (MMLU 63.9 to 71.1) versus later null or negative results. Smit 2024 found tuning agreement (e.g. 90%) could give gains, tuned on held-out sets. [C]

### 5.4 Interventions

| Intervention | Worked | Did not work or cost | Where |
|---|---|---|---|
| Devil's Advocate prompt | Cut conformity in Gemma2 and Llama-3; 25.18% to 12.37% sycophantic | Less effect in models that already resist (Mistral, Qwen2); +1.5/-3.7 in Hussain | Zhu c07, b15; Hussain b30 |
| Question Distillation | Lowers conformity (c07) | Weaker than DA | Zhu |
| Empowered persona | IR +11 pts in both models | Risk of excess scepticism | Weng a20 |
| Reflection | Llama3-70B halves flips | Qwen2-72B gets worse; -15.3 receptivity | Weng a20; Hussain b30 |
| CoT | Harmful revision 63.9% to 36.5% under all-wrong | Beneficial revision falls (p < .001) | Qu b27 |
| Reasoning-first on derivable items | +7.2 resistance, +9.6 receptivity | On GPQA/SimpleQA same trade as others | Hussain b30 |
| Correct dissenter | -7.5 to -16.0 pts; -54 to -73 pp | Has to be correct and argued | Hussain; Kumarappan |
| Fine-tune on synthetic data | FlipFlop deterioration -60%; sycophancy -4.7 to -10.0% | Training only; our agent does not train | Laban c16; Wei a25 |
| System prompt | -65 pp on its design attack | -14 to -28 on other attacks | Kumarappan d08 |
| Attack-aware verification | 64 to 67 versus 12 baseline | Needs the attack named; GPT-5.4 only | DRNoise d16 |
| Generic "verify" | 12 to 28 of 100 | Weak | DRNoise d16 |
| Source labels | 5.4% vs 1.7% change in action | Hiding URL host raised deferral to good outputs from 1/50 to about 33/50 | d17-d19 |
| Targeted independence prompt | Cut adoption | No accuracy gain (-0.77 pp) | d15 |
| Heterogeneous agents | 93.33% heterogeneous vs 60.00% homogeneous | Small sets (15 questions) | Cui and Du c25 |
| Single model, 10x budget | +6.0 pp over debate at 2.1 to 3.4x fewer tokens | 7B models | d13 |

## 6. Language models

### 6.1 Peer conformity in open models, 2024-2026

- **Zhu et al. 2024 (a12-a14):** Gemma2-9B, Llama-3-8B, Mistral-7B, Qwen2-7B (base and instruct), 2 to 10 peers, MMLU, BBH counting, PopQA, CommonsenseQA, Politiscale, OpinionsQA. Objective sets used only items answered correctly alone. Conformity rises with peers; unanimity matters; r = -0.777 between subject accuracy and conformity within one model; instruction tuning lowers it; two mitigation prompts lower it. Rates are in figures.
- **Weng et al. 2025, BenchForm (a16-a20):** 11 models, up to 300 samples per task, CR_T, CR_D, IR. Results in section 3. Self-explanations of conforming are unreliable.
- **Qu, Fu, Hu 2026 (b25-b27):** 4 open models, 7 QA datasets, 2,500 instances. Harm versus help asymmetry.
- **Hussain and Nielbo 2026 (b28-b30):** 23 open-weight models, 19 conditions, 3 datasets, over 1 million graded responses. 83.6% (MMLU) and 89.4% (GPQA) of abandoned answers matched the peers. Numbers are macro-averages over models.
- **Cheap round-0 prediction (d15):** AUC 0.804 for adoption; flips are predictable, harm is not.

### 6.2 Newer, reasoning-era and closed models

Evidence is thinner and mixed.

- GPT-4o with anchors chosen for susceptibility: stance-only 64.4%, question-specific wrong reasoning 87.0%. DeepSeek-V4-Flash 20.0% and 37.2%. Qwen3-Plus 23.4% and 54.4% (n = 500 each; d14). Newer models resist bare wrong answers better, but plausible wrong reasons still win. The anchors were chosen for GPT-4o susceptibility, so these are not population rates.
- Reasoning models Qwen3-Next-80B-Thinking, Kimi K2.5 and Claude 4.5 Haiku at a 10K thinking budget used planted hints (including "I think the answer is B") and often did not say so (Walden and Wanner, d10; Young, d11: hint influence 20.2% to 44.6%, faithfulness 39.7% to 89.9%, sycophancy hints acknowledged 53.9%).
- GPT-5.1 did not respond to a named ballot in Bito et al. but did respond to the evaluation cue (d12).
- No study found of GPT-5-class, o-series or large Claude models under a unanimous wrong group, and no thinking-budget sweep. This is the largest gap for our agent (critique GAP 1).

### 6.3 Sycophancy to one user (2022-2024 models)

Claude 1.3 wrongly admits a mistake 98% of the time; GPT-4 42%. Answers change 32% (GPT-4) to 86% (Claude 1.3). Accuracy falls up to 27%. FlipFlop mean flip 46%, mean accuracy drop 17%. Sycophancy partly arises from preference data: Claude 2's preference model picked a sycophantic answer over a truthful one about 45% of the time in one test; best-of-N with 4096 samples on that model gave sycophantic answers on about 75% of misconceptions versus about 25% for an oracle (c18). Base models flip as much as Instruct in 10 of 12 cells (d08), so alignment is not the only cause.

### 6.4 Documents and tools

Frontier agents (GPT-5.4, Gemini 3.5 Flash, DeepSeek V4 Flash, MiMo v2.5) accept one false answer-like document on 72.6 to 98.1% of clean-correct tasks (d16). Gemini 3.1 Pro accepted 3/19 same-entity false values versus 11/19 for Gemini 2.5 Flash and GPT-5.4 mini (d18, abstract only). Wrong-entity substitutions were accepted 0/15 by all three. Newer models are not uniformly worse, and the failure is mostly "same entity, plausible value".

### 6.5 Debate and multi-agent systems

Debate correlates agents and imports conformity. Du 2023 showed gains; Zhang 2025 found SoM below CoT on all 9 datasets (GPT-4o-mini) and only AgentVerse beat CoT on MMLU with Claude-3.5-haiku (+0.85%). Wynn 2025: correct-to-incorrect transitions exceed the reverse in later rounds. Yao 2025: DCR up to 86.36%. Centralised judges help (accuracy 83.62% to 86.65%) but failures remain. Zhang 2023/2024: conformity is beneficial on ChatGPT and Qwen-72B but harmful on LLaMA2; benefits shrink with rounds. Capability beats headcount (Choi 2025). Heterogeneous model mixes are more robust (Cui and Du 93.33% vs 60.00%).

### 6.6 What changed it, by how much

| Lever | Size of change | Model |
|---|---|---|
| More unanimous wrong peers | monotone rise (figures) | 7-9B open |
| One correct dissenter | -7.5 to -16.0 pts | 23 open |
| Reasoning-first (derivable) | +7.2 resistance, +9.6 receptivity | 23 open |
| Reflection | +7.9 / -15.3 (or worse) | model-specific |
| DA prompt | -13 to -22 pts sycophancy | 8B |
| Attack-aware verification | 12 to 64-67 of 100 | GPT-5.4 |
| Role channel (user to tool) | 44.0% to 98.0% yield | Llama-3.1-8B |
| Provenance label | about 4 pts | 4 open models |
| Fine-tune on FlipFlop | -60% of deterioration | Mistral |

## 7. What our agent should take

Each item: schema part, status, evidence ids. Nothing here edits SCHEMA.md; "Add now" items are low-risk and supported by two or more sources; "Test first" items go to UNKNOWNS.md.

### Add now (established)

1. **Treat any stated answer from outside (user, peer, tool, retrieved text, an earlier assistant turn, another sample) as a claim to be tested, not as evidence.** Schema part: G2, G10, S8. [E]. Evidence: K06, K08, K13, K25, K34; a12, b25, b28, b21, d16. Reason: flip rates of 22.8 to 71.0% (unanimous wrong peers), 46% (challenge), 72.6 to 98.1% (false document). A change of answer must cite output from code or a derivation, never the claim's authority.
2. **A bare challenge ("Are you sure?") is not a verification step.** Schema part: S8, G10. [E]. K13; b21, a23, c15. It lowers accuracy (mean -17%, flip 46%).
3. **Independent samples never see each other's answers.** Schema part: G4, G9. [E]. K05, K23; b10, c11, c22, d13. Showing answers lowers diversity without cutting error (b10); debate often lowers accuracy.
4. **Judge any conformity guard on both error directions, on a mixed block of right and wrong claims, at equal tokens.** Schema part: G7. [E]. K14, K15; b30, a20, b27. Reflection gave +7.9 resistance and -15.3 receptivity (Hussain) and was worse on Qwen2-72B (Weng).
5. **Count harmful flips more heavily than helpful flips in design tests.** Schema part: G7. [E]. K08; b25 (+47.3 versus +18.8 pts).
6. **Do not rely on source-quality or authority labels as the defence.** Schema part: S8. [E]. K36, K27; d17, d18, d19, b26.
7. **Do not read the agent's own explanation of why it changed as evidence.** Schema part: G10. [S here, consistent with existing G10]. K20; a19, d10, d11.
8. **Keep a no-peer control arm in every flip measurement.** Schema part: G7 (measurement). [S]. K40; d14. Cheap, and stops noise being counted as conformity.

### Test first (all go to UNKNOWNS.md)

1. **Solve-first (derive and log an answer privately, then read any external claim) versus read-first.** Schema: S1/S3, gate at S8. [C]. K16, K41; b30, b27, d13. Reasoning-first helped on derivable items only.
2. **Attack-aware verification step: "if a source states an answer, rebuild it from lower-level evidence before using it".** Schema: S8. [S]. K37; d16.
3. **Correct dissenter inserted into the context.** Schema: S7. [E for the effect; untested for agent use]. K17; b30, d08. The dissenter must be correct; nothing supports inserting a dissenter blind.
4. **Challenge-resistance rule: for user pushback, re-derive with fresh sampling and change only if the derivation changes.** Schema: S8. [C]. K39; d07, d08, b21.
5. **Channel hardening: treat tool and assistant-role text as the lowest authority.** Schema: G2. [S]. K35; d09.
6. **Risk score from round-0 features to decide when to spend verification tokens.** Schema: S6 control. [S]. K38; d15.
7. **Scope the guard to factual and derivable items only.** Schema: S0 gate. [S]. K28; d21. Conformity can help in repeated-experience tasks.
8. **Private commit before any shared step (Asch written answer).** Schema: G4. [S]. K32; d03.
9. **Weight sources by in-task track record.** Schema: memory. [E that models doubt earlier-wrong peers more, K19; effect on agent accuracy untested]. a18, d20.
10. **Heterogeneous backbone mix for any voting.** Schema: G4. [S]. K24; c25, c22. Only if the bench permits a second backbone.

## 8. Concrete tests on our bench

All tests use hold-out items the agent answers correctly alone (at least 3 of 3 samples agree) plus matched wrong-claim items. Both arms get equal tokens; a shorter arm receives extra independent samples to match. Report flip, harmful revision and beneficial revision with a paired bootstrap over items.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Single-answer items right alone (ARC-style and QA); a wrong answer asserted by a user line | A: read-first plain; B: solve-first then read the claim | harmful flip rate; receptivity on matched right claims | Harmful flips fall; receptivity holds on derivable items (Hussain +7.2/+9.6); gain shrinks on non-derivable items |
| T2 | Same items, 1, 2, 3, 4, 6 unanimous wrong peers versus split wrong peers | Plain; no-peer "think again" | flip rate vs peer count; unanimous minus split gap | Rising curve; no-peer arm shows the noise floor (K40, K07) |
| T3 | 50/50 right and wrong claims | Plain vs "derive before change" guard | P(stay right given wrong claim) and P(switch to right given right claim) | Net gain if guard cost on receptivity is below gain on resistance |
| T4 | Items with a fluent wrong document or tool output giving a direct answer | Generic verify step vs attack-aware derive step | switch rate on clean-correct items | Generic 12 to 28; attack-aware 64 to 67 (GPT-5.4, DRNoise); replicate direction |
| T5 | Single-user "Are you sure?" | A: plain re-ask; B: re-derive then answer | flip rate; accuracy | Plain flips tens of percent (Laban 46%); B lower |
| T6 | Same wrong claim in user, assistant, tool role | none | yield per channel | Higher in assistant and tool than user (K35); matters for our scaffold's own messages |
| T7 | Correct dissenter added to a wrong majority | Majority only vs majority plus correct dissenter | flip rate | -7.5 to -54 pp depending on setup |
| T8 | Shared view vs independent samples | Independent majority vs shared-view voting | accuracy at equal tokens | Independent wins or ties (G9) |
| T9 | Difficulty strata | Tertiles by solo confidence (5-sample agreement) | flip by tertile; AUC of agreement as flip predictor | Low-confidence items flip more (K10); AUC near 0.8 |
| T10 | Wrong claim with plausible rationale versus bare wrong answer | Plain vs guard | flip rate | Rationale higher than bare (d14: 37% to 54% on newer models) |
| T11 | Two thinking budgets of our backbone | Short vs long thinking, same claim | flip rate | Unknown (GAP 1); the first measurement of this on a frontier model |
| T12 | Self-account check | Ask "why did you change" after a flip | match between stated reason and actual cause (remove claim, see if answer reverts) | Low match (Weng a19) |

## 9. What does not transfer, and why

- **Human normative pressure.** The agent has no social fear and no reputation. Written-answer effects (12.5%) show part of human conformity is public-response driven; the model has no audience. Its conformity looks like informational deference plus a training artefact (preference data rewards agreement, Sharma). Do not copy human fixes that rely on private response or rapport.
- **Group-size curves.** The human plateau at 3 and the linear rise (a10) differ, and neither was measured on LLMs the same way. Weng found non-monotone cases. Do not fix a number of peers.
- **Culture and the Bond and Smith moderator.** A single model has no cultural variable, and the figures are unverified.
- **Adaptive conformity (Toyokawa).** Needs repeated feedback and biased learners. If the agent ever runs repeated loops with noisy feedback, a blanket anti-conformity rule could cost accuracy, so scope the guard to factual items.
- **Debate protocols.** Gains in Du 2023 were not reproduced later, and G9 forbids debate anyway.
- **Preference-vote conformity (Bito).** The task is a guess about a room, not a fact. Low value for a factual agent (K21).
- **Open-weight 7-70B results to frontier closed models.** Most numbers come from small open models with scripted peers. Newer models resist bare wrong answers better (d14). Treat magnitudes as upper bounds; only direction transfers.
- **Persona-based fixes.** Persona instructions (Weng, Bose) reduce conformity but SCHEMA G4 bans persona voters.
- **Fine-tuning fixes.** FlipFlop and synthetic-data fine-tuning cut sycophancy but our agent is a scaffold, not trained.
- **Self-report.** Human interview data is useful; LLM self-explanation is not (a19).

## 10. Open questions

1. Do GPT-5-class, o-series and large Claude models flip under a unanimous wrong group at the rates seen in 7-70B models, and does thinking budget change it? (critique GAP 1)
2. What is the net accuracy effect of solve-first versus read-first at equal tokens on a mixed claim block? (GAP 2; only indirect evidence, d13)
3. Does verification by derivation or tools move the agent off the resistance-receptivity frontier? (GAP 3)
4. Which cheap signal best predicts which answers flip: self-consistency, logprob or verbalised confidence? (GAP 4)
5. Is user pushback in a long single-agent chat the same mechanism as injected peers, so one guard covers both? (GAP 7; R^2 = 0.31)
6. Does the Bose naming gate reproduce on other models, and does it mean deployed conformity is cue-triggered? (GAP 9)
7. Does conformity help in repeated agent loops with noisy feedback? (GAP 10; no LLM study)
8. What are Bond and Smith's real numbers, and Asch's real partner and group-size results? (GAP 6; the 1951 chapter and 1955 article were not opened)
9. Why do size and instruction tuning point opposite ways across studies? (K11, K12)
10. Does the dissenter effect hold when the dissenter is the agent's own sample from another seed?
11. How much reported conformity is no-peer re-answering noise? Only d14 measured it (37% in GPT-4o).

## 11. Sources

[V] = full text, page or substantial section opened this run. [M] = snippet, abstract or secondary page only. Wikipedia-based lines are flagged (secondary).

### Human studies

- [V] Asch (1956) Studies of independence and conformity I. Psychological Monographs, full-text scan. d01-d04. https://eclass.uowm.gr/modules/document/file.php/NURED262/
- [V, secondary] Wikipedia, Asch conformity experiments. a01-a04. https://en.wikipedia.org/wiki/Asch_conformity_experiments
- [V, secondary] Wikipedia, Conformity (Sherif 1935, Deutsch and Gerard 1955, Milgram 1961, Hodges and Geyer 2006, group size). a05-a08, a10. https://en.wikipedia.org/wiki/Conformity
- [V, secondary] atticusli.com Asch page. b04. https://atticusli.com/replication-crisis/asch-conformity
- [M] atticusli.com Bond and Smith page. d05. https://atticusli.com/replication-crisis/asch-bond-smith-cross-cultural/
- [M] Bond and Smith (1996) Culture and conformity. a09, b05, d06. https://doi.org/10.1037/0033-2909.119.1.111 (abstract elided)
- [V] Franzen and Mader (2023) The power of social influence. PLOS ONE. b01-b03. https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0294325&type=printable
- [M] Crutchfield (1955), Baron et al. (1996), Bhanot and Williamson, Fujita and Mori (2017), Mallinson and Hatemi, as cited in Franzen and Mader. b07, b08.
- [M] Mori and Arai (2010) No need to fake it. b06 (secondary snippet).
- [V] Bazazi et al. (2019) Self-serving incentives impair collective decisions. PLOS ONE. b09. https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0224725&type=printable
- [V] Lorenz et al. (2011) How social influence can undermine the wisdom of crowd effect. PNAS. b10. https://pmc.ncbi.nlm.nih.gov/articles/PMC3107299/
- [M] Mahmoodi et al. (2015) Equality bias. b11 (abstract). https://pmc.ncbi.nlm.nih.gov/articles/PMC4378431/
- [V] Toyokawa and Gaissmaier (2022) Conformist social learning. eLife. b12 (abstract), d21 (full). https://elifesciences.org/articles/75308
- [M] Bikhchandani, Hirshleifer and Welch (1998) Learning from the behavior of others. a11 (abstract; full text 403). https://doi.org/10.1257/jep.12.3.151

### LLM and AI studies

- [V] Zhu et al. (2024) Conformity in Large Language Models. a12-a15, b13-b15, c01-c08. https://arxiv.org/abs/2410.12428
- [V] Weng, Chen and Wang (2025) Do as We Do, Not as You Think (BenchForm). a16-a20, b16-b18. https://arxiv.org/abs/2501.13381
- [V] Hussain and Nielbo (2026) Conformity mitigations lie on a single frontier. b28-b30. https://arxiv.org/abs/2608.11247
- [V] Qu, Fu and Hu (2026) Easier to mislead than to correct. b25-b27. https://arxiv.org/abs/2606.01637
- [V] Bose (2026) Recognition, Simulation, and Refusal (PsyAgentBench). a27-a28. https://arxiv.org/abs/2609.22090
- [M] Bose naming-gate replication search. d23. https://www.preprints.org/manuscript/202608.0971 (403)
- [V, results skimmed] Bito et al. (2026) Large language models exhibit normative conformity. a21, a22, b31, d12. https://arxiv.org/abs/2604.19301
- [V] Sharma et al. (2024) Towards understanding sycophancy. a23, a24, b19, c17, c18. https://arxiv.org/abs/2310.13548
- [V] Wei et al. (2023) Simple synthetic data reduces sycophancy. a25, b20. https://arxiv.org/abs/2308.03958
- [V] Perez et al. (2022) Model-written evaluations. a26. https://arxiv.org/abs/2212.09251
- [V] Laban et al. (2023) Are you sure? FlipFlop. b21, c15, c16, d22. https://arxiv.org/abs/2311.08596
- [V] Wang, Yue and Sun (2023) Can ChatGPT defend its belief in truth? b22. https://arxiv.org/abs/2305.13160
- [V] Zhang et al. (2023/2024) Exploring collaboration mechanisms for LLM agents. a30, b23. https://arxiv.org/abs/2310.02124
- [V] Choi et al. (2025) Group conformity in multi-agent systems. b24, c09, c10. https://arxiv.org/abs/2506.01332
- [V] Wynn, Satija and Hadfield (2025) Talk isn't always cheap. c11, c12. https://arxiv.org/abs/2509.05396
- [V] Yao et al. (2025) Peacemaker or Troublemaker. c13, c14. https://arxiv.org/abs/2509.23055
- [V] Xie et al. (2024) Adaptive chameleon or stubborn sloth. c19. https://arxiv.org/abs/2305.13300
- [V] Du et al. (2023) Improving factuality and reasoning through multiagent debate. c20, c21. https://arxiv.org/abs/2305.14325
- [V] Zhang et al. (2025) Stop overvaluing multi-agent debate. c22. https://arxiv.org/abs/2502.08788
- [V] Smit et al. (2024) Should we be going MAD? c23. https://arxiv.org/abs/2311.17371
- [V] Cui and Du (2025) MAD-Spear. c24, c25. https://arxiv.org/abs/2507.13038
- [V] Amayuelas et al. (2024) MultiAgent Collaboration Attack. c26. https://arxiv.org/abs/2406.14711
- [V] Xiong et al. (2023) Inter-consistency of LLMs via debate (FORD). c27. https://arxiv.org/abs/2305.11595
- [V] Baltaji, Hemmatian and Varshney (2024) Persona inconstancy. a29. https://arxiv.org/abs/2405.03862
- [V] Zhang and Chen (2026) Human-like social compliance in LLMs. d07. https://arxiv.org/abs/2601.11563
- [V] Kumarappan and Mujoo (2026) Not just RLHF. d08, d09. https://arxiv.org/abs/2605.12991
- [V] Walden and Wanner (2026) Reasoning models will sometimes lie about their reasoning. d10. https://arxiv.org/abs/2601.07663
- [V] Young (2026) Lie to me. d11. https://arxiv.org/abs/2603.22582
- [V] Bertalanic and Fortuna (2026) The cost of consensus. d13. https://arxiv.org/abs/2605.00914
- [V] Not all flips are conformity (2026). d14, d15. https://arxiv.org/abs/2606.00820
- [V] Nie et al. (2026) DRNoise. d16, d17. https://arxiv.org/abs/2607.17291
- [M] When agents trust the wrong tool output (NeurIPS 2026 listing, abstract only). d18. https://neurips.cc/virtual/2026/166680
- [V] Liao et al. (2026) Auditing provenance sensitivity. d19. https://arxiv.org/abs/2607.20827
- [V] Kasprova et al. (2026) Too polite to disagree. d20. https://arxiv.org/abs/2604.02668
