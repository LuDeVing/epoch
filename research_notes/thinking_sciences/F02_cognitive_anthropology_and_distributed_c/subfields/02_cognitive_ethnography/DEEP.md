# Cognitive ethnography: deep document

*Subfield F02.02 in cognitive anthropology and distributed cognition. Built from evidence_a-d.jsonl (ids a01-a28, b01-b25, c01-c26, d01-d19), claims.jsonl (F02.02-K01 to K22) and critique.md in this folder. Status labels: [E] established, [S] single-source, [C] contested. Numbers were re-checked against source text where critique.md says so.*

## 1. What it is

Cognitive ethnography is a method. The observer watches real people do real work in their normal setting. The observer records talk, gesture, tools, screens, paper and space, often on video. The observer then asks cognitive questions: what is remembered, what is computed, what is passed on, and where.

The key move is the unit of analysis. It is not one head. It is the whole socio-technical system: people plus artifacts plus the environment. Hutchins asks of a cockpit the questions a psychologist asks of a person. How is information stored? How is it transformed? How does it move? (a01, a06)

Four features define it:
- It is event-centred. It follows an activity from start to end, not a trait or a stored belief (a07, b03).
- It is not one technique. It mixes interviews, surveys, participant observation, and video and audio recording (a07).
- It looks at action, not only at what people know. This separates it from the 1960s-70s cognitive anthropology that studied knowledge in heads (a07, a18).
- It is a loop: observe, build theory, redesign work materials, observe again. Experiments are "ethnographically natural" tests of changes (a08).

Why this matters for our agent. Our agent is one model plus tools, notes, files and checks. The method gives one design idea: treat those external things as parts of the thinking system and design them as memory and computation, not as logs. It also gives a method for people: read agent traces the way an ethnographer reads work, and let what you see drive design changes. The evidence for the first idea is thin and human-only. The evidence for the second is early and promising but unmatched on tokens.

What this document is honest about. The founding studies are qualitative. There are no error counts and no replication of them (a01, b01, b25). Most "LLM" studies found here use LLMs as coders or as simulated people. None applies Hutchins-style ethnography to LLM agents (K15, weak negative from a rate-limited search).

## 2. History and theories in depth

### 2.1 Cognitive anthropology before Hutchins

Cognitive anthropology (1950s-70s) put culture in the head. It studied folk taxonomies and shared knowledge. D'Andrade (1981) split the labour: psychology studies how people think, anthropology studies what they think (a18). That left the material and social world as something people think about, not something they think with. Formal tools made the field testable: multidimensional scaling and cultural consensus modelling (Romney, Weller and Batchelder 1986), which tells you how many informants are enough (Boster 1985) (b07). Consensus models fit knowledge questionnaires. They do not fit coded video of work (b07 limits).

### 2.2 Navigation ethnography (1980s)

Hutchins studied bridge navigation on US Navy ships. Result: a navigation team is a cognitive system whose computation spreads over people, charts, instruments and tables. Outcomes that mattered were not set by any one navigator but by interactions among several (a09, a11). He also compared Western and Micronesian navigation. In the Micronesian etak scheme the canoe is held still under the stars and the islands move. Western researchers called it illogical. Hutchins argues it is a different frame with different easy and hard inferences (a12, a13). The book Cognition in the Wild (1995) was not opened here. Team size, fix cycle and error counts are unverified (a11, d19, critique gap 9). Seifert and Hutchins (1992) "Error as opportunity" analyses errors in this setting; its text was not read (d19).

### 2.3 The cockpit paper (1995)

"How a cockpit remembers its speeds" (Cognitive Science 19:265-288) is the founding worked case (a01-a05, b01, b02). Basis: more than 100 observer flights over 6 years in commercial cockpits (a01). The account is stylised, not a raw log. The analysis started in November 1988 (b01).

The chain of media (a02):
1. A gross-weight readout selects a speed card from a booklet. One card covers about a 2,000 lb band.
2. The pilot not flying (PNF) says the speeds aloud. Visual becomes spoken, so the busy pilot flying hears it.
3. Both pilots set speed bugs on their own airspeed indicators.
4. Later, the needle-versus-bug relation tells when to extend flaps.
5. The PNF calls out deviations over 5 knots at 500 ft above field level.

Example card, 122,000 lb: minimum-manoeuvring speeds 227 (flaps 0 retracted), 177 (0 extended), 155 (11), 152 (15), 142 (28), 137 (40). Landing reference speed Vref 132 (28 extended) and 128 (40 extended). Bugs are set about 25-30 minutes before landing at light workload and used 10-15 minutes later (the 10-15 minute figure was not re-checked, critique.md).

The theory claims (a03, a04):
- Bugs do not improve pilot memory. They replace a memory task (remember speeds, read the dial, compare numbers) with a perceptual one (is the needle near the bug). Memory becomes a property of the larger system.
- Work is distributed across people, across time (compute at low workload, use later), and across media.
- Redundancy catches errors. The checklist item "flight instruments and bugs" has each pilot compare bug positions with the other pilot's and with the card. At least three independent representations exist: card, speech, bug (b02).
- Opportunistic structure use: pilots use the salmon bug's width as a yardstick on the dial. The bug is about 10 knots wide so it never hides more than one 10-knot tick. Designers did not specify this use (a05, single engineer anecdote).

### 2.4 The programme paper (2000)

Hollan, Hutchins and Kirsh (ACM TOCHI) state two principles (a06, b04):
1. The boundary of the unit of analysis is set by functional relations, not by the skull.
2. Cognition uses internal and external resources, and runs at several time scales.

