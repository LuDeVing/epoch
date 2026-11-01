# Expert-novice differences: deep document

Subfield E08.02 of troubleshooting and fault diagnosis. Row in SUBFIELDS.md: "Experience and schemas. Key works: Gott; Rasmussen. Agent link: Memory; S0."
Evidence ids (a01-a28, b01-b25, c01-c24, d01-d21) and claim ids (E08.02-K01 to K33) refer to the files in this folder. Critique caveats are folded in.

## 1. What it is

This subfield asks what skilled fault-finders have that beginners lack, and whether that can be written down and handed over.

The human answer, from 40 years of avionics and electronics studies, is narrow and consistent:

- Experts hold an accurate model of how the system works (a01, a09).
- From the first symptom they build a small, correct space of possible faults (a03).
- They split the right space with cheap, well-chosen tests (a08, a09).
- They do not swap parts before testing (a14).
- They are not better at running tests, and they do not know more theory in a way an exam catches (a04, a06).

The machine answer, from 2025-2026 benchmarks, is that strong coding agents are novices in the same ways. They anchor on the loudest anomaly (b02, b06, d12). They fail on new fault types (b08). They give right answers with no grounded evidence (c17, a24). They lose a lot when system knowledge, such as source code, is removed (b03).

What this means for one agent with a scaffold: the schema should hold system-specific structure and distilled strategy, not a persona and not a longer list of generic rules. Stored experience must be gated before it is trusted.

Scope notes. Chunking, recognition-primed decisions, mental models, model-based diagnosis, Sherlock-style training systems and fault localisation are covered in sibling subfields. Here we cover only what the expert-novice contrast says about memory and S0.

## 2. History and theories in depth

### 2.1 Rasmussen: skills, rules, knowledge (1974, 1983)

- Rasmussen and Jensen (1974) studied electronic technicians in real jobs. They described search strategies: topographic search (walk the signal path, good point to bad point), symptom-based search (match the pattern to a stored fault), and exhaustive or trial-and-error search. Technicians mixed them. This paper was not opened (b19, [M]). Johnson's 1995 review cites it for topographic search (a18).
- Rasmussen (1983) gave three levels of control: skill-based (signals, automatic), rule-based (signs, stored if-then rules that can be stated), knowledge-based (symbols, a mental model, slow, used when the first two fail). Fault diagnosis is the standard knowledge-based example. The skill/rule boundary is not sharp and moves with training (a17, from a web summary, not the IEEE paper).
- Johnson (1995): people choose topographic, exhaustive and trial-and-error searches because they need little thinking effort (a18).
- Status: a framework, hard to falsify (b20, [M]). Useful as a design gate, not as a tested law.

### 2.2 Johnson (1987): the generator-set studies

Study 1: 5 novices (about 0.5 year on generator sets) and 5 experts (over 10 years). Experts knew principles and system function much better. They were more accurate at tracing the battery, ground and AC circuits on schematics. Novices lacked an accurate model of equipment they repair daily (a01).

Study 2: think-aloud on two rare faults.

- Experts: 5 of 5 on both.
- Novices: fuel pump 3 of 5, open wire 2 of 5.
- Cutoff 45 minutes. Only 1 of 5 failures hit the limit, so novices mostly gave up (a02).
- Open-wire (electrical) task: experts about 5 times faster.
- Fuel-pump (mechanical) task: novices who solved it were faster than experts. Novices had mechanical but not electrical experience, so expertise is domain-bound.

Qualitative findings: experts read more from the first symptom. For example, Expert 1 inferred the battery, fuse and board were good from the fuel pump clicking. Novice 1 said only "I get nothing, I am just going to look around" (a03). Experts chose technical tests, novices chose sensory checks (sight, sound, smell, touch). Skill at running the chosen test did not differ (a04).

Limits: 5 vs 5, two problems, factory staff vs trainees (role and experience mixed). No replication found (critique).

### 2.3 Johnson (1995) and Johnson et al. (1993): styles and theory

A review of over fifty troubleshooters over eight years (a05).

- Five strategies: trial and error, exhaustive, topographic, half-split, functional.
- Strategy type did not separate high from low performers. Range did. Low performers were strategy-bound. Skilled ones used several and even went back to trial and error when stuck.
- Theory did not predict skill. Systems exam in a student avionics course: high performers 19.82 (SD 1.94), low performers 19.88 (SD 2.13), t(32)=0.073 (a06). About 34 students, so absence of a difference is not proof of none.
- Both groups kept their first frame and rarely checked other subsystems, even when cued (a07). Anchoring hits experts too.
- Training formats: concept maps raised behavioural understanding (U=2.50, p<.01) but not structure knowledge. Flow diagrams gave more expert-like knowledge maps (t(82)=-4.705) (a07).

### 2.4 Lesgold, Gott, Katz: Sherlock and Hydrive

- Task analysis of Air Force test-station repair: an expert solved the sample problem in 7 steps, trainees in 14 and 20. Experts split the space. Trainees traced circuits end to end. What differs is which space gets split (a08).
- The station breaks about once a month. Routine work is about 95% of the job, so novices rarely practise the hard 5% (a08).
- Steinberg and Gitomer (1992), PARI analysis of F-15 hydraulics technicians, list seven differences (a09): attend to physical clues; explicit accurate mental models; procedural expertise such as disabling systems to rule out areas; hierarchical functional classification of components; knowledge of failure characteristics; flexible strategy with space splitting; cost/benefit awareness. Novices are limited to remove-and-replace.
- Katz et al. (1997): three knowledge types (conceptual, strategic, procedural). Procedure did not separate experts from novices in hydraulics. Strategy and system knowledge did (a10).
- Gott et al. (1992, ten years of fieldwork): good learners used existing device models and a task schema as flexible blueprints for a new system. Weak learners over-simplified and over-generalised old structures and acted like novices (a15).

