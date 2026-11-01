# Cognitive artefacts and cockpit studies: deep document

*Subfield F02.05. Built from evidence_a-d.jsonl (about 100 lines, many repeats of the same source), claims.jsonl (K01-K27) and critique.md in this folder. Evidence ids (a01, b13, d03 ...) point to those files. Status marks: [E] established, [S] single-source, [C] contested.*

## 1. What it is

This subfield asks one question. When a tool, a card, a checklist or a spoken callout sits between a person and a task, what does it do to the task?

Two answers compete.

- **Personal view.** The tool makes the person smarter. It adds memory or speed.
- **System view (Hutchins, Norman).** The tool changes the task. A different mental job is done, often a cheaper one. The unit that "remembers" or "computes" is the person plus the tools plus the other people.

Four bodies of work sit here.

1. **Cockpit ethnography.** Hutchins (1995) watched MD-80 crews set and use landing speeds. He argues the cockpit, not the pilot, remembers the speeds. (a01, a03, b01, c01)
2. **Lab work on external representations.** Zhang and Norman (1994) used Tower of Hanoi puzzles in disguise. They showed that where a rule lives (in the head or in the display) changes how hard the same puzzle is. (a08-a11)
3. **Checklist science.** Degani and Wiener (NASA, 1991) on flight-deck checklists. Then surgical and ICU checklists (Haynes, Pronovost, Urbach, Reames, Haugen) as a large natural experiment on whether checklists work. (a16-a22, b04-b12)
4. **LLM work that tests the same ideas.** Scratchpads, program-aided reasoning, agent-computer interfaces, self-correction, checklist-based judging, hard gates. None of it tests Hutchins directly. All of it tests a piece of the claim. (Section 6)

Why this matters for our agent. The schema (SCHEMA.md) already holds guardrails G1-G12 and a code-run state graph. This subfield asks whether those guardrails act like cockpit checklists. It also asks which parts of a checklist make it work: the list, the enforcement, the second reader, or the artefact it is written on.

Main answer in one paragraph. Checks work when they are run, when they use a signal from outside the author, and when the artefact makes the check cheap. A list that is merely shown, or a model grading itself with no outside signal, does little or harms. The best LLM evidence says: gate what code can decide, keep judgement items as advice, and log whether each check actually ran.

## 2. History and theories in depth

### 2.1 Roots

- **Cognitive artefacts (Norman 1991, 1993).** An artefact is an artificial device that holds, shows or operates on information for a representational purpose. Norman's core point: an artefact does not make the person smarter. It changes the task the person faces. His "personal view" versus "system view" split is the frame for everything below. Both works are known here only from a bibliographic record and a quoted definition (a15, c04, opened:false). Do not quote detailed claims from them.
- **Distributed cognition (Hutchins, Hollan, Kirsh).** Two principles (a12). The unit of analysis is set by functional relations, not by skin and skull. The mechanisms include external, material and social ones. Three kinds of distribution: across people, between inside and outside structure, and through time, because the products of earlier events change later events.
- **Epistemic action (Kirsh and Maglio 1994).** In Tetris some moves change the world to ease thinking instead of carrying out a plan. A standard step-by-step information-processing model could not explain human data (a14, abstract only).

### 2.2 Hutchins 1995, "How a cockpit remembers its speeds"

Method. Cognitive ethnography. More than 100 flights observed as a member of crews, plus ground-school training on the 747-400, MD-80 and A320 (a01). The account is "stylized". There are no transcripts, no statistics and no error counts.

Three descriptions of one activity (a02): procedural (what a pilot would say), external representations and processes (observable), and internal representations (inferred). The external description constrains the internal one.

What the cockpit does (a03-a06, a30, b01, b24):

- **Speed card booklet.** A durable memory. Gross weight acts as a filter on it. Weight and speeds are printed on the same card, so picking the card by weight picks the speeds. The computation is built into the object. Cards come in about 2,000 lb steps. Frequent speeds are in larger type. A box surrounds Vref. The booklet is set up 25 to 30 minutes before landing.
- **Speed bugs.** Pointers set on the airspeed indicator. Hutchins: they do not help pilots remember. They change the task. Reading a scale and holding numbers becomes a judgement of spatial closeness between needle and bug.
- **The salmon bug.** Its base is about 10 kt wide. "Needle on the bug body" therefore means within 5 kt of Vref. The 5 kt callout tolerance matches. A Boeing 757/767 indicator engineer confirmed the width is not in the specification. It fits between large ticks at 10 kt intervals. This is opportunistic use of structure nobody planned (a06, b03).
- **Time shifting.** Speeds are computed in a low-workload phase (descent, before 18,000 ft) and used 10 to 15 minutes later in a high-workload phase (a04).
- **Social shifting.** The pilot not flying turns a visual deviation into a spoken one, so the pilot flying keeps eyes outside. Callout at 500 ft AFL, example: "Five hundred feet, plus four, seven down" (4 kt fast, 700 ft/min down). Callout any time speed deviates more than 5 kt (a03, c02).
- **Redundancy.** Challenge and response: "Set on the left and cross-checked" and "Set on the right and cross-checked". Two airspeed indicators. The speed card sits a few inches from the weight display so a wrong-weight pick is visible. Setting approach speeds is a "killer item": Hutchins saw no crew fail to set them, no count given (a05, b24). Part of the redundancy is a by-product. The flap call by one pilot and handle move by the other was introduced to free hands, and cross-checking followed.

Fragile parts (b02): transposition errors on cards are "probably" the most frequent error (cited from Norman 1991 and Wickens and Flach 1988, not measured here). Rehearsed speeds are open to interference. A breakdown pushes pilots into a different strategy.

The central claim (a07, c01): "Speed bugs do not help pilots remember speeds; rather, they are part of the process by which the cockpit system remembers speeds." Individual-memory theory explains why the system needs so many outside parts, not how the system works. Cockpit memory is a mix of recognition, recall, pattern matching, cross-modality checking, construction and reconstruction.

Weakness (K06, b23, critique.md): no with-and-without comparison. No crew without bugs. An internal-representation account predicts the same behaviour in this setting. Hutchins himself writes that "lacking additional evidence, we cannot know the duration or quality of these memories" (a02). Treat the claim as a design description, not a measured effect.