They name three kinds of distribution: across members of a group, between internal and external structure, and across time. They propose cognitive ethnography as the empirical method and a design loop that feeds findings back into artifacts. Example: pilots using needle airspeed indicators rarely read airspeed as a number. They read needle position in a space of meaningful speeds. A new airspeed tape was designed to keep that salience. The authors say it needs experimental test, and report none (a08, b05). They argue the Boeing 737-700 copies the old dial on a screen, as a sign of design not grounded in ethnography (a10). That is circumstantial support only. They also admit observation under-constrains inference, so findings should suggest experiments (b03).

Known weakness: the analyst chooses the boundary, and there is no test for choosing it wrongly (b04).

### 2.5 Later work

- Micro-scale video analysis. Alac and Hutchins (2004): fMRI scientists make brain images meaningful through gesture, speech and material structure together. In "learning to see retinotopy" an expert traces V1 borders on a paper chart, then repeats the trace on the brain image. Basis: three labs, 15 participants, nine months of ethnography, one episode picked from eight hours of video. No counts, no coder agreement (a17).
- Material anchors (2005). Thinking needs stable representations of constraints. Stability comes from shared cultural models or from tying concepts to material structure. Queues, constellations and charts act as anchors for conceptual blends (a14).
- Cultural ecosystem (2013). Moves from single extended-mind assemblies to the cultural-cognitive ecosystem. Conjecture: practices that project an imagined trajector onto a spatial array (queues, constellations, loci, number line, flight-deck charts) recur because they work. Conjectures, untested here (a15).
- Instrumented digital ethnography (2013). One qualified crew flew a scenario in a Boeing 787 simulator. Data: several HD video streams, audio, digital pen data, wearable eye tracking on both pilots, simulator logs. The vignette covers a few seconds, with fixations of about 0.5 s, 0.5 s and almost 1 s. One crew, no statistics (a16, b06). Tools built by the lab: ChronoViz for time-coded multi-stream data (CHI 2011) and eye-tracking integration (ETRA 2012) (a20).
- Computational models. Hutchins and Hazlehurst (1991, 1995): communities of connectionist networks that learn while building external structures (a lexicon) that mediate each other. Over generations the system gets abilities no single agent reaches in a lifetime. Toy worlds (a19).
- Aviation design lines. The Integrated Mode Management Interface (1994) was tested head to head against the 747-400 mode control panel in a NASA Ames simulator; results are not on the page read (a24). A Hutchins 2024 project joining cognitive ethnography with generative AI was reported second-hand; no outputs found (c23).

### 2.6 Rival and neighbouring views