### 2.5 Other founding work (not opened)

- Chase and Simon (1973), chess recall: masters recall real positions far better, but the gap shrinks on random boards. Numbers not checked; primary text blocked (a27, d21, [M]). Do not cite figures.
- Chi, Feltovich and Glaser (1981), physics sorting: experts sort by deep principle, novices by surface (a28, b23, [M]).
- Gugerty and Olson (1986): expert programmers debug faster, novices add new bugs (b22, [M]). Another subfield.
- Kalyuga et al. (2003) expertise reversal; Macnamara et al. (2014) deliberate-practice meta-analysis (b24, b25, [M]). Both are boundary conditions on "more experience gives more skill" and on "give the novice instruction". Sibling subfields.
- Gott, Bennett and Gillett (1986), de Kleer and Williams (1987): early AI models of competence and multiple-fault diagnosis. Not opened (c21, c23, [M]).

### 2.6 Competing explanations

- Schema/model view: experts know the system (Johnson 1987, Gott).
- Strategy view: experts split the right space (Lesgold).
- Pattern store view (chunking): experts recall many cases (Chase and Simon). Contested here because the primary text is unopened (K24).
- Knowledge-type view: strategic and system knowledge, not procedure and not theory, separate groups (Katz).
- Strategy flexibility view: range of strategies, not type (Johnson 1995). This conflicts in part with Gott 1995, where violations of logical sequence separate groups (a14). Possible reconciliation: range versus sequence quality. Open.

## 3. Core findings with exact numbers

Status key: established (at least 2-3 independent sources agree), single-source, contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Experts find rare faults novices miss | Experts 5/5 on both; novices fuel pump 3/5, open wire 2/5; 45 min cutoff; N=5 vs 5 | a02, Johnson 1987 | single-source (K01) |
| Experts build a correct starting space from the first symptom | Qualitative: most expert checks inside true space; novices often outside | a03, a08, a09 | established (K02) |
| Experts halve the right space; trainees trace end to end | Expert 7 steps; trainees 14 and 20 | a08 (one worked example) | established (K03), weak numbers |
| Theory knowledge does not predict skill | Exam 19.82 vs 19.88 (max 24), t(32)=0.073 | a06 | established as direction (K04); partly conflicts with a01 |
| Strategy range, not type, separates | Over 50 troubleshooters, no counts | a05, a07 | single-source (K05) |
| Test skill is the same; test choice differs | No counts in surviving text | a04 | single-source |
| Sherlock lifts novices to master level on trained tests | VTT3: control 59 (SD 37), tutored 95 (5), masters 85 (12). VTT4: 58, 91, 86. NIT: 75, 87, 86. Effect 1.27, 1.17, 0.87 SD. N=23/18/13 | a12 | established (K07), developer data |
| Transfer to a new station (Frankenstation) | VTT 55 (31) vs 82 (23), 0.96 SD, p=.006. NIT 72 vs 80, 0.76 SD, p=.025. Solve rate 63.6/70.6/83.3% (control/tutored/masters). N=21/17/12 | a13 | established (K07) |
| Premature swapping marks novices | Swaps with no test: control 50, tutored 3, masters 8. Self-test used badly: 11/16, 4/12, 2/14. Sequence violations 21, 9, 20 | a14 (Frankenstation, event counts) | single-source (K06) |
| Gains persisted | 16 tutored airmen, about 28 months experience, 20 h tutoring, retest at 6 months, gains held | a16 (abstract only) | single-source |
| Strategy tutor beat procedure tutor | Hydrive pre/post t(19)=4.14, p<.001; others not significant. Within-group, not between-group | a10, d16 | single-source (K08) |
| Field samples are small and from the developers | Tutored 18, untutored 23, masters 13; t[39]=-4.04, -3.72; Frankenstation t[36]=-2.93 | a11, d17 | caveat (K31) |
| LLM agents fail on realistic faults | ITBench SRE 13.8% (94 scenarios, 2024 models). ORCA-bench best 25.3% Medium, 10.0% Hard; strict 30.9% (Sonnet 4.6) on 884 incidents. Cloud-OpsBench joint accuracy 0.76 / 0.68 | a23, b09, b01, a24 | established (K09) |
| Right answer, no grounded path | OpenRCA 2.0: any correct service 76.0%, grounded path 61.5%, exact set 20.7%, Node F1 62.2% vs Edge F1 43.4%. Cloud-OpsBench evidence closure 0.38 / 0.15 | c17, d10, a24 | established (K10) |
| Evidence closure reorders models | Conditional grounding about 91% (Qwen3.6-Max) vs about 66% (Sonnet 4.6) at comparable F1 | d11 | single-source (K29) |
| Agents anchor on first or loudest anomaly | SREGym diagnosis 72.6 to 62.6 (Claude Code), 70.0 to 59.3 (Codex), 61.5 to 51.5 (Stratus). Incorrect runs 3.29 coded failure modes vs 0.71 in correct runs | b06, d12, d13, b02 | established (K11) |
| System knowledge is a lever | ORCA-bench: no source code cuts RCA 9-16 pts, hallucination up for all. Context cut: down 19-50 pts. GALA graph: AC@1 74.44% vs 48.35% best prior and 21.35% GraphRAG | b03, b04, b10 | established (K12) |
| Novel fault types collapse performance | SREGym E2E 63.7 to 17.9 (Stratus), 60.8 to 28.2 (Claude Code), 57.8 to 15.4 (Codex) | b08 | established (K15), difficulty confounded with novelty |
| Pattern-matched fixes work without diagnosis | Mitigation succeeded 22-62% after wrong diagnosis; 3.82 attempts vs 1.88 (no-noise condition only) | b07 | single-source (K13) |
| Right diagnosis does not give right repair | R2Act: RCA service 91.4-99.7% vs recovery validity 36.8-60.3%. Of 755 invalid plans: 67.9% wrong operation, 29.7% invalid structure, 1.3% wrong target. Gold RCA plus fixed mapper 0.599. Live replay 48.3% (146/302) | c18, d08, d09 | single-source (K14, K28) |
| Distilled experience beats raw traces | A@1: harness 59.0, no-evolve 41.4, ICL (3 raw rollouts) 38.4, bare 36.1. Tokens 106k / 106k / 112k. Cold-start +5.3, self-evolution +17.6 | c02, c03, c05, d03 | contested (K16, K27) |
| Memory writes need a gate | Final-window A@1 0.83 full, 0.43 no-evolve, 0.33 no-verify. 37% of proposals rejected; 1.7 attempts. Trace2Policy bypass fell to 66.8 / 67.5 | c04, d02, d07 | established (K17, K26), sizes small |
| Unrefined rules can hurt strong models | Opus 82.7 zero-shot vs 74.1 with v1 rules; Haiku 84.2 vs 77.0; weak Kimi +22.8. Not diagnosis | d06 | single-source |
| Open adaptive investigation beats rigid pipelines | Top 3 frameworks 77.6-79.6 Acc@1, span 2.0 pts; mABC 42.6; bare general agents beat hand-built RCA agents (36.1 vs 17.9 vs 5.6) | c06, c01, c13 | established (K18) |
| More rounds and more effort do not help | Failed runs up to 11.4 more rounds; effort +2-4 pts at 1.5-4x time | c08, c14 | established (K19) |
| Small evidence guard helps | DiagGuard Acc@1 up in 14/14 configs, median +10.5 (range 3.5-35.1); tokens not matched | c10, d14 | single-source (K20) |
| Expert persona does not help | 162 personas, 4 model families, 2,410 factual questions, no gain; best persona unpredictable | a22, d18 | established for facts; untested for diagnosis (K21, K32) |
| Expert-behaviour notes from an LLM beat expert-written notes | Study 1 F(5,605)=35.01; Study 2 100 novices/condition, gap 0.843 to -0.088 (CI -0.784 to 0.607) | a19, d19 | single-source (K23), tutoring task |
| Single agent matched multi-agent | 2 scenarios, 6 practitioners, 120 runs, no consistent quality difference | c20 | established as weak (K25) |
| Structured LLM help for novices in hardware debugging | 65.48 vs 34.21 (N=15, t(38)=2.73); sensor task 25% to 100%; I2C address wrong 38%, register hallucinated 100% on one task | b17, b18 | single-source, small |

