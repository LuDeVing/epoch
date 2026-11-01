# Social influence on crowds: deep document

*Subfield A17.04. Sources: evidence_a-d.jsonl (ids a01-a26, b01-b26, c01-c26, d01-d21), claims.jsonl (K01-K32), critique.md. Status tags: [E] established, [S] single-source, [C] contested. Ids in brackets point to evidence lines. Several evidence lines are the same paper (Lorenz: a01-a05, b04, c03; Bazazi: a09, a10, b01-b03, c01, c02; Becker 2017: a15, b19, c04, c05; Schoenegger: a19, b14, c19, c20). Count papers, not lines.*

## 1. What it is

The question: what happens to a group's answer when its members can see what the others answered?

The classic "wisdom of crowds" result (Galton 1907, the ox-weight median) needs independent errors. The group answer is good because individual errors cancel. Social influence breaks the independence. People move toward what they see. The group gets tighter. The question is whether it also gets better.

Two linked claims make up this subfield.

1. **Mild influence shrinks diversity without raising accuracy** (Lorenz et al. 2011). Showing people the group mean, or all answers, narrows the spread of estimates. It does not move the group answer closer to the truth. People also feel more sure.
2. **Individual incentives raise convergence on the group mean** (Bazazi et al. 2019). When each person is paid for their own accuracy, they copy the shown group mean, and the group gets worse. When they are paid for the group's accuracy, they do not.

Why it matters for our agent. Our schema draws many attempts and picks an answer with code. If attempts see each other, they are no longer independent samples. They shrink toward each other. The pool looks agreed and confident, and it is not more correct. This is the human-side case for guardrails G4 (samples are not independent; agreement is a hint, not proof) and G9 (no debate), and for S3 (each attempt in a fresh context that shows no other attempt).

Scope: human lab and field studies (2011-2026), the models and re-analyses that explain them, and every LLM or AI study found that tests the same thing: multi-agent debate, herding, conformity, self-correction, mixed vs same-model groups, and aggregation. It does not repeat the voting and self-consistency material from earlier A-series documents. It links to them where they overlap.

## 2. History and theories in depth

**Before 2011: the ingredients.**
- Galton (1907): the median of 784 farmers' guesses of an ox's weight was close to the truth. Not opened [a26, b10].
- Page's diversity prediction theorem: collective squared error = average individual squared error minus diversity (the variance of the guesses). It is an exact identity [a04, b25]. Both sides of the Lorenz debate use it.
- French (1956) and DeGroot averaging: people update opinions as a weighted average of their own and others'. This is the default model of influence [a08, a26].
- Salganik, Dodds, Watts (2006): in an artificial music market, visible download counts made hits unpredictable. Latane's social impact theory: conformity grows as a power of group size with exponent below 1. Both not opened [a26].

**2011: Lorenz, Rauhut, Schweitzer, Helbing (PNAS).** The founding study [a01, a02, b04]. 144 ETH Zurich students, 12 sessions of 12, six hard Swiss facts (e.g. murders in 2006, true value 198; population density, true 184). Each person estimated five times in a row for real money (pay for accuracy only, no pay for matching others). Three conditions: no information, the last-round group mean, or all 12 trajectories. They name three harms. The *social influence effect*: diversity falls, collective error does not. The *range reduction effect*: the truth drifts to the edge of the answer range, so a group that brackets the truth early stops bracketing it. The *confidence effect*: people grow surer with no accuracy gain. They purposely left out leaders, persuasion and competition [a05]. They say the effect needs questions of moderate difficulty: if people know the answer, copying cannot show.

**2011: the same-year dispute.** Farrell re-analysed the data and showed individuals gain: their average reward rises and their confidence tracks that reward [a06]. Rauhut et al. agreed, and said this is exactly what the diversity theorem predicts when the crowd mean stays put. The harm is at group level: an outsider sees a tight, confident group and trusts it. They call it *collective tunnel vision* [a07]. So both are right. They judge different levels (K02, [E]).

**2013: Mavrodiev, Tessone, Schweitzer.** They quantify the influence rule [a08]. A guess changes in proportion to the distance to the last group mean, across questions whose answers differ by about 10 orders of magnitude. The slope varies by question (0.97 to 0.27), so the weight on others is not constant.

**2015: Madirolas and de Polavieja.** Humans combine private and social estimates as a weighted geometric mean. People who resist influence give much better group estimates [b09, b10].

**2015-2019: the "influence can help" line.** Kao et al. (2018) show guesses are log-normal and a bias-corrected mean survives influence [c06]. Jayles et al. (2017) show influence helps when the stream carries reliable information [a11, b05]. Becker, Brackbill, Centola (2017) show network structure decides the sign [a15, c04, c05]. Becker, Porter, Centola (2019) show gains even on partisan facts [a16].

**2019: Bazazi, von Zimmermann, Bahrami, Richardson (PLoS ONE).** They ask why people copy. Lorenz paid for individual accuracy. Theory split. Contest models said relative (individual) pay makes people discount public signals. Other theory (Mann and Helbing 2017, not opened [b21]) said individual pay plus a minority bonus gives good diversity [a10]. Bazazi tested it head-on. Individual pay produced copying and worse group error. Collective pay did not [a09, b01]. The authors also note that copying can help on problem-solving (search) tasks, because the group reaches a good-enough answer fast [b03]. The finding is about estimation, where diversity matters.

**2020-2022: field support and boundaries.** Da and Huang (2020) found a field version on Estimize: more public estimates made individual forecasts better and the consensus worse; hiding public data at random gave a better consensus; the platform went blind in Nov 2015 [d20, abstract only]. Almaatouq et al. (2022) reanalysed four experiments and tied the sign of the effect to the shape of the first estimates and the centralisation of influence [b08]. Mercier and Claidiere (2022) showed free discussion of reasons did not hurt on checkable problems [d21, abstract only].

**2023-2026: the same question for language models.** Du et al. (2023) showed multi-agent debate beating a single instance (not opened [b26]). Since then a run of matched-budget tests found that debate does not beat independent samples plus a vote [d01, d03, d05, d07, c09], that LLM agents conform [c07, c08, c11, b15], that they collapse in meaning [c13, c14, c17], and that a mixed pool does not beat the best single model sampled many times [d12, a21]. Section 6 covers these.