- Situated action (Suchman 1987): plans are resources for action, not controllers. Distributed cognition keeps a computational description. This is a conceptual dispute. No quantitative test pits them against each other (b24, K04 [C]).
- Extended mind (Clark): sibling idea, covered in a separate subfield in this run. Interactivity experiments point the same way (b08, tertiary source): cards and tokens aided Bayesian reasoning and cut base-rate neglect (Vallee-Tourangeau et al. 2015); interactivity reduced the harm of working-memory depletion on mental arithmetic (2016). Primary papers not opened.
- Epistemic action (Kirsh and Maglio 1994): Tetris players rotate pieces on screen to learn fit sooner than by mental rotation. Recalled, not opened here (a21, b09). See the sibling note on epistemic action.
- Interaction analysis (Jordan and Henderson 1995): groups of analysts watch tape together with foci such as use of space, turn-taking and artifacts. Claims are checked by group viewing, not a kappa. Recalled, not opened (a22).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Cockpit speed memory is a property of crew plus card, speech and bugs | 100+ observer flights over 6 years; card for 122,000 lb: Vref 132 (flaps 28) and 128 (flaps 40); bugs set 25-30 min before landing; callout at 5 kt deviation and 500 ft AFL; no error counts | Hutchins 1995 (a01, a02, b01) | [S] qualitative, one author |
| Bugs transform the task (memory to perceptual match) | No with/without-bug comparison | Hutchins 1995 (a03) | [S] interpretive |
| Work is spread across people, time and media | Compute at low workload, use 10-15 min later; 3+ redundant representations | Hutchins 1995; HHK 2000 (a04, b02, a06) | [E] as a design pattern (K03); not rate-tested |
| New airspeed tape designed from ethnography | No pilot data reported | HHK 2000 (a08, b05) | [S] untested |
| Micro-ethnography of fMRI practice | 15 participants, 3 labs, 9 months; one episode from 8 h of video | Alac and Hutchins 2004 (a17) | [S] illustrative |
| 787 simulator, one crew | Fixations about 0.5 s, 0.5 s, almost 1 s; 18 scales on the panel | Hutchins 2013 (a16, b06) | [S] one vignette |
| Checklist (nearest tested analogue), before-after | Deaths 1.5% to 0.8% (P=0.003); complications 11.0% to 7.0% (P<0.001); N=3733 before, 3955 after; 8 hospitals | Haynes 2009 (d01) | [C] no control group |
| Checklist bundle in ICUs | 103 ICUs, 375,757 catheter-days; mean infections 7.7 to 1.4 per 1000 catheter-days at 16-18 months; rate ratio 0.62 to 0.34 | Pronovost 2006 (d02) | [C] bundle, no concurrent control |
| Checklist mandate, natural experiment: no effect | 101 hospitals; 109,341 vs 106,370 procedures; death 0.71% to 0.65% (OR 0.91, CI 0.80-1.03, P=0.13); complications 3.86% to 3.82% (OR 0.97, P=0.29) | Urbach 2014 (d03) | [C] failed to replicate large effect in typical practice |
| No controlled test of speed bug or card found | Weak negative: PubMed and arXiv only | d04, b25 | [S] absence of evidence |
| VLM alone near human on video annotation | Mean human-normalised score (HNS) 97.0; 15 tasks; 1,459 instances; met or beat human on 9 of 15 | Shen 2026 (b14, c01) | [S] one VLM |
| VLM accuracy depends on phenomenon | Attention 17.8; sign recognition 35.4; mistake handling 47.0; dominance 82.9; outcome/breakdown 89.6; workflow 118.2; co-speech gesture 128.4; intent 134.0 | Shen 2026 (b15, c02) | [S] |
| Human verification of VLM labels best on average | HNS 121.5; beat human-alone on 11 of 15; time 45.0 s to 23.0 s per video (-48.9%); cost -31.3% to -44.5%; VLM $16.03 total, $1.07 per video hour | Shen 2026 (b14, c03, c04) | [S] |
| Verification can hurt | Behaviour interval 101.6 to 86.5; animal behaviour 110.8 to 90.5; helped most on attention 17.8 to 140.1, mistake handling 47.0 to 113.8, sign recognition 35.4 to 100.0 | Shen 2026 (c03, d09) | [C] anchoring suspected, not tested |
| Self-verification without outside signal flips answers | GPT-3.5 CommonSenseQA 75.8 to 38.1 (round 1), 41.8 (round 2); GSM8K 75.9 to 75.1 to 74.7 | Huang 2024 (d08) | [E] older models, prompt dependent |
| GPT-4 qualitative coding falls with codebook difficulty | Kappa A 0.94-0.97 (18 codes), B 0.74-0.75 (24), C 0.55-0.58 (32); humans 0.97, 0.83, 0.63 | Kirsten 2024 (b11) | [S] short paper, German data |
| GPT-3.5 invents categories | 47 non-codebook codes in Task B; GPT-4: 2. Kappa A 0.74-0.85, B 0.56-0.60, C 0.34-0.43 | Kirsten 2024 (b12) | [S] |
| GPT-3.5 guessing on some codes | 4 of 13 Trump-tweet codes not different from random | Chew 2023 (d17) | [S] closed codebooks |
| LLM text annotation beats crowd workers | n=6,183 items, 4 datasets; about +25 points accuracy; under $0.003 per item; about 30x cheaper | Gilardi 2023 (c06) | [E] easy label sets, 2023 model |
| GPT-4 beats experts and single crowd workers on political tweets | Plurality of 10 MTurk workers beat experts; LLM slightly above that | Toernberg 2023 (c07) | [S] one task |
| LLM thematic coding stable across runs | Kappa across runs Gemini 2.5 Pro 0.907, GPT-4o 0.853, Claude 3.5 Sonnet 0.842 (widest span 0.396); one transcript, 18 runs | Jain 2026 (b17) | [C] consistency is not validity |
| Review range of human-LLM kappa | 0.40 to 0.91, median 0.72; accuracy 77-96% | Review snippet (b19) | [S] snippet only |
| Reflection and planning raise believability | TrueSkill: full 29.89, no reflection 26.88, no reflection or planning 25.64, crowdworkers 22.95, no memory/planning/reflection 21.21; d=8.16; H(4)=150.29; 100 raters | Park 2023 (b20, c12) | [S] raters, not task success |
| Memory embellishment | 6 of 453 awareness answers hallucinated (1.3%) | Park 2023 (c14) | [S] |
| Reflexion over plain episodic memory | HotPotQA +8 points absolute (100 questions); HumanEval 91% vs GPT-4 80% | Shinn 2023 (d13) | [S] same lab |
| Stored experience propagates errors | Agents copy similar past records; filtering helps; deltas not extracted | Xiong 2025 (d14) | [S] |
| Interview-grounded agents predict surveys, not games | v2: GSS 72.8% vs retest 79.5% (about 92%) vs demographics only 60.4%; Big Five r 0.86 vs retest 0.95; games MAE 0.29 vs 0.27 demographic, retest 0.21. v1: games normalised r 0.66 interview vs 0.48 demographic, ANOVA F(4,5255)=1.63, p=0.16 | Park 2024 (c15, d16, critique) | [S] versions differ |
| Digital twins | N=2,058; 71.72% mean accuracy; 87.67% of test-retest | Toubia 2025 (d15) | [S] |
| Role/SOP structure beats free chat | MetaGPT HumanEval 85.9%, MBPP 87.7%; executability 3.75 of 4 vs ChatDev 2.25; 541 s; 31,255 tokens; 124.3 tokens per line vs 248.9 (the 503 s figure is the no-feedback variant) | Hong 2024 (c16, critique) | [C] own benchmark |
| Multi-agent vs single at matched tokens | 260 configs, 6 benchmarks: +80.8% to -70.0%; planning -39% to -70%; single agent above about 45% accuracy gains nothing; independent agents amplify errors 17.2x, centralised 4.4x | Kim 2026 (d10) | [E] with d11 |
| Debate often loses to self-consistency | 5 methods, 9 benchmarks, 4 models | Zhang 2025 (d11) | [E] |
| CoThinker gain, not at equal tokens | +5.1 (Reasoning vs CoT), +5.3 (Data vs IO), +6.0 (Language vs SR); 14,323 output tokens vs 643 for CoT; 16 of 25 comparisons pass Holm; instruction following loses | Shang 2026 (c19, d12) | [S] |
| Blackboard multi-agent | +4.33% average over CoT, +5.02% over static multi-agent; 6 benchmarks | Han and Zhang 2025 (c18) | [S] small subsets |
| Trace reading as design method (MAST) | 150+ traces, then 1,600+ traces over 7 frameworks; kappa 0.88 (6 experts, 15 traces); LLM annotator kappa 0.77; ChatDev ProgramDev-v0 25.0 to 34.4 (prompts) to 40.6 (topology); AG2 GSM-Plus GPT-4 84.75 to 89.75 (prompts), topology 85.50 (p=0.4) | Cemri 2025 (d05, d06) | [S] tokens not matched |
| LLMs cannot yet do trace attribution | 53.5% agent-level, 14.2% step-level (127 systems) | Zhang 2025 Who&When (d07) | [S] |
| Offloading profiles in students | N=97, 564 prompts; volume clusters 51/22/17/7; authorship 5.00, 3.76, 1.16, 0.53 | Poquet 2026 (b22) | [S] correlational |
| Heavy-tailed agent coordination | 1.5 million interactions; power-law exponents 2-3; deficit-triggered integration helps most where imbalance is largest | Venkatesh and Cui 2026 (c20) | [S] |
| Cognitive Workspace memory reuse | 54-60% vs 0% for RAG; d 23-196; 8 documents; GPT-3.5 | An 2025 (a25, b21) | [S] weak metric |
| Video annotation in HCI | 125 of 1,702 CHI 2026 papers annotate video; external view 56.0%, egocentric 37.6%, screen 11.2%; automatic 58.4%, expert 44.0%, participant 4.0% | Shen 2026 (b13, c05) | [S] |

