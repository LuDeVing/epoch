# Social epistemology of discovery: deep document

*Subfield D01.09. Key works: Longino; Weisberg and Muldoon; Hong and Page; Zollman. Relevance to our single agent: background, with a few usable parts (keep alternatives, parallel branches, mixing different methods). Evidence ids (a01 to d16) and claim ids (D01.09-K01 to K32) refer to the files in this folder. The cross-check of 2026-11-19 is in critique.md; where it corrected a number, the corrected number is used here.*

## 1. What it is

Social epistemology of discovery asks how a group of inquirers finds out more than one inquirer would. The group may be scientists, a jury, a team or, now, a set of language-model agents.

Four questions run through the field.
1. Does a group of different thinkers solve problems better than a group of the best thinkers (diversity versus ability)?
2. How should a community split its effort between rival research programmes (division of cognitive labour)?
3. How should information flow between inquirers so that good ideas win but bad ideas are not locked in too early (network structure, transient diversity)?
4. What social rules make a community's criticism work (Longino's norms, standpoint theory)?

The work is mostly philosophy and agent-based simulation. There is little direct experiment. The human data that exist are observational (who publishes what, who gets cited). The AI work since 2023 is the first set of real experiments that test the same ideas on artificial inquirers: mixtures of models, debate, persona prompts, ideation groups.

Why it matters for our agent. Our agent is ONE model run through a scaffold. It has no peers. So the direct social claims (standpoint, mavericks, networks) do not apply. What can transfer is the structural idea: keep several distinct lines of attack alive, delay merging them, and do not let one early answer capture everything. The AI studies also tell us how much real diversity a language model can supply (little) and when mixing in more voices helps (rarely at equal compute).

## 2. History and theories in depth

### 2.1 Longino: objectivity as a social property (1990, 2002)
Helen Longino (Science as Social Knowledge, 1990; The Fate of Knowledge, 2002) argues that objectivity is not a property of one scientist's method. It is a property of a community that subjects claims to transformative criticism. Background assumptions (what counts as evidence, what is taken for granted) are invisible to those who hold them. They become visible only when people with different assumptions challenge them.

Four norms make a community's criticism effective:
- public venues for criticism;
- uptake of criticism (the community must respond and change, not just tolerate);
- shared public standards that criticism appeals to;
- tempered equality of intellectual authority (all relevant perspectives get a hearing, regardless of status).

Status in our evidence: a17, b21, c27. None was opened; summarised from background knowledge. There is no quantitative data. Critics say it is vague about how much diversity is enough. No empirical test of the four norms was found (K25).

### 2.2 Standpoint theory
The standpoint idea (Harding, Wylie and others) is that people in marginalised positions can see features of the social world that dominant groups miss, and that this is an epistemic resource. Longino's version is community-level. The only direct empirical test found, with LLMs, is Wang, Morgenstern and Dickerson (c15, c16): identity-prompted models do not reproduce the views of the real in-group, and they flatten group variation (section 6). No human experiment of the strong claim was found in this run.

### 2.3 Kitcher: division of cognitive labour (1990)
Philip Kitcher (Journal of Philosophy, 1990) modelled a community as a decision problem. A community does best if scientists are spread across rival research programmes, even when some of them pick a programme that looks worse to them. Individual and community optima differ. Strevens (1993, 2003) built a related model on credit for priority. Zollman notes that the Kitcher and Strevens models assume success or failure is known to all (a18; not opened). Kummerfeld and Zollman (2016) add that exploration beyond one's own best guess is a public good that is under-supplied, a free-rider problem (a26, via the Wu and O'Connor review a12).

### 2.4 Weisberg and Muldoon: epistemic landscapes (2009)
Weisberg and Muldoon (Philosophy of Science 76(2)) put agents on a 2-D landscape where height is epistemic significance. Agents follow rules: controls, followers (move toward evidence from others) and mavericks (avoid visited sites). The reported result is that populations with mavericks reach high ground faster and more fully, and mavericks stimulate followers (a19, b15, c25; not opened, abstract level only).

Challenge: Alexander, Himmelreich and Thompson (2015, Philosophy of Science 82) argue that the maverick advantage depends on the follower rule. With a better search rule the benefit of division of labour weakens or disappears (a20, b16; recalled, not opened). A replication in another language (OpenAlex abstract, "Epistemic Landscapes Reloaded") reproduces the original code results, but small rule changes change the results (critique.md, point 9). Poyhonen (2017) finds that cognitive diversity and social learning help only when problems are hard enough (c26; snippet).

### 2.5 Hong and Page: diversity trumps ability (2004)
Hong and Page (PNAS 2004; opened at PMC528939) model each agent with a perspective (how it encodes solutions) and a heuristic (how it searches). A team can only stall at a point that is a local optimum for every member. They prove, and show by simulation, that a team of randomly chosen agents can beat a team of the individually best agents.

The theorem needs four assumptions: agents are intelligent (find a weakly better point), the problem is hard (no agent always finds the optimum), the agents are diverse (for every non-optimal point some agent can improve), and the best agent is unique. The random group must be large. In the finite version the best group is made of identical agents, which the authors call an artefact. The authors' own design hint: mix similar perspectives (cheap to communicate) with diverse heuristics (a05). The model has no communication or learning.

Critiques:
- Thompson (2014, Notices of the AMS): the theorem is trivial or conditional; the simulation parameters do not carry the real-world claim (a21, b13; not opened).
- Grim, Singer, Bramson, McGeehan and Berger (2019): the diversity advantage is sensitive to landscape randomness and to how ability and expertise are defined (abstract confirmed in the cross-check; a23, b14).
- Singer (2019): diversity, not randomness, is the active ingredient (a22; recalled).
- A 2023 extension (a15, a16; authors not recorded) adds a noisy communication channel. Diverse teams still tend to beat more expert but homogeneous teams. The gain depends on four interacting factors: problem complexity, number of approaches, encoding of the problem, and institutional search method. Relationships are non-linear and sometimes non-monotonic. A routine that cuts miscommunication in one setting can amplify it in another.
- Karge (2025, Episteme) derives exact conditions in a Condorcet jury model: diversity (modelled as the influence of an opinion leader) beats ability only above a threshold (a14).

Page (2007, The Difference) adds the diversity prediction theorem (b25): collective squared error equals mean individual squared error minus the diversity of predictions. It is an identity for squared-error averaging. It does not say how to get diversity without lowering individual accuracy.