**Competing explanations of the core result.**
- *Averaging with weights* (French, DeGroot): errors cancel only if weights follow accuracy [a08, a15].
- *Information loss*: after one round the group holds fewer independent signals, so the effective sample size is smaller [b10, c15]. Even perfect Bayesian agents lose accuracy when they swap free evidence in homophilous groups [b12].
- *Metric artefact* (Jayles 2017): "diversity falls, error unchanged" is partly an identity, since mean individual squared error = collective error + diversity [b05].
- *Cluster copying*: people copy popular clusters, not averages [b18].
- *Incentive-driven discounting*: pay structure decides whether the public signal is used [a10, b11].

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Mild influence narrows spread with no gain in collective error (hard right-skewed estimates) | N=144 students, 12 sessions of 12, 6 questions x 5 rounds; 24 groups per condition; wisdom-of-crowd indicator about 1 unit lower with information than control | Lorenz 2011 [a01, a02] | [C] one lab study; field support abstract-only |
| Arithmetic mean is a bad aggregate for skewed guesses | Closer to truth than individuals in 21.3% of cases; in log space 77.1%. Swiss density: true 184, arithmetic mean 2,644 (+1,337.2%), geometric mean 132 (-28.1%), median 130 (-29.3%) | Lorenz 2011 [a03, b04] | [E] |
| Confidence rises with no accuracy gain | Significant in both information conditions vs control (clustered-SE regression; coefficients in a figure) | Lorenz 2011 [a02] | [S] |
| Individuals gain even when the crowd does not | Mean reward per estimate higher in full and aggregate conditions after 5 rounds (figure only) | Farrell 2011; Rauhut 2011 [a06, a07] | [E] (identity) |
| Change in a guess is linear in the distance to the group mean | Slopes Q1 0.97, Q2 0.27, Q3 0.83, Q4 0.60, Q5 0.40, Q6 0.46; 192 samples per question; all p<0.005 | Mavrodiev 2013 [a08] | [E] |
| People weight own view above the group | Median sensitivity S=0.34; confident quarter has S=0 peak about 7x the S=1 peak; followers under 2x; S rises up to about 2.5 orders of magnitude of distance | Jayles 2017 [a11, b06] | [E] |
| Resisting-influence subgroup beats the plain crowd (Lorenz data) | Error -17% vs -60% (true 9272); other subgroups -28%, -32%, -18% vs -60% | Madirolas 2015 [b09] | [S] post-hoc |
| Reliable sources make influence help | Virtual experts giving the truth at 0/20/43/80% of the sequence; at 0% no collective gain; gain grows with the share; 29 questions, 5,394 x 2 estimates | Jayles 2017 [a11, b05] | [E] |
| Wrong planted sources did not wreck the crowd; a push against the underestimation bias helped | 20 sessions of 9; 32 questions; n=0/5/15 virtual influencers per 20 humans | Jayles 2020 [a13] | [S] |
| Full list vs average: comparable small gains | 18 groups, 3 treatments x 6 tau; 42 questions x 12 subjects = 504 estimates per condition; estimates narrow in all | Jayles 2021 [a14, b07] | [S] |
| Decentralised networks: influence narrows and improves | N=1,360; SD -43% (13 trials, p<0.001); individual error -23%; median error 0.76 to 0.67 SD (-12%); mean 0.69 to 0.62 (-10%); control SD -3% | Becker, Brackbill, Centola 2017 [a15, c04] | [S] boundary study |
| Centralised networks follow the hub | Hub toward truth (12 trials): mean error -43%, median -48%. Hub away (13 trials): mean +19%, median +32%. Hub first guess vs group shift rho=0.92, n=57 | Becker 2017 [c05] | [S] |
| Revision size tracks initial error | rho=0.41, 95% CI [0.39, 0.43], 4,340 estimates, 1,040 subjects | Becker 2017 [a15] | [E] (also b06, c06) |
| Partisan same-party exchange improved accuracy | Error of the mean -35% vs -15% control (p<0.03); all 12 Republican and 12 Democrat trials improved (p<0.001) | Becker, Porter, Centola 2019 [a16] | [S] |
| Shape of first estimates and centralisation decide the sign | 2,885 people, 99 groups, 54 tasks, 15,562 individual and 687 collective estimates | Almaatouq 2022 [b08] | [S] reanalysis |
| Individual pay makes people copy the shown mean; collective pay does not | N=141, 23 groups of 4-8 (70 individual, 71 collective pay). Diversity: probability of less diversity with info 99.88% (individual pay) vs 73.35% (collective). Group error: 99.57% vs 69.13%. Overall payoff effect weak (diversity 76.25%, error 65.35%) | Bazazi 2019 [a09, b01, c01] | [S] one lab, one task |
| Field: more public estimates, better individuals, worse consensus | Estimize; randomised hiding of public data gave a more accurate consensus; sample sizes not recorded | Da and Huang 2020 [d20] | [S] abstract only |
| Free discussion of reasons on checkable problems did not hurt | N=1,958, groups 22-212 (mean 59); demonstrative problems: individual and aggregate improved | Mercier and Claidiere 2022 [d21] | [S] abstract only |
| LLM groups: seeing numbers gave a small gain; deliberation much more | Study 1, 14 jar photos: influence vs own first answer z=3.58, p=3.5e-4, d=0.24; deliberation beat influence d=3.25; consensus squared log error 0.164 vs 0.195 pooled (d=0.40); 167 of 168 groups converged | Barrera-Lemarchand 2026 [a20, a21] | [S] preprint |
| Copies of one model gain nothing from deliberating | z=1.22 (d=0.087, BF 5.60 for null), z=0.51 (d=0.144, BF 3.99), z=0.30 (d=0.062, BF 6.19); mixed vs clones z=3.61, d=0.48 | Barrera-Lemarchand 2026 [a21] | [S] |
| Best single model deliberating with itself beat the mixed consensus | d=0.88 | Barrera-Lemarchand 2026 [a21] | [S] |
| Same-model debate loses to independent voting at matched call count | GPT-3.5 GSM8K, 9 responses: vote 88.2 vs debate 83.0 | Huang 2024 [d01] | [E] with d03, d05, d07 |
| Debate is a martingale; vote wins | 5 agents, 7 tasks: Qwen2.5-7B vote 0.7691 vs best debate 0.7377; Llama3.1-8B 0.7242 vs 0.6929. Arithmetic (Qwen): vote 0.99 vs debate 0.76 | Choi 2025 [d03] | [E] |
| Debate beats CoT in few cells | 36 model x dataset cells: about 15% for SoM, EoT, ChatEval, AgentVerse; Multi-Persona never. MMLU: CoT 80.73, SC 82.13, SoM 74.73 | Zhang 2025 [d05] | [E] |
| Majority after debate falls vs majority of first answers | 3x Llama MMLU 61.6 to 57.8; 3x Mistral MMLU 33.6 to 24.4; 3x GPT-4o-mini 81.4 to 82.2 (flat) | Wynn 2025 [d07] | [E] |
| Debate destroys correct answers, and is costly | Ministral GSM-Hard: debate 20.7% vs self-correction 48.3% vs single shot 24.7%; modal adoption up to 85.5%; vulnerability up to 70.0%; oracle gap up to 32.3; 2.1-3.4x tokens | Bertalanic 2026 [c09, c10] | [E] |
| Oracle lock adds about 9 points to debate | Qwen2.5-7B: vanilla 0.7332, Conformist 0.7625, Follower 0.7629, oracle 0.8236; vote without debate 0.7691 | Choi 2025 [d04] | [S] |
| Re-reading own answer without outside facts loses accuracy | GPT-3.5 CSQA 75.8 to 38.1; GPT-4 GSM8K 95.5 to 89.0 (round 2); oracle label GSM8K 75.9 to 84.3; intrinsic 74.7 | Huang 2024 [d02] | [E] |
| Naive revision turns correct answers wrong | About 38% of correct answers converted to wrong by a revise-trained PaLM 2-S* | Snell 2024 [d14] | [E] with d02, d15 |
| Asch-type shift toward a supplied word | 22 points at n=1, 49 at n=10, under 3 points between n=5 and n=10; far distractor under 2; per model at n=10: +73 to +33 (claude-sonnet-5-5 +39, claude-opus-5-5 +33) | Rajasekaran 2026 [c11, c12] | [E] with b15, c07 |
| Herding in LLM peer groups | 2-agent flip rate 0.48; strong-factors bundle 0.63/0.59; prompt controls 0.55 either way | Herd Behavior 2025 [c07, c08] | [E] |
| Adversarial agent drags the group | Accuracy -10 to -40%; wrong-answer agreement up over 30% | Kraidia 2026 [b15] | [S] |
| Semantic collapse in LLM loops | Cosine distance last 500 vs first 10 rounds 0.192; 13 interventions failed | Kong 2026 [c13, c14] | [S] |
| Narrow attention bounds effective sample size | Werewolf narrow 0.00 vs wide 0.87 at n=6; HiddenBench +0.64 | Liu 2026 [c15, c16] | [S] |
| Exposure format matters (open models) | StrategyQA: baseline 58.3, candidates only 65.7 (+7.4), reasoning exchange 51.9 (-6.4); similarity 0.845 vs 0.916 | Kaesberg 2025 [d10] | [S] |
| Mixed pools do not beat the best model sampled many times | Self-MoA beat mixed MoA by 6.6 points (AlpacaEval 2.0), 3.8 on average | Li 2025 [d12] | [E] with a21, d06 |
| Median of many samples wins on estimates | LLaMA-3.1-8B MARBLES normalised error: median 0.81, majority 0.94, mean 4.80, greedy 2.80 | Chuang 2025 [c21] | [C] |
| 12-LLM crowd matches 925 humans | Brier 0.20 vs 0.19, t(60)=0.19, p=0.850; 31 questions | Schoenegger 2024 [c19] | [E] |
| Showing a strong reference helps, but averaging helps more | GPT-4 Brier 0.17 to 0.14 (p=0.003); Claude 2 0.22 to 0.15 (p<0.001); updated forecasts worse than plain average (0.13, 0.14) | Schoenegger 2024 [c20] | [E] |
| Single-attempt accuracy flat in temperature 0 to 1 | GPT-3.5 CoT, 1,000 questions, H(10)=10.439, p=0.403 | Renze 2024 [d17] | [E] |