## 4. Mechanisms and models

Each mechanism is written so an engineer could build and test it.

### 4.1 Task-transforming artifact (speed-bug mechanism)

Idea: an external object does not just hold data. It changes the operation the agent must do.
- Before: the agent must recall target value T, read the current value V, compare. Three steps, each can fail.
- After: a pre-computed marker at T is placed next to the display of V. The check becomes "does V sit on the marker?" One cheap step.

Implementation sketch for an LLM agent:
1. Planning pass (low load, early): compute target values, thresholds, expected formats and invariants. Write them into a scratch file as a "card" keyed by the situation (like weight band to speed set).
2. Execution pass (later): do not recompute. At each step, copy the current value next to the card entry and mark match or mismatch.
3. Deviation rule: if the difference exceeds a threshold (cockpit: 5 knots at 500 ft), call out and stop to re-plan.

Why it should work: the check no longer depends on the model re-deriving the target under load and long context. Why it might not: the model may skip the card (d01-d03: checklists help when used; a mandate can become box-ticking). So log whether the card is actually read at each step.

### 4.2 Distribution across time

Compute in a cheap, calm moment; use later under pressure. For an agent: an early pass writes plans, tests and checks; later passes only compare. Cost is paid once. Risk: stale cards when the situation changes. Add an invalidation rule: if inputs change, regenerate the card.

### 4.3 Distribution across people: modality conversion and the second reader

The PNF reads the dial and says it aloud, so the pilot flying gets the cue without looking. The agent analogue: one pass or role extracts the observation into a short structured message and another pass acts on it. Keep this as role-switching inside one agent first (Kim 2026 and Zhang 2025 show true multi-agent setups lose at matched tokens).

### 4.4 Redundant representations with cross-check

Three independent representations (card, speech, bug) and a challenge-response checklist where each pilot checks the other. Agent analogue: derive the same quantity two ways (compute and also look up; or two different decompositions) and compare. Transposition-type errors are the target (b02: the error-frequency claim comes from other literature). Redundancy only helps if the routes are independent. Self-verification on the same route can flip right answers (d08).

### 4.5 Opportunistic structure use

Users find uses designers never specified (the bug as a ruler). Agent analogue: let the agent write its own helper notes, and review traces for notes that were invented and then reused. Then promote the useful ones to designed tools. This is the "observe then redesign" loop of a08.

### 4.6 Trace ethnography as a design loop (MAST pattern)

1. Collect 50-150 traces. Read them with an open mind and name failure types by grounded theory.
2. Build a taxonomy. Check agreement among two or more readers (MAST: kappa 0.88 on 15 traces).
3. Annotate more traces with the taxonomy (an LLM annotator reached kappa 0.77, accuracy 94% on MAST; but it cannot do causal attribution: 53.5% agent, 14.2% step).
4. Change the design where failures cluster. MAST: topology change beat prompt change on ChatDev (25.0 to 40.6 vs 34.4).
5. Rerun at matched tokens (MAST did not).

Add a state-holder label to each step: who or what holds which piece of state (model context, file, tool output, human). Look for state held in only one fragile place.

### 4.7 Verification of machine-coded observations

Shen 2026 workflow: machine labels everything, human verifies. Gains concentrate where the machine is worst. Losses appear where machine output is already precise and plausible. Implementation: gate verification by task type or by a confidence or disagreement signal rather than verifying everything. Keep a blind variant to test anchoring.

### 4.8 Memory stream with reflection (Generative Agents pattern)

Store observations with timestamps. Retrieve by recency, importance and relevance. Periodically write higher-level reflections and store them as new memories. Plan from retrieved memories. Failure modes: retrieval gets harder as memory grows, embellishment (1.3%), and error copying (d14). Add a filter on stored records.

### 4.9 Cultural process model (Hutchins and Hazlehurst)

Agents learn while writing to a shared external structure (a lexicon) that others learn from. Over generations the shared structure carries knowledge no single agent has. Agent analogue: a persistent shared notes file that later runs learn from. Only toy-world evidence (a19).

