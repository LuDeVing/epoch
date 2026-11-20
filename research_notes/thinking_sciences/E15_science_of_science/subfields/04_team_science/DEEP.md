# Team science: deep document

*Subfield E15.04 of science of science. Sources: evidence_a-d.jsonl (ids a01-a27, b01-b27, c01-c25, d01-d16), claims.jsonl (K01-K29), critique.md. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested. Background rating for the agent: Low. The human literature is observational. The LLM literature is the useful part.*

## 1. What it is

Team science studies how groups of people make knowledge. It asks how big teams are, who joins them, how they form, and what kind of work they produce. Its data are author lists on papers and patents, with citations as the outcome.

Two headline facts frame the field.

- Teams keep growing. The Fortunato et al. (2018) review says team size grows about 17 per cent per decade, and that team-authored work rose from about 50% (1955) to 90% (2013) (b01, d01). The exact 17% is a review summary, not a measured constant (K04, K26).
- Complementary long-term coauthors ("super ties") are linked to a little more output and more citations (a06, a07).

The deeper finding is a trade. Large teams collect more citations. Small teams produce more disruptive work, meaning work that replaces older work instead of building on it (a01, a12).

For our agent the human results are background. They do not tell us how to build a single-agent scaffold. What transfers is a set of questions, now tested on LLM teams (2023-2026):

1. Does adding more members help?
2. Does it depend on the task structure?
3. Do members add diversity or only redundancy?
4. Where do team failures come from?

The LLM answers are mostly "no, depends, redundancy, coordination and verification". That supports guardrails G4, G9, G10 and G11 in SCHEMA.md and gives a few things to test (section 7 and UNKNOWNS.md).

Links to other subfields run in parallel (not covered here): Collective intelligence factor c, Coordination and common ground, Social epistemology of discovery, Organisational ambidexterity.

## 2. History and theories in depth

**Team growth (2005-2009).** Guimera, Uzzi, Spiro and Amaral (2005) modelled team assembly with three parameters: team size, share of newcomers, and tendency to reuse past collaborators. Network structure and success follow from those rules (a25, recalled only, not opened). Wuchty, Jones and Uzzi (2007) counted 19.9 million papers and 2.1 million patents over five decades. Teams dominated nearly every field and got more citations than solo authors (d04, abstract opened; body paywalled). The commonly quoted rise in mean team size in science and engineering, about 1.9 to 3.5, is recalled and not verified (a24).

**Why teams grow: burden of knowledge.** Jones (2009) argued that knowledge accumulates, so each person must specialise more, and teams must be larger to cover the same ground. Patent team size rose from 1.73 (1975) to 2.33 (1999), a 35% rise over 24 years. The trend holds after controlling for technology class and domestic vs foreign patents (d03).

**Team-size distribution.** Milojevic (2014) gave the first model of team-size distribution. There are two modes (a09, a10):
- Core teams: a Poisson process, dominant up to about 8 authors.
- Extended teams: grow by cumulative advantage on members' productivity, giving a power-law tail, dominant at 10 or more authors.

In astronomy, mean team size went from 1.5 (1961-65) to 6.7 (2006-10), yet 90% of articles still have fewer than ten authors. The probability of publishing with an extended team stayed at 0.3 over 50 years, and the repeat-publication probability was 0.8. So the average rises mostly because the tail grows. The same analytic form fits many fields: 2006-10 mean team size was astronomy 6.14, ecology 3.54, social psychology 2.93, mathematics 1.93, literature 1.05 (a10).

**Impact vs disruption.**
- Lariviere, Sugimoto, Tsou and Gingras (2015): more authors, more addresses and more countries mean more citations since 1900, and not only through self-citation. Authors per paper have to keep rising for a paper to beat the world-average citation rate (a12, a13).
- Wu, Wang and Evans (2019): the opposite direction on a different outcome, the CD (disruption) index. Disruption falls with team size (a01).

These are consistent. One measures impact, the other measures whether a paper displaces its references.

**Cognitive extent.** Milojevic (2015): bigger teams cover less lexical territory per article. Teams of 10 cover 85% of the maximum extent, about 60 members 60%, over 100 authors in physics 35%. In biomedicine extent peaks at 3-5 members (a11).

**Ties.** Petersen (2015) defined super ties from the extreme tail of collaboration duration and paper overlap (a06 to a08). The result is the "apostle effect". Granovetter's weak-tie theory is the counter-position, supported in DBLP computer science by a later study (b09).

**Distance.** Lin, Frey and Wu (2023): remote teams are less disruptive than on-site teams (a14).