## 4. Mechanisms and models

**4.1 Diversity prediction identity (implement as a diagnostic).**
For answers x_i and truth t (use log(x/t) for skewed quantities):
mean_i (x_i - t)^2 = (mean(x) - t)^2 + var(x).
Two consequences.
- If peer exposure shrinks var(x) and the mean does not move, average individual error falls. That is a fake gain at the group level.
- Log both numbers every time: error of the pooled answer, and mean error of attempts. Credit only the first.

**4.2 Weighted-average influence (French / DeGroot, fitted).**
New guess = (1 - S) x own + S x social, with S the weight on others. Humans: median S = 0.34 [a11]. In Mavrodiev, the guess change equals slope x (group mean - own previous guess), slope 0.27 to 0.97 by question [a08]. Weight rises with distance up to about 2.5 orders of magnitude [b06] and with group size [c06]. For a harness: measure S per attempt as |new - old| / |peer - old|.

**4.3 Why mean pooling goes wrong on skewed data.**
Guesses are log-normal or Cauchy-like [a11, c06]. The arithmetic mean is dominated by the right tail (+1,337% on density). Use the median or geometric mean. Kao's corrected mean is another option [c06]. For LLMs the finding repeats: the median beat majority and mean on numeric estimates [c21].

**4.4 Sequential vs simultaneous influence.**
Lorenz is simultaneous round-wise feedback of the whole mean. Jayles is a sequence in which each person sees the geometric mean of 1 to 11 prior answers (tau). Sequence plus reliable sources produces gains; sequence without them does not [b05]. A harness that shows attempt k the earlier k-1 attempts is a sequential design. A harness that shows all N the previous round's mean is a Lorenz design.

**4.5 Network centralisation and shape of first estimates (Almaatouq).**
Let R measure heavy-tailedness (log-normal vs normal fit of first estimates). Rule from the reanalysis: skewed or heavy-tailed first estimates plus centralised influence can help; a crowd centred near the truth plus dominant voices hurts [b08]. Becker adds that a hub's first guess predicts the group shift (rho=0.92) [c05]. An implementable gate: compute kurtosis of log answers across N first-round attempts, and allow exposure only in the heavy-tail class. Untested for LLMs (U5).

**4.6 Incentive model (Bazazi).**
Pay A: each agent scored on its own error. The rational response to a shown group mean is to move toward it. This lowers its own error and the group's diversity. Pay B: each agent scored on the error of the group mean. Moving toward the mean gains nothing, since the mean does not improve by a copy of itself. Result: copying vanishes [a09]. Theory agrees: pay "reformers" whose input reduces collective error even if personally wrong [b11]. Engineering reading: in a harness, the incentive is not a sentence in a prompt. It is the selection rule. If code keeps only the answer that wins on a group or external check, copying has nothing to gain.

**4.7 Debate as a martingale (Choi).**
Mean belief in the correct answer does not change across rounds in unbiased debate. It rises only if the update rule is biased toward correction (an oracle lock adds about 9 points) [d03, d04]. The Conformist and Follower prompts add about 3 and still lose to plain voting [d04]. Test: log per-attempt correct-to-incorrect and incorrect-to-correct flip rates after exposure. If they are equal, the exchange step is only cost.

**4.8 Flip probability by social position (Wynn).**
P(correct to incorrect) is largest when no peer agrees and drops with each agreeing peer [d08]. Resistance falls in round 2. One confident wrong peer pulls a lone correct attempt most.

**4.9 Conformity saturates (Rajasekaran).**
The pull on an LLM grows up to about 5 sources, then flattens (under 3 points from 5 to 10). A far-off word gets no pull. Influence works on plausible alternatives [c11].

**4.10 Hidden anchors.**
Each LLM has an internal opinion that pulls it whatever neighbours say; classical consensus models fit poorly (held-out R2 0.44 vs 0.05 on Llama) [c17]. DeGroot predicted only 60% binary and 32% three-class accuracy of final opinions [c18]. Do not model LLM influence with a fixed averaging weight.

**4.11 Effective sample size.**
Narrow attention yields herding: the effective sample size stays bounded however many agents are added [c15]. Same-model samples are already alike, so the starting effective N is below the nominal N. Exposure lowers it further.

**4.12 Gated acceptance.**
Accept a revision only if an exact check passes. The oracle version adds 9 points (debate) and lifts GPT-3.5 GSM8K 75.9 to 84.3 versus 74.7 with no label [d02, d04]. With a real exact check this is the schema's S5 rule (G2: revise only from real output).

## 5. What holds up

**Replications and support for the core claim.**
- Lorenz 2011 has not been replicated directly in a larger or non-student sample. No failed replication was found either (gap 7 still open). Closest: Da and Huang 2020 on Estimize, a randomised field test pointing the same way (abstract only) [d20]. Treat the core claim as [C]: strong logic, one lab design, one field analogue.
- The mean-vs-median result is solid. Three independent sources agree: Lorenz [a03], Kao [c06], Chuang for LLMs [c21] (K03 [E]).
- The individual vs group level split (Farrell vs Rauhut) is an identity, not an empirical dispute (K02 [E]).
- Bazazi 2019: no replication found. The pay-scheme main effect is weak (diversity 76.25%, error 65.35%). The effect lives in the interaction. The reported numbers are posterior probabilities of direction, not effect sizes. Say "individual pay made copying likely," not "impairs" [critique].

**Failed or partial replications (the effect flips under other designs).**
- Jayles 2017/2021, Becker 2017/2019, and Barrera-Lemarchand's LLM Study 1 (d=0.24) all find some collective gain when influence is sequential, networked, or carries reliable information. The difference is design: simultaneous round-wise mean feedback on hard right-skewed questions (Lorenz) vs sequential or network designs. Almaatouq's account (shape of first estimates and centralisation) unifies them but is itself one reanalysis [b08].
- Becker 2017 replicates the drop in diversity (43%) but not the "no accuracy gain". It is a boundary study, not a replication.
- Jayles 2021 only partly tests Lorenz's contrast, and notes that individual accuracy can improve without collective accuracy if estimates converge with no median shift, as in Lorenz [a14].
- Mercier and Claidiere 2022: free discussion of reasons on checkable problems did not hurt (N=1,958) [d21]. Boundary, not a replication.
- Rosenberg et al. 2023: a structured chat linked by an LLM beat the survey crowd on a gumball estimate (error within 12% vs 25% survey crowd; 241 people). One task, vendor authors, no replication; probably works because small sub-groups deliberate [c26].