## 5. What holds up

### 5.1 What holds up
- The conceptual frame is widely adopted and coherent (a06, b04), but it is a stance, not an empirical result.
- Task-structuring artifacts such as checklists reduce errors in before-after studies (d01, d02). This is the nearest tested analogue to the speed bug.
- At matched token budgets, multi-agent systems do not generally beat one agent (d10, d11). Two independent papers, 9 plus 6 benchmarks.
- Self-verification without an external signal is unreliable on older models (d08).
- LLM annotation beats crowd workers on easy text label sets (c06, c07). Cost and speed gains are large.

### 5.2 Failures and non-replications
- Checklist mandate in Ontario: no significant effect, OR 0.91, P=0.13, 101 hospitals (d03). Likely causes (unproven): box-ticking, short windows, quality of use not observed.
- No replication, failed or otherwise, of the Hutchins cockpit or navigation studies was found, and no inter-coder reliability study of cognitive-ethnographic video coding (b25, K02). The search was rate-limited, so this is weak.
- Interview-grounded simulations fail on incentivised economic games: v1 ANOVA p=0.16; v2 MAE 0.29 vs 0.27 for the demographic baseline (c15, d16). Headline numbers differ between versions, so always cite the version.
- Cognitive Workspace effect sizes (d up to 196) are not credible (a25, K11).
- Shang 2026 gains are not an equal-token result: 14,323 tokens vs 643 (d12).
- Generative Agents: crowdworker role-players did not differ significantly from the fully ablated agent (critique.md).

### 5.3 Moderators and boundary conditions
- Task difficulty and codebook size. GPT-4 kappa 0.94-0.97 (18 codes) falls to 0.55-0.58 (32 codes). Humans fall too (0.97 to 0.63) (b11).
- Phenomenon type in video. Observable movement, interface events and speech-linked gesture: strong. Attention and mental-state cues: weak (b15). Viewpoint and reasoning horizon did not predict accuracy.
- Task type and baseline strength for multi-agent. Planning is always worse; a single agent above about 45% accuracy gains nothing from more agents (d10).
- Load. CoThinker gains concentrate on high intrinsic load tasks; overhead dominates on easy ones; it loses on instruction following (c19, d12).
- Model. Claude's run-to-run kappa span was widest (b17). GPT-3.5 is far worse than GPT-4 on invented codes (b12). AG2 gains depended on the model (d06).
- Context of use. Checklists work in the originating setting with engaged teams and not always under a mandate (d01 vs d03).

### 5.4 Interventions that worked, and that did not
Worked:
- A structured prompt framework (task, background, output format) made LLM thematic analysis usable to researchers; the outcome is self-reported confidence only (b16, c10).
- Few-shot examples cut formatting errors and off-codebook codes for GPT-3.5 (b12).
- Human verification on weak tasks (c03).
- Topology fix on ChatDev (d06).
- Reflection over plain memory in Reflexion (d13).
- Filtering stored experience (d14).

Did not work:
- Few-shot on GPT-4 kappa (b11).
- Verification on behaviour interval and animal behaviour (c03).
- Topology change on AG2 with GPT-4 (p=0.4) (d06).
- Persona grounding on incentivised games (d16).
- Debate over self-consistency (d11).
- Any multi-agent form on planning tasks (d10).

## 6. Language models

No study applies cognitive ethnography to LLM agents (K15). What exists falls into five groups.

1. LLMs as ethnographic coders of video (Shen 2026; b14, b15, c01-c05). One VLM (named gemini-3.7-flash in the source), 15 tasks, about 100 videos per task. Mean HNS 97.0 alone and 121.5 with human verification. Large spread by task (17.8 to 134.0). Time -48.9%, cost -31.3% to -44.5%. Caveats: each human condition ran on half the benchmark and full-benchmark human time was extrapolated by doubling; open datasets, not fieldwork recordings; no repeated runs; the attention result may be partly bounding-box noise. Failure seen: the model treated later activity as proof of successful repair.
2. LLMs as qualitative text coders. Closed codebooks: GPT-4 kappa 0.55-0.97 by task, with off-codebook invention near zero for GPT-4 (2) and high for GPT-3.5 (47). GPT-4 few-shot did not help kappa. Crowd comparisons: +25 points (Gilardi), beats experts on one task (Toernberg). Repeat-run kappa 0.84-0.91 (Jain). Open-codebook kappa and the current-model invention rate were not measured (K22).
3. LLM agents with memory (Park 2023; Reflexion; Xiong 2025; Cognitive Workspace). Reflection adds believability by rater rank (29.89 vs 21.21) and adds task success in Reflexion (+8 points HotPotQA). Embellishment 1.3%. Error copying from stored experience.
4. Multi-agent systems as distributed cognition. Structured roles beat free chat in the originating paper (MetaGPT). At matched tokens the gains vanish or reverse (+80.8% to -70.0%). Shared collective memory (CoThinker, blackboard) gives +4 to +6 points at much higher token cost.
5. Trace reading as ethnography of agents. MAST taxonomy kappa 0.88; LLM annotator kappa 0.77; topology fix +15.6 points on ChatDev ProgramDev-v0 (25.0 to 40.6), prompt fix +9.4. LLMs fail at who-and-when attribution: 53.5% agent, 14.2% step.

What changed behaviour and by how much:
- Codebook examples: GPT-3.5 invented codes more than halved.
- Human verification: +24.5 HNS on average.
- Topology redesign: +15.6 points.
- Reflection: +8 points.
- Structured prompts: qualitative only, no numbers.