## 4. Mechanisms and models

### 4.1 The expert loop, as steps

1. Read the first symptom for what it rules in and out (a03). Output: a small candidate set.
2. Classify components by function, not by swappable unit (a08, a09).
3. Use failure priors: which parts fail how often and how (a09).
4. Pick the test with the best split per cost, not the nearest or easiest (a09: cost/benefit awareness).
5. Split the remaining space by function. Switch strategy when stuck (a05).
6. Verify the fault before changing anything (a14).
7. Stop when the fault is localised and confirmed.

Implementable as: a typed device model (components, functions, links) plus a failure-prior table plus a test catalogue with costs. The agent chooses the next test by expected split per cost. Code can compute split size from the model. The model proposes, code ranks (G5).

### 4.2 Rasmussen as an S0 gate (a17, a18, d15)

- Rule level: match symptom to a stored rule or case. Cheap.
- Knowledge level: reason from the device model. Slow. Entered only on failed match.
- Rule: default to the recalled rule. Allow an override only after a named conflict check on raw evidence (K30).
- Reason: Luo et al. found a tool candidate right in over 80% of trajectories. Agents that gathered more evidence sometimes dropped it. Overrides outnumbered corrections in every configuration. Raw-metric checks helped (corrections 2.7% to 5.3%). Competing analysis hurt (overrides 9.3%) (d15). Qwen3-32B overrode nearly a third of correct candidates. One model family only.

### 4.3 Schema adaptation, not copying (a15)

A retrieved case has device-specific parts and reusable parts. Store both and mark which is which. A learner who copies the device-specific parts into a new system acts like a novice. Store the case as: symptom pattern, function-level cause, device-specific details tagged as such.

### 4.4 Memory as distilled expertise with a write gate (c02-c05, d01-d07)

OpsHarness design, in implementable form:

1. Mine past runs (success and failure) into artifacts: workflow skeleton, operation skill, note-rule, persisted tool.
2. Test each proposed change in a sandbox copy.
3. Inner gate: no accuracy loss and no cost rise on the source cases, with a strict gain in at least one. Cost tolerance 0.05.
4. Outer gate: no regression on a held-out testbed, re-sampled before each evolution, disjoint from mined cases, stratified by fault family.
5. Up to 3 refine-and-retry rounds, then discard.

Artifact use (Table III, d04): workflow skeleton 6 items, recall 91.7%, precision 73.5%. Operation skill 19, 82.5% / 84.3%. Note-rule 21, 64.7% / 85.1%. Persisted tool 11, 61.0% / 77.2%. Coarse artifacts fire broadly. Fine rules fire rarely and precisely. These are descriptive co-occurrence numbers, not causal.

Failure example: the evolver up-weighted network anomalies after network faults. That mislabelled CPU and memory cases that were right before (c04, d02). Weak models mine spurious patterns more.

Trace2Policy (d05-d07) is a second source: one-shot distillation plateaus near 70%. Eight error-clustered patch rounds, each kept only if it passes a gate, reach about 79%. Rollback if validation drops more than 2%. Per-round accuracy is not monotonic (round 5 crash 90 to 70). Logistics audit, not diagnosis.

### 4.5 Evidence closure (c17, d10, d11, a24)

Score or require a verified causal path from root cause to symptom, not only the named cause. Compute closure in code: does every link in the claimed path have an observed output? This is G2 and G10 applied to diagnosis.