### 2.6 Zollman: network structure and transient diversity (2007, 2010)
Zollman (2007, 2010) used bandit-network models. Agents try one of two options with slightly different success rates, update by Bayes, and share results with neighbours. In a densely connected network one early misleading result can sway everyone, and the community settles on the wrong option. Less connected networks keep disagreement alive longer and reach the correct consensus more often. The price is speed. Zollman calls the goal transient diversity: diversity that lasts long enough to test alternatives and then ends. A division of labour survives if information is limited or agents hold extreme beliefs; if both hold, diversity never ends and the group fails to converge (a09). Historical illustration: the bacterial theory of ulcers was dismissed from 1954 to the 1980s after one flawed study (a10).

Related NK-landscape work: March (1991) and Lazer and Friedman (2007) find that less connected groups find better solutions in the long run while fully connected groups are faster early (a11, a25; second-hand).

Boundary condition: Rosenstock, Bruner and O'Connor (2017) show the Zollman effect depends on parameters. It appears mainly on hard problems; on easy problems almost every community succeeds, and cutting communication is highly inefficient (a13, a24; second-hand via the review). Status: contested (K04).

### 2.7 Later models (2018 to 2026)
- Wu and O'Connor (2023) review seven mechanisms that keep diversity of practice alive: low connectivity, stubbornness, confirmation bias, funders favouring risky science, inter-group distrust, proprietary industry research, testimonial injustice (a12). Each also raises polarisation risk. Mild confirmation bias helps; higher levels polarise (Gabriel and O'Connor 2021). They cite decision-theory exploration rules (Gittins index, epsilon-greedy) as better than blunt diversity (a13).
- Fazelpour and Steel (2022) extend the bandit-network model with two social groups (a06 to a08). See section 4.3.
- Fazelpour, O'Brien and Rubin (2026) model scientists with AI advisors on NK landscapes. See section 6.
- Peterson (2025) models knowledge collapse. See section 6.

### 2.8 Empirical human studies
- Hofstra et al. (2020): underrepresented groups introduce more novel concept links but their novelty is taken up less and pays off less (b03).
- Yang et al. (2022): mixed-gender teams produce more novel and more highly cited medical papers (b04).
- AlShebli et al. (2018): ethnically diverse author sets get more citations (b24; recalled).
- Horwitz and Horwitz (2007) meta-analysis: task-related diversity helps team performance, bio-demographic diversity does not (b19; recalled).
- Stasser and Titus (1985): groups discuss shared information more than unique information (hidden profile) (b20; recalled).
- Woolley et al. (2010): a collective intelligence factor tied to social sensitivity, equal turn-taking and proportion of women (b18; recalled). Linked to cognitive diversity only indirectly. See the parallel subfield "Collective intelligence factor c".
- Levine et al. (2014): ethnically diverse experimental markets priced more accurately (b23; recalled).

All are observational or lab studies with human teams. None is randomised for the diversity variable in a discovery task.

## 3. Core findings with exact numbers