**Measurement crisis.** Park, Leahey and Funk (2023) said papers and patents are becoming less disruptive (b04). Holst et al. (2024) showed that most of that decline is a data artefact (a16, b05).

**AI and science.** Hao, Xu, Li and Evans (2024/25): AI users gain personally while science narrows (a17, d05).

**LLM teams (2023-2026).** The same questions were then asked of LLM agent groups: AgentVerse, debate, Mixture-of-Agents, MacNet, MAST, Kim et al.'s scaling science, Ringelmann scaling, distributed-systems framing (section 6).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Disruption falls as team size rises | From 1 to 50 members: -70% papers, -30% patents, -50% software. Data: over 50M works (arXiv text; 65M in the Nature abstract) | Wu, Wang, Evans 2019 (a01, b02) | [E] direction; no independent replication of the team-size result (K24) |
| Solo equals 5-person on hit rate, but more disruptive | Solo 72% more likely to write a top-5% disruptive paper; 10-person teams 50% more likely to be a top-5% cited hit | a02 | [S] |
| Effect is two thirds within-person | Fixed-effect beta -0.00018 vs random -0.00027; about 100 topic controls; holds in about 90% of fields and all eras; reviews excluded | a03, d16 | [S] |
| Small teams search older work | Sleeping Beauty index of 1-2 person teams is 4x that of 10-person teams; distant-journal combination peaks at 8-10 members | a04 | [S] |
| Funding does not rescue small-team disruption | Funded small teams look like large teams (2008-12 papers) | a05 | [S] |
| Large teams get more citations | Sole-authored natural/medical papers 87% (1900) to 7% (2011); social science and humanities 97% to 38%; 11-20 author papers rose 0.22% to 4.5% (1980-2011) | Lariviere 2015 (a12, a13) | [E] |
| Team size growth | About 13-18% per decade. Papers 2 to 5.5 (1954-2014, about 18%); patents 1.7 to 2.7 (about 13%); Jones patents 1.73 to 2.33 (1975-99, about 13%). 17% is a review average | b01, d01-d03 | [E] direction; exact 17% unpinned |
| Team-authored share | About 50% (1955) to 90% (2013) | b01 | [E] |
| Team-size model | Two modes (Poisson core + power-law tail); astronomy mean 1.5 to 6.7 (1961-2010) | Milojevic 2014 (a09, a10) | [E] |
| Bigger teams cover less ground | 10 authors 85% of max extent; 60 authors 60%; 100+ in physics 35%; biomedicine peak at 3-5 | Milojevic 2015 (a11) | [S] |
| Super ties give small output gain | Productivity coefficient 0.11 (about 5.2% gain); citation boost 1.17 (about 21 extra citations biology, 8 physics); 473 careers, 166,000 collaborator records; 60-80% of ties last one year | Petersen 2015 (a06, a07, b06) | [S] |
| Super-tie benefit contested | DBLP: weaker ties go with higher h-index at equal achievement; country strong ties help (72 countries, 1993-2013) | b08, b09 | [C] |
| Remote teams less disruptive | Raw P(D>0) 28% to 22% papers, 67% to 55% patents; controlled 20.4% to 19.5% and 58.2% to 56.5%; new concepts 0.40% to 0.32%; same scientist conceives 63% to 51% when remote | Lin 2023 (a14, a15, b03, d14) | [S] same group |
| Disruption decline is largely an artefact | 972,161 papers and 142,362 patents have CD5=1; 97% and 78% of them list zero references; 93% and 98% of 100 sampled actually had references | Holst 2024 (a16, b05) | [C] |
| AI users gain personally, science narrows | 3.02x papers, 4.84x citations, 1.37 years earlier to lead, topics -4.63%; matched cohort only +24.45% citations, +9.61% productivity at year 10; AI teams 19.29% smaller | Hao 2025 (a17, d05-d07) | [S] observational |
| Multi-agent gain depends on task | +80.8% (finance, centralised) to -70.0% (sequential planning, independent); decentralised +9.2% web navigation; PlanCraft -39% to -70% for all variants | Kim 2025 (a22, b13, c06) | [E] direction (3 sources) |
| Capability ceiling | Single agent above about 0.45 raw: extra agents negative, beta -0.236, p=0.004; held-out frontier MAE 0.061 | Kim 2025 (c05, d08) | [S] |
| Error amplification by topology | Single 1.0; centralised 4.4; hybrid 5.1; decentralised 7.8; independent 17.2 | Kim 2025 (a23, b14) | [S] |
| Debate does not beat self-consistency at equal compute | Du 2023: GSM8K single 77.0, majority 81.0, debate 85.0. Zhang 2025: five methods, nine benchmarks, beat CoT in about 15% of 36 configs | b16, b17, b18, b19, c11 | [E] |
| Sampling and voting scale | GSM8K +12 to +24, MATH +6 to +10, MMLU +5 to +11, HumanEval +4 to +9; Llama2-13B x15 gets 59% GSM8K vs Llama2-70B 54% | Li 2024 Agent Forest (b15) | [E] |
| Self-MoA beats mixing models | +6.6 AlpacaEval 2.0; +3.8% average over MMLU, CRUX, MATH; quality weight 2.558 vs diversity 1.841 on MMLU (R2 0.771) | Li 2025 (b20, c13, d11) | [E] / [C] on diversity |
| Failure modes of LLM teams | 14 modes; 41% to 86.7% failure across 7 frameworks; design 44.2%, misalignment 32.3%, verification 23.5%; kappa 0.88; 1,642 traces | Cemri 2025 (b21, c07, d12) | [E] |
| Fixes help modestly | ChatDev: +9.4% from role specification, +15.6% from adding a task-objective verification step | c08, d12 | [S] |
| Coordination cost | Parallel tasks stay below Amdahl bound (median 2.19x); self-coordinated teams send more messages, duplicate claims | Mieczkowski 2026 (a20, a21) | [E] |
| Homogeneous debate ceiling | Effective team size 1/c about 1.2 to 1.8; 30 debaters no more diverse than 1 on MMLU-Hard; each extra member OR 0.92 in 7,150 runs | Bertalanic 2026 (a18, a19, d13); Riedl 2026 (c15) | [E] (two preprints) |
| Weak models conform to wrong feedback | About 10% of MGSM errors were a correct GPT-3.5 agent talked out of its answer; not seen with GPT-4 | AgentVerse (b23, c17) | [E] |
| Topology | MacNet mean quality: CoT 0.5757, AgentVerse 0.5805, Chain 0.6078, Mesh 0.6316, Random 0.6522 | Qian 2025 (b22, c01, c02) | [C] |