### 4.6 Anti-anchor guard (c10, d12-d14)

Rule-based checks, run by code or a short fixed prompt:

- Was any piece of evidence omitted from the verdict?
- Was any evidence misread? Silence read as health (30% of the Sonnet failure pool in one table).
- Is any claim unsupported by an output?
- Search-space profile before the investigation (the "Grounder").

DiagGuard raised Acc@1 in 14 of 14 configs. Median +10.5. But arms were not token-matched and the same group built the taxonomy and the fix, so treat as unproven at equal tokens.

### 4.7 Typed repair (d08)

Before any repair action, check that the operation fits the diagnosed fault type and the plan has valid structure and a target. This targets the main repair failure (wrong operation 67.9%).

## 5. What holds up

### 5.1 Holds up

- Expert-novice differences are in system model, problem-space construction and test choice, not in procedure, theory or test-running skill. Three or more sources agree (K02, K03, K04). All human evidence is from avionics-style tasks and one generator study.
- Machine analogues agree in direction: agents without system knowledge (no source code, no graph) do worse. Three sources (K12).
- Agents are weak on realistic faults and worse on novel ones. Four sources (K09, K15).
- Final-answer scores overstate diagnosis. Three sources (K10).
- Memory without a gate decays. Three sources (K17, K26).
- A bare strong agent beats hand-built diagnosis agents. Four sources (K18).
- More rounds or effort do not buy accuracy (K19).

### 5.2 Weak or contested

- No independent replication of Johnson 1987 or Gott 1995 was found. The search was limited: the quota ran out, and arXiv, OpenAlex and Semantic Scholar returned 429 (critique). Treat "not found" as "not searched", not "does not exist".
- Sherlock data come from the developers. Tutored groups got feedback. Tests were partly built from the same task analysis as the tutor. Control SD is large (37). Tutored novices scored above masters on trained tests.
- Johnson 1987 says experts know principles better. Johnson 1995 says theory does not predict skill. Different samples (workers vs students) and different measures.
- Strategy type versus strategy range versus sequence violations: unsettled (section 2.6).
- Masters made more sequence violations (20) than tutored (9). So logical sequence is not a clean expert marker (a14).
- Chunking and pattern-store view: primary texts unopened (K24, K33).
- Hydrive vs F-15 tutor differ in developer, task analysis method and content. The t(19)=4.14 is a within-group test (d16). No component ablation exists in any Sherlock/Hydrive document (K31).

### 5.3 Moderators and boundary conditions

- Domain match: novices beat experts on the mechanical fuel-pump task (a02).
- Fault depth: for weaker agents, accuracy falls with causal-chain depth (89.5 to 57.1 from depth 2 to 5). Strong Sonnet ThinkDepth stayed flat (85.7 to 96.8) (c07).
- Model strength: cold-start expertise helps weak models most (DeepSeek-V4 20.3 to 31.6; GPT-5.5 51.2 to 52.8) (c03). Unrefined rules can hurt strong models in a non-diagnosis task (d06).
- Noise: about 10 points off diagnosis for every agent (d12).
- Input context: cutting it costs 19-50 points (b04).
- Same system versus new system: OpsHarness gains are in-system (time-split on the same systems), not cross-system (c02, d03).
- Tool level: higher-level tools save time but can hurt a model that rarely uses them (Qwen3-8B) (c19).

### 5.4 Interventions that worked and did not

Worked:
- Coached practice on an expert-derived task analysis (a12, a13).
- Distilled strategy artifacts with a gate (c02, c04).
- A dependency graph bounding exploration (b10).
- A small evidence guard (c10).
- Structured LLM help for human novices in hardware debugging (b17).
- Expert-behaviour-derived guides in tutoring (a19).

Did not work or hurt:
- Expert persona prompts on factual QA (a22).
- Raw retrieved cases (ICL) beyond the bare agent: 38.4 vs 36.1 (c03).
- Ungated self-evolution (c04).
- Adding competing analysis to a tool candidate (d15).
- More rounds, more effort (c08, c14).
- Rigid pipelines and hand-built agents (c06).
- A rigid three-step structure for the notes (d19).
- Multi-agent orchestration, with no consistent quality gain (c20).
- GraphRAG: 21.35% AC@1 despite the most tokens (b10).

## 6. Language models

### 6.1 Baseline behaviour

- 2024-era models on ITBench: SRE resolved 13.8%; GPT-4o diagnosis pass@1 13.81%, mitigation 11.43%. Without traces: diagnosis 9.52%, mitigation 2.86% (a23, b09).
- 2026 frontier agents on ORCA-bench (1,079 tasks, 50 GB telemetry): best 25.3% Medium, 10.0% Hard. On 884 incidents best strict accuracy 30.9% (Sonnet 4.6), best partial depth 48.8% (GPT-5.5). Weakest model invents an implausible cause in 40% of reports. 26-40% of telemetry calls error or return empty (b01, b05, c11).
- Verified subset (32 tasks): Fable 5 depth 58.2 +/- 5.8, accuracy 40.6 +/- 8.8 (b01).
- Cloud-OpsBench: 754 cases, 57 fault types, 10 agents; joint accuracy 0.76 (Online Boutique) and 0.68 (TrainTicket); evidence closure 0.38 and 0.15 (a24).
- RCABench trajectories: Claude Code 79.6 Acc@1; Sonnet ThinkDepth 90.0 (+10.8 over Qwen) (c06).
- RCAtlas (90 cases): simple harnesses PR@1 65-77% on mid-tier models; published LLM agents 16-53%; non-LLM 6-39% (c13).
- Fault localisation in novice programs: Codeflaws Top-1 at Lv5 vs Lv1: o3 44 vs 64; GPT-4 35 vs 65; GPT-3.5-Turbo 27 vs 55. Over-reasoning hides the fault line (b12, b14).