### 2.3 Zhang and Norman 1994, distributed representations

Idea (a08): a task's representation is a set of internal and external representations that together carry the abstract task structure. Method: take a hierarchical task, split it into levels, test each level. Four experiments on Tower of Hanoi isomorphs (cups of coffee and objects). N = 24 (Exp 1A), 24 (1B), 18 (Exp 2), 36 (Exp 3), all undergraduates.

Results are in section 3. Short form: same abstract problem, different order of difficulty depending on which rules were visible in the display; externalised rules gave no errors; location beat size and colour for carrying the same dimension.

### 2.4 Checklist science

**Aviation.** Degani and Wiener, NASA CR-177549, 71 pages (a16-a18, b04, d15, d16). Sources: NTSB 1983-88 accidents, 1969-88 recommendations, ASRS 1981-89 reports, interviews. Three accidents in 15 months had checklist misuse as a probable cause: Air New Orleans BAe J-31, Northwest 255 (MD-80, Detroit, no flap or slat takeoff) and Delta 1141 (B-727, Dallas-Fort Worth, same cause). Two methods: challenge-response and do-list (call-do-response). Challenge-response has two redundancies: configuration redundancy (the list checks only what was already set from memory) and mutual redundancy (two crew verify). The do-list drops configuration redundancy. Some airlines let one pilot challenge and answer himself, which removes mutual redundancy. Northwest 255: the TAXI checklist normally ran 1 to 2 minutes after the plane moved. Interruptions (new weather, runway data) removed the usual external cue and the list was missed. Takeoff, approach and landing are 27% of flight time and 76.3% of hull-loss accidents (Lautman and Gallimore 1988). Monan 1979 ASRS study: 169 distraction reports, 22 tied to checklist procedures. **The report has no empirical skip rates.** ASRS narratives were used as illustration and were not analysed statistically. The 1993 Human Factors paper was not opened. A search summary gave "42 crews, 72 flights, 140 hours" (c08); it is unverified. Do not cite it.

**Medicine.** Pronovost 2006 and Haynes 2009 made checklists famous. Later work (Urbach, Reames, Matching Michigan) did not reproduce the size of effect. Section 5 has the numbers and the reading.

### 2.5 Where LLM work meets this