What did not: GPT-4 few-shot (kappa flat); verification on precise-boundary tasks (-15 and -20 HNS); debate vs self-consistency.

Newest-model gap: most coding and verification data are from 2023-24 models. Frontier-model reruns are missing.

## 7. What our agent should take

Schema parts: G guardrails (G1-G12), S states (S0-S9), O operators (O1-O8), memory. Status: [E] established, [S] single-source, [C] contested. Claim ids K01-K22.

### Add now (established)
1. [E] Treat external notes as task-transforming artifacts, not logs. Part: memory, S0. Evidence: a01, a03, a06, b01, b03 (K01). Note: as a design framing it is established; whether it lowers errors is [S] and is tested in U1.
2. [E] Split work across time: compute targets and checks early at low load, use them late. Part: S0, O, memory. Evidence: a02, a04, b02 (K03).
3. [E] Keep redundant representations and cross-check them, but derive them by independent routes, not by re-reading the same answer. Part: G. Evidence: b02, d08.
4. [E] Do not assume multi-agent beats one agent. Default to a single agent with role-switching passes. Use multi-agent only for decomposable tasks and compare at equal total tokens. Part: O. Evidence: d10, d11 (K19).
5. [E] Report per-task results, not only the mean, whenever a verifier or coder is evaluated. Part: bench practice. Evidence: b14, b15, c03 (K05).
6. [E] When an LLM annotates easy text categories, a rerun majority is an acceptable aggregator; check at equal tokens before relying on it. Part: O. Evidence: c06, c07, b17 (K08).

### Test first
- [S] Closed-label guardrail: stay inside the list and count off-list outputs. Part: G. Evidence: b12, d17 (K07, K22).
- [S] Trace ethnography loop: code 50 own traces for who or what holds which state, change the design, rerun at equal tokens. Part: S. Evidence: d05, d06, d07 (K17).
- [S] Reflection step and memory filter, measured on pass rate. Part: memory. Evidence: b20, d13, d14 (K10, K21).
- [C] Verification pass blind to the first answer versus shown it. Part: O verify, G. Evidence: c03, d08, d09 (K06, K18).
- [C] Task-transforming card versus plain log notes, with a card-use check. Part: memory. Evidence: d01-d03 (K16).
- [S] Consensus of repeat runs versus a single run on coding-like items. Part: O. Evidence: b17, c09-c11 (K09).
- [C] Role-switching single agent versus multi-agent at equal tokens. Part: O. Evidence: c16-c19, d10-d12 (K13).
- [S] Routed verification, only where the first pass is weak or uncertain. Part: O. Evidence: c03.
- [S] Persona grounding for behaviour questions (low priority). Part: none. Evidence: c15, d15, d16 (K12).

## 8. Concrete tests on our bench

All arms use equal total tokens (input plus output). Report per-item-type results and run each arm 3 or more times for variance.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Task-transforming card | Multi-step tasks with computed targets (unit-conversion chains, constraint checks, multi-constraint puzzles) | A: plan pass writes a target card, execution pass matches against it. B: plan pass writes plain log notes. C: no notes | Accuracy; card-read rate per step | A over B by 3-8 points on long tasks; none on short ones |
| T2 Time split | Same items, long chains | A: early planning pass then compare-only pass. B: single pass with the same total tokens | Accuracy; late recomputation errors | A modestly better; gain grows with chain length |
| T3 Blind vs shown verification | Items with a known first-pass error rate of 20-40% | A: verify blind (re-solve, then compare). B: verify shown the first answer. C: no verification | Final accuracy; right-to-wrong and wrong-to-right flip rates | A beats B when the first pass is plausible but wrong; B can lose to C on precise-boundary items |
| T4 Verify routing | Mixed item types, easy and hard | A: verify everything. B: verify only low-confidence or disagreeing items. C: none | Accuracy per type; tokens | B matches A at lower cost; A hurts on high-accuracy types |
| T5 Trace ethnography loop | 50 own traces on a long task set | Before: current design. After: design edited from state-holder labels | Pass rate at equal tokens; labeller kappa on 15 shared traces | +5-15 points if state is lost in one fragile place; kappa above 0.7 |
| T6 Reflection ablation | Long tasks with unit tests | A: memory plus reflection. B: memory only. C: memory with filter | Pass rate; error-copy rate | A over B about +5-8 points (Reflexion size); filter helps if bad records propagate |
| T7 Role-switching vs multi-agent | Sequential (planning) and decomposable (parallel subtasks) | A: one agent role-switching. B: multi-agent at the same total tokens | Accuracy per item type | A wins on sequential; near tie or B wins on decomposable |
| T8 Closed-label guardrail | Coding of 30 traces into a fixed codebook of 15-30 labels | A: stay-in-list guardrail with examples. B: none | Off-list rate; kappa vs human | Off-list drops sharply; kappa flat for strong models |
| T9 Rerun consensus | Coding-like and classification items | A: majority of k runs. B: one deeper pass at k times the tokens | Accuracy; kappa across runs | A over B on noisy label items; no gain on easy ones |
| T10 Open coding | Open coding of 30 traces | Current model with and without the codebook-so-far in context | Invented-code rate; theme overlap with human | Measures the K22 gap; no direction assumed |

## 9. What does not transfer, and why