Numbers are not comparable across benchmarks. Each uses a different system, metric and model set.

### 6.2 Novice-like failure modes

- Anchor lock, salience bias, loudest-anomaly bias (b02, d12, d13). Incorrect runs show 3.29 coded modes vs 0.71 for correct runs.
- Silence read as health (c10).
- Unsupported reasoning and invented components (b11).
- Looping on a few moves: Qwen acts on the prior result in 24.9% of rounds vs 54.3% for Sonnet. Sonnet runs resource_probe in 82.8% of trajectories vs 16.6% for Qwen. Resource-fault accuracy 75% vs 94%; JVM code 66% vs 93%; HTTP 88% vs 87% (c09).
- Dropping a correct tool candidate after gathering more evidence (d15).
- Wrong repair operation after a right diagnosis (d08).
- Hallucinated domain facts (b18). In hardware debugging, models are overconfident: one claimed 99% confidence on wrong op-amp pins (c16).

No study compares agents against human experts on the same faults (critique). "Novice-like" is inferred from failure modes.

### 6.3 What changed behaviour, by how much

| Change | Effect | Source |
|---|---|---|
| Dependency graph bounding exploration | AC@1 74.44% vs 48.35% | b10 |
| Source-code access | +9-16 pts RCA | b03 |
| Self-evolved harness | +22.9 pts (+5.3 cold start, +17.6 evolution) | c02 |
| Gate on memory writes | 0.83 vs 0.33 final window | d02 |
| Evidence guard | median +10.5 Acc@1 | c10 |
| Free-to-look simple harness | 65-77% vs 16-53% | c13 |
| Stronger model | +14-18 PR@1 | c14 |
| Multi-turn loop | solves 10-11 pts more cases at least once | c14 |
| More reasoning effort | +2-4 pts at 1.5-4x time | c14 |
| Expert persona | none | a22 |
| 3 raw correct rollouts in prompt | +2.3 pts (38.4 vs 36.1) | c03 |

Notes:
- The multi-turn result conflicts with Laban et al. (2025), who found multi-turn costs reliability. Laban was not read (c24). Task types differ.
- Experience gains are smallest on the strongest model at cold start (GPT-5.5 +1.6) (c03).
- Same content as Python rules vs as a prompt: +9.8 points as Python (Trace2Policy, logistics) (c15). This supports G5.
- Single agent matches multi-agent (c20).

### 6.4 LLMs simulating novices

GPT-4.1 playing a student is too coherent, too long and overconfident, and overestimates learner success. Richer context made it worse (+0.14, Welch t=5.01, p<.001). A 7B open model replicated it (a21, d20). So an LLM cannot be run as a novice by persona. Expert-novice arms must differ by information given, not by role.

## 7. What our agent should take

Status key: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | Do not use expert persona prompts. Already covered by G4. Keep persona out of S0 and memory | none (not to add) | [E] for facts | a22, d18, K21 |
| A2 | Memory writes pass a gate: no regression on the source cases and none on a fresh held-out set stratified by problem family. Weak models are most at risk. Fits G7 | memory write | [E] | c04, d01, d02, d05, d07 (K17, K26) |
| A3 | Store distilled, tagged lessons, not raw past episodes. Established against raw traces only, not against no text (see T1) | memory | [E] vs raw traces | c03, d03, K16 |
| A4 | In diagnosis items, require a grounded evidence path before accepting a cause: each link in the claimed path points to an observed output. Same as G2 and G10 | G (evidence) | [E] as a diagnosis of weakness | c17, d10, a24 (K10) |
| A5 | Keep the scaffold light and free to look: open adaptive investigation over rigid pipelines | structure | [E] | c06, c01, c13, K18 |
| A6 | Do not raise effort or rounds hoping for gains. Cap steps and compare accuracy per token. Fits G11 | G11 | [E] | c08, c14, K19 |
| A7 | When a problem class has a usable system model (source, graph, schema), give it to the agent; log whether a model was present | memory/S0 | [E] direction | b03, b10, c12, K12 |
| A8 | Report novel-versus-familiar splits in every bench. Expect a large drop on novel items | bench design | [E] | b08, K15 |
| A9 | Log repair success separately from diagnosis success | run log | [E] direction | c18, K14 |

### Test first (single-source or contested)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Distilled strategy text vs no text vs raw traces on novel fault families | memory/S0 | [C] | c02, d03, d06, K27 |
| T2 | Forced "what do the symptoms rule out" before any test (build the problem space) | S1/S2 | [S] | a03, a08, K02 |
| T3 | Verify-before-act guard: no change before a test that localises the fault | G | [S] | a14, d08, K06, K28 |
| T4 | Enumerate-alternatives step to break anchoring, at equal tokens | G1 / O | [S] | d12-d14, b02, K11, K20 |
| T5 | Evidence closure as a selection signal for best-of-N | G / S7 | [S] | d10, d11, K29 |
| T6 | Rule-first, override-only-after-named-conflict-check on raw evidence | S0 | [S] | d15, a17, K30 |
| T7 | Tag device-specific vs reusable parts in stored lessons | memory | [S] | a15 |
| T8 | System-model-only, strategy-list-only and verify-only arms to split Sherlock's components | memory/S0 | [S] | d16, K31 |
| T9 | Forced strategy switch after N fruitless checks | O / S6 | [S] | a05, a07, K05 |
| T10 | Cost-aware test choice (split per cost) | S4 | [S] | a09 |
| T11 | Typed action space and precondition check before repair | G | [S] | d08, K28 |
| T12 | Gate size: how many held-out cases are enough | memory | open | d05, d07, K26 |

## 8. Concrete tests on our bench