- Scratchpad, PAL, interpreter use: external state and external computation (Norman's "tool changes the task").
- SWE-agent: interface design for a fixed model (Norman's artefact design).
- Self-refine, CoVe, TICK, CRITIC: checks and checklists for models.
- Hard gates, ledgers, SOPBench: enforced checklists and "ticking without doing".
- Cognitive Workspace (c20): cites Hutchins and extended mind, self-reported only.

## 3. Core findings with exact numbers

Status: [E] established, [S] single source, [C] contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Speed bugs turn recall into adjacency judgement | Bug base about 10 kt; on the bug = within 5 kt of Vref; callout over 5 kt; more than 100 flights; no statistics | Hutchins 1995 (a01, a03, b01) | [S] descriptive |
| Speeds computed early, used 10-15 min later | Computed before 18,000 ft; cards in 2,000 lb steps; booklet set 25-30 min before landing | Hutchins 1995 (a04, b02) | [S] descriptive |
| No with/without test of bugs | None reported | Hutchins 1995 (b23) | [E] that the gap exists |
| External rules are error-proof in Hanoi isomorphs | Exp 2: 18 students, 54 games; errors on external rules = 0, all errors on internal rules; main effects p<.05 time and steps, p<.005 errors | Zhang and Norman 1994 (a10) | [S] |
| Order of difficulty depends on what is external | Exp 1A (all internal): II < II3 < II234 and II23, II234 vs II23 ns. Exp 1B (all but one external): difficulty rises with rule count; no errors; slowest to fastest solution time up to 10:1 | Zhang and Norman (a09) | [S] |
| Same dimension easier by location than size or colour | Exp 3, 36 students; size vs location p<.01 (time), p<.03 (errors); size vs colour not different on nominal | Zhang and Norman (a11) | [S] |
| Checklist misuse and interruption cause accidents | 3 accidents in 15 months; 169 distraction reports, 22 checklist-linked; 76.3% of hull losses in 27% of flight time | Degani and Wiener 1991 (a16, a18, d15) | [E] (2 sources) |
| No skip-rate data in the aviation checklist report | ASRS not analysed statistically | Degani and Wiener (d15) | [E] |
| WHO checklist, uncontrolled | 8 hospitals; 3,733 before, 3,955 after; deaths 1.5% to 0.8% (p=.003); complications 11.0% to 7.0% (p<.001) | Haynes 2009 (a20, b05) | [E] as observed; [C] as cause |
| Keystone ICU programme | 103 of 108 ICUs; 375,757 catheter-days; median 2.7 to 0 per 1,000 catheter-days (3 months); mean 7.7 to 1.4 (16-18 months); IRR 0.62 then 0.34 | Pronovost 2006 (a19, b11) | [E] as observed; bundled with culture and feedback |
| Mandated checklist at scale: null | 101 Ontario hospitals; 109,341 before, 106,370 after; death 0.71% to 0.65%, OR 0.91 (0.80-1.03), p=.13; complications 3.86% to 3.82%, OR 0.97 (0.90-1.03) | Urbach 2014 (a21, b06) | [E] |
| Michigan surgery programme: null (two studies) | 64,891 pts, 29 hospitals: complications 12.4% to 13.2% (p=.26), mortality 2.1% to 1.9% (p=.32); Medicare 1,002,241 pts, 95 vs 950 hospitals: mortality RR 1.03 (0.97-1.10), complications RR 1.03 (0.99-1.07) | Reames 2015 x2 (b09, b10) | [E] |
| Matching Michigan (UK ICUs) | 98 staff interviews; 19 ICUs observed, 17 in programme; 1 transformed, 5 strengthened existing work, 11 little change | Dixon-Woods 2013 (b12) | [E] qualitative |
| Randomised evidence favours WHO checklist for complications | Stepped-wedge, 5 clusters, 2 hospitals: 2,212 vs 2,263 procedures; complications 19.9% to 11.5%; adj OR 1.95 (1.59-2.40); mortality 1.6% to 1.0% ns | Haugen 2015 (b08) | [C] small |
| Pooled checklist effect | 7 studies: any complication RR 0.59 (0.47-0.74); mortality RR 0.77 (0.60-0.98); SSI RR 0.57; published before Urbach | Bergs 2014 (b07) | [C] |
| 2024 review quality filter | 17,821 titles, 93 retrieved, 13 of enough quality; 9 of 10 reporting complications found a drop | Review 2024 (a22) | [C] |
| Effect shrinks as design strengthens | Haynes -36% relative complications, Haugen -42% (2 hospitals), Urbach OR 0.97, Reames RR 1.03 | Synthesis (b25) | [E] pattern; mechanism argued |
| Self-review with no outside signal hurts | GPT-3.5 CommonSenseQA 75.8 to 38.1 (first pass) then 41.8; GSM8K 75.9 to 75.1 to 74.7 (1, 3, 5 calls); GPT-4 GSM8K 95.5 to 91.5 to 89.0; HotpotQA GPT-3.5 26.0 to 25.0 | Huang 2024 (a26, b13) | [E] |
| Oracle labels explain earlier gains | GPT-3.5 GSM8K 84.3, CSQA 89.7; GPT-4 GSM8K 97.5 with oracle | Huang 2024 (b13) | [E] |
| Sound external verifier gives the gain | 100 instances/domain: Game of 24 standard 5%, LLM+LLM 3%, LLM+sound verifier 36-38%; Blocksworld 40%, 55%, 60-87%; graph colouring 16%, 2%, 38%; LLM verifier false-negative 20.7% (Game of 24), 97.09% (Mystery Blocksworld) | Stechly 2024 (b14) | [E] |
| Plain sampling with the same verifier is strong | Game of 24 k=15 28%, k=25 42% vs critique 36-38%; Blocksworld k=15 68%, k=25 72% vs 83-87% | Stechly 2024 (b15) | [E] |
| Tools carry the gain in CRITIC | text-davinci-003 HotpotQA F1 CoT 46.1, no tool 46.1, with tool 50.5; AmbigNQ 58.6/58.3/64.9; TriviaQA 74.5/74.7/80.6; GSM8K PoT 70.1, CRITIC 72.2, CRITIC without tool 68.3 | Gou 2024 (d06) | [E] |
| Prompted self-feedback rarely works | Survey; no success except in tasks unusually suited | Kamoi 2024 (a29, d07) | [E] |
| Factored check beats joint check | Llama 65B: FACTSCORE 55.9 base, 60.8 joint, 63.7 factored, 71.4 factor+revise; list precision 0.17 base, 0.29 joint, 0.32 factored, 0.36 two-step; MultiSpanQA F1 0.39, 0.46, 0.48 | Dhuliawala 2023 (a27, b16, d05) | [S] no equal-token control |
| Model-written YES/NO checklists improve judging | Human agreement 46.4% to 52.2%; Krippendorff alpha 0.194 to 0.256; check-then-score 48.7 | TICK (a23, b17) | [E] (3 related lines, 1 paper) |
| STICK refinement | Command-R+: InFoBench +6.5, WildBench +7.1, LiveBench +3.8 (reasoning +7.8); GPT-4o LiveBench +0.8; Self-Refine -8.3 both models; best-of-8 WildBench 64.9 to 71.2 | TICK (b17) | [S] small for strong model |
| Checklist rewards help training | Qwen2.5-7B: FollowBench hard +5.4% rel, InFoBench +6.9%, Arena-Hard +6.4%; CM2 over SFT: tau-Bench +8, BFCL-V4 +10, ToolSandbox +12 | RLCF (a24), CM2 (b21) | [E] training, not scaffold |
| Hard gate beats shown state | Qwen3-235B, 128 episodes/cell: S=10 raw 0.38, shown checklist 0.55, ledger 0.70, directive gate 0.84, enforcement gate 0.98; S=15 dense 0.50, 0.59, 0.79, 0.87, 0.98; gate used 0.92x and 0.79x raw-transcript tokens | Zhang 2026 (d01, d03) | [S] preprint |
| Gate helps only when violations are frequent and code-decidable | tau2 airline 235B pass^1 0.39 to 0.54; 35B no change; PM-Bench 35B raw 0.63, checklist 0.72, judgement-bound gate 0.55, state-bound gate 0.66; with thinking on gap within noise (0.95 vs 0.88) | Zhang 2026 (b19, d02) | [S] |
| Ticking without doing exists in LLM agents | 24 of 26 (S=10) and 20 of 20 (S=15) on-turn re-executions were steps already marked done; raw transcript at S=10: 70 re-executions, 31 premature, 35 omissions per 128 episodes | Zhang 2026 (d03) | [S]; [E] for the effect via SOPBench |
| SOPBench scores skipped checks as failure | 167 tools, 7 domains, 903 cases; o4-mini-high 76.08, Gemini-2.0-Flash-Thinking 67.66, DeepSeek-R1 62.13, GPT-4o 62.13, Claude-3.7-Sonnet 54.26; only 5 models above 60% (row alignment approximate) | Li 2025 (d04) | [S] |
| Mandatory validation causes failures | 307 skill-induced failures: 125 functional, 182 efficiency; 67 from excessive verification, 30 from heavy pipelines | Skills paper 2026 (b20) | [C] abstract only |
| Verification is a main multi-agent failure class | 1,600+ traces, 7 frameworks, failure rate 41% to 86.7%; premature termination 6.20%, no verification 8.20%, incorrect verification 9.10%; kappa 0.88 | MAST (c11) | [S] |
| External scratchpad helps | Polynomial: few-shot 8.8% to 20.1%, fine-tuned 31.8% to 50.7%; program execution 11/20 to 26.5/41.5; 9-10 digit addition fails without scratchpad | Nye 2021 (a28, c18) | [E] |
| Offload to interpreter | GSM8K PAL 72.0 vs CoT 65.6; "run it in text" 23.2, only +4.5 over direct | PAL (b18) | [E] |
| Interface design moves a fixed model | 2,294 SWE-bench tasks 12.47% vs prior 3.8%; Lite 300: ACI +10.7 over shell; editor lint 18.0, no lint 15.0, no edit tool 10.3; viewer 100 lines 18.0 vs full file 12.7; search summarized 18.0, none 15.7, iterative 12.0; Claude 3 Opus 10.5% | SWE-agent (c12) | [S] tool and prompt confounded |
| Cognitive tools raise maths | Qwen2.5-7B 75.8 to 80.5; 32B 79.6 to 84.2; Llama3.1-8B 48.7 to 59.4; Llama3.3-70B 52.8 to 79.5; AIME GPT-4.1 32.0 to 53.0; Qwen2.5-32B AIME 17.2 to 32.1; Qwen2.5-7B AIME 12.5 to 14.6 (noise); Llama3.1-8B MATH500 50.7 vs 53.3 CoT | Ebouky 2025 (a25) | [S] |
| At matched budget, debate is voting | Self-consistency 20 samples matches or beats MAD (18 queries) and Reflexion (19); GSM8K 9 responses SC 88.2 vs debate 83.0; Qwen2.5-7B MAD T=2 0.7377, T=3 0.7112, T=5 0.7050 vs single 0.7205 | Wang 2024 (d08), Choi 2025 (d10), Huang (b13) | [E] |
| Counter-result: Pareto debate/MoA | MMLU-Pro n=1000: CoT 64.3, SC 68.7 (10 samples), debate 70.0, MoA 71.4; +1.3 and +2.7 over SC, interval about plus or minus 3 | Wunderlich 2026 (d09) | [C] |
| LLM errors are correlated | 350+ models; agree 60% of the time when both wrong (one dataset); more for same provider and larger models | Kim 2025 (d11) | [S] |
| Self-conditioning decays long tasks | Qwen3-32B below 50% in 15 turns despite near-perfect first step; DeepSeek-V3 no-think fails at about 4 steps per turn; R1 over 100; GPT-5 over 2100; Claude-4 Sonnet 432 | Sinha 2025 (d12) | [S] |
| Output format changes accuracy | Strict JSON/XML/YAML lowers reasoning (Tam 2024, abstract); GPT-3.5 varies up to 40% by template on code translation (He 2024, abstract) | d13, d14 | [S] abstract only |
| Cognitive Workspace | 58.6% memory reuse (54-60%) vs 0% RAG; 17-18% net efficiency | c20 | [S] self-reported, not verified |

## 4. Mechanisms and models

Each mechanism below is written so it can be built.

### 4.1 Task transformation (Norman, Hutchins, K01)

The artefact swaps a hard mental operation for an easy one.

| Hard operation | Artefact | Easy operation |
|---|---|---|
| Recall weight-dependent speed, read scale, subtract | Card + bug | Is the needle on the bug? |
| Compute a sum in head | Interpreter / tool | Read a number |
| Judge "is this answer right" | Test, validator | Read pass/fail |
| Hold rule 3 of 4 in mind | Display that shows rule 3 | Look |

Implementation rule. For every check in the schema, ask: what is the hard operation the model would do, and can code turn it into a lookup, a diff or a pass/fail? If yes, build the artefact. If no, the check is a judgement and has low value (section 5).

### 4.2 Chain of media (K02)

Constants are computed once at low load, written to a durable store, and read back at high load. In agent form:

1. Early state (S1/S2): compute thresholds, definitions, units, target format, constants. Write each as a line in a ledger (key, value, how derived).
2. Later states (S4, S5, S8): the program injects the ledger values into the prompt and checks that outputs match them. The model does not recompute.
3. Read-back: a line is "done" only when code sees a tool call or a matched string, not when the model says so (K21).

Status: the ledger-versus-recomputation test has not been run (Gap 5). Zhang 2026 shows a self-written ledger beat a shown checklist (0.70 vs 0.55 at S=10) but did not compare it to recomputing. Sinha 2025 shows why it might matter: errors that stay in context make later steps worse.

### 4.3 Redundancy (K03, K24)

Cockpit redundancy has three kinds: representation (card + bug + indicator), processing (two people read), checking (challenge and response, callouts on deviation). Degani and Wiener add: configuration redundancy and mutual redundancy.

For an LLM, redundancy only works if the second reader is independent. Same-family samples are not. Kim 2025: two wrong models agree 60% of the time on one dataset. Independence has to come from a different view of the input, a tool, or retrieval. A checker that sees a different representation (code result vs prose answer) is closer to a second pilot looking at a second indicator than a second sample of the same model is.

Implementation: rate a checker by the overlap of its missed errors with the main solver's. Pick the pair with least overlap (U4 test).

### 4.4 Challenge-response as a protocol

The cockpit item is a fixed phrase with a value: "Flight instruments and bugs: set and cross-checked." Not "ok". Agent form: a check returns a structured record `{item, expected, observed, source, pass}` produced by code, and the program refuses to advance until every record has `source` set to a tool call or a read-back. This is a gate.

### 4.5 Hard gate versus shown state (K20)

Zhang 2026 ladder, same model and episodes, S=10:

| Rung | What the agent gets | Strict success |
|---|---|---|
| Raw transcript | Nothing extra | 0.38 |
| Shown checklist | Accurate state as text | 0.55 |
| Self-written ledger | Agent keeps own marks | 0.70 |
| Directive gate | Per-turn instruction from state | 0.84 |
| Enforcement gate | Code refuses violating actions | 0.98 |

Gate conditions (d02): the violation must be decidable by code; the agent must violate often; the matcher and compiled state must be right (corrupting state degrades success monotonically). When the gate encodes a judgement (PM-Bench), it fell below the raw transcript (0.55 vs 0.63).

### 4.6 Factored verification (K13)

CoVe: draft, plan verification questions, answer each in a fresh context that does not show the draft, then revise. Cuts copying of the draft's errors. Costs many more calls than one pass. No equal-call control exists.

### 4.7 Why checklist effects shrink at scale (K09)

Working reading from b25, b12, a21 and editorials: a checklist is a trigger for a practice. If the practice and culture are present, the list helps. If staff tick boxes without doing the step, no gain (Urbach compliance was near 100% by report but outcomes did not move). This is argued by editorialists. It is not measured in those studies. The LLM analogue of ticking without doing is measured (d03, d04).

### 4.8 Cost of over-checking (K15)

Mandatory validation produced 67 of 307 skill-induced failures through excessive verification (b20). Degani and Wiener argue long lists invite non-use (argued, not measured). No dose-response curve exists. Treat list length as a parameter to test.

## 5. What holds up

### 5.1 Replications and failures

| Claim | Original | Replication or test | Verdict |
|---|---|---|---|
| Checklist cuts surgical harm | Haynes 2009: 11.0% to 7.0% complications, 1.5% to 0.8% deaths | Urbach 2014: OR 0.97 and 0.91, null; Reames x2 null; Haugen RCT: complications 19.9% to 11.5%, deaths ns | Partial. Effect shrinks with design strength and scale. |
| ICU checklist cuts line infections | Pronovost 2006: median 2.7 to 0 | Matching Michigan: 1 of 17 units transformed | Effect needs local practice and culture. |
| Cockpit memory is a system property | Hutchins 1995 | No with/without test; no experimental test of the claim | Description, not tested. |
| External rules reduce errors | Zhang and Norman 1994, small N | Consistent with Kotovsky, Hayes and Simon (1985) on solution times (a10) | Plausible, student sample. |
| LLM self-correction works | Self-Refine (about 20% average gain), Reflexion (HumanEval 91% vs 80%) | Huang 2024: no gain without outside signal; Kamoi 2024 survey | Gains need an external signal. |
| Debate beats voting | MAD papers | Wang 2024, Choi 2025, Huang: no gain at matched budget; Wunderlich 2026: +1.3 to +2.7, within noise | Mostly voting. |

### 5.2 Moderators that recur

- **Enforcement and local culture** decide checklist outcomes in people (b12, b25). In agents: hard gate 0.98 vs shown checklist 0.55 (d01).
- **Outside signal.** Tool, test, retrieval or oracle label. Without it, review is flat or negative (Huang, CRITIC, Kamoi, Stechly).
- **Model size and reasoning mode.** CRITIC tool benefit grows with size (TabMWP +4.7, +9.4, +16.0 at 7B, 13B, 70B). Gate benefit vanishes when the agent rarely violates (35B on tau2) and shrinks with thinking on (d02). STICK gain is small for GPT-4o (+0.8).
- **Decidability.** Code-decidable items gain from gates. Judgement-bound gates lose (d02).
- **Independence of the second reader.** Same-family errors correlate (d11).
- **Compute matching.** Gains from critique loops often vanish against best-of-N with the same verifier (b15, d08).

### 5.3 What worked

- External scratchpad and interpreter (Nye, PAL, CRITIC with tools).
- Hard gates on code-decidable state (d01).
- Per-item YES/NO checklists for judging and refinement (TICK), mainly for weaker models.
- Factored verification (CoVe), though not tested at equal calls.
- Interface design: lint on edit, 100-line viewer, summarised search (SWE-agent).
- Checklist-based reward in training (RLCF, CM2). Training, not a scaffold.

### 5.4 What did not work

- Prompted self-review of reasoning with no signal (Huang).
- LLM-as-verifier in some domains (false-negative rate 97.09% on Mystery Blocksworld).
- Asking the model to "run" a program in text (PAL +4.5 only).
- Vanilla Self-Refine on LiveBench (-8.3 in TICK).
- Debate and Reflexion at equal budget.
- Iterative search tool (12.0, below no search 15.7).
- A shown accurate checklist as the only intervention (0.55 vs gate 0.98).
- Mandatory validation in every skill (b20).

### 5.5 Weak spots to remember (critique.md)

- Hutchins has no statistics and no control.
- Zhang and Norman used undergraduates, N = 18 to 36 per experiment.
- Haynes is uncontrolled before-after. Haugen is two hospitals. Bergs pools seven mostly weak studies.
- No LLM study tests Hutchins' mechanism directly. SWE-agent, PAL and scratchpad confound tool with prompt.
- LLM numbers come from different models and benchmarks and are not comparable.
- CoVe's "hallucinated entities 2.95 to 0.68" is unreliable: 2.95 belongs to Llama 2 70B Chat CoT; Llama 65B few-shot is 0.98. Do not cite it.
- Huang's table columns are LLM calls (1, 3, 5), not rounds. Some earlier lines (b13, c09) mislabel them.
- Several 2026 preprints (b19-b22, c20, c22) have not been checked by a second pass.

## 6. Language models

No study tests "a chain of media beats one long context". These are the closest results.

### 6.1 External state and computation

| Study | Model | Result |
|---|---|---|
| Scratchpad (Nye 2021) | small 2021 transformers | Polynomial few-shot 8.8% to 20.1%; fine-tuned 31.8% to 50.7%; long addition fails without |
| PAL (Gao 2023) | Codex | GSM8K 72.0 vs 65.6; text "run" only 23.2 |
| Long-horizon execution (Sinha 2025) | Qwen3-32B, DeepSeek-V3, R1, GPT-5, Claude-4 | Self-conditioning; thinking helps; scale does not remove it |
| Cognitive Workspace (c20) | not verified | 58.6% reuse vs 0% RAG; self-reported |

### 6.2 Tool and interface design

SWE-agent: 12.47% of 2,294 tasks, prior best 3.8%. Ablations on 300 Lite tasks, ACI over shell +10.7; lint 18.0 vs 15.0 vs 10.3. Ported to Claude 3 Opus at 10.5%. Outside code, the evidence is abstract-level only: strict structured output lowers reasoning accuracy (Tam 2024); template alone moves GPT-3.5 by up to 40% on code translation (He 2024; GPT-4 less). Cognitive tools (Ebouky 2025) raised maths accuracy, unevenly, and sometimes ended below plain CoT.

### 6.3 Checks and self-correction

Section 3 has the numbers. Summary: gains come with an outside signal (oracle label, tool, test, sound verifier) and vanish or reverse without it. Plain sampling at equal budget is a strong rival. Model-written checklists are the exception that sometimes works without a tool (TICK, +7.8 on LiveBench reasoning for Command-R+), but the gain was small for GPT-4o and quality fell or plateaued by iteration four.

### 6.4 Enforced checklists and gates

Zhang 2026 is the only controlled ladder found. Qwen3-235B no-thinking: 0.38, 0.55, 0.70, 0.84, 0.98 from raw to gate at S=10. Tokens per gated run: 0.92x and 0.79x the raw transcript. At 35B on tau2 airline, no gain, because the model rarely violates policy. With thinking on, gates were within noise. One task family, one preprint.

### 6.5 Compliance without doing

- Zhang 2026: 24 of 26 and 20 of 20 on-turn re-executions repeated steps already marked done in the agent's own ledger.
- SOPBench: a case passes only if the final state is right and required check calls were made first. Only 5 models above 60%. Appending "use the most appropriate tool asap" cut pass rates sharply (largest relative drop 60.1%).
- GitAuto blog (d17, not opened): 41-check list in prompt, 3 categories ignored. Anecdote.
- MAST: 8.20% of traces show no or incomplete verification and 9.10% incorrect verification.

### 6.6 Second readers

MoA with different models +2.7 over SC, debate +1.3, both within about plus or minus 3 on n=1000 (Wunderlich). Debate adds nothing over voting in seven benchmarks (Choi). Errors correlate across models (Kim). Two independent checkers versus one checker twice has not been tested directly.

### 6.7 Cockpit-LLM systems

AdaptiveCoPilot (c22): N=8 licensed pilots in VR, no effect size seen. LeRAAT and Virtual Co-Pilot 90.5% and 86.5% (c23): search summary only. Not usable as evidence.

## 7. What our agent should take

Status marks: [E], [S], [C]. Schema part: G, S, O or memory.

### Add now (established)

1. **Enforce code-decidable guardrails in code; keep judgement items as advice.** G / enforcement. [E] for the principle (Haynes-vs-Urbach pattern, b25); the size of the gain is [S] (Zhang 2026, d01, d02). Evidence: K09, K20, d01, d02, b25. G2, G3, G5 and the S8 final check are already code-decidable. Make the program refuse to advance, not just tell the model. Size of gain on our tasks is untested (U1).
2. **Every check is tool-backed or dropped.** G2 / S4 / S8. [E]. Evidence: K11, K12, K22, a26, b14, d06, d07. A check with no outside signal must be tested on and off and dropped unless it helps (U5). This agrees with G2 and G10.
3. **Compare any added checker with best-of-N at equal tokens.** G7 / G9. [E]. Evidence: K12, K23, b15, d08, d10. Already G7 and G9. Keep it as a rule for every new element from this subfield.
4. **Do not rely on the model's own "done" mark.** G / audit. [E] (SOPBench, Zhang 2026). Evidence: K21, d03, d04. Log whether each guardrail check was actually executed by code (tool call, read-back, matched string), separate from the model's claim. Add to section 6 run log (U10).
5. **Offload exact computation to a tool or interpreter.** S / O. [E]. Evidence: K16, a28, b18. The model writes the program; the interpreter runs it. Do not ask it to simulate a run in text.
6. **Do not cite Hutchins as proof that artefacts improve accuracy.** Evidence hygiene. [E]. K06, K27, b23, d15. Use it as design inspiration only.
7. **Expect effect shrinkage.** Planning rule: first results on a new check overstate (Haynes to Urbach). Require equal-token wins on at least two item types before adding.

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Gate vs advice on one decidable guardrail | G / enforcement | [S] | K20, d01-d03 |
| T2 | Ledger of early-computed constants, read back later, vs recompute | S / memory | [S] | K02, K25, d03, d12 |
| T3 | Factored check in fresh context vs in-context check vs best-of-N | O / S8 | [S] | K13, a27, d05 |
| T4 | Second checker with different view vs same checker twice | G / redundancy | [S] and [C] | K03, K24, d09-d11 |
| T5 | Checklist length dose-response (3, 8, 20 items) | G | [C] | K15, b20, d15 |
| T6 | Per-task YES/NO checklist, generated once, vs unstructured self-critique | G / S8 | [E] for judging, [S] for our use | K14, a23, b17 |
| T7 | Interface-only change: evidence format and error messages | O / S4 | [S] | K17, K26, c12, d13, d14 |
| T8 | Interruption robustness: inject a distractor turn, with and without step ledger | G / S | [E] in aviation, untested in LLM | K07, a18, d16 |
| T9 | Representation of state: list vs table vs grid | S2 | [S] | K05, a11 |
| T10 | Over-verification budget cap | G7 / G12 | [C] | K15, K18, b20, c11 |

UNKNOWNS.md holds the designs and thresholds.

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens (include setup and checker tokens). Report accuracy, tokens, and number of guardrail violations. Use at least two models and two item types. Pre-set the threshold before running.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| 1 | Tasks with a code-decidable rule (output format, units, number matches ledger, tests were run) | A: rule shown in prompt. B: rule enforced by a gate that refuses and returns the failed field | Violation rate; final accuracy | B cuts violations by more than half; accuracy gain only where A violates more than 20%; little or none for strong thinking models |
| 2 | Multi-step tasks with constants computed in step 1 (unit conversions, thresholds), lengths 5, 10, 20, 40 steps | A: recompute in place. B: ledger read back. C: ledger plus read-back check | Accuracy by length; recompute count | Gap grows with length; C at least B |
| 3 | Fact or code-claim drafts with a draft and 3 to 5 check questions | A: in-context check. B: factored, fresh context. C: best-of-N at equal tokens | Errors caught; false alarms | B beats A by 1.5 to 4 points (CoVe size); B vs C unknown |
| 4 | Items with a ground truth the model can miss | A: same model checks twice. B: different-view checker (tool or reformatted input). C: different family | Overlap of missed errors; caught-error rate | B has the least overlap; A is near 60% overlap |
| 5 | Same tasks, checklist of 3, 8 and 20 items | Three lengths | Accuracy; tokens; items skipped | Peak at a middle length; over-verification cost at 20 |
| 6 | Instruction-following and open tasks | A: free self-critique. B: model-written YES/NO checklist generated once. C: no review | Accuracy; tokens | B > A; A <= C on reasoning tasks (Huang) |
| 7 | Same items with tool output in plain text vs structured, and with or without a lint-style error message | Fixed model, interface only | Accuracy | A few points; direction unknown outside code |
| 8 | Long procedures with an injected distractor turn at a random step | A: no ledger. B: ledger of done steps checked by code | Steps skipped or repeated | B reduces skips (Northwest 255 analogue) |
| 9 | Spatial or tabular puzzles | State as prose list, as table, as grid | Accuracy | Small gains for table or grid; location beat size and colour in humans |
| 10 | Every self-review check in the schema | On vs off | Accuracy at equal tokens | Drop checks with no tool and no gain |

Logging for all: whether each check was executed (tool call or read-back) vs claimed.

## 9. What does not transfer, and why

- **Memory.** Pilots forget. A model does not forget a line in context, but it can fail to use it and it conditions on its own earlier errors. The ledger's value is correctness and checkability, not capacity. Sinha 2025 supports this only indirectly.
- **Drill.** Pilots drill the checklist until it is routine. Models do not carry drill across runs. Behaviour must be enforced on each run.
- **Real redundancy.** A second pilot is independent. A second sample from the same model is not (Kim 2025; G4).
- **Hutchins' bug as perception.** The bug turns a number into a spatial fit, an operation people do fast with their eyes. A text model has no such perceptual advantage. The analogue is a lookup, a diff or a pass/fail from code, not a picture.
- **Hawthorne and culture.** Medical checklist gains partly rest on team culture and attention to being observed. An agent has neither. This may make enforcement matter more.
- **Human-scale checklists.** 5 to 19 items for people; the right size for a model is unknown (U6).
- **Ethnographic evidence.** Hutchins' description gives no effect size, so it cannot predict a threshold.
- **Training-time checklist rewards (RLCF, CM2).** Valid for training pipelines, not for our inference scaffold.
- **Older model results.** CoVe, CRITIC, PAL, scratchpad are Llama 65B, text-davinci-003, Codex, 2021 transformers. Current reasoning models may behave differently; thinking-on shrinks gate gaps (d02).

## 10. Open questions

1. Does a hard gate beat advice at equal tokens on our benchmarks, and for which guardrails (Gap 1; Zhang 2026 closes it for one family only)?
2. Which of G1-G12 have an outside signal? Which are pure self-review and may cost accuracy (Gap 2)?
3. Does factored checking beat in-context checking at equal tokens, and how much is just best-of-N (Gap 3)?
4. What is the best number of checklist items (Gap 4)? No dose-response data exists.
5. Does a ledger of early constants beat recomputation, and at what task length (Gap 5)?
6. Does an interface change alone move accuracy outside code (Gap 6)? Evidence is abstract-level.
7. Do two independent checkers with different views beat one checker run twice (Gap 7)? No controlled test found.
8. How often do our agents tick without doing (Gap 8)? Prevalence on our agent is unmeasured.
9. Degani and Wiener 1993 and Norman 1991/1993 are not verified from full text (Gap 9). The 1991 report has no skip rates.
10. Why did checklist effects shrink at scale in medicine? Real use versus paper use is argued, not measured.
11. Does a gate hold up once the agent thinks (thinking on shrinks the ladder)? Test with our default mode.
12. Is there an agent "killer item": one step that is always gated (for example, run the held-out check before submit)?

## 11. Sources

[V] = opened and read this session (or full text re-checked in critique.md). [M] = snippet, abstract-level or bibliographic record only.

**Cockpit and distributed cognition**
- [V] Hutchins (1995) How a cockpit remembers its speeds. Cognitive Science 19(3):265-288. https://courses.ischool.berkeley.edu/i290-3/s05/papers/How_a_cockpit_remembers_its_speeds.pdf and https://pages.ucsd.edu/~johnson/COGS102A/Hutchins95
- [V] Reader notes on Hutchins (secondary only). https://ferd.ca/notes/paper-how-a-cockpit-remembers-its-speed.html
- [V] Zhang and Norman (1994) Representations in distributed cognitive tasks. Cognitive Science 18(1):87-122. https://pages.ucsd.edu/~scoulson/203/zhang.pdf (some statistics garbled in the text copy)
- [V] Hollan, Hutchins and Kirsh (2000) Distributed cognition: toward a new foundation for HCI research. ACM TOCHI 7(2). https://hci.ucsd.edu/hollan/Pubs/tochi-revised.pdf (the ACM version, c25, was not opened: [M] https://doi.org/10.1145/353485.353487)
- [M] Kirsh and Maglio (1994) On distinguishing epistemic from pragmatic action. Cognitive Science 18(4). https://doi.org/10.1207/s15516709cog1804_1 (abstract only)
- [M] Norman (1991) Cognitive artifacts; Norman (1993) Things that make us smart. https://apice.unibo.it/xwiki/bin/view/Publication/Norman91Cognitiveartifacts

**Checklists in aviation**
- [V] Degani and Wiener (1991) Human factors of flight-deck checklists: the normal checklist. NASA CR-177549. https://ntrs.nasa.gov/citations/19910017830
- [M] Degani and Wiener (1993) Cockpit checklists: concepts, design, and use. https://ntrs.nasa.gov/citations/19930068509 (the "42 crews, 72 flights, 140 hours" figures are unverified)

**Checklists in medicine**
- [V] Haynes et al. (2009) NEJM 360:491-9. https://pubmed.ncbi.nlm.nih.gov/19144931/
- [V] Pronovost et al. (2006) NEJM 355:2725-32. https://pubmed.ncbi.nlm.nih.gov/17192537/
- [V] Urbach et al. (2014) NEJM 370:1029-38. https://pubmed.ncbi.nlm.nih.gov/24620866/
- [V] Bergs et al. (2014) Br J Surg. https://pubmed.ncbi.nlm.nih.gov/24469991/
- [V] Haugen et al. (2015) Ann Surg. https://pubmed.ncbi.nlm.nih.gov/24824415/
- [V] Reames et al. (2015) JAMA Surg. https://pubmed.ncbi.nlm.nih.gov/25588183/
- [V] Reames et al. (2015) Med Care. https://pubmed.ncbi.nlm.nih.gov/25464163/
- [V] Dixon-Woods et al. (2013) Matching Michigan, Implementation Science (abstract only). https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22Matching+Michigan%22+Bion&resultType=core&format=json&pageSize=3
- [V] Systematic review 2024, WHO surgical checklists (truncated abstract). https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22surgical%20safety%20checklist%22%20Ontario%20Urbach&format=json&resultType=core

**LLM studies**
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798
- [V] Stechly, Valmeekam, Kambhampati (2024) Self-verification limitations. https://arxiv.org/abs/2402.08115
- [V] Dhuliawala et al. (2023) Chain-of-Verification. https://arxiv.org/abs/2309.11495
- [V] Gou et al. (2024) CRITIC. https://arxiv.org/abs/2305.11738
- [V] Kamoi et al. (2024) Survey of self-correction (abstract and intro). https://arxiv.org/abs/2406.01297
- [V] Madaan et al. (2023) Self-Refine. https://arxiv.org/pdf/2303.17651
- [V] Shinn et al. (2023) Reflexion. https://arxiv.org/pdf/2303.11366
- [V] Yao et al. (2023) ReAct. https://arxiv.org/pdf/2210.03629
- [V] Nye et al. (2021) Scratchpads. https://arxiv.org/pdf/2112.00114
- [V] Gao et al. (2023) PAL. https://arxiv.org/abs/2211.10435
- [V] Yang et al. (2024) SWE-agent. https://arxiv.org/pdf/2405.15793
- [V] Ebouky et al. (2025) Cognitive tools. https://arxiv.org/pdf/2506.12115
- [V] Cook et al. (2024) TICK/STICK. https://arxiv.org/abs/2410.03608
- [V] Viswanathan et al. (2025) RLCF. https://arxiv.org/html/2507.18624v2
- [V] Cemri et al. (2025) MAST. https://arxiv.org/pdf/2503.13657
- [V] Wang et al. (2024) Budget-aware evaluation. https://arxiv.org/html/2406.06461v3
- [V] Wunderlich et al. (2026) Pareto-optimal test-time scaling. https://arxiv.org/pdf/2605.01566
- [V] Choi, Zhu, Li (2025) Debate or vote. https://arxiv.org/abs/2508.17536
- [V, abstract only] Kim et al. (2025) Correlated errors in LLMs. https://arxiv.org/abs/2506.07962
- [V] Sinha et al. (2025) Long-horizon execution. https://arxiv.org/pdf/2509.09677
- [V] Zhang, Kweon, Han (2026) How strongly should task state influence an LLM agent? https://arxiv.org/abs/2609.25686 and https://arxiv.org/html/2609.25686 (read through a fetch summary)
- [V] Li et al. (2025) SOPBench. https://arxiv.org/abs/2503.08669
- [V, abstract only] Tam et al. (2024) Let me speak freely. https://arxiv.org/abs/2408.02442
- [V, abstract only] He et al. (2024) Prompt formatting. https://arxiv.org/abs/2411.10541
- [V, abstract only; not re-opened in critique] Agent skills can be harmful (2026) https://arxiv.org/abs/2608.11888 ; CM2 (2026) https://arxiv.org/abs/2602.12268 ; Planning representations for web agents (2026) https://arxiv.org/abs/2605.29927
- [V, abstract/intro only] Cognitive Workspace (2025). https://arxiv.org/abs/2508.13171
- [V, abstract only] VeriLA (2025). https://arxiv.org/abs/2503.12651
- [V, small] AdaptiveCoPilot (2025). https://arxiv.org/pdf/2501.04156
- [M] Figueiredo (2025) Cognitive scaffolding. https://arxiv.org/pdf/2508.21204
- [M] LeRAAT / Virtual Co-Pilot. https://arxiv.org/html/2503.16477v1
- [M] Auto-Eval Judge. https://arxiv.org/pdf/2508.05508
- [M] GitAuto blog (anecdote). https://dev.to/gitautoai/our-agent-had-the-checklist-and-ignored-it-478g

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 8 established claims: 6 confirmed as written, 2 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **F02.05-K21** (reworded: the sources support less). The counts (24 of 26 and 20 of 20 on-turn re-executions with the step already marked DONE) and SOPBench's procedure-completeness rule are accurate, but they show agents ignoring their own marks and a benchmark rule requiring verification calls, not marks written without action; the ledger arm actually beat the accurate checklist (0.70/0.79 vs 0.55/0.59), so 'compliance without doing' is not shown. Corrected claim: In an LLM-agent study with a self-written ledger, 24 of 26 and 20 of 20 on-turn re-executions fired with the step already marked DONE in the agent's own ledger, so re-reading its own record did not prevent redoing steps (though the ledger still beat an accurate checklist); and SOPBench requires the check calls to precede each service call, so a trajectory that skips them fails even if the final database state is correct.
- **F02.05-K22** (reworded: the sources support less). Numbers match for text-davinci-003, but the generalisation fails: for ChatGPT, CRITIC w/o Tool beats CoT by about 3 F1 on HotpotQA (46.1 vs 42.8) and AmbigNQ (67.3 vs 64.3), and on TabMWP (davinci) w/o Tool still adds +20.3 over PoT, so 'flat or negative' is not general; Kamoi's finding is about feedback from prompted LLMs and has an exception clause. Corrected claim: Checks with an outside signal (interpreter, retrieval, tests) carry most of the gain in CRITIC: on text-davinci-003, CRITIC without the search tool equals plain CoT on QA F1 (HotpotQA 46.1 vs 46.1, AmbigNQ 58.3 vs 58.6, TriviaQA 74.7 vs 74.5) and loses 1.8 points on GSM8K program-of-thought (68.3 vs 70.1), though on ChatGPT and on TabMWP the tool-free variant still gains; Kamoi et al. find no prior work showing successful self-correction with feedback from prompted LLMs, except in tasks exceptionally suited to it.
- **F02.05-K06** (now single-source: only one opened source, code check).
- **F02.05-K07** (now single-source: only one opened source, code check).
- **F02.05-K27** (now single-source: only one opened source, code check).