## 4. Mechanisms and models

**M1. Two-mode team size (Milojevic).** Implementable as a generator. Each paper draws a core team from a Poisson distribution. With probability 0.3 it adds an extended team. Extended members are chosen with probability proportional to past productivity (cumulative advantage), and a returning member is chosen with probability 0.8. The result is a mean that rises with a power-law tail. Use: simulate how a pool of agent "specialists" grows if the pool reuses its most productive members (a09).

**M2. Search depth explains the trade (Wu).** Small teams cite older, less popular work. Large teams cite recent high-impact work and get cited sooner (a04). Operational form for an agent: a branch that is told to build on the current best attempt will converge. A branch seeded from the bare task or from old material will diverge. This is what S3 open mode already does (isolated attempts from the bare task).

**M3. Burden of knowledge (Jones).** Required team size grows with the amount of prior knowledge a task needs per specialist. If the task needs k skills and one person holds at most m, then team size is about k/m. For agents this has no direct analogue until context limits bind (section 9).

**M4. Ringelmann scaling for LLM teams (Bertalanic and Fortuna).** Effective team size ratio R(N) = Neff / N = 1 / (1 + c (N-1) N^-alpha). Three regimes: alpha = 0 gives a hard ceiling Neff = 1/c; sublinear; linear (a18). To use it: run N = 1 to 5 agents, measure the number of distinct answers or the diversity score, fit c and alpha, and predict the ceiling. Fits had R2 above 0.99 on 44 model-task-condition cells. Reported c: Qwen2.5-32B 0.96 / 0.77 / 0.97 (MMLU-Hard / GSM-Hard / GPQA) vs 7B 0.85 / 0.57 / 0.81. Qwen3-8B thinking c = 1.00 at 87.2% solo accuracy (d13). Only architectural diversity lowered c. Communication mode changes did not (a19).

**M5. Capability ceiling and task structure (Kim et al.).** A fitted model over 260 configurations predicts the change from a single agent using task features and agent features. The decision rule: multi-agent is advisable only when single-agent raw accuracy is below about 0.45 (beta -0.236) and the task is decomposable into independent parts. It picks the best architecture for 87% of held-out configs. Cross-validated R2 is 0.373 (0.413 with the agentic capability index). The overall mean multi-agent change was -0.3% (95% CI -58.7 to +77.2) (critique.md item 2), so the sign is a function of task and baseline, not of team size (c03, c05, d08).