All arms at equal tokens. Each run reports familiar and novel item splits, one strong and one weak model where possible, and at least 3 seeds. Where our bench has no fault diagnosis items, use debugging, circuit-fault or log-cause items built with a known injected cause and a code check.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 strategy memory | Held-out novel fault families (injected faults, code-checked) | (a) no text, (b) 3 raw past traces, (c) distilled strategy text | Accuracy on novel faults; tokens per case | (c) beats (a) and (b) by about 5-10 pts on the weak model, less on the strong. If (c) is below (a) on the strong model, the Trace2Policy pattern is confirmed |
| T2 rule-out step | Faults with 2-3 plausible symptom explanations | plain vs forced "what do the symptoms rule out, name 3 candidates" | Share of first hypotheses inside the true space; accuracy | Small gain on accuracy, larger on first-hypothesis hit rate |
| T3 verify-before-act | Diagnosis plus repair items | plain vs guard: no repair call until a localising test output is cited | Actions before verification; recovery validity | Fewer premature actions; recovery validity up a few points |
| T4 anti-anchor | Faults with a persistent decoy anomaly (like SREGym noise) | plain vs enumerate-alternatives step vs extra sampling at the same tokens | Diagnosis accuracy under decoy minus no-decoy | Decoy drop (about 10 pts) shrinks by half if the step works. The extra-sampling arm controls for plain compute |
| T5 closure selection | Same items, N=5 attempts | pick by majority vote vs by confidence vs by evidence closure (code) | Accuracy of the picked attempt | Closure beats vote by 3+ pts, since G4 says votes from one model are correlated |
| T6 rule then override | Items where a recalled rule is right in about 80% of cases | free override vs override after a named conflict check on raw evidence | Overrides vs corrections count; accuracy | Fewer harmful overrides, net gain small but positive |
| T7 tagged lessons | New system that shares function but not parts with the source | untagged lessons vs lessons tagged device-specific/reusable | Accuracy on the new system | Tagged better on cross-system items, equal in-system |
| T8 component split | Held-out systems | system model only / strategy list only / verify rule only / all three | Accuracy; premature actions | Shows which part carries the gain |
| T9 strategy switch | Faults where first strategy stalls | fixed strategy vs forced switch after N=3 fruitless checks | Accuracy; steps | Gain only on stalled items |
| T10 cost-aware tests | Items with test catalogue and costs | nearest test vs split-per-cost test | Cost to localise | Lower cost at same accuracy |
| T11 typed repair | R2Act-style repair items | free-text plan vs typed operation with precondition check | Recovery validity | Larger gain than diagnosis steps because 67.9% of errors are wrong operation |
| T12 gate size | 12-window memory loop | no gate, inner only, inner plus outer; held-out set of 40, 140, 400 cases | Final-window held-out accuracy; share of bad writes passed | Outer gate needs several hundred cases to beat noise. At 40-139 cases a 2% rule is within noise |

## 9. What does not transfer, and why

- Persona or "you are an expert" prompts. An LLM cannot be told into expertise (a22, a21). Only content moves.
- Theory training. Human experts do not differ on exam knowledge (a06). More general text will not help either.
- Years of experience as a source of skill. Machines have no slow practice. They can store distilled lessons but memory fails without a gate (c04).
- Human test-running skill. Not the difference (a04). Agents' tool calls fail for other reasons: 26-40% of telemetry calls error or return empty (b05).
- Sherlock's 20 hours of coached practice. No equivalent training step exists. The takeaway is its content (task analysis), not its form. All coaching gains are developer data with small N.
- Human memory limits. LLMs lack the novice's working-memory limits (a21), so novice-versus-expert contrasts built from personas are fake.
- Chess-style pattern stores. Chess is closed, fully observed and has a perfect oracle (a26). Real faults are open.
- Tutoring results (a19, d19, c16, b15, b17). These train humans or concern tutoring, not an agent diagnosing. They show distilled notes help, not that they help an agent on faults.
- Human strategy taxonomies (a05). The five strategies are descriptive. An agent can switch cheaply, so flexibility costs less than it does for people.
- Rigid structures. A rigid three-step note format was worse (d19). Rigid pipelines lose (c06).
- Multi-agent orchestration and debate. No gain (c20) and G9 already excludes debate.
- Logistics rule-distillation numbers (c15, d05-d07). Not diagnosis; skewed base rates.

## 10. Open questions

1. Does distilled strategy text (not raw traces, not tools) beat no text on held-out novel faults at equal tokens? OpsHarness is time-split on the same systems and adds tools (K27).
2. Which part of Sherlock transfers: system model, strategy list, or verify-before-swap? No ablation exists (K31).
3. Is there an independent replication of Johnson 1987 or Gott 1995, or a modern human study with larger N? Search was limited (critique).
4. Do agents show first-symptom anchoring under controlled decoys, and does an enumerate-alternatives step alone remove it at equal tokens? (K11, K20)
5. How large must the memory regression gate set be? Studies used 40 and 139 cases; OpsHarness testbed size not stated (K26).
6. Is evidence closure a better selection or training signal than answer accuracy? (K29)
7. Does expert persona fail on diagnosis tasks specifically? Only factual QA tested (K32).
8. Can we detect when an agent should switch from a recalled rule to model-based reasoning? Luo et al. give a proxy only (K30).
9. Chase and Simon and Chi et al. numbers are unopened. How large is the pattern-store advantage on fault cases, and does it vanish on novel cases? (K33)
10. Is the repair gap missing operational knowledge or weak action validation? R2Act argues the latter, but "wrong operation" can be read either way (K28).
11. Strategy range versus sequence quality: which separates skill? (section 2.6)
12. Multi-turn: does it add aptitude (Bi et al.) or cost reliability (Laban et al.)? Task types differ (c14, c24).
13. How do agents compare with human experts on the same faults? No study.

## 11. Sources

[V] = opened and read this session. [M] = snippet, abstract only, recalled, or secondary.