**Moderators that change the sign.**
1. Quality of the information in the stream: planted correct sources help; 0% experts gives no gain [a11].
2. Network structure: decentralised helps, centralised follows the hub [a15, c05].
3. Shape of first estimates: heavy-tailed helps, centred crowd hurts [b08].
4. Task difficulty: Lorenz needs moderate difficulty; Jayles used hard low-demonstrability questions [a05, b05].
5. Whether reasons are exchanged and a checkable answer exists [d21, d10].
6. Incentive: individual pay produces copying, collective pay does not [a09].
7. Direction of the bias: a modest push against the human underestimation bias helps [a12, a13]. This would not hold for an unbiased or overestimating crowd.
8. Group size: weight on social info rises with group size [c06, b07].
9. Person: confident people follow less and are more accurate [a11, b06]. Over-confident keepers lose value others hold.

**Interventions that worked.**
- Median or geometric mean instead of arithmetic mean on skewed data [a03].
- Pooling only people who resist influence (-17% vs -60% error) [b09]; post-hoc.
- Planting reliable sources [a11].
- Collective-outcome pay in humans [a09].
- Exchange of candidate answers only after independent first drafts (open LLMs, StrategyQA +7.4) [d10].
- Structured decomposition: groups that split an estimate into parts beat groups told to combine guesses (1,140 deliberations in 3 studies; Study 2 N=240) [b13].
- Gated acceptance via oracle or exact check [d02, d04].

**Interventions that did not work.**
- Persona prompts: 1.9 points over 45 configs and 3.1 over 81 configs [d11]; stubborn/agreeable system prompt: flip rate 0.55 same as baseline [c08].
- A prompt saying the model is paid for correctness: no drop in correct-to-incorrect flips [d08].
- Showing self-reported confidence: no effect on agreement (coefficient 0.025, SE 0.015) [d09]; confidence- or perplexity-based weighting may worsen blind conformity [a24].
- Simple prompt warnings against a persuasive adversary [b15].
- 13 interventions on semantic collapse (decoding, prompts, composition, steering, RL), except a custom RL [c14].
- Adding agents or rounds against an adversary [b15]; more discussion rounds before a vote hurt [d10].
- A judge cut disagreement collapse (81% to 35-41%) but judges copy debaters (r=0.639) [d11].

**Contradictions to keep in view.**
- Debate evidence is split by setting. Same-model debate is no better than independent ensembling [d01, d03, d05, d07, c09]. Mixed-model deliberation does better than copies [a21, a23]. But the best single model sampled many times beats the mix [d12, a21 d=0.88, d06]. Hegazy has no equal-token independent baseline [a23].
- The anti-conformity prompt (FREE-MAD) beat Society of Minds in one round (GSM-Level6 70.00 vs 52.50; AIME2024 53.33 vs 33.33) but was never compared with plain voting, and AIME has 30 items [d19].
- Tuned agreement level gave +15% (Multi-Persona) and +5% (SoM) but was tuned on the test subset, and the best level flips between tasks [d13].

## 6. Language models

**6.1 Do LLM agents conform?** Yes, and not weakly.
- Asch cloze test, six frontier models, temperature 1, 100 trials per cell: shift toward a plausible supplied word was 22 points at n=1 and 49 at n=10. Flat after about 5 (under 3 points from 5 to 10). A far-off word moved under 2 points. Per model at n=10: gemini-3.8-flash +73, gpt-6-sol +68, gemini-4-argon +42, claude-sonnet-5-5 +39, gpt-6-luna +36, claude-opus-5-5 +33. Filler words were chosen in only 583 of 197,976 trials. Caveat: fabricated consensus, one task type, approximate heat-map values [c11, c12].
- Herd Behavior (OpenAI models): average flip rate 0.48 in a two-agent test with a persuasive wrong peer; the flip is higher when the model's own confidence is low and the peer looks confident. Showing disagreeing peers first raised conformity. Five-agent strong-factors bundle flip rate 0.63 and 0.59, weak bundle 0.36 and 0.23. System prompts "be stubborn" or "be agreeable" did nothing on MMLU-Pro (0.55 each) [c07, c08].
- Adversarial persuasion: one confident adversary cut accuracy 10-40% and raised wrong agreement over 30% across GPT-4o, GPT-3.5, LLaMA, Mistral, Qwen, Yi. GPT-3.5 lost up to 30% [b15].
- In debate, Llama3.3-70B 2-agent systems collapsed into early agreement up to 86.36% with no gain. Dropping a correct answer is echoing: r=0.902 between sycophancy score and abandoning-correct rate [d11].

**6.2 Does conformity cost accuracy?**
- Wynn et al.: of agents that change answers, more go correct to incorrect than the reverse in all groups. P(correct to incorrect) is highest with 0 agreeing peers. Weak models: majority after debate is below majority of independent first answers (Llama MMLU 61.6 to 57.8, GSM8K 87.6 to 84.2; Mistral MMLU 33.6 to 24.4). GPT-4o-mini flat (CSQA 75.6 to 74.8; MMLU 81.4 to 82.2; GSM8K 94.0 to 94.4) [d07, d08]. Model-row mapping inferred from single-agent rows.
- Bertalanic: modal-answer adoption up to 85.5%; correct trajectories destroyed up to 70.0%; oracle gap up to 32.3 points. Consensus rate on Qwen GSM-Hard 83.5% in debate vs 73.0% in self-correction. Conformity is near ceiling at 2 peers (69.4% at 2 vs 73.4% at 9 on GSM-Hard). Llama-3.1-8B differences were not significant (p=0.155, 0.131) [c10, c09].
- Strong models in an incorrect majority corrected themselves only about a third of the time (gemini-2.5-flash 34.4%, gpt-5-mini 30.0%, flash-lite 3.6%). Correct majorities stay correct above 97% [d09]. Task is a logic puzzle with a unique answer.
- A collaboration tax: two LLMs with private views do worse together than one alone; the tax falls as capability rises. Cascade ends in accepting the partner's answer without re-deriving it [c25, abstract and first page].

**6.3 Debate vs independent samples at matched budget.** Four tests, all favour independent sampling plus a vote:
- GPT-3.5, GSM8K, 9 responses: vote 88.2, debate 83.0; debate round 2 adds nothing [d01].
- 5 agents, 7 tasks, T=1.0: Qwen2.5-7B vote 0.7691 vs 0.7377; Llama3.1-8B 0.7242 vs 0.6929 [d03]. Centralised debate was worst (Qwen 0.6551; Llama 0.6094).
- Four models, nine benchmarks, 6 calls: debate beat CoT in about 15% of 36 cells; SC won where applicable (MMLU SC 82.13 vs SoM 74.73) [d05].
- Majority after debate vs before [d07].
Costs: debate used 2.1-3.4x the tokens [c09]. Call count, not tokens, was matched in d01 and d05, so the true equal-token gap is probably larger.
No test used a current frontier or reasoning model on numeric estimation. This is the main open gap (U1).