**M6. Error amplification.** Count how many wrong sub-results propagate to the final output versus the single-agent rate. Single 1.0, centralised 4.4, hybrid 5.1, decentralised 7.8, independent 17.2. Overhead: independent 58%, centralised 285%, hybrid up to 515% (b14). The cost of containing errors is tokens. Contained errors need a verifier that sees the output.

**M7. Amdahl bound for LLM teams (Mieczkowski).** Speedup = 1 / ((1 - p) + p/N), where p is the parallel fraction. Real teams stay below it (median 2.19x on highly parallel tasks). Serial tasks gain nothing. Self-coordinated teams duplicate claims (three Gemini agents all claimed the same task in round one). Pre-assignment by code cuts messages (a20, a21).

**M8. Quality-diversity fit for mixtures (Li).** Per dataset, fit score = a * quality + b * diversity over about 70 mixtures. Quality is the mean proposer accuracy and diversity is the Vendi score. a exceeds b on MMLU (2.558 vs 1.841; R2 0.771). At fixed quality, more diversity helps. Adding a weaker model costs more than the diversity gains (d11).

**M9. Synergy and complementarity (Riedl).** Measure whether a group acts as one unit with information-theoretic synergy. Three arms: plain, persona, persona plus "think about what others might do". Only the third gave identity-linked differentiation and goal-directed complementarity. Preliminary grid: 13 group sizes x 11 temperatures x 50 groups = 7,150 runs with GPT-4.1. Each extra member cut the odds of success by about 8% (OR 0.92). Temperature +1 raised the odds about 50% (OR 1.50) (c15, c16). This is the nearest LLM analogue of a complementary pair, though it concerns roles inside one run, not persistence across runs.

**M10. Super-tie definition (Petersen).** For each author, fit an exponential tail to tie strength (papers together, years together). Call a tie "super" if it exceeds an analytically derived threshold K_c. The label depends on the exponential tail assumption: if every tie were one paper, every tie would be super (b07). Implementation: you need a persistent pair log, not just per-call roles.

## 5. What holds up

**Replications and failures.**
- Wu 2019: no independent replication of the team-size result was found. Lin 2023 agrees in direction for distance but comes from the same group. The nearest independent test, Holst 2024, refuted the related Park 2023 time trend. Holst did not rerun team size (d15). Nobody has removed zero-reference entries from Wu's data. Wu's SI uses author fixed effects, topic controls, journal and subfield controls, review exclusion, and reference-based measures, but states no zero-reference filter (d16). The risk is real and unmeasured (K24).
- Lin 2023 counts reconciled. Raw 28% to 22% (papers), 67% to 55% (patents); with full controls 20.4% to 19.5% and 58.2% to 56.5%. The percentile figures (89 to 84, 76 to 67) are a third metric. The controlled effect is small (d14).
- 17% per decade: not reproduced exactly. Papers about 18%, patents about 13% (our arithmetic on d02, d03). Mean 1.9 to 3.5 over about 45 years would give 14-15% per decade (critique.md item 9). Safe range: 13-18%.
- Super ties: 473 careers in two fields, productivity gain 5.2%. The "17%" is a citation boost. Do not confuse with team growth (K26).
- Hao 2025: multipliers confirmed in the arXiv v4 text; after matching on early trajectory the gain falls to +24.45% citations and +9.61% productivity. Causal share unproven (d05, d06).

**Moderators and boundary conditions (human).**
- Fields with conference proceedings (engineering, computer science) are exceptions to the paper pattern (a01 limits).
- Funding does not restore small-team disruption (a05).
- Gap between small and large is larger for high-impact work (b02).
- Topic controls improved model fit by an order of magnitude, so topic matters (a03).
- Team diversity raises paper and citation counts but lowers satisfaction and perceived effectiveness (22 working groups) (b12).
- Nobel laureate careers before the prize look like those of ordinary scientists (b10). Highly cited scientists involve collaborators in new topics (b11).

**LLM replications.**
- Debate: Du 2023's gains (GSM8K 77.0 to 85.0) shrink when baselines are tuned (Smit 2024, Wang 2024, Zhang 2025). A single agent with a strong prompt matches the best discussion method; discussion beats a single agent only when the prompt has no demonstrations (b18). On Claude-3.5-haiku MMLU only AgentVerse beat CoT (+0.85%); others lost by at least 3.60% (c11). Self-consistency usually beat CoT and debate.
- Heterogeneity (resolved in part, d09-d11): Zhang beats the average of two similar models (+6.4% SoM, +8.2% EoT). Li beats the best single model. Different baselines. Quality outweighs diversity in Li's fits. Kim shows family dependence: Anthropic low-capability orchestrator plus high-capability sub-agents scored 0.42 vs 0.32 for all-high (+31%). OpenAI and Gemini degrade under the same mix.
- Ceiling: Kim's 0.45 and Bertalanic's 1/c agree in direction. Both are single-group and preprints. Bertalanic's frontier check is thin (Gemini 3.1 Pro at N=1 only, 97.0% MMLU-Hard, 80.6% GSM-Hard, 88.9% GPQA) (d13).