Human studies
- [V] Johnson (1987) Knowledge and skill differences between expert and novice service technicians. https://files.eric.ed.gov/fulltext/ED290043.pdf (a01-a04)
- [V] Johnson (1995) Understanding troubleshooting styles to improve training methods. https://files.eric.ed.gov/fulltext/ED389948.pdf (a05-a07, a18)
- [V] Lesgold, Lajoie, Bunzo and Eggan (1988) Sherlock. https://files.eric.ed.gov/fulltext/ED299450.pdf (a08)
- [V] Steinberg and Gitomer (1992) Cognitive task analysis, interface design, and technical troubleshooting. https://files.eric.ed.gov/fulltext/ED384677.pdf (a09)
- [V] Katz et al. (1997) Cognitive task analysis and intelligent computer-based training systems. https://files.eric.ed.gov/fulltext/ED411309.pdf (a10, a11, d16, d17)
- [V] Gott group (1995) Tutoring for transfer of technical competence. https://files.eric.ed.gov/fulltext/ED382817.pdf (a12-a15)
- [M] Parker (1990) Success in tutoring electronic troubleshooting, NASA CP-3059. https://ntrs.nasa.gov/citations/19900016252 (a16, abstract only)
- [M] Rasmussen (1983) via web summary. https://www.smithsrisca.co.uk/PSYrasmussen1983.html (a17)
- [M] Rasmussen and Jensen (1974) Mental procedures in real-life tasks (b19, no URL, recalled)
- [M] Rasmussen (1983) IEEE original (b20, recalled)
- [M] Gott et al. (1993) Cognitive analysis of avionics troubleshooting (b21, recalled)
- [M] Gott, Bennett, Gillett (1986); Lesgold et al. (1992) Sherlock; de Kleer and Williams (1987) https://doi.org/10.1016/0004-3702(87)90063-4 (c21-c23, recalled)
- [M] Chase and Simon (1973) Perception in chess (a27; ScienceDirect 403)
- [M] Chi, Feltovich, Glaser (1981) (a28, b23; Wiley blocked)
- [M] Gugerty and Olson (1986); Kalyuga et al. (2003); Macnamara, Hambrick, Oswald (2014) (b22, b24, b25, recalled)
- [M] Wikipedia, Chunking (psychology), secondary summary. https://en.wikipedia.org/wiki/Chunking_(psychology) (d21)