- The cockpit numbers (speeds, 5-knot callouts, 500 ft) belong to one aircraft type and one airline procedure (a02). Only the pattern transfers.
- Physical affordances (a needle near a bug) are perceptual. A text-only model has no perceptual match. Our version is a textual match, which may not be cheaper for a model. This is open (T1).
- Humans have limited working memory and attention under load. A model has a context window and attention dilution. The mechanisms overlap but differ, so cognitive-load results transfer only loosely.
- Ethnographic validity comes from long immersion (nine months in Alac and Hutchins, six years in the cockpit). An LLM annotator has no such immersion, and its kappa results come from benchmarks (c08).
- Cultural consensus modelling fits knowledge questionnaires, not coded video (b07).
- Believability ratings (Park 2023) are not task success (K10, K21).
- Simulated people tracking survey answers (K12) matter little to our reasoning scaffold, except as a warning about behaviour under incentives.
- Offloading profiles of students (Poquet, b22) concern human-AI team design, not agent internals (K14).
- Token-heavy multi-agent gains (CoThinker, 14,323 tokens) do not transfer to a fixed token budget (d12).
- The conceptual dispute with situated action is not testable on a bench (K04).

## 10. Open questions

- Does a task-transforming artifact lower errors against plain memory in a controlled test, in aviation or elsewhere? None found (d04).
- What are the ship-navigation numbers in Cognition in the Wild (team size, fix cycle, errors)? The book was not opened (critique gap 9).
- Is verification anchoring real? Shen suspects it; no blind-versus-shown test exists (K18).
- What is kappa for current models on open-codebook video and field-note coding, and how often do they invent categories (K22)?
- Does MAST-style trace reading lead to design gains at equal tokens? MAST did not match tokens (K17).
- Do Park's reflection and memory ablations hold for task success in other labs (K21)?
- Do newer models close the incentivised-behaviour gap in simulated people, and why does it exist (K12)?
- Does MetaGPT's structured-role gain survive at equal tokens? Not checked in d10.
- Shen 2026 uses one VLM and no repeat runs. How stable is the per-task spread?
- Was the Hutchins 2024 project joining cognitive ethnography and generative AI published (c23)?
- Seifert and Hutchins 1992 "Error as opportunity" and Hutchins and Klausen 1996 were not read (d19, a23).

## 11. Sources

[V] opened; [M] snippet or citation only. Ids refer to the evidence files.