**Interventions that worked.**
- Task-objective verification step: +15.6% (ChatDev, same model) (d12).
- Role specification alone: +9.4% (d12).
- Sampling and voting: gains scale with size (b15).
- Pre-assignment of tasks reduces coordination messages (a21).
- Persona plus "what will others do" prompt creates complementary roles (c16).
- Human co-pilot checkpoints raised clarity (+0.48) and soundness (+0.35) but lowered significance (-0.3) and contribution (-0.1); co-pilot 4.13/10 vs autonomous 3.8/10, still 1.45 below an accepted-paper average (c22).

**Interventions that did not work.**
- Adding debate rounds beyond about 3 (3 to 10 rounds changed accuracy little) (c09).
- Changing communication mode in homogeneous teams (a19).
- Mixing weaker models into a strong proposer set (b20).
- Any multi-agent topology on sequential planning (-39% to -70%) (c06).
- Splitting a strong single agent (above 0.45) into a team (c05).

## 6. Language models

**Direct tests of team size.**
- Kim 2025: 260 configurations, 6 benchmarks, 5 architectures, 3 LLM families. Gains from +80.8% (Finance-Agent: 0.631 vs 0.349 centralised; decentralised +74.5%) to -70.0% (independent, sequential planning vs 0.568 baseline). Sequential planning: centralised -50.3%, decentralised -41.5%, hybrid -39.1%, independent -70.0%. Workbench -11% to -2%. Tool-heavy tasks (16 tools) lose from coordination cost (beta -0.096, p = 0.002). Non-agentic HumanEval: 89% with five voters (a22, b13, c05, c06).
- MacNet: quality rises with agent count along a logistic curve up to 1,000+ agents; about 2^4 nodes is a reasonable size. No topology wins on every task: HumanEval AgentVerse 0.7256 vs Chain 0.3720; CommonGen Tree 0.7718, Star 0.7382, Chain 0.5903 (c01, c02).
- MultiAgentBench (MARBLE): in a research scenario built from 20 papers with 7 or more authors, overall KPI fell as agents went 1, 3, 5, 7. Coordination score rose from 1 to 3 agents. Cognitive planning raised milestone rate 3% (c14).
- Bertalanic and Fortuna: Ringelmann ceiling. Asymptotes 1/c of about 1.2, 1.8, 1.2 on three tasks. A noise placebo tracked self-correction on free-form math and at 4x scale, so the debate gain is re-evaluation, not peer content (a18, a19).
- Riedl: OR 0.92 per added member (c15).
- Mieczkowski: Amdahl ordering p0.9 > p0.5 > p0.2 (Kruskal-Wallis H = 61.4); serial tasks gain nothing; Claude Sonnet 4.6 alone did not plateau significantly (a20).

**What changed the results, and by how much.**
| Change | Effect | Id |
|---|---|---|
| Add a task-objective verification step | +15.6% success | d12 |
| Better role specification | +9.4% | d12 |
| Heterogeneous model mix in debate (vs average of the two) | +6.4% to +8.2% | c12, d10 |
| Self-MoA instead of mixing models | +6.6 AlpacaEval, +3.8% avg | b20 |
| Sampling and voting, more samples | +12 to +24 GSM8K | b15 |
| Persona plus theory-of-mind line | complementary roles appear | c16 |
| Cognitive planning (MARBLE) | +3% milestone rate | c14 |
| Temperature +1 | odds x1.50 | c15 |
| Central verifier vs none | amplification 4.4 vs 17.2 | a23 |

**Failures (MAST).** Top modes: step repetition 15.7%, reasoning-action mismatch 13.2%, unaware of termination 12.4%, disobey task spec 11.8%, incorrect verification 9.1%. Category shares are inconsistent inside the paper (44.2/32.3/23.5 vs 41.8/36.9/21.3) (c07, d12). Modes 1.3, 1.5, 3.1, 3.2 and 3.3 do not need a second agent, so they can occur in a single chain. No study has coded single-agent scaffold traces with MAST (K28).