Status key: established = replicated or supported by 3 or more sources; single-source; contested = sources disagree. Rows built on recalled sources are marked in the text above.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Random teams beat best-ability teams on a ring landscape | 50 trials. 10 agents, l=12: best 92.56 (sd .020, diversity 70.98%) vs random 94.53 (sd .007, 90.99%). 20 agents, l=12: 93.78 (74.95%) vs 94.72 (91.46%). 10 agents, l=20: 93.52 (73.69%) vs 96.08 (94.31%). Gaps 1 to 2.5 points on a 0-100 scale. Single run: best agent 87.3, 10-best group 93.2, 10-random group 94.7 | Hong and Page 2004 (a02, a03, b01) | Single-source (simulation); gap shrinks with team size |
| The Hong-Page result is conditional | Needs hard problem, locally optimal agents, large diverse pool, unique best agent; sensitive to landscape randomness and definition of ability | Hong and Page theorem (a04, b02); Grim et al. 2019 (a23, b14); Thompson 2014 (a21) | Contested |
| Miscommunication dents but does not erase the diversity gain | Qualitative; non-monotonic; four interacting factors | 2023 extension (a15, a16) | Single-source |
| Diversity beats ability in Condorcet voting only above thresholds | Formulas not read | Karge 2025 (a14) | Single-source |
| Less connected networks reach correct consensus more often, but slower | Bandit arms 0.5 vs 0.499; 1,000 pulls per trial; priors on [0,4] | Zollman 2010 (a09); review a11 | Contested (Rosenstock 2017: parameter-dependent, costly on hard problems) |
| Exploration is under-supplied (free rider) | Model result, no numbers | Kummerfeld and Zollman 2016 via a12 | Single-source |
| Demographic diversity helps only at moderate out-group trust and low conformity | Bandit arms 0.5 vs 0.501; 10,000 runs of 3,000 experiments; w=0.005 worst, w=1 second worst, moderate best; kappa 0 to 0.1, order flips to homogeneous-better at higher kappa | Fazelpour and Steel 2022 (a06 to a08) | Single-source |
| Maverick populations explore better | No numbers read | Weisberg and Muldoon 2009 (a19, b15, c25) | Contested (a20, c26) |
| Underrepresented scholars: more novelty, less uptake | 1.2M US PhDs 1977-2015. Underrepresented genders: about 5% lower odds of a faculty job, 6% lower odds of a sustained career. Races: 25% and 10% lower. At +2 SD novelty the faculty gap grows from about 3.5% to 9.5% (4.3% to 15% for impactful novelty) | Hofstra et al. 2020 (b03) | Single-source, observational, no replication found |
| Mixed-gender teams more novel and cited | 6.6M medical papers. Large teams: 48% vs 44% novel (9.1% more likely); 10.2% vs 8.9% top-5% cited (14.6% more likely) | Yang et al. 2022 (b04) | Single-source, observational |
| Different-model proposers beat copies of one model (MoA ablation) | AlpacaEval 2.0 LC, aggregator Qwen1.5-110B: n=6 61.3 vs 56.7; n=3 58.0 vs 56.1; n=2 58.8 vs 54.5; n=1 47.8 both. Llama-3-70B: 45.0 as aggregator, 60.6 as proposer | Wang et al. 2024 (b07) | Single-source; judge is a model |
| MoA headline | LC win rate 65.1 vs GPT-4o 57.5 (+7.6); MoA-Lite 59.3; three repeats. Use 65.1 (the intro text says 65.8 once) | Wang et al. 2024 (a27, b06) | Single-source |
| Self-MoA beats a mixed MoA under Li et al.'s setup | 65.7 vs 59.1 (+6.6) on AlpacaEval 2.0 LC; average +3.8% over MMLU, CRUX, MATH. Caution: 59.1 is Li et al.'s own 2-layer mix; the original 3-layer MoA gets 65.1, so Self-MoA is only 0.6 above it | Li et al. 2025 (a28, c10, d15) | Contested |
| Quality-diversity trade-off | Regression on quality and Vendi diversity: both p<0.001; R2 about 0.7 on each of MMLU, CRUX, MATH; about 70 points per dataset | Li et al. 2025 (c11) | Single-source |
| Debate among different model families beats copies | GSM8K solo Gemini-Pro 78, PaLM 2-M 64, Mixtral 70; diverse debate after 4 rounds 91; 3 Gemini copies 82 (80 without CoT); ASDiv solo 89/86/81, debate 94; small models +17 vs +10 | Hegazy 2024 (a29, c01, c02) | Single-source (one author) |
| Heterogeneous debate helps | Heter-SoM +6.4% over SoM-average; Heter-EoT +8.2% over EoT-average; up to +5.8% over CoT-average (a maximum; some columns show -1.4% and -2.0%). Two models, p=0.5 per agent | Zhang et al. 2025 (c09) | Single-source; "consistently" is too strong |
| Debate does not reliably beat CoT or self-consistency | 5 MAD methods, 9 benchmarks, 4 models. Multi-Persona won 0% vs CoT; ChatEval and AgentVerse about 15%; one case +0.85% (Claude-3.5-haiku, MMLU) | Zhang et al. 2025 (c08); Smit et al. 2024 (b09, c07, d07); Choi et al. 2025 (d05) | Established |
| Original debate result | Arithmetic: single 67.0, reflection 72.1, majority 69.0, debate 81.8. GSM8K 77.0, 75.0, 81.0, 85.0. Chess pawn score 91.4, 102.1, 102.2, 122.9. 3 agents, 2 rounds, copies of one model | Du et al. 2023 (c03) | Contested (gain shrinks against strong baselines) |
| Persona prompts in debate | MMLU 71.1 to 74.2 | Du et al. 2023 (c04) | Contested |
| Personas in system prompts do not help on factual questions | 162 roles, 2,410 questions, 9 open models; in-domain coefficient 0.004 (p<0.01); role selection no better than random | Zheng et al. 2024 (d14) | Single-source (large) |
| Debate in mixed groups can lower accuracy | More answers flip correct to incorrect than the reverse; flips rise with the number of disagreeing peers; payoff prompt did not help | Wynn et al. 2025 (d06) | Single-source |
| Majority vote explains most of debate's gain | Martingale argument; mean accuracy across rounds flat; 7 benchmarks, 5 agents | Choi et al. 2025 (d05) | Single-source (theory plus data) |
| Single agent matches or beats multi-agent at equal thinking tokens above about 500 | Average accuracy at 2000 tokens: single 0.421, debate 0.403, ensemble 0.372. At 100: single 0.290, debate 0.370, sequential 0.364, ensemble 0.280. At 500: 0.390, 0.380, ensemble 0.310. At 1000: 0.418, 0.388, 0.333. At 5000: 0.427, 0.420, 0.411. 3 model families, 8 cells, multi-hop QA | Tran and Kiela 2026 (d01) | Single-source; all copies of one model |
| Context damage: multi-agent catches up only at heavy damage | Differences 1 to 3 points, overlapping intervals (deletion 0.3: 0.245 vs 0.221; substitution 0.7: 0.200 vs 0.225) | Tran and Kiela 2026 (d02) | Single-source |
| Answer-level diversity drives debate gain, not temperature | Pass@5 round 0, random vs diversity-selected: Qwen-7B 0.7921 vs 0.9097; Llama-8B 0.7423 vs 0.9026. Unique answers@5: 1.45 vs 1.61; 1.92 vs 2.32. 62 datasets | Zhu et al. 2026 (d03) | Single-source; selection costs extra samples |
| Debate as martingale | Homogeneous agents and uniform updates keep expected correctness; confidence correlated with correctness makes it a submartingale | Zhu et al. 2026 (d04); Choi et al. 2025 (d05) | Single-source theory |
| Plain sampling and voting scale | GSM8K 12% to 24%, MATH 6% to 10%, HumanEval 4% to 9%; Llama2-13B at 15 samples matches Llama2-70B; up to 40 samples | Li et al. 2024 (b11) | Single-source |
| Approach-diverse prompting beats CoT and SC | GPT-4: graph colouring CoT 15.0, SC 23.0, IDIV-SE 74.0, DIV-SE 97.0; Blocksworld 3: 70, 73, 82, 94; Blocksworld 4/5: 40, 41.2, 57, 69.6; AQuA GPT-3.5: 59.0, 63.37, 62.6, 72.83. No gain on GPT-3.5 planning. About 4x cheaper than SC-10 few-shot. No variance reported | Naik et al. 2024 (b05, d13) | Single-source; no replication |
| Self-reflection degenerates; debate with a judge helps | Disagreement falls toward 0 under reflection; tables not extracted | Liang et al. 2023 (b10, c06) | Single-source |
| Agents drift to consensus | Qualitative consensus plots; stubborn prompts lengthen debate and help; 20-problem GSM8K study | Du et al. 2023 (c05) | Single-source |
| LLM outputs are homogeneous | Infinity-Chat: 26K queries, 70+ models, 31,250 labels (25 raters per item). Same model, 50 samples (top-p 0.9, T=1.0): 79% of cases mean pairwise similarity above 0.8. Cross-model 71% to 82% (DeepSeek-V3 vs qwen-max 0.82, vs gpt-4o 0.81). Temp 2.0 with min-p 0.1: 79% still above 0.8; min-p: 81% of pairs above 0.7, 61.2% above 0.8 | Jiang et al. 2025 (b08, c12, c13) | Established (with c20, c21, d08) |
| Idea generation saturates | 4000 seed ideas, about 200 non-duplicates (cosine cutoff 0.8) | Si et al. 2024 (c20) | Single-source |
| Epistemic diversity below a search baseline | 27 LLMs, 155 topics, 12 countries, 1.7M responses, 70M claims; rose over 3 years; larger models less diverse; RAG raised diversity | Epistemic diversity paper 2025 (c21) | Single-source |
| Multi-agent ideation loses diversity through structure | Over 10,000 proposals, 20 topics. Vendi/N falls 1.03 to 0.47 for N=3 to 7. Horizontal groups Vendi 8.08 vs expert-role groups 4.65 (quality 8.50 vs 7.88). Vendi agrees with 5 experts in 87% of pairs | Chen et al. 2026 (d08) | Single-source |
| Blind writing and subgroups keep diversity higher | Highest semantic diversity with a blind-writing start; mid-debate rebound with subgroups; figures only; no accuracy result | Chen et al. 2026 (d09) | Single-source |
| LLM groups fail on hidden profiles | 65 tasks, 15 LLMs: 30.1% distributed vs 80.7% full info. Peak at 15 rounds, falls at 20 (0.233 vs 0.733 full). N=3 to 7: communication gain +0.348 to +0.006 (GPT-4.1) | Li, Naito and Shirado 2026 (d10) | Single-source |
| Forced exchange protocol rescues hidden-profile accuracy | 18 tasks, 5 runs, 4 agents: GPT-4.1 0.037 to 0.800; Gemini-2.5-Flash 0.173 to 0.727; Flash-Lite 0.043 to 0.743. Against no protocol, not against free self-critique | Li et al. 2026 (d10) | Contested |
| Identity prompts misportray groups | 3200 humans, 16 identities, 4 LLMs, 9 questions. Closer to out-group imitation than in-group portrayal: non-binary 16/24 and 32/48; impaired vision 18/24 and 27/48; Gen Z 27/48; woman 26/48. Temp 1.0, 1.2, 1.4 does not restore variance | Wang et al. 2025 (c15, c16) | Single-source |
| Multi-agent systems fail often | 1642 traces, 7 frameworks, failure rate 41% to 86.7%; kappa 0.88 on 150 traces. Design 41.8%, misalignment 36.9%, verification 21.3%. Step repetition 15.7%, reasoning-action mismatch 13.2%, not recognising completion 12.4%, disobey spec 11.8%, incorrect verification 9.1%, incomplete 8.2%, derailment 7.4%, wrong assumptions 6.8%, premature termination 6.2%, ignoring input 1.9%, withholding 0.85% | Cemri et al. 2025 (b12, d11) | Single-source (large) |
| Verification fixes help but not universally | ChatDev ProgramDev 25.0, 34.4 (+9.4 prompts), 40.6 (+15.6 topology with objective verification); HumanEval 89.6, 90.3, 91.5; AG2 GSM-Plus GPT-4 84.75 to 89.75 and 85.50 | Cemri et al. 2025 (d12) | Single-source |
| Discovery agent with adversarial tournament | 203 goals; top-ranked 78.4% top-1 GPQA diamond; Elo rose with test-time compute; improvement step 70.9% to 75.4%; meta-review AUC 0.629 to 0.634 (GPQA, 1680 ideas) and 0.521 to 0.597 (paper-QA, 600 ideas) | Gottweis et al. 2025 (c17, c18) | Single-source; Elo self-judged |
| LLM ideas rated more novel than expert ideas | Novelty 4.84 human vs 5.64 AI vs 5.81 AI plus human rerank; 49 ideas each; 298 reviews; slightly lower feasibility | Si et al. 2024 (c19) | Single-source |
| Knowledge collapse | A 20% discount on AI content gives public beliefs 2.3 times further from truth | Peterson 2025 (c22) | Single-source (simulation) |
| AI monocultures in science | 1000+ runs, 100 agents, Hamming distance near 0; uniform AI guidance helps only for decomposable problems and moderate use; personalisation beats randomisation | Fazelpour, O'Brien and Rubin 2026 (c23, c24) | Single-source (simulation) |