- [V] Hutchins (1995) How a cockpit remembers its speeds. https://onlinelibrary.wiley.com/doi/10.1207/s15516709cog1903_1 and https://courses.ischool.berkeley.edu/i290-3/s05/papers/How_a_cockpit_remembers_its_speeds.pdf (a01-a05, b01, b02)
- [V] Hollan, Hutchins and Kirsh (2000) Distributed cognition: toward a new foundation for HCI. https://hci.ucsd.edu/hollan/Pubs/tochi-revised.pdf and https://hci.ucsd.edu/hollan/Papers/dcog-tochi.pdf (a06-a10, b03-b05)
- [M] Hutchins (1995) Cognition in the Wild. https://mitpress.mit.edu/9780262581462/cognition-in-the-wild/ ; author page [V] https://pages.ucsd.edu/~ehutchins/ShipNav.html (a11, b10, d19)
- [V] Hutchins project page, robust navigation. https://pages.ucsd.edu/~ehutchins/RobustNav.html (a12)
- [M] Hutchins and Hinton (1984) Why the islands move. https://pages.ucsd.edu/~ehutchins/MicroNav.html (a13)
- [V] Hutchins (2005) Material anchors for conceptual blends. https://pages.ucsd.edu/~ehutchins/documents/MaterialAnchorsPragmatics.pdf (a14)
- [V] Hutchins (2013) The cultural ecosystem of human cognition. https://pages.ucsd.edu/~ehutchins/documents/publishedCulturalEcosystemHumanCog.pdf (a15, a16, a20, b06)
- [V] Alac and Hutchins (2004) I see what you are saying. https://pages.ucsd.edu/~ehutchins/documents/ISeeWhatYouAreSaying.pdf (a17)
- [V] Bender, Hutchins and Medin (2010) Anthropology in cognitive science. https://groups.psych.northwestern.edu/medin/documents/BenderHutchinsMedin.pdf (a18, b07)
- [V] Hutchins and Hazlehurst computational models. https://pages.ucsd.edu/~ehutchins/CulturalProcess.html (a19)
- [M] Kirsh and Maglio (1994). https://onlinelibrary.wiley.com/doi/10.1207/s15516709cog1804_1 (a21, b09)
- [M] Jordan and Henderson (1995) (a22); Hutchins and Klausen (1996) https://pages.ucsd.edu/~ehutchins/dcogAviation.html (a23)
- [V] Hutchins A320 and aviation pages. https://pages.ucsd.edu/~ehutchins/A320Expertise.html (a24)
- [V] An (2025) Cognitive Workspace. https://arxiv.org/abs/2508.13171 (a25, b21)
- [V] Osler (2025) Knowing oneself through and with AI. https://arxiv.org/abs/2512.03682 (a26)
- [M] Theater of Mind listing (a27); [V] Thinking with Many Minds. https://arxiv.org/abs/2501.02348 (b23)
- [V] Wikipedia, Distributed cognition (tertiary). https://en.wikipedia.org/wiki/Distributed_cognition (b08)
- [M] Suchman (1987) Plans and Situated Actions. https://www.cambridge.org/core/books/plans-and-situated-actions/ (b24)
- [V] Kirsten et al. (2024) Decoding Complexity. https://arxiv.org/abs/2403.06607 (b11, b12)
- [V] Shen et al. (2026) Can VLMs analyze human-centered video? https://arxiv.org/abs/2609.27327 (b13-b15, c01-c05, d09)
- [V] Zhang et al. (2024) Redefining qualitative analysis in the AI era. https://arxiv.org/abs/2309.10771 (b16, c10)
- [V] Jain et al. Multi-LLM thematic analysis. https://arxiv.org/abs/2512.20352 (b17)
- [M] QualiGPT kappa numbers (snippet) https://arxiv.org/abs/2310.07061 (b18); [V] description only (c09)
- [M] Review of LLM-human thematic coding (snippet). https://journal-fip.um.ac.id/index.php/edcomtech/article/download/4884/2232/12722 (b19)
- [V] Park et al. (2023) Generative Agents. https://arxiv.org/abs/2304.03442 (b20, c12-c14)
- [V] Poquet et al. (2026) Profiling cognitive offloading. https://arxiv.org/abs/2606.10434 (b22)
- [V] Gilardi, Alizadeh and Kubli (2023). https://arxiv.org/abs/2303.15056 (c06)
- [V] Toernberg (2023). https://arxiv.org/abs/2304.06588 (c07, c08)
- [V] Gao et al. (2023) CollabCoder. https://arxiv.org/abs/2304.07366 (c11)
- [V] Park et al. (2024) Generative agent simulations of 1,000 people. https://arxiv.org/abs/2411.10109 (c15, d16; version differences in critique.md)
- [V] Hong et al. (2024) MetaGPT. https://arxiv.org/abs/2308.00352 (c16)
- [V] Qian et al. (2023) ChatDev. https://arxiv.org/abs/2307.07924 (c17)
- [V] Han and Zhang (2025) Blackboard architecture. https://arxiv.org/abs/2507.01701 (c18)
- [V] Shang et al. (2026) CoThinker. https://arxiv.org/abs/2506.06843 (c19, d12)
- [V] Venkatesh and Cui (2026) Intellectual elites. https://arxiv.org/abs/2604.02674 (c20)
- [V] Liu et al. (2026) Cognitive models as templates. https://arxiv.org/abs/2602.22523 (c21)
- [V] Multi-agent LLM systems for social science (2025). https://arxiv.org/abs/2506.01839 (c22)
- [M] Hutchins 2024 generative-AI project. https://www.youonai.ai/fieldguide/txt/edwinhutchins.html (c23)
- [M] Sumers et al. (2023) CoALA. https://arxiv.org/abs/2309.02427 (c25)
- [V] Haynes et al. (2009). https://pubmed.ncbi.nlm.nih.gov/19144931/ (d01)
- [V] Pronovost et al. (2006). https://pubmed.ncbi.nlm.nih.gov/17192537/ (d02)
- [V] Urbach et al. (2014). https://pubmed.ncbi.nlm.nih.gov/24620866/ (d03)
- [V] Cemri et al. (2025) Why do multi-agent LLM systems fail? https://arxiv.org/abs/2503.13657 (d05, d06)
- [V] Zhang et al. (2025) Who&When. https://arxiv.org/abs/2505.00212 (d07)
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (d08)
- [V] Kim et al. (2026) Towards a science of scaling agent systems. https://arxiv.org/abs/2512.08296 (d10)
- [V] Zhang et al. (2025) Stop overvaluing multi-agent debate. https://arxiv.org/abs/2502.08788 (d11)
- [V] Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366 (d13)
- [V] Xiong et al. (2025) Memory management and experience-following. https://arxiv.org/abs/2505.16067 (d14)
- [V] Toubia et al. (2025) Twin-2K-500. https://arxiv.org/abs/2505.17479 (d15)
- [V] Chew et al. (2023) LACA. https://arxiv.org/abs/2306.14924 (d17)
- [V] Xiao et al. (2023) Codebook with GPT-3. https://arxiv.org/abs/2304.10548 (d18; c26 was the earlier unverified note)
- [M] Gap notes without a source: a28, b25, c24, d04 (weak negatives from a limited search)

## Source audit (2026-11-20)

Fresh auditors re-opened the sources of 4 established claims: 1 confirmed as written, 3 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **F02.02-K01** (now single-source: the sources are not independent). Content is supported (Hutchins 1995 takes the cockpit as unit of analysis and shows the speed bug substitutes a spatial-proximity judgment for scale reading; Hollan, Hutchins and Kirsh 2000 restates it), but both opened sources are by Hutchins, so they are one lab, not independent; the 'memory' part of 'memory and reading task' is framed in the paper as memory shifted into the artifact.
- **F02.02-K03** (now single-source: the sources are not independent). Hutchins 1995 supports every detail (bugs set 25-30 min before landing at light workload, PNF turns a visual speed relation into an aural call-out, card/speech/bug redundancy), but the only other source, Hollan, Hutchins and Kirsh 2000, is a same-lab restatement and does not add independent evidence.
- **F02.02-K19** (reworded: the sources support less). Numbers check out (260 configs, +80.8% to -70.0%, 45% threshold, 5 MAD methods/9 benchmarks/4 models), but Zhang et al. did not match tokens (MAD used far more compute), planning degradation was measured on one benchmark (PlanCraft) not planning in general, and the 45% result is negative returns for multi-agent, not just zero gain. Corrected claim: Multi-agent systems do not generally beat one agent: debate often fails to beat chain of thought or self-consistency even while using much more compute (5 methods, 9 benchmarks, 4 models), and a 260-configuration study with matched tool and total reasoning-token budgets found relative change from +80.8% (decomposable finance) to -70.0% (PlanCraft sequential planning), with all multi-agent variants worse on PlanCraft; where a single agent already exceeds about 45% accuracy, adding agents gave negative returns.