**Conformity.** In AgentVerse, about 10% of MGSM errors came from a correct GPT-3.5 agent being talked out of its answer. Not seen with GPT-4 (b23). Zhang 2024 (social psychology of agents): MMLU accuracy ranged roughly 34% to 70% by society and strategy; best strategies start with debate; token cost varied 2.2x (4364 vs 1976). Conformity helps only if agents lean right (c09, c10).

**Research-agent systems.**
- AI Scientist: papers for under $15; automated reviewer F1 0.57 vs humans 0.49, AUC 0.65 both. Failures: hallucinated plot, missing related work, ideas leaking future tokens (c19).
- Co-Scientist: generate-reflect-rank-evolve tournament; Elo of top hypotheses rose across ten time buckets (203 goals); expert ranks: preference 2.36, novelty 3.64, impact 3.09 of 5 on 15 goals; top answer GPQA diamond accuracy 78.4% (b24, c20, c23).
- Virtual Lab: LLM PI plus scientist agents with human feedback designed 92 nanobodies; two showed better binding to JN.1 or KP.3 (b25).
- Agent Laboratory: cost down 84% vs earlier autonomous methods; o1-preview report quality 3.4/5 (c21).
These are role-split pipelines with a selector. Ranking is only safe when calibrated against known answers (c23).

**LLM use inside team science itself.** Hao 2025 used a language-model classifier (F1 = 0.875) to label AI-augmented papers among 41.3 million papers. This is an LLM as a measurement tool, not a test of team behaviour (a17).

**Caveats.** Many results are 2025-2026 preprints (Bertalanic, Mieczkowski, Riedl, Kim) and several use 7B-32B open models. No LLM study tests 17% growth or complementary super-ties directly (K24, c24).

## 7. What our agent should take

The honest summary: the human team literature gives questions, not rules. The LLM team literature mostly confirms existing guardrails.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | Do not split a task into a team by default. Use one thread for sequential reasoning. Parallel subagents only for decomposable work (independent subtasks). | G9, O3 (Decompose) | [E] | a22, b13, c03, c06 (K09) |
| A2 | Keep G9 (no debate). Debate does not beat self-consistency at equal compute. | G9 | [E] | b16-b19, c11 (K12) |
| A3 | Prefer N samples of the single best model with code-side selection over mixing weaker models. | S3, G4 | [E] | b15, b20, c13 (K13) |
| A4 | Homogeneous samples saturate. Do not expect extra same-model samples to add diversity beyond a small N. Count distinct answers, not agreement. | G4 | [E] | a18, a19, c15 (K18) |
| A5 | Pre-assign work by code in any parallel step. Do not let subagents self-coordinate. | G1, S3 | [E] | a20, a21 (K17) |
| A6 | Add stop and termination rules, and a check against the stated task spec, because most team failures are design and coordination failures. | G6, S8 | [E] | b21, c07 (K15) |
| A7 | Do not let an attempt be talked out of a correct answer by unsupported pressure. Revise only from real output. | G2 | [E] | b23, c17, c10 (K19) |

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Add an external task-objective verification step at S8, run in code with a fresh context. Largest measured fix (+15.6%). | S8 | [S] | d12 (K16, K28) |
| T2 | Role specification text in S1/S3 prompts (+9.4% in ChatDev). | S1 | [S] | d12 (K16) |
| T3 | Skip branching when the class's plain pass rate exceeds about 0.45 on a branching-hostile class; branch when low. Extends G12. | S0, G12 | [S] | c05, d08 (K10) |
| T4 | Diverse isolated restarts then merge vs a single deep chain at equal tokens, for novelty. (Mirrors "small teams disrupt".) | S3 open mode | [S] by analogy | a01, a04 (K01); gap 3 in critique |
| T5 | Seed some restarts from old or distant material, others from the latest best attempt, and compare novelty. | S3, O7 | [S] by analogy | a04 |
| T6 | Persistent complementary roles (writer plus critic with a stable pair log) vs fresh roles each call. Super-tie analogue. | memory | [S] | a06-a08, c15, c16 (K05) |
| T7 | Share full context vs summaries only between sub-attempts, for novelty (the remote-team analogue). | G4, S3 | [S] | a14, a15 (K07) |
| T8 | Code our own traces with MAST modes 1.3, 1.5, 3.1, 3.2, 3.3 and add rules for the commonest. | G-verify | [S] | d12 (K28) |
| T9 | Add a "think about what the other roles will do" line when roles are used. | S3 | [S] | c16 |
| T10 | Add a central verifier when running independent parallel samples; verify code-side. | G5, S7 | [S] | a23, b14 (K11) |
| T11 | Guard against narrowing: keep exploration wide when one retrieval tool or one chain dominates. | G10, S3 | [S] | d05, d06 (K21) |