**6.4 Own earlier attempts as peers (self-influence).**
- Off-the-shelf models lose accuracy when they re-read their own answer without outside facts. GPT-3.5 CommonSenseQA 75.8 to 38.1 (round 1), 41.8 (round 2). GPT-4 GSM8K 95.5 to 91.5 to 89.0. GPT-4 CSQA 82.0 to 79.5 to 80.0. GPT-3.5 keeps its first answer 74.7% of the time on GSM8K; changes go more often correct to incorrect [d02].
- A model trained to revise turns about 38% of correct answers wrong unless a verifier or vote picks the final answer. Sequential beat parallel narrowly at equal budget when a PRM or majority selected [d14].
- Six LLMs favour their own output when judging it. External feedback with accurate assessment reduces self-bias [d15, abstract and intro].
- Still open: peers that are verbatim copies of the same model's own earlier samples in a current frontier model (U2).

**6.5 Format and settings.**
- Candidates only, after independent drafts: StrategyQA 65.7 vs baseline 58.3. Exchange of reasoning 51.9. All-agents-drafting 62.8. Critical response generator 59.4. Answer similarity: reasoning 0.916, baseline 0.888, AAD 0.870, CI 0.845. Voting beat consensus by up to 13.2% on reasoning tasks, consensus beat voting by 2.8% on knowledge tasks [d10].
- Agreement instruction swings accuracy: +15% Multi-Persona and +5% SoM on a USMLE subset (376 questions), best level flips by task, tuned on test [d13, a22].
- Temperature: single-attempt accuracy is flat from T=0 to 1.0 (p=0.403); falls sharply above 1.0 and near zero at 1.6. Self-consistency holds across T=0.3-0.7 [d17, d18]. Nothing measured how temperature changes the benefit or harm of exposure.
- Persona prompts: 1.9 and 3.1 point swings only [d11].
- Narrow attention: Qwen2.5-7B, wide minus narrow +0.64 on HiddenBench, +0.61 on Werewolf. Narrow Werewolf 0.00 at n=6-16 vs wide 0.87 to 0.59. Llama-3.1-8B narrow 0.02. Weak or absent in debate (Du variant 0.30 to 0.37) and GovSim (survival 12 months in all conditions) [c15, c16].

**6.6 Collapse of diversity.**
- Closed-loop interaction among 3 LLM instances converges in meaning over 200-1,000 rounds while wording stays varied. Cosine distance last 500 vs first 10 rounds: 0.192 (SD 0.056). 13 interventions failed [c13, c14].
- Hidden anchors: at margin 0.10 Llama opinions leave the initial hull in 77% of runs; Qwen and gpt-oss about 25% or fewer [c17].
- Pairs given the same stance drift away when they talk, across GPT-3.5, GPT-4o, LLaMA-3.1-70B, Qwen2.5-72B and others [b16]. Opinion topics only.
- Consensus formation ignores starting opinions and centrality (DeGroot RMSE 0.32) [c18].