## 4. Mechanisms and models

Each model below is stated so it can be coded.

### 4.1 Hong-Page ring search
- World: ring of n=2000 positions, value v(x) drawn uniform on [0,100]. Fixed for a trial.
- Agent: heuristic = ordered tuple of k=3 step sizes drawn from {1..l}. Pool sizes: l=12 and l=20 (6,840 heuristics at l=20).
- Individual search: start at x. Try the first step; if v(x+s)>v(x) move there. Cycle through the tuple until no step improves. The agent is stuck at a local optimum for its own heuristic.
- Team search: agents act in sequence. The first searches, passes the point to the next, and so on, cycling until no one improves. The team stops only at a point that is a local optimum for every member.
- Ability = mean final value over random starts. Best team = top N1 by ability. Random team = N1 drawn at random.
- Diversity measure = share of agent pairs with different heuristics (the percentages in section 3).
- Why it works: top-ability agents have similar heuristics (diversity 71% to 75% in the best team, 91% to 94% in the random team), so their stuck points coincide. Random agents have different stuck points.
- LLM translation: an "agent" is a distinct prompt, method or model. "Pass the point on" is a pipeline in which each branch tries to improve the previous branch's best answer. The pipeline stops only when no branch can improve it.
- Limits: ability is measured on the same problem the team then solves; the pool must be large; with 20 agents the best group is already more diverse (finite pool).

### 4.2 Bandit-network model (Zollman)
- Two options A and B with success probabilities, e.g. 0.5 and 0.499.
- Each agent holds Beta(alpha, beta) beliefs about each option. Each round every agent picks the option it currently believes better, runs n trials (1,000 pulls in the cited setup), sees its own results and its neighbours' results, and updates.
- Network: complete (everyone sees everyone), cycle, wheel. Success = all agents converge on the truly better option.
- Mechanism: in a complete network one unlucky run of the better option makes everyone abandon it, and the data to correct that never arrive. In a sparse network some agents keep trying it longer.
- Knobs: connectivity; prior strength (extreme priors keep agents on their option); stubbornness. Trade-off: success probability up, speed down.
- Branch-merge translation: run branches in parallel with no sharing for a set number of steps, then share. Compare final accuracy with immediate sharing. This has not been shown for LLM agents (K30).

### 4.3 Diversity, trust and conformity (Fazelpour and Steel)
- Same bandit setup, two social groups (near-equal size works best), 10 agents, complete, cycle or wheel network, 10,000 runs of 3,000 experiments.
- Trust: data from an out-group member is down-weighted by factor w in (0,1]. Conformity: agents move their stated belief toward the group with strength kappa (Other-Total-Ratio rule), kappa from 0 to 0.1.
- Result: w near 0 worst; w=1 second worst; moderate best, mostly in complete networks. Low kappa: mixed groups beat homogeneous ones. Higher kappa: homogeneous groups win (between-group polarisation; a wrong public consensus while some agents privately disagree).
- Reading for an engineer: the gain comes from reduced uncritical uptake, not from different knowledge. The group label carries no task knowledge in their model.