[C] items (not added, no test): network topology choice (K20); model heterogeneity (K14); super-tie benefit (K06). Heterogeneity is mostly a quality-gap and baseline effect, so for a single-agent scaffold, the safe reading is "restart the best model".

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens, same item sets, 3 seeds, setup cost counted (G7). Use NoveltyBench items for novelty, ARC and BRAINTEASER for accuracy.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 (T4) | NoveltyBench open prompts | (a) one deep chain; (b) N isolated restarts from bare task + code merge | distinct-answer count; quality-filtered novelty | b above a by at least 1.0 distinct answers; no quality loss (from our existing 3.18 to 9.63) |
| B2 (T5) | NoveltyBench | (a) all restarts from bare task; (b) half from old/distant analogue | novelty and quality | small gain in novelty, wider spread (O7 note: distant sources lower the average) |
| B3 (T1) | ARC, BRAINTEASER | (a) S8 verify on unfitted part; (b) plus task-objective check in fresh context | accuracy; flips right to wrong | +3 to +10 points if +15.6% partly transfers |
| B4 (T6) | Role-based sub-tasks (draft + critique) on open items | (a) persistent writer/critic pair with log; (b) fresh roles each call | accuracy; novelty | unknown; null likely |
| B5 (T3) | Mixed-difficulty ARC | (a) always branch; (b) branch only when plain pass rate below 0.45 | accuracy per token | b higher at equal tokens; confirms G12 |
| B6 (T7) | Open items | (a) restarts see full context; (b) restarts see a summary | novelty | b more novel (small, as in Lin's controlled 1-2 points) |
| B7 (T8) | Our own traces | code with MAST modes 1.3, 1.5, 3.1, 3.2, 3.3; add stop/verify rules | rate of each mode before and after; accuracy | mode rate falls by half |
| B8 (T10) | Parallel samples | (a) samples + vote; (b) samples + one verifier | accuracy; error amplification | b amplification near 4.4 vs 17.2 pattern |
| B9 (A5) | Parallel subtask steps | (a) self-claim; (b) code pre-assignment | duplicated work count | duplicates near zero in b |
| B10 (A7) | Items with injected wrong feedback | plain vs "revise only from real output" rule | flip rate | lower flip rate |

## 9. What does not transfer, and why

- **Authorship counts.** Team size here means co-authors on a paper, a social and credit fact. Our agent has no co-authors, no careers and no credit.
- **Citation outcomes.** Citations measure reception, not correctness or novelty. Disruption (CD index) is a fragile proxy (Holst, a16).
- **Growth per decade.** A 13-18% growth in author counts has no meaning for a single-agent loop. It reflects burden of knowledge (Jones) and funding structures. Our agent's "knowledge" fits in a context window.
- **Super ties.** Repeated coauthorship builds trust, reputation spillover and shared language across years. An LLM gets none of these unless we build a persistent pair log. Even then the "tie" is a prompt, not a relationship. The human effect is small (5.2%) and contested (b09).
- **Remote work.** Distance matters because of travel, time zones and informal talk. For LLMs the analogue is context sharing, not kilometres.
- **Selection effects.** Part of the human effect is sorting of people into teams (one third in Wu). Our agent has no sorting.
- **Observational design.** All human findings are correlational. They cannot support causal rules for design.
- **Open-model ceilings.** Ringelmann ceiling values come from 7B-32B models and may not carry to frontier models (d13).
- **Debate-style teams.** Directly forbidden by G9.

## 10. Open questions

1. Does Wu 2019 survive removal of zero-reference entries? Nobody has rerun it (gap 1).
2. What is the exact 17% per decade, over which years and fields? Wuchty body text unread (gap 2).
3. At equal tokens, do diverse restarts plus a merge beat a single deep chain on novelty? No LLM study measures disruption-like novelty against team size (gap 3).
4. At what single-agent accuracy does branching stop helping for frontier models? Kim's fit includes frontier models, but no sweep varies one frontier model (gap 4).
5. Does persistent complementary role pairing beat fresh roles per call? No study (gap 5).
6. Which MAST modes appear in single-agent scaffold traces (gap 6)?
7. How much of Hao's gain is causal rather than selection (gap 7)?
8. Is the Ringelmann ceiling reproduced by an independent group on frontier models (gap 8)?
9. Is the remote penalty replicated outside Wu's group (gap 9)?
10. Why do heterogeneous debate and heterogeneous mixing differ? Mostly baseline and quality gap, but family effects (Kim) are unexplained (gap 10).
11. Do the MAST category shares (44.2/32.3/23.5 vs 41.8/36.9/21.3) reconcile?
12. Smit 2024 and Wang 2024 exact scores were not extracted.

## 11. Sources

[V] = opened and read this session. [M] = snippet or recall only.

- [V] Wu, Wang, Evans 2019, Large teams develop and small teams disrupt. https://arxiv.org/abs/1709.02445 ; https://www.nature.com/articles/s41586-019-0941-9
- [V] Petersen 2015, weak, strong and super ties. https://arxiv.org/abs/1509.01804 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC4553788/
- [V] Milojevic 2014, team formation. https://arxiv.org/abs/1403.2787
- [V] Milojevic 2015, cognitive extent of science. https://arxiv.org/abs/1511.00040
- [V] Lariviere et al. 2015, Team size matters. https://arxiv.org/abs/1410.8544
- [V] Lin, Frey, Wu 2023, Remote collaboration. https://arxiv.org/abs/2206.01878 ; https://www.nature.com/articles/s41586-023-06767-1
- [V] Holst et al. 2024, dataset artefacts. https://arxiv.org/abs/2402.14583
- [V] Park, Leahey, Funk 2023. https://www.nature.com/articles/s41586-022-05543-x
- [V] Hao, Xu, Li, Evans 2024/25, AI and science. https://arxiv.org/abs/2412.07727
- [V] Fortunato et al. 2018, Science of science. https://pmc.ncbi.nlm.nih.gov/articles/PMC5949209/
- [V] Jones 2009, Burden of knowledge. https://www.kellogg.northwestern.edu/faculty/jones-ben/htm/BurdenofKnowledge.pdf
- [V] Wuchty, Jones, Uzzi 2007, abstract only (body paywalled). https://doi.org/10.1126/science.1136099
- [M] Guimera, Uzzi, Spiro, Amaral 2005. https://doi.org/10.1126/science.1106340
- [V] Strong ties in international collaboration. https://pmc.ncbi.nlm.nih.gov/articles/PMC9844855/
- [V] Strength of weak ties (DBLP). https://pmc.ncbi.nlm.nih.gov/articles/PMC8948253/
- [V] Nobel laureate careers. https://pmc.ncbi.nlm.nih.gov/articles/PMC7211484/
- [V] Collaborators and new topics (PNAS). https://pmc.ncbi.nlm.nih.gov/articles/PMC9388131/
- [V] Specht and Crowston 2022. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0278043
- [V] Kim et al. 2025, scaling agent systems. https://arxiv.org/abs/2512.08296
- [V] Cemri et al. 2025, MAST. https://arxiv.org/abs/2503.13657
- [V] Bertalanic and Fortuna 2026, Ringelmann. https://arxiv.org/abs/2606.02646
- [V] Mieczkowski et al. 2026, distributed systems. https://arxiv.org/abs/2603.12229
- [V] Riedl 2026, emergent coordination. https://arxiv.org/abs/2510.05174
- [V] Li et al. 2024, Agent Forest. https://arxiv.org/abs/2402.05120
- [V] Du et al. 2023, multiagent debate. https://arxiv.org/abs/2305.14325
- [V] Smit et al. 2024, Should we be going MAD. https://arxiv.org/abs/2311.17371
- [V] Wang et al. 2024, multi-agent discussions. https://arxiv.org/abs/2402.18272
- [V] Zhang et al. 2025, Stop overvaluing debate. https://arxiv.org/abs/2502.08788
- [V] Li et al. 2025, Rethinking Mixture-of-Agents. https://arxiv.org/abs/2502.00674
- [V] Qian et al. 2025, MacNet. https://arxiv.org/abs/2406.07155
- [V] Chen et al. 2023, AgentVerse. https://arxiv.org/abs/2308.10848
- [V] Zhang et al. 2024, collaboration mechanisms. https://arxiv.org/abs/2310.02124
- [V] Zhu et al. 2025, MultiAgentBench. https://arxiv.org/abs/2503.01935
- [V] Lu et al. 2024, The AI Scientist. https://arxiv.org/abs/2408.06292
- [V] Gottweis et al. 2025, AI co-scientist. https://arxiv.org/abs/2502.18864
- [V] Schmidgall et al. 2025, Agent Laboratory. https://arxiv.org/abs/2501.04227
- [V] Swanson et al. 2025, Virtual Lab. https://www.nature.com/articles/s41586-025-09442-9