**6.7 Mixing models.**
- Barrera-Lemarchand: Claude Haiku 4.5, GPT-5-nano, Gemini 3.1 Flash Lite on jar photos (38-589 disks). Influence beat own first answer (d=0.24). Deliberation beat influence (d=3.25). Clones gain nothing. Mixed beat clones (d=0.48). Best single model alone with itself beat the mix (d=0.88) [a20, a21].
- Hegazy: Gemini-Pro + Mixtral + PaLM 2-M reached 91% on GSM-8K vs 82% for three Gemini-Pro. No equal-token independent baseline [a23].
- Self-MoA beat mixed MoA by 6.6 (AlpacaEval 2.0) and 3.8 points. Regression: diversity coefficient 2.558 (MMLU), 4.548 (CRUX), 4.719 (MATH); quality 1.841, 1.421, 2.839; R2 0.771, 0.685, 0.760. Mixing helps only in specific cases (+0.17, +0.35 points) [d12].
- Heter-MAD: +6.4% vs the SoM average, measured against the two-model average. My arithmetic on their Table 3: GPT-4o-mini CoT alone 77.0 vs SoM-Heter 76.7 [d06, our calculation, not the authors'].
- Learned aggregation of 15 LLMs beat every single model on 254 prediction-market questions. Weights followed error diversity (rho +0.482), not individual rank (rho -0.075). Two-model formula Brier 0.231 vs 0.265 for the 15-model mean. Contamination: gap fell from 35.8% to 8.9% on the 94-item clean subset [c22, c23, a25]. This is aggregation of independent outputs, which our schema allows (code selects, G5).

**6.8 Forecasting crowds.**
- 12 LLMs vs 925 humans: Brier 0.20 (SD 0.12) vs 0.19 (SD 0.19), p=0.850. Models show acquiescence (mean forecast above 50%) [c19].
- Showing the human median: GPT-4 0.17 to 0.14, Claude 2 0.22 to 0.15, interval width narrowed (GPT-4 17.75 to 14.22). A plain average of model and human was better still: Brier 0.13 and 0.14 [c20].

**6.9 Aggregation of independent samples.**
- Median of 30 sampled paths beat greedy, majority and mean on estimates. LLaMA-2-7B: median 1.25 vs majority 88.44 vs mean 3,704.85. GPT-4: median 1.00, majority 1.07, mean 1.29, greedy 1.04. Gain is small on the strongest model [c21].
- Conclusion for estimates: use the median of independent samples.

**6.10 Other mixed evidence.**
- Gated relay (WILC): each next model fixes the previous output's bottleneck and is accepted only if it improves the answer; abstract claims performance near GPT-5.2 at about 7x lower cost. Benchmark figures not extracted [c24].
- MAPoRL: small models do not improve over turns of discussion; with RL on a collective verifier reward, accuracy rises with turns. Rewarding useful influence even when wrong gave a 17.2% improvement in the influence measure; rewarding only correct influence gave -1.32% [d16]. It trains a policy, so it does not show that a frozen model changes behaviour when told it is scored on the group.

## 7. What our agent should take

Part codes: G = guardrail, S = state, O = operator, M = memory/aggregation.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| 1 | Keep attempts isolated in S3. No attempt sees another attempt's answer or reasoning before selection. Human case: spread shrinks with no gain at the group level. LLM case: peer exposure costs accuracy or adds nothing at matched cost. | G4, G9, S3 | [E] for the LLM debate side (four matched-budget tests); [C] for the human Lorenz claim itself | a01, a09, d01, d03, d05, d07, c09, K14 |
| 2 | Treat agreement as a hint, not proof. After exposure, agreement is inflated by copying. Agreement among isolated attempts is the only agreement worth logging. | G4 | [E] | c13, c15, c17, K16 |
| 3 | For numeric or skewed answers, aggregate in code with the median or geometric mean, never the arithmetic mean. | M (S7 select), G5 | [E] | a03, c06, c21, K03 |
| 4 | Report two numbers whenever exposure is tested: error of the pooled answer, and mean error of individual attempts. Credit only the first. | G4 (reporting), S9 | [E] | a04, a06, a07, b05, K02 |
| 5 | Do not let a model re-read its own answer and revise without an external check. Revision needs real failing output (already G2). Count correct-to-incorrect flips as a cost. | G2, S5 | [E] | d02, d14, d15, K25 |
| 6 | Do not add persona voters, stubborn/agreeable prompts, payment-for-correctness sentences, or confidence display as fixes for herding. They did nothing or little. | G4 (4b not to add) | [E] | c08, d08, d09, d11, K28 |
| 7 | Do not mix weaker models into the pool on the hope that diversity helps. The baseline is the strongest model sampled N times. | G9, G7 | [E] | d12, d06, a21, K29 |
| 8 | Reliable information is the only thing that makes shared answers help. If an attempt is shown anything, it should be the output of an exact check (run code, unit test, held-out example), not another attempt's opinion. This matches S5 (show the failing output). | S5, G2, G3 | [E] | a11, b05, d02, d04, K04 |
| 9 | Selection rule, not prompt, is the incentive. Code picks by group behaviour on fresh inputs (S7), so no attempt can gain by copying. | G5, S7 | [E] by design; the human basis for it is [S] | a09, d08, d16 |

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Same model, N independent attempts + median vs same N after one round of seeing each other's answers, equal tokens, on a current frontier model with numeric and reasoning items. | G4, G9, S3 | [C] (open-model evidence only) | d01, d03, d05, d07, K14 |
| T2 | Peer answers that are the model's own earlier attempts vs other-agent attempts: does flip rate differ? | G4, S5 | [C] | d02, d11, K25 |
| T3 | Format of exposure: verdict only, answer list, answers plus reasoning. | G4, S5 | [S] open models | d10, a14, K11, K26 |
| T4 | Exposure accepted only through an exact check (gated revision). | S5, G2 | [C] | d02, d04, c24, K20 |
| T5 | Heavy-tail gate: allow exposure only when first-round attempts are heavy-tailed. | S0 gate / S6 | [S] | b08, K06 |
| T6 | Pool only attempts that did not change after exposure (Madirolas). | M / S7 | [S] | b09, K10 |
| T7 | Confidence-weighted pooling against equal weights. | M | [E] for humans (confident follow less); [C] for LLM | a11, b06, d09, K09 |
| T8 | Collective-outcome scoring in a selection rule (score attempts by ensemble result). | G9, S7 | [S] | a09, b11, K07, K08 |
| T9 | Decomposition-based exchange: groups split the problem and combine sub-answers. | O3 | [S] | b13, K20 |
| T10 | Temperature (0.7 vs 1.0) x exposure. | G9 | [C] | d17, d18, K30 |
| T11 | Reference exposure: show a strong external reference to a revising attempt vs plain average with it. | M | [S] | c20, K18 |

Details of tests are in sections 8 and in UNKNOWNS.md.

## 8. Concrete tests on our bench

All arms get equal total tokens. Report accuracy, correct-to-incorrect flip rate, incorrect-to-correct flip rate, log-variance across attempts, and tokens used. Use only post-cutoff or private items to avoid contamination [K19].

| ID | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Numeric estimation (Fermi, jar counts, MARBLES-style) and short-answer reasoning (GSM-Hard style) | (a) N isolated attempts + median/vote; (b) same N after one round of seeing the other N-1 answers, then median/vote | Error of pooled answer in log space; accuracy; pooled-answer log-variance | (a) better or equal; (b) lower variance, no gain in pooled error. Expected gap of 0 to 5 points in favour of (a), widening with weak models |
| T2 | Items with a known answer where the model errs about 30-60% | (a) peers are own earlier samples verbatim; (b) peers are other-model samples; (c) no peers | Flip rate of correct to incorrect; flip rate of incorrect to correct | Flip rates close to equal in (a) and (b); (c) is baseline. Expect (a) is no safer than (b) |
| T3 | Same as T1 | Verdict only; answer list; answers + reasoning; each after isolated drafts | Final accuracy; answer similarity | Candidate list best; reasoning worst (d10 gave +7.4 vs -6.4 on open models) |
| T4 | Code tasks with unit tests; math with checkable answer | (a) N isolated + vote; (b) free revision after seeing own attempts; (c) revision accepted only if exact check passes | Accuracy; flip rate | (c) at least (a); (b) below (a). Check what share of gain is oracle-like |
| T5 | Numeric estimates split by kurtosis of first-round log answers | Exposure allowed vs blocked by tail class | Pooled error by class | Exposure helps only in heavy-tail class, hurts or null otherwise (human result from reanalysis) |
| T6 | Same as T1 | Pool all vs pool only unchanged attempts | Error of pooled answer | Unchanged-only better by a few points if humans transfer (-17% vs -60% in Lorenz data) |
| T7 | Same as T1 | Equal-weight median vs confidence-weighted median (self-rated, verbalised) | Pooled error | Small or none: stated confidence had no effect on agreement (d09) |
| T8 | Simulated multi-attempt ensemble with a public mean | Attempt score = own error vs ensemble error (in the selection rule, not the prompt) | Diversity (log variance), pooled error | Ensemble scoring keeps diversity; prompt wording alone does nothing (d08) |
| T9 | Multi-part estimation | Joint answer vs parts estimated separately then combined | Pooled error | Decomposition wins (b13) |
| T10 | Same as T1 | T=0.7 and T=1.0, with and without exposure | Log-variance; pooled error | Single-attempt accuracy flat; exposure effect may differ by temperature |
| T11 | Forecast-style items with a known strong reference | (a) attempts revise after seeing a strong reference; (b) plain average of attempt and reference | Brier / log error | (b) at least (a) (c20) |

Practical order of costs: T1, T4 and T3 reuse the same attempts and need only one extra round; T5 and T6 are analysis on logged data.

## 9. What does not transfer, and why

- **Payment incentives.** Bazazi paid people. A frozen LLM has no stake. A prompt line about payment did not reduce flips (d08). Only the selection rule acts, and the rule belongs in code (G5).
- **Social motives.** Humans copy partly for approval, reputation, fear of being odd. A sampled LLM answer has none of these. Its conformity looks more like completion pressure: the supplied answer sits in context and raises its probability. The Asch effect on LLMs appears even for fabricated consensus [c11].
- **Student lab samples and small groups.** 144 students, 141 people. LLM groups differ in size (we can run 10 or 100), in independence (same-model samples are already alike), and in noise.
- **Numeric estimation tasks.** Lorenz and Jayles use skewed estimates. Reasoning chains and code are not numbers; transfer to them is untested. Debate studies use math and multiple choice, not estimation.
- **Non-independence at baseline.** Same-model samples share biases (hidden anchors [c17], semantic collapse [c13]). The human starting point had far more independent errors. Mixed-model pools do not fix this since the best model alone beats the mix [d12, a21].
- **Forced social exposure.** Our scaffold decides whether to expose. Humans cannot be forced to be isolated in many real settings.
- **Free human discussion.** Mercier and Claidiere showed discussion of reasons helps on checkable problems with large human groups; LLMs show sycophancy and echoing instead [d11]. Both claims can be true.
- **Quantity of rounds.** Humans: 3-5 rounds. LLMs: 200-1,000 rounds of closed-loop collapse [c13]. We use at most 1-2 revision rounds (S5), so the long-run collapse is not directly relevant.
- **Rajasekaran and Pokharel** measure shifts toward supplied words or opinions, not accuracy loss with ground truth [critique]. Do not cite as proof of lower accuracy.
- **Network structure.** Becker's hub effect depends on a network. Our scaffold has no network unless we build one. The warning remains: a single "leader" attempt shown to all is a star network.

## 10. Open questions

1. At equal tokens, does a single frontier model's N independent samples pooled by median beat the same N after one round of exposure, on numeric and reasoning tasks? No study does this for frontier models.
2. Does conformity (Asch, herding) turn into accuracy loss when the peers are the model's own earlier attempts?
3. Does scoring each attempt on the collective outcome reduce copying in a frozen LLM, through a selection rule instead of a prompt?
4. Can heavy-tailedness of first-round attempts gate exposure? Is the tail shape of LLM sampled numeric answers even like human guesses?
5. Which format (mean, list, verdict, reasoning) minimises herding in current frontier models? Only human data (Jayles 2021) and open-model data (Kaesberg) exist.
6. Does a verifier-gated acceptance rule restore the gain seen with planted correct sources?
7. Is there a failed or null replication of Lorenz 2011 in a larger or non-student sample? None found; full text of Da and Huang 2020 still to read.
8. Does mixing model families help once the best-model baseline and equal tokens are controlled? Closed for aggregation, open for debate with frontier models.
9. How do temperature and prompt diversity change the benefit or harm of exposure?
10. Does the effect size depend on item difficulty the way Lorenz says (moderate difficulty only)?
11. Do reasoning models (thinking-on) behave differently from non-reasoning models under peer exposure? Almost all evidence is on instruction models.
12. Do the hidden-anchor findings (Llama strongly anchored; Qwen and gpt-oss less) mean that exposure risk is model-specific? If so, a per-model gate is needed.

## 11. Sources

[V] = opened and read (full text or substantial HTML/PDF text). [M] = abstract, snippet or memory only.

**Founding and human studies**
- [V] Lorenz, Rauhut, Schweitzer, Helbing (2011), PNAS. https://pmc.ncbi.nlm.nih.gov/articles/PMC3107299/ (DOI 10.1073/pnas.1008636108)
- [V] Farrell (2011), Social influence benefits the wisdom of individuals in the crowd. https://pmc.ncbi.nlm.nih.gov/articles/PMC3169111/
- [V] Rauhut, Lorenz, Schweitzer, Helbing (2011), Reply to Farrell. https://pmc.ncbi.nlm.nih.gov/articles/PMC3169123/
- [V] Mavrodiev, Tessone, Schweitzer (2013), Quantifying the effects of social influence. https://pmc.ncbi.nlm.nih.gov/articles/PMC3584930/
- [V] Madirolas and de Polavieja (2015), Improving collective estimations using resistance to social influence. https://pmc.ncbi.nlm.nih.gov/articles/PMC4643903/
- [V] Bazazi, von Zimmermann, Bahrami, Richardson (2019), Self-serving incentives impair collective decisions by increasing conformity, PLoS ONE 14(11):e0224725. https://pmc.ncbi.nlm.nih.gov/articles/PMC6855459/ (also https://europepmc.org/article/PMC/PMC6855459)
- [V] Jayles et al. (2017), How social information can improve estimation accuracy in human groups. https://pmc.ncbi.nlm.nih.gov/articles/PMC5703270/
- [V] Jayles et al. (2020), The impact of incorrect social information on collective wisdom in human groups. https://pmc.ncbi.nlm.nih.gov/articles/PMC7536058/
- [V] Jayles, Sire, Kurvers (2021), Impact of sharing full versus averaged social information. https://pmc.ncbi.nlm.nih.gov/articles/PMC8315836/
- [V] Becker, Brackbill, Centola (2017), Network dynamics of social influence in the wisdom of crowds, PNAS. https://pmc.ncbi.nlm.nih.gov/articles/PMC5495222/
- [V] Becker, Porter, Centola (2019), The wisdom of partisan crowds. https://pmc.ncbi.nlm.nih.gov/articles/PMC6561169/
- [V] Kao et al. (2018), Counteracting estimation bias and social influence, J R Soc Interface. https://pmc.ncbi.nlm.nih.gov/articles/PMC5938592/ (page summary read, not full PDF)
- [V] Kao et al. (2019), Modular structure within groups. https://pmc.ncbi.nlm.nih.gov/articles/PMC6553586/
- [M] Strategies for integrating disparate social information (Proc R Soc B, 2020). https://pmc.ncbi.nlm.nih.gov/articles/PMC7739494/ (abstract only)
- [V] Almaatouq, Rahimian, Burton, Alhajri (2022), The distribution of initial estimates moderates the effect of social influence. https://pmc.ncbi.nlm.nih.gov/articles/PMC9530231/
- [V] Barrera-Lemarchand et al. (2026), Collective problem decomposition. https://pmc.ncbi.nlm.nih.gov/articles/PMC13538491/
- [V] Wang, Su, Wang, Plotkin (2025), Individual incentives that promote collective intelligence. https://pmc.ncbi.nlm.nih.gov/articles/PMC12745784/
- [V] Stein, Cruz, Grossi, Testori (2026), Free information disrupts even Bayesian crowds. https://pmc.ncbi.nlm.nih.gov/articles/PMC13056096/
- [V] Denton, Feldman, Johannemann (2026), Conformity to popular, not average, opinions. https://pmc.ncbi.nlm.nih.gov/articles/PMC13291653/
- [V] Ueshima, Jones, Christakis (2024), Simple autonomous agents can enhance creative semantic discovery. https://pmc.ncbi.nlm.nih.gov/articles/PMC11189566/
- [V] Rosenberg, Willcox, Schumann (2023), Towards Collective Superintelligence. https://arxiv.org/abs/2311.00728
- [M] Da and Huang (2020), Harnessing the Wisdom of Crowds, Management Science. https://doi.org/10.1287/mnsc.2019.3294 (Crossref abstract)
- [M] Mercier and Claidiere (2022), Does discussion make crowds any wiser? Cognition 222:104912. https://doi.org/10.1016/j.cognition.2021.104912 (abstract)

**Cited from memory or secondary mention only [M]**
- [M] Galton (1907); Page (2007) The Difference; Salganik, Dodds, Watts (2006); Latane social impact theory; French (1956) / DeGroot. https://doi.org/10.1073/pnas.1008636108 (via Lorenz references)
- [M] Mann and Helbing (2017), Optimal incentives for collective intelligence. https://doi.org/10.1073/pnas.1618722114
- [M] Frey and van de Rijt (2021), Social influence undermines the wisdom of the crowd in sequential decision making. https://doi.org/10.1287/mnsc.2020.3713
- [M] Gurcay, Mellers, Baron (2015), The power of social influence on estimation accuracy. https://doi.org/10.1002/bdm.1843
- [M] Navajas et al. (2018), Aggregated knowledge from a small number of debates. https://doi.org/10.1038/s41562-017-0273-4
- [M] Du et al. (2023), Improving factuality and reasoning through multiagent debate. https://arxiv.org/abs/2305.14325
- [M] Page (2007). https://press.princeton.edu/books/paperback/9780691138541/the-difference

**LLM and AI studies**
- [V] Schoenegger, Tuminauskaite, Park, Bastos, Tetlock (2024), Wisdom of the Silicon Crowd. https://arxiv.org/abs/2402.19379 (also https://pmc.ncbi.nlm.nih.gov/articles/PMC11800985/)
- [V] Barrera-Lemarchand, Sigman, Navajas (2026), The Wisdom of Artificial Deliberative Crowds. https://arxiv.org/abs/2609.22497
- [V] Smit et al. (2024), Should we be going MAD? https://arxiv.org/abs/2311.17371
- [V] Hegazy (2024), Diversity of Thought in multi-agent debate. https://arxiv.org/abs/2410.12853
- [V] Wu, Song, Yao, Wan, Lin, Lv (2026), DEAR. https://arxiv.org/abs/2608.03648 (abstract and intro)
- [V] Douven (2026), Wisdom of LLM Crowds. https://arxiv.org/abs/2607.18269
- [V] Kraidia et al. (2026), When collaboration fails. https://pmc.ncbi.nlm.nih.gov/articles/PMC13061921/
- [V] Coppolillo, Manco, Aiello (2026), Unmasking conversational bias. https://pmc.ncbi.nlm.nih.gov/articles/PMC13484959/
- [V] Herd Behavior in LLM-based multi-agent systems (2025). https://arxiv.org/abs/2505.21588
- [V] Bertalanic and Fortuna (2026), The Cost of Consensus. https://arxiv.org/abs/2605.00914
- [V] Rajasekaran and Vasileiou (2026), Asch conformity in frontier LLMs. https://arxiv.org/abs/2610.36668
- [V] Kong, Lai, Piao, Evans (2026), Semantic collapse. https://arxiv.org/abs/2605.17193
- [V] Liu, Xiong, Zhang, Tang (2026), Social Networks of LLM Agents. https://arxiv.org/abs/2607.03695
- [V] Pokharel and Dantu (2026), Hidden anchors. https://arxiv.org/abs/2606.19494
- [V] Yazici et al. (2026), Opinion consensus among networked LLMs. https://arxiv.org/abs/2601.21540
- [V] Chuang et al. (2025), Probing LLM world models: wisdom of crowds decoding. https://arxiv.org/abs/2501.17310
- [V] Fang, Wei, Chen (2026), WILC. https://arxiv.org/abs/2607.29087 (abstract and framing)
- [V] Sun et al. (2026), The Collaboration Tax. https://arxiv.org/abs/2608.22152 (abstract and first page)
- [V] Huang et al. (2024), LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798
- [V] Choi, Zhu, Li (2025), Debate or Vote. https://arxiv.org/abs/2508.17536
- [V] Zhang et al. (2025), Stop overvaluing multi-agent debate. https://arxiv.org/abs/2502.08788
- [V] Wynn, Satija, Hadfield (2025), Talk isn't always cheap. https://arxiv.org/abs/2509.05396
- [V] Wu, Li, Li (2025), Can LLM agents really debate? https://arxiv.org/abs/2511.07784
- [V] Kaesberg et al. (2025), Voting or consensus? https://arxiv.org/abs/2502.19130
- [V] Yao et al. (2025), Peacemaker or troublemaker. https://arxiv.org/abs/2509.23055
- [V] Li, Lin, Xia, Jin (2025), Rethinking Mixture-of-Agents. https://arxiv.org/abs/2502.00674
- [V] Snell, Lee, Xu, Kumar (2024), Scaling test-time compute. https://arxiv.org/abs/2408.03314
- [V] Xu et al. (2024), Pride and Prejudice. https://arxiv.org/abs/2402.11436 (abstract and intro)
- [V] Park et al. (2025), MAPoRL. https://arxiv.org/abs/2502.18439
- [V] Renze and Guven (2024), Effect of sampling temperature. https://arxiv.org/abs/2402.05201
- [V] Wang et al. (2023), Self-consistency. https://arxiv.org/abs/2203.11171
- [V] Cui et al. (2025), FREE-MAD. https://arxiv.org/abs/2509.11035

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 11 established claims: 5 confirmed as written, 6 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A17.04-K02** (reworded: the sources support less). Lorenz et al. state the identity (collective error + diversity = average individual error) and Farrell argues shrinkage helps individuals, but Farrell also disputes the bracketing measure and asks whether estimates shrank too much, so the two sides do not differ 'only' in level judged; the Rauhut reply could not be opened (captcha). Corrected claim: The diversity prediction identity (collective error + group diversity = average individual error) means that shrinking spread lowers average individual error even when the crowd mean does not move; this reconciles much of Farrell's 'individuals benefit' (rewards rise) with Lorenz's 'crowd does not improve', though Farrell also disputes the bracketing metric and raises over-shrinkage as an open question.
- **A17.04-K03** (reworded: the sources support less). Lorenz et al. verified (arithmetic mean closer than individuals in 21.3% of cases, 77.1% in log space; geometric mean and median recommended for their data), but Kao et al. 2018 find the median tends to underestimate and the geometric mean can be the worst choice for small samples at large numerosities, so 'use median or geometric mean' is not a general rule. Corrected claim: For right-skewed (lognormal-like) estimates the arithmetic mean is a poor aggregate (closer to the truth than individuals in only 21.3% of cases in Lorenz et al., 77.1% in log space); Lorenz et al. found the geometric mean and median work well for their data, but Kao et al. (2018) show the median underestimates and the geometric mean is not uniformly best, motivating bias-corrected aggregators.
- **A17.04-K09** (now single-source: the sources are not independent). All three claim parts (median S=0.34, linear rise with distance up to ~2.5 orders, confident people follow less and are more accurate) are verified in Jayles et al. 2017, but a11 and b06 are the same paper; Mavrodiev et al. 2013 only corroborates the linear distance dependence (slopes 0.27-0.97) and does not test own-vs-group weighting.
- **A17.04-K16** (reworded: the sources support less). Kong et al. (semantic collapse over 200-1000 rounds, thirteen interventions 'did not reliably restore' diversity; a custom diversity-targeted RL gave some positive effect) and Pokharel and Dantu (hidden anchors, 3 open models, 90 runs) verified; but Yazici et al. show consensus departs from the DeGroot centrality-weighted forecast (binary accuracy 60% vs 50% chance, 3-class 32%), which is weaker than 'ignores starting opinions'. Corrected claim: Interaction among LLM agents drives semantic collapse (Kong et al.); thirteen interventions did not reliably restore semantic diversity (only a custom diversity-targeted RL gave a partial positive effect); in three open models each carries a hidden anchor belief that pulls opinions (Pokharel and Dantu), and networked-LLM consensus departs from the DeGroot prediction from initial opinions and network centrality (Yazici et al.), though initial opinions retain weak predictive value (binary 60% vs 50% chance).
- **A17.04-K29** (reworded: the sources support less). Numbers verified (Li: Self-MoA +6.6 AlpacaEval 2.0 and +3.8 average, reported as % improvements; Zhang Table 3/4: GPT-4o-mini CoT mean of 9 datasets = 77.01 vs Heter-SoM 76.7; Barrera-Lemarchand: best single model deliberating with its own copies beat the heterogeneous consensus, d=0.88). But the headline 'does not beat' is wider than the sources: Li say Self-MoA wins in 'a large number of scenarios', and Barrera-Lemarchand also find mixed groups beat size-matched clone groups (d=0.48). Corrected claim: Mixing model families usually does not beat sampling the best single model many times once the best model is the baseline: Self-MoA beat mixed MoA by 6.6% on AlpacaEval 2.0 and 3.8% on average over MMLU, CRUX and MATH (Li et al.), in a large number of but not all scenarios; Heter-MAD's gain is measured against the two-model average, and from Zhang et al.'s tables GPT-4o-mini CoT alone averages 77.0 vs Heter-SoM 76.7; Barrera-Lemarchand found the best single model deliberating with copies of itself beat the heterogeneous consensus (d=0.88), although mixed groups beat size-matched clone groups of weaker models (d=0.48).
- **A17.04-K30** (reworded: the sources support less). Renze and Guven (GPT-3.5 CoT 1,000 questions H(10)=10.439 p=0.403; nine models, 100-question exam; collapse above 1.0), Wang et al. (robust across T=0.3-0.7 and top-k) and Li et al. (temperatures 0.5-1.2 varied jointly with mixtures) verified; but 'no study measured' temperature effects on peer exposure is an absence claim the sources cannot show, and the confound statement is the researcher's inference. Corrected claim: Single-attempt accuracy is flat in sampling temperature from 0.0 to 1.0 (GPT-3.5 CoT, 1,000 questions, Kruskal-Wallis p=0.403; nine models on a 100-question exam) and drops quickly above 1.0; self-consistency gains hold across T=0.3-0.7 and top-k settings (LaMDA-137B, GSM8K); this search found no study measuring how temperature changes the benefit or harm of peer exposure, and the Self-MoA regression over temperatures 0.5-1.2 varies temperature together with the model mix.
- **A17.04-K04** (now single-source: only one opened source, code check).