### 4.4 Epistemic landscape (Weisberg and Muldoon)
- Grid landscape, height = significance. Agents: controls (random walk), followers (move toward the best spot seen among nearby agents' visited spots), mavericks (move to unvisited neighbours).
- Metric: how fast and how completely agents reach high ground.
- Boundary: the result changes with the follower rule (Alexander et al.), with parameters, and across implementations. Not a basis for agent rules.

### 4.5 Mixture-of-Agents (Wang et al.) and Self-MoA (Li et al.)
- MoA: layer 1 has n proposer models answer the prompt. Layer 2 agents each see all layer-1 outputs and produce a new answer. Repeat (3 layers in the original). A final aggregator model produces the output.
- Self-MoA: the same pipeline, but the proposers are n samples from one model (the best).
- Quality-diversity regression (Li et al.): score ~ b1 * quality + b2 * Vendi diversity, fitted on about 70 ensembles per dataset, R2 about 0.7, both terms significant. Vendi score = exponential of the entropy of the eigenvalues of the normalised similarity matrix of outputs (the effective number of distinct outputs).
- Rule of thumb: measure each candidate's solo quality first. If the best is far ahead, sample it. Mix only when qualities are close.

### 4.6 Debate and its martingale account
- Debate: N agents each answer, read the others' answers, revise, for R rounds; final answer by vote.
- Choi et al. and Zhu et al.: if agents are homogeneous and update uniformly, expected correctness stays the same from round to round (a martingale), so debate adds nothing beyond the initial vote. A gain appears only if updates are tied to something correlated with truth (confidence, an oracle, an external check). Conformity (copying the majority) moves answers to the majority but cannot lift accuracy above the initial vote.
- Consequence: measure the initial vote first. Debate is worth testing only with a truth-correlated update signal.

### 4.7 Diversity collapse in agent groups (Chen et al.)
- Measure: Vendi score on text embeddings (text-embedding-3-large, checked with BGE-large) of each agent's idea. Vendi/N = diversity per agent.
- Findings: Vendi/N falls from 1.03 to 0.47 as N goes from 3 to 7. Authority-led groups are less diverse. Blind writing first (nominal group technique) starts highest. Subgroups rebound mid-debate.
- Use: log Vendi/N across branches; stop adding branches when Vendi/N stops rising.

### 4.8 Forced exchange protocol (Li, Naito and Shirado)
- Each agent holds private facts. Protocol: each agent shares its facts and states one reason the current front-runner may be wrong; then all decide.
- Why it works: groups converge on shared evidence early. A forced counter-reason surfaces unshared evidence.
- Limit: the comparison baseline is no protocol (accuracy 0.04 to 0.17), not free self-critique.

### 4.9 Diversity prediction theorem
- (c - theta)^2 = mean of (s_i - theta)^2 minus mean of (s_i - c)^2, where s_i are individual guesses, c their mean, theta the truth. The second term is prediction diversity.
- Use: for numeric estimates averaged in code, the spread among branches is exactly the amount by which the average beats the typical branch. It is an identity, not a recipe: spread from worse guesses also raises the first term.

## 5. What holds up

### 5.1 Replications and re-checks
- Hong-Page: the original numbers were re-read and confirmed (critique, point 1). The theorem is conditional by the authors' own account. Sensitive to landscape randomness (Grim et al., abstract confirmed). Treat as a conditional model result, not an empirical law.
- Weisberg-Muldoon: a replication in another language reproduces the code results, but small rule changes alter the outcome (OpenAlex abstract). Alexander et al. details unverified.
- Zollman: reproduced in later models (Wu and O'Connor review) but parameter-dependent (Rosenstock et al.; details unverified).
- Hofstra and Yang: no replication found; sources not re-opened (critique, point 10).
- MoA: the 65.1 headline is internally consistent. "Self-MoA beats MoA by 6.6" is against Li et al.'s weaker 2-layer mix. Against the original 65.1 the margin is 0.6.
- Debate: the original positive result (Du et al.) did not survive strong baselines in Smit et al. (2024), Zhang et al. (2025), Choi et al. (2025) and Tran and Kiela (2026). This is the clearest failed replication in the series. Du et al.'s debaters are copies of one model.

### 5.2 Failures and null results
- Debate versus CoT and self-consistency: Multi-Persona won 0% of comparisons; ChatEval and AgentVerse about 15% (c08).
- Personas: no gain over no persona across 162 roles (d14). Identity prompts fail to reproduce real standpoint (c15, c16).
- Equal-token single agent: above about 500 thinking tokens, a single agent matches or beats five multi-agent designs (d01).
- GPT-3.5 shows no gain from approach-diverse prompting on planning (d13). LLaMA-2 70B zero-shot gain is negligible.
- Decoding diversity (temperature, min-p) does not restore diversity (c13, c16, d03).
- More rounds hurt after about 15 (d10); more agents give diminishing returns (d08, d10).

### 5.3 Moderators and boundary conditions
- Problem difficulty: ring and bandit models show the diversity benefit appears on hard problems and vanishes on easy ones (a04, a13, c26).
- Pool quality: mixing models helps when qualities are close and hurts when one is clearly best (c10, c11).
- Heterogeneity in debate: helps with strong, similar models (a29, c09) but can lower accuracy with weaker minority models (d06).
- Trust and conformity: interior optimum (a07, a08).
- Budget: multi-agent wins only at very small thinking budgets (100 tokens) or with damaged context (d01, d02).
- Model strength: approach-diverse prompting needs strong instruction following (d13).
- Task type: a structured exchange helps in hidden-profile tasks (d10). Nothing shows it helps in search or discovery.

### 5.4 Interventions that worked
- Approach-diverse prompting with a strong model (d13): large gains on structured tasks, no variance reported.
- Selecting initial answers for distinctness (d03): Pass@5 0.79 to 0.91, costs a larger candidate pool.
- Confidence-weighted updates over plain vote (d03, d04), if confidence tracks correctness.
- Forced counter-reason step in hidden-profile tasks (d10).
- Blind-first writing and subgroups for idea diversity (d09); diversity only.
- Verification step or objective-verification topology: +9.4 to +15.6 points on ChatDev (d12), not universal.
- Mixing different models when qualities are close (b07, c09).
- Larger same-model sample ensembles on hard problems (b11).

### 5.5 Interventions that did not work
- Vanilla debate against majority vote (d05, d03, c08).
- Correctness-payoff prompt in debate (d06).
- Persona prompts and automatic role selection (d14).
- Raising temperature for diversity (c13, c16, d03).
- Adding weak models to a mix (c10, c11).
- Adding a verifier alone: verifiers check superficially (d12).

## 6. Language models

### 6.1 What diversity do LLMs supply?
Little. Same-model samples are above 0.8 similar in 79% of cases; cross-model similarity is 71% to 82% (b08). Temperature 2.0 with min-p still leaves 79% above 0.8 (c13). Idea saturation: about 200 non-duplicates in 4000 (c20). Epistemic diversity stays below a search baseline for all 27 models; larger models are less diverse; RAG raised diversity; diversity rose slowly across three years (c21). Diversity is scarce and decoding does not buy it.

### 6.2 Does mixing different models help?
Mixed evidence, mostly measured with more compute than the baseline.
- For: MoA ablation 61.3 vs 56.7 at n=6 (b07); Hegazy 91% vs 82% (c01); Heter-MAD +6.4% and +8.2% over averages (c09).
- Against: Self-MoA 65.7 vs 59.1 (c10), but against a weaker mix; the original MoA is 65.1 (d15). The quality-diversity regression says both matter, R2 about 0.7 (c11). Heterogeneous debate with weaker minorities can lose accuracy (d06).
- Reconciliation, from one paper: the quality gap decides (K12).

### 6.3 Does debate help?
Not reliably. At equal cost it is no better than majority vote or self-consistency in four independent studies (c08, c07/d07, d05, d01). The original gain of 4 to 15 points (c03) was against weak baselines. Debate is sensitive to settings: tuned agreement modulation helped (b09, c07). Heterogeneous groups can flip correct answers to wrong (d06). The martingale theory (d04, d05) explains why. This matches existing guardrail G9.

### 6.4 Personas and standpoints
Persona prompts: 71.1 to 74.2 on MMLU inside a debate (c04) versus no gain and an unpredictable best role across 162 roles and 2,410 questions (d14). Identity prompts do not reproduce the real in-group view and flatten variation (c15, c16). So persona "perspectives" are not a substitute for real cognitive diversity. Discovery tasks were not tested; c04 and c15 are not reconciled.

### 6.5 Equal-token evidence
Tran and Kiela (d01): single agent 0.421 vs debate 0.403 vs ensemble 0.372 at 2000 thinking tokens; multi-agent leads only at 100 tokens. Heterogeneity at equal tokens remains untested. Naik et al. (d13) matched cost by dollar estimate, not tokens, with single runs. Self-MoA is partly equal-compute.

### 6.6 Hidden information and premature convergence
HiddenBench (d10): LLM groups reach 30.1% with distributed information vs 80.7% for one agent with full information. More rounds past 15 and larger groups (3 to 7) reduce the benefit of communicating. A short structured protocol raised accuracy to 0.73 to 0.80 on three models. This is the LLM version of the human hidden-profile effect (Stasser and Titus, recalled).

### 6.7 Failure rates of multi-agent systems
41% to 86.7% of runs fail across 7 frameworks. Design flaws are 41.8% of failures, misalignment 36.9%, verification 21.3% (d11). Added verification gives +9.4 to +15.6 points on ChatDev, not universally (d12). "Ignoring other agents' input" is only 1.9%, so stubbornness is not the main problem.

### 6.8 AI in science as a social system
- Co-scientist (c17, c18): generate-debate-rank with Elo; Elo rose with test-time compute; review agent gains small (AUC 0.629 to 0.634 on GPQA). Elo is self-judged.
- Idea novelty: AI ideas 5.64 vs human 4.84, slightly less feasible (c19). Idea level only.
- Knowledge collapse and monoculture simulations (c22 to c24): uniform AI guidance converges to one solution; personalisation beats randomisation. These are simulations, not LLM agents.

## 7. What our agent should take

The agent is one model, so the social claims mostly do not apply. Items are mapped to the schema (G guardrails, S states, O operators, memory). Existing guardrails G4 (samples from one model are not independent), G9 (no debate), G11 (short independent attempts) and G12 (spend by difficulty) already agree with this subfield.

### Add now (established)
1. **Keep G9 (no debate) and cite the reason.** Debate is a martingale unless the update signal tracks truth; most of its gain is the initial vote. Schema part G9. [E] K13; c08, c07, d05, d01, d07. Supports an existing rule; only the citation changes.
2. **Keep G4 and state the scale of the problem.** Same-model samples are above 0.8 similar in 79% of cases and decoding tweaks do not fix it. Branches must differ in method, not in temperature. Schema part G4, O (parallel branches). [E] K18; b08, c12, c13, c20, c21, d08.
3. **Do not use persona or role prompts as perspectives.** No gain over plain across 162 roles; the best role cannot be selected. Consistent with G4 (no persona voters). [E for objective questions, one large source] K19, K20; d14, c15, c16. A cited reason, not a new rule.
4. **Do not rely on a verifier agent as a cure.** Verification gaps are 21.3% of multi-agent failures and verifiers check superficially. Verification stays by outputs (G2, G3, G10). [S] K32; d11, d12. Supports existing guardrails.

### Test first
5. **Method-diverse branches versus k same-config samples at equal tokens.** Schema part O (parallel branches), G4. [S] K17, K11; b05, d13, b07. Test U1.
6. **Select branches for distinct answers before merging.** Schema part G (keep alternatives), O. Pass@5 0.79 to 0.91 on two small models. [S] K29; d03. Test U3.
7. **Delayed merge of parallel branches (transient diversity).** Schema part O, merge timing. Contested in humans (Zollman versus Rosenstock); never shown on accuracy for LLM groups. [C] K04, K30; a09, a24, d09, d10. Test U4.
8. **Mandatory counter-reason step on the front-runner.** Schema part G (adversarial check). Hidden-profile gain 0.04-0.17 to 0.73-0.80 against no protocol only. [C] K31; d10, d05, d06. Test U5.
9. **Log branch diversity (Vendi/N) and stop adding branches when it flattens.** Schema part S6 control, G12. [S] K29; d08, c11. Test U6.
10. **Minority hypothesis held for N steps before pruning.** Schema part G. Model result only. [S] K05; a12, a26. Test U7.
11. **Cross-run memory of earlier answers to avoid monoculture across restarts.** Schema part memory. Simulation only. [S] K24; c22 to c24. Test U8.
12. **Pairwise tournament ranking in code instead of single scores.** Schema part O; G5 and G8 stay. [S] K22; c17, c18. Test U9.
13. **Mix models only when the solo quality gap is small.** Schema part G7. Only relevant if more than one model is allowed. [C] K12; c10, c11, d15. Test U2.
14. **Discount the agent's own novelty claims.** LLM ideas were rated novel by blind reviewers but lack diversity; G8 already says novelty is judged by running. [S] K23; c19, c20. No new test beyond existing novelty benches.

## 8. Concrete tests on our bench

All arms run at equal total tokens. Setup, branches, merge and verification all count.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Approach-diverse vs same-config samples (U1) | Hard search or planning items (graph colouring, ARC-style, constraint tasks) with plain accuracy 20% to 70% | (a) k samples of one best prompt, vote; (b) k branches each told to use a different method from a model-written list, vote or code-verified pick | Accuracy over 5 seeds with 95% intervals | +5 to +15 points on hard items; near zero on easy items; none on weak models |
| T2 Mixed vs best-single ensemble (U2) | Same items; two or more models of known unequal quality | (a) k from the best model; (b) k from a mix; (c) k from a mix of near-equal models | Accuracy vs solo-quality gap and Vendi | Mix wins only when the gap is under about 5 points |
| T3 Diverse-selected branches (U3) | Items with discrete answers | (a) 5 random of 15 branches; (b) 5 chosen for distinct answers from 15, costed as 15; (c) 15-sample vote | Pass@5 and final accuracy | +5 to +10 points Pass@5; final gain only if the extra samples are counted fairly |
| T4 Delayed vs immediate merge (U4) | Multi-step discovery items with a misleading first lead | (a) immediate sharing of partial results; (b) blind branches until step m, then share; (c) subgroups | Final accuracy; tokens to correct answer | Small positive on hard items with misleading leads; negative on easy |
| T5 Mandatory counter-reason vs free self-critique (U5) | Items with a plausible wrong front-runner | (a) free self-critique; (b) forced "one reason the leader is wrong" before acceptance; (c) none | Accuracy; rate of correct-to-wrong flips | +3 to +8 points over free critique if real; watch flips |
| T6 Diversity logging as a stop rule (U6) | Any branching item | (a) fixed k; (b) add branches until the Vendi/N gain falls under a cutoff | Accuracy per token | Same accuracy with 20% to 40% fewer tokens |
| T7 Minority hold (U7) | Items where the right hypothesis starts with low prior | (a) prune to the best after round 1; (b) keep the minority for N=2 and 4 rounds | Accuracy; tokens | Small gain on deceptive items |
| T8 Cross-run memory (U8) | One open-ended item repeated 10 times | (a) fresh runs; (b) runs see earlier answers and must differ | Vendi across runs; quality by a code check | Higher diversity; equal quality |
| T9 Tournament ranking (U9) | Idea sets with a code-checkable outcome | (a) single-score ranking; (b) pairwise comparisons aggregated in code | Agreement with the executed outcome | Small or null (G8 says model judges rank near chance) |
| T10 Persona branches vs plain (U10) | Discovery items | (a) k plain samples; (b) k persona or standpoint prompts | Accuracy; diversity | Null, per d14; confirm on discovery |

Report variance for every test. Count the cost of generating the method list in T1.

## 9. What does not transfer, and why

- Demographic diversity results (Hofstra, Yang, AlShebli, Levine, Woolley): they measure people with different life experience, networks and bias. A single model has none of these. They are observational.
- Longino's norms and tempered equality: they describe a community of people. For one agent only "explicit uptake of an objection" has a counterpart (T5), and no data test it.
- Standpoint: LLM identity prompts do not reproduce standpoint and flatten groups (c15, c16). A standpoint branch is not a real perspective.
- Weisberg-Muldoon mavericks: the result depends on rule details (a20, K03). Do not build agent rules on it.
- Hong-Page: the random-beats-best theorem needs a large, truly diverse pool and ability measured on the same problem. Our "agents" are prompts of one model with highly correlated errors.
- Zollman network structure: our branches communicate through code and we choose what is shared. Translation to LLMs is by analogy only, and the effect is contested even for humans.
- Credit and priority, funders, testimonial injustice, propaganda: no counterpart for one agent.
- Conformity and trust parameters (Fazelpour and Steel): branches share one model, so "out-group" is undefined.
- Multi-agent debate and failure results (MAST): they apply to systems we are not building (G9). They are a warning only.
- Co-scientist: a multi-agent system with self-judged Elo; a different architecture.

## 10. Open questions

1. At equal tokens, does heterogeneity (different prompts, methods, models) beat k samples of the best single configuration, and at what quality gap? (Gap 1.)
2. Does transient diversity (delayed sharing among parallel branches) improve final accuracy for LLM agents, and at which difficulty? (Gap 2, K30.)
3. What embedding or Vendi diversity is needed before ensemble gain appears? No threshold found. (Gap 3.)
4. Does Naik et al. replicate across models and tasks, with variance? (Gap 4.)
5. What exactly do Alexander, Himmelreich and Thompson (2015) and Thompson (2014) show, with numbers? Sources were not reachable. (Gap 5.)
6. At which parameters does the Zollman effect hold or reverse (Rosenstock et al. 2017)? (Gap 6.)
7. Do persona or standpoint prompts help on discovery tasks at equal tokens? The objective-question result is null. (Gap 7.)
8. Does mandatory uptake of critique beat free self-critique? (Gap 8.)
9. Which of the 14 MAST failure modes map onto our guardrails G1 to G12? (Gap 9.)
10. Do Hofstra et al. and Yang et al. replicate in non-US and non-medical data, and do they bear on how our agent should discount its own novelty ratings? (Gap 10.)
11. Does the quality-diversity regression (one paper, R2 about 0.7) hold in other model sets?
12. Do hidden-profile fixes carry over to a single agent that must collect and weigh its own scattered evidence?

## 11. Sources

[V] = opened and read in this series (page or PDF text). [M] = snippet, abstract only, or recalled, not opened.

Human science
- [V] Hong and Page (2004) Groups of diverse problem solvers can outperform groups of high-ability problem solvers. https://pmc.ncbi.nlm.nih.gov/articles/PMC528939/ (a01 to a05, b01, b02)
- [M] Hong and Page (2004), PNAS DOI. https://doi.org/10.1073/pnas.0403723101 (c28)
- [V] Fazelpour and Steel (2022) Diversity, Trust, and Conformity. https://www.cambridge.org/core/journals/philosophy-of-science/article/diversity-trust-and-conformity-a-simulation-study/E1102A15D9D865DD6E988811061EF0CE (a06 to a08; b22 is a recalled duplicate)
- [M] Zollman (2010) The Epistemic Benefit of Transient Diversity (page notes and abstract only; paywall). https://doi.org/10.1007/s10670-009-9194-6 (a09, a10, b17)
- [V] Wu and O'Connor (2023) How should we promote transient diversity in science? (author names unconfirmed). https://doi.org/10.1007/s11229-023-04037-1 (a11 to a13)
- [V] Karge (2025) When Diversity in Voting Trumps Ability (formulas not read). https://www.cambridge.org/core/journals/episteme/article/when-diversity-in-voting-trumps-ability/8B352EA09F742692FD684EDB07B039EA (a14)
- [V] Authors not recorded (2023) Does (mis)communication mitigate the upshot of diversity? https://pmc.ncbi.nlm.nih.gov/articles/PMC10038257/ (a15, a16)
- [V] Hofstra et al. (2020) The diversity-innovation paradox in science. https://pmc.ncbi.nlm.nih.gov/articles/PMC7196824/ (b03)
- [V] Yang et al. (2022) Gender-diverse teams produce more novel and higher-impact scientific ideas. https://pmc.ncbi.nlm.nih.gov/articles/PMC9456721/ (b04)
- [M] Longino (1990) Science as Social Knowledge; (2002) The Fate of Knowledge. https://doi.org/10.1515/9780691209753 ; https://press.princeton.edu/books/paperback/9780691020518/science-as-social-knowledge (a17, b21, c27)
- [M] Kitcher (1990) The division of cognitive labor. https://doi.org/10.2307/2026796 (a18)
- [M] Weisberg and Muldoon (2009) Epistemic Landscapes and the Division of Cognitive Labor. https://doi.org/10.1086/644786 ; https://repository.upenn.edu/philosophy_papers/7 (a19, b15, c25)
- [M] Alexander, Himmelreich and Thompson (2015). https://doi.org/10.1086/681766 ; https://openresearch-repository.anu.edu.au/items/dbb090c6-1d24-481c-aff8-101ec8decd5e (a20, b16)
- [M] Thompson (2014) Does Diversity Trump Ability? https://www.ams.org/notices/201409/rnoti-p1024.pdf (a21, b13)
- [M] Singer (2019) Diversity, Not Randomness, Trumps Ability. https://doi.org/10.1086/702443 (a22)
- [M] Grim, Singer, Bramson, McGeehan and Berger (2019) Diversity, Ability, and Expertise in Epistemic Communities. https://doi.org/10.1086/701070 ; https://doi.org/10.1086/706253 (a23, b14; abstract seen in the cross-check via OpenAlex)
- [M] Rosenstock, Bruner and O'Connor (2017) In Epistemic Networks, Is Less Really More? https://doi.org/10.1086/690717 (a24)
- [M] Lazer and Friedman (2007) The Network Structure of Exploration and Exploitation. https://doi.org/10.2189/asqu.52.4.667 (a25)
- [M] Kummerfeld and Zollman (2016) Conservatism and the Scientific State of Nature. https://doi.org/10.1093/bjps/axv013 (a26)
- [M] Poyhonen (2017) Modelling the division of cognitive labour and heterogeneity of learning heuristics. https://doi.org/10.1007/s11229-016-1147-4 (c26)
- [M] Woolley et al. (2010) Evidence for a collective intelligence factor. https://doi.org/10.1126/science.1193147 (b18)
- [M] Horwitz and Horwitz (2007) Effect of team diversity on team outcomes. https://doi.org/10.1177/0149206307300814 (b19)
- [M] Stasser and Titus (1985) Pooling of unshared information. https://doi.org/10.1037/0022-3514.48.6.1467 (b20)
- [M] Levine et al. (2014) Ethnic diversity deflates price bubbles. https://doi.org/10.1073/pnas.1407301111 (b23)
- [M] AlShebli, Rahwan and Woon (2018) The preeminence of ethnic diversity in scientific collaboration. https://doi.org/10.1038/s41467-018-07634-8 (b24)
- [M] Page (2007) The Difference. https://press.princeton.edu/books/paperback/9780691138541/the-difference (b25)

LLM and AI
- [V] Wang et al. (2024) Mixture-of-Agents. https://arxiv.org/abs/2406.04692 ; https://arxiv.org/pdf/2406.04692 (a27, b06, b07; re-opened in the cross-check)
- [V] Li, Lin, Xia and Jin (2025) Rethinking Mixture-of-Agents (Self-MoA). https://arxiv.org/abs/2502.00674 (a28, c10, c11; re-opened in the cross-check; d15 carries the correction and is marked not re-opened)
- [V] Hegazy (2024) Diversity of Thought Elicits Stronger Reasoning in Multi-Agent Debate Frameworks. https://arxiv.org/abs/2410.12853 (a29, c01, c02)
- [V] Du et al. (2023) Multiagent Debate. https://arxiv.org/abs/2305.14325 (a30, c03 to c05)
- [V] Naik et al. (2024) Diversity of thought improves reasoning abilities of LLMs. https://arxiv.org/abs/2310.07088 ; https://arxiv.org/pdf/2310.07088 (b05, d13)
- [V] Jiang et al. (2025) Artificial Hivemind. https://arxiv.org/abs/2510.22954 ; https://arxiv.org/pdf/2510.22954 (b08, c12 to c14)
- [V] Smit et al. (2024) Should we be going MAD? https://arxiv.org/abs/2311.17371 ; https://arxiv.org/pdf/2311.17371 (b09, c07, d07; per-cell numbers not extracted)
- [V] Liang et al. (2023/2024) Encouraging Divergent Thinking in LLMs through Multi-Agent Debate. https://arxiv.org/abs/2305.19118 ; https://arxiv.org/pdf/2305.19118 (b10, c06; tables not extracted)
- [V] Li et al. (2024) More agents is all you need. https://arxiv.org/pdf/2402.05120 (b11)
- [V] Cemri et al. (2025) Why do multi-agent LLM systems fail? https://arxiv.org/abs/2503.13657 ; https://arxiv.org/pdf/2503.13657 (b12, d11, d12)
- [V] Zhang et al. (2025) Stop Overvaluing Multi-Agent Debate. https://arxiv.org/abs/2502.08788 (c08, c09; re-opened in the cross-check)
- [V] Wang, Morgenstern and Dickerson (2025) LLMs that replace human participants can harmfully misportray and flatten identity groups. https://arxiv.org/abs/2402.01908 (c15, c16)
- [V] Gottweis et al. (2025) Towards an AI co-scientist. https://arxiv.org/abs/2502.18864 (c17, c18)
- [V] Si, Yang and Hashimoto (2024) Can LLMs Generate Novel Research Ideas? https://arxiv.org/abs/2409.04109 (c19, c20)
- [V] Measuring epistemic diversity of LLMs across time and cultures (2025). https://arxiv.org/abs/2510.04226 (c21)
- [V] Peterson (2025) AI and the Problem of Knowledge Collapse. https://arxiv.org/abs/2404.03502 (c22)
- [V] Fazelpour, O'Brien and Rubin (2026) Navigating Epistemic Monocultures in AI-Driven Science. https://arxiv.org/abs/2608.19390 (c23, c24)
- [V] Tran and Kiela (2026) Single-Agent LLMs Outperform Multi-Agent Systems Under Equal Thinking Token Budgets. https://arxiv.org/abs/2604.02460 (d01, d02)
- [V] Zhu et al. (2026) Demystifying Multi-Agent Debate: The Role of Confidence and Diversity. https://arxiv.org/abs/2601.19921 (d03, d04)
- [V] Choi, Zhu and Li (2025) Debate or Vote. https://arxiv.org/abs/2508.17536 (d05)
- [V] Wynn, Satija and Hadfield (2025) Talk Isn't Always Cheap. https://arxiv.org/abs/2509.05396 (d06)
- [V] Chen et al. (2026) Diversity Collapse in Multi-Agent LLM Systems. https://arxiv.org/abs/2604.18005 (d08, d09)
- [V] Li, Naito and Shirado (2026) Systematic Failures in Collective Reasoning under Distributed Information (HiddenBench). https://arxiv.org/abs/2505.11556 (d10)
- [V] Zheng et al. (2024) When 'A Helpful Assistant' Is Not Really Helpful. https://arxiv.org/abs/2311.10054 (d14)
- [M] Status line d16: Alexander et al., Thompson, Zollman 2007, Rosenstock et al. 2017 and replications of Hofstra and Yang could not be opened in the gap pass. Not evidence.