LLM and AI studies
- [V] Ruoss et al. (2024) Amortized planning with large-scale transformers: chess. https://arxiv.org/abs/2402.04494 (a26)
- [V] Zheng et al. (2024) When a helpful assistant is not really helpful: personas. https://arxiv.org/abs/2311.10054 (a22, d18)
- [V] Jha et al. (2025) ITBench. https://arxiv.org/abs/2502.05352 (a23, b09)
- [V] Cloud-OpsBench (2026). https://arxiv.org/abs/2603.00468 (a24)
- [V] Gong et al. (2026) ORCA-bench. https://arxiv.org/abs/2607.28545 (a25, b01-b05, c11, c12)
- [V] Clark et al. (2026) SREGym. https://arxiv.org/abs/2605.07161 (b06-b08, d12)
- [V] Tian et al. (2026) GALA. https://arxiv.org/abs/2608.08968 (b10, b11)
- [V] Xu et al. (2025) Novice program fault localization. https://arxiv.org/abs/2512.03421 (b12-b14)
- [V] Ma et al. HypoCompass. https://arxiv.org/abs/2310.05292 (b15, b16)
- [V] Englhardt et al. (2023) LLMs for embedded system development and debugging. https://arxiv.org/abs/2307.03817 (b17, b18)
- [V] Huang et al. (2026) OpsHarness. https://arxiv.org/abs/2608.25661 (c01-c05, d01-d04)
- [V] Lu et al. (2026) Beyond fault localization. https://arxiv.org/abs/2608.21310 (c06-c10, d13, d14)
- [V] Bi et al. (2026) Free to Look, Free to Reason. https://arxiv.org/abs/2610.35767 (c13, c14)
- [V] Zha et al. (2026) Trace2Policy. https://arxiv.org/abs/2606.10457 (c15, d05-d07)
- [V] Hu and Ash (2026) Chat Debugging. https://arxiv.org/abs/2608.02955 (c16)
- [V, abstract and intro] Fang et al. (2026) OpenRCA 2.0. https://arxiv.org/abs/2606.27154 (c17, d10, d11)
- [V, abstract and intro] Qi et al. (2026) R2Act. https://arxiv.org/abs/2607.04623 (c18, d08, d09)
- [V, abstract] Luo et al. (2026) Rethinking tool design for agentic RCA. https://arxiv.org/abs/2610.05009 (c19, d15)
- [V] Jansson et al. (2026) Westermo test-failure analysis. https://arxiv.org/abs/2609.21843 (c20)
- [V] Cho et al. (2026) LLMs can explain experts better than experts. https://arxiv.org/abs/2608.07488 (a19, d19)
- [V, weak] Oveisi and Manjunatha (2026) search-and-rescue LLM. https://arxiv.org/abs/2606.19514 (a20)
- [V, abstract] Borchers, Vie, Azevedo (2026) LLMs as students who think aloud. https://arxiv.org/abs/2602.01015 (a21, d20)
- [M] Laban et al. (2025) LLMs get lost in multi-turn conversation (c24, via the citing paper)

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 17 established claims: 6 confirmed as written, 11 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E08.02-K03** (reworded: the sources support less). Lesgold et al. give one expert (7 steps) vs. three trainees (14, 20, others similar) on a single sample problem and say most trainees also try to be systematic by space splitting or sequential tracing; the contrast is not general. Corrected claim: In Lesgold et al.'s Sherlock task analysis, the expert solved one sample problem in 7 steps by splitting the suspect space, while one trainee took 14 steps and another 20, tracing circuit paths end to end; the authors say what differs with expertise is which space is split, and Johnson (1995) found strategy type did not separate high from low performers but range of strategies did.
- **E08.02-K04** (reworded: the sources support less). The theory-knowledge null comes from one student sample (Johnson et al. 1993, n=34, t(32)=0.073) that the author hedges as 'may not be as important', and a null test is not proof of no prediction. Corrected claim: In one student study (Johnson et al. 1993, n=34) systems-exam scores did not differ between high and low troubleshooters (19.82 vs 19.88 of 24), suggesting theory knowledge may be a weak predictor of troubleshooting skill; range of strategies (Johnson 1995) and strategic and system knowledge (Katz et al. 1997; Steinberg and Gitomer 1992) were what separated skilled from unskilled technicians.
- **E08.02-K07** (now single-source: the sources are not independent). Numbers match, but Katz et al., the Gott et al. report and Parker are all the Sherlock developers' own evaluations (Katz summarises the same data as Gott), so there is no independent source.
- **E08.02-K09** (reworded: the sources support less). Numbers are right, but Cloud-OpsBench's 0.76/0.68 is the best joint RCA accuracy (a high score, not a failure), and ITBench tested 2024-era models (GPT-4o, Llama) rather than strong current agents. Corrected claim: ITBench found agents on 2024-era models resolved only 13.8% of SRE scenarios, ORCA-bench's best RCA accuracy was 25.3% on Medium and 10.0% on Hard tasks, and Cloud-OpsBench's best joint RCA accuracy was 0.76 (OnlineBoutique) and 0.68 (TrainTicket) but with evidence closure of only 0.38 and 0.15.
- **E08.02-K12** (reworded: the sources support less). ORCA 9-16 pts is right, but GALA+ 74.44% vs 48.35% compares a whole multi-phase system with a different published method (Flow-of-Action), not a with/without dependency-graph ablation. Corrected claim: Removing source code cut RCA accuracy by 9-16 points across models in ORCA-bench, and GALA+, a method that bounds exploration with the service dependency graph, reached 74.44% AC@1 on Online Boutique against 48.35% for the best prior LLM method (Flow-of-Action), though this compares whole systems and is not a dependency-graph ablation.
- **E08.02-K15** (reworded: the sources support less). Only SREGym supports it (63.7% to 17.9% is Stratus/Sonnet 4.6, n=13 new-failure problems); the second source is a human transfer study that says nothing about LLM agents. Corrected claim: On SREGym, end-to-end success of LLM SRE agents fell on its 13 new failure scenarios compared with ported problems (Stratus/Sonnet 4.6 63.7% to 17.9%, Claude Code 60.8% to 28.2%, Codex 57.8% to 15.4%), while similar-failure problems stayed near ported levels; this is one benchmark.
- **E08.02-K16** (reworded: the sources support less). OpsHarness numbers match, but Trace2Policy found one-shot distilled rules (69.2%) no better than no rules (70.3%) and worse than few-shot (73.3%); only error-refined rules (78.9%) won, and OpsHarness's 59.0% bundles knowledge, skills, tools and a cold-start substrate. Corrected claim: In OpsHarness, a harness that mines past diagnoses into knowledge, skills and tools reached 59.0% final A@1, against 38.4% for in-context retrieval of three correct past rollouts and 36.1% for the bare agent; in Trace2Policy only error-refined rules (78.9%) beat few-shot examples (73.3%), while one-shot distilled rules (69.2%) did not.
- **E08.02-K21** (reworded: the sources support less). Only Zheng et al. (one paper, listed twice) tests it, on factual MMLU questions with open models, and finds small domain-alignment effects; Borchers et al. is about LLMs simulating novice students, not expert personas. Corrected claim: In one large study (Zheng et al. 2024: 162 personas, 4 open LLM families, 2,410 factual MMLU questions) adding a persona, including expertise-domain roles, to the system prompt did not improve accuracy over no persona on average, and picking the best persona per question was about as good as random; domain-aligned roles helped only slightly.
- **E08.02-K22** (reworded: the sources support less). The 65.48 vs 34.21 score is the mean over all 15 participants (students, faculty, professional engineers) on embedded development tasks, not novices only or debugging only; HypoCompass is software debugging and Hu and Ash is qualitative. Corrected claim: In a 15-participant study of embedded-system development and debugging, participants using GPT with a structured workflow scored 65.48 vs 34.21 without GPT (t(38)=2.73, p<0.01), with all five users on the environmental-sensor task scoring 100% (including some with no hardware experience) against 25% without GPT; the models also hallucinated hardware facts (e.g. wrong I2C address from pin voltage in 38% of trials, a wrong register or configuration value in 100%).
- **E08.02-K25** (reworded: the sources support less). Westermo paper reports no consistent quality advantage (scenario-dependent) from 2 scenarios and 6 practitioners; Bi et al. compares simple harnesses with published agents, not single vs multi-agent. Corrected claim: In an exploratory Westermo case study (2 failure scenarios, 6 practitioners, 120 runs) neither the single-agent nor the orchestrated multi-agent RCA configuration showed a consistent practitioner-rated quality advantage, and the single agent was faster and cheaper.
- **E08.02-K26** (reworded: the sources support less). The two-stage design is described accurately, but only the whole gate was ablated (no stage-by-stage test), and the second source (Trace2Policy) uses a single validation regression gate in a different domain, so 'should pass a two-stage gate' is not shown. Corrected claim: OpsHarness verifies each proposed memory or tool change with an inner gate (no accuracy or cost regression on the source cases) and an outer gate (no regression on a freshly re-sampled held-out testbed stratified by fault family and time); removing the whole gate made accuracy decay (final-window A@1 0.33 vs 0.43 for no-evolve) and hurt weak backbones most, but the two stages were not ablated separately; Trace2Policy independently found a regression gate necessary, in a different domain.
