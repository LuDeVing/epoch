# Kuhn and paradigm crisis: deep document

*Subfield F03.13. Evidence ids (a01-a31, b01-b26, c01-c25, d01-d16) refer to evidence_a-d.jsonl in this folder. Claim ids (K01-K30) refer to claims.jsonl. Status tags: [E] established, [S] single-source, [C] contested, [D] our design choice, not a finding.*

## 1. What it is

Kuhn (1962) said science runs in cycles. Normal science works inside one paradigm and treats failures as puzzles to solve. Anomalies pile up. Some resist. Confidence breaks down (crisis). A rival paradigm appears and replaces the old one (revolution). Then normal science starts again (a01, a02, a03).

Why we care: our schema has a control state S6 that decides when to abandon an operator or a frame. The idea to test is: switch frame after several independent failures. This subfield asks what Kuhn actually said, what psychology and lab studies show about how people respond to anomalies, and whether any LLM study tests such a trigger.

Three facts shape everything below.

1. Kuhn gives no count. He never says how many anomalies make a crisis. In chapter IX (read in primary text) he points to the "extent and stubbornness" of the anomaly instead (d01, K07 [E]). So any failure count N is our design choice [D].
2. Anomalies alone do not force a switch. A rival must exist and fit better (a07, b24). Popper needs one reproducible anomaly. Kuhn does not (a02).
3. No study found tests "switch frame after N independent failures" with a measured N. The closest are Smith 2026 (not isolated, and the paper says it did not matter), Alderete 2026 (monitor, synthetic task), and EvoSCM 2026 (competing models plus correction rules) (b26, d04, c13, c12).

Limit of this document: Kuhn's book was read only for chapter IX and the 1969 postscript. Chapters VII-VIII (crisis, decision to reject) and Kuhn 1977 were not opened; they are known through the Stanford Encyclopedia (a01-a05).

## 2. History and theories in depth

**Kuhn 1962 and 1970.** Five phases: pre-paradigm, normal science, anomaly, crisis, revolution. Puzzle-solving is the normal mode: the solver expects a fair chance of success and relies on skill and familiar methods (a03). Normal science neither tests nor tries to confirm its guiding theory and explains anomalies away where it can (a02). Over one million copies sold; second edition 1970 with a postscript; 50th anniversary edition 2012 (a06). The 1970 postscript answered critics who counted many senses of "paradigm" by reading it as exemplar and disciplinary matrix (a05).

**Crisis in chapter IX (d01).** Kuhn calls crisis a growing sense, often in a narrow part of the community, that the paradigm has stopped working. A discovery's importance is often proportional to the extent and stubbornness of the anomaly that foreshadowed it. Useful criteria for choosing between paradigms: accuracy of prediction (especially quantitative), balance of esoteric and everyday subject matter, number of problems solved. Less useful: simplicity, scope, compatibility. No numeric threshold appears.

**Theory choice (Kuhn 1977, via SEP a04).** Five shared values: accuracy, consistency, scope, simplicity, fruitfulness. They are imprecise and can conflict, so they do not fix a choice alone. Kuhn: they let rational people disagree.

**Incommensurability (a05).** Methodological, observational and semantic forms. Kuhn said it does not mean non-comparability. Practical reading: a new frame cannot be scored only in the old frame's terms.

**Critics.** Popper: one reproducible anomaly can refute. Lakatos: research programmes have a hard core and a protective belt; a programme is progressive if it predicts new facts, degenerating if it only patches. Many programmes coexist, unlike Kuhn's single paradigm (a30, d03). Toulmin: revision inside normal science is more common than Kuhn allows. Hanson: the theory is circular and unfalsifiable. Feyerabend: normal science fits organised crime too (a07). Lakatos: no fixed waiting period; a degenerating programme can recover (the Flynn effect reversed a verdict 13 years later) (d03).

**Psychology lines.**
- Bruner and Postman (1949) is the card study Kuhn is said to have used as a model (a08; the 1949 paper does not cite Kuhn, and Kuhn's use is from memory).
- Chinn and Brewer (1993) give a taxonomy of seven responses to anomalous data: ignore, reject, exclude from domain, hold in abeyance, reinterpret, change theory peripherally, change theory (a12, b21). Only the last is Kuhn-style change.
- Dunbar (1997) studied four molecular biology labs in vivo (a18).
- Luhmann and Ahn (2011) studied reinterpretation of conflicting observations (b17).
- Ecker lab (2025) tested continued influence of retracted information (b18).

**Formal and computational lines.**
- Thagard's explanatory coherence (ECHO): propositions linked by positive and negative constraints, split into accepted and rejected sets that satisfy the most constraint weight. Applied to the chemical revolution (a23, c24; the Wikipedia page does not name ECHO; mostly from memory).
- Sterman (1985) and later system-dynamics models: confidence in the paradigm falls when anomalies exceed an acceptable level or puzzle-solving progress slows (a24; not read, search summary only).
- Schapiro, Black and Varshney (2025): a scientific conceptual space as a directed acyclic graph; sinks are axioms; changing axioms has the most transformative potential; maps Kuhn's cycle onto it (a25). Theory only.
- Klein et al. (2023) plausibility transition model: gaps cannot be filled, strain builds, a tilt occurs, a search for another story starts (b16). Exploratory.
- Langley, Simon et al. (1987) BACON: law rediscovery by search (c23, from memory).

**Large-scale data.** Chu and Evans (2021): as fields grow, citations concentrate on famous papers and new ideas struggle to enter the canon (b13, b14). Singh et al. (2022): fields follow a rise-and-fall curve; early-stage fields have more cross-field authors, smaller teams, higher disruption (b15).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Kuhn gives no count of anomalies for a crisis | No threshold anywhere in ch. IX | a02, d01, K07 | [E] |
| Trick playing cards need about 4x exposure to recognise | N=28. Mean threshold 28 ms normal vs 114 ms incongruous, t=3.76, p<.01. 100% of normal cards recognised by 350 ms; 89.7% of incongruous at 1000 ms | Bruner and Postman 1949 (a08) | [C] (see replication) |
| Dominance reaction on trick cards | 27 of 28 subjects (96%) vs 2 of 28 on normal. Six subjects kept dominance responses for 50 exposures up to 1000 ms; runs of 24, 44, 16 wrong responses | a09 | [C] |
| Thresholds fall after prior clashes | Incongruous threshold 360 ms with no prior cards; 420 ms after normal cards (n.s.); 230 ms after one trick card; 84 ms after 2-3 | a10 (230 ms figure not re-seen) | [C] |
| 2011 replication did not reproduce resistance | Pure sets: trick and regular cards identified equally well. Mixed set: slower for both. Exp 2: similar frustration, trial-and-error strategy. Sample sizes unread (abstract only) | Horner and Tung 2011 (d02) | [S] |
| Entrenched theories give theory-preserving responses; data judged through theory | N=64 (2x2). 6 of 10 volcano-theory proponents accepted the data vs 4 of 32 meteor-theory holders (p<.01). Believability 12 vs 5.1 as printed (scale doubt), t(40)=2.48 | Chinn and Brewer 1993 (a15) | [S], not re-verified |
| Data are not wholly theory-laden | Discount measure vs belief change r=-.46; delta R2=.25, F(1,63)=23.66 | a16 | [S], not re-verified |
| An available alternative theory did not change belief | Belief drop .97 with alternative vs .72 without, F<1. Data strength: 5.4 vs 5.6, F<1. 7 of 16 who rejected strong data attacked one of two independent lines | a14 | [C] |
| Real scientists attend to surprise | Lab A: 22 expected, 18 unexpected, 30 exploratory conditions. 23 group interactions for expected vs 176 for unexpected. Of 18 unexpected, 8 consistent with hypothesis, 10 inconsistent | Dunbar 1997 (a19) | [E] (two sources, one secondhand) |
| Surprise handling depends on timing and target | Early + auxiliary: ignored. Early + core: focused on. Late: attended whatever it touches. No counts | a20 | [S] |
| Groups catch errors | HIV lab talk: 11 inductions, 7 modified or dropped by others; 30% of inductions shared by more than one person | a21 | [S] |
| Conceptual change from one clear surprise plus talk | 99 analogies in 16 meetings, mean 6.1, 40 within organism, 57 other organism, 2 non-biological | a22 | [S] |
| Field-size lock-in | 90,637,277 papers, 241 subjects. Predicted top-50 rank correlation 0.25 at 1,000 papers/yr vs 0.74 at 100,000. Disruptive share D>0: 49% to 27% to 13%. Median wait to top 0.1%: about 9 years vs under 1 | Chu and Evans 2021 (b13) | [E] (correlational) |
| Top-1% citation share rises with field size (one example field) | 8.6% at 10,000/yr, 11.9% at 50,000, 16.7% at 100,000 (Electrical Engineering) | b14, critique item 8 | [S] |
| Fields rise and fall on one curve | 1,456,403 arXiv articles, 175 fields, 72 kept; 66 of 72 (91.6%) fit Gumbel. Early stage 2.36 fields/article vs 2.05; about 2 authors vs 4.5 | Singh 2022 (b15) | [S] |
| Retracted misinformation: continued influence is mixed | Three experiments, N=301, 300, 301. Effect in 1 of 3. Meta-analysis likability -0.13, p=.253; inference 0.25, p=.073 | Ecker lab 2025 (b18) | [C] |
| Early expectations can dominate reinterpretation; load flips to recency | Exp 1C N=17 primacy 45.41 vs -31.35, t(16)=8.06; Exp 1B N=16 with load recency, t(15)=2.54; Exp 2 N=44 | Luhmann and Ahn 2011 (b17) | [S] |
| Intrinsic self-correction does not help, oracle correction does | GPT-3.5 GSM8K: oracle 75.9 to 84.3; intrinsic 75.9 to 75.1 to 74.7. CSQA oracle 75.8 to 89.7; intrinsic 75.8 to 38.1 to 41.8. GPT-4 GSM8K intrinsic 95.5 to 91.5 to 89.0 | Huang 2024 (b01, b02) | [E] (4 sources, K10) |
| Locating the error is the bottleneck | GPT-4 best mistake-location 52.87%. Backtracking with true location: +18 to +44 points on incorrect traces, -0 to -11 on correct ones. Random location: +5 to +22 and -7 to -16 | Tyen 2024 (b05) | [E] |
| Resampling explains much of loop gain | Graph colouring, 100 instances: any-time-correct about 40% for all back-prompt types. LLM verifier accepted 2 of 100 optimal colourings | Stechly 2023 (b07, b08) | [S] |
| Retry with lesson works with an external signal | ALFWorld 130 of 134 in 12 trials; ReAct alone plateaus between trials 6 and 7 | Reflexion (b09) | [S] |
| Reasoning models over-switch | Wrong answers: 225% more tokens, 418% more thought switches. Switch penalty: QwQ AIME24 38.3 to 44.1; R1-Distill-32B 61.4 to 64.1; R1 73.8 to 74.8. Prompt "persist" on R1: 73.8 to 72.4 | Wang 2025 (b10, b11, d11, d12) | [S] |
| Models under-test hypotheses | Wason-style success 6% to 78% across 11 models; confirmation share vs success rho -0.779 (p=.003); OR 0.016 | Jhaveri 2026, FalsifyBench (c01, c05) | [E] (3 sources) |
| Opposite-test prompts help strong models, can hurt weak | Qwen3-32B thinking 0.41 to 0.61 (TiO); Dual-Goal Qwen3-32B non-thinking 0.33 to 0.10 | c03 | [S] |
| Agents rarely revise on contradiction | 619 tasks: ignored evidence in 68%, unsupported claims 53%, changed output 26% (press report only). Altered physics: top model 16.7%, 11 others 0% | c14, c15, d15 | [E] with caveats (K16) |
| Models raise false anomaly claims | 36.1% of reports on normal-physics controls rejected | c15, d15 | [S] |
| Prediction can fit while the law is wrong | DiscoverPhysics: explanation score 0.61 (Opus) vs 0.10 (Llama-3.3-70B); pass@1 26.4 vs 1.8 | c11 | [S] |
| Code tools make strong models exploit early | GPT-5 72.9 to 69.6; GPT-4.1 5.3 to 16.1 | NewtonBench (c10) | [S] |
| Regime-change monitor cuts premature submission, not accuracy | Exactly-N submission 28.0% (14/50) vs 6.0% (3/50), p=.003. Accuracy 93.9% vs 95.3%, n.s. Base vs monitor 14.0% vs 6.0%, p=.159. Stochastic condition: no advantage (73-77%) | Alderete 2026 (c13, d10) | [S] |
| Competing causal models plus correction rules | GPT-5.4 pass@1 1.86% to 38.08%. Ablation: K=1 63.27%, K=4 74.86%, K=6 75.09%. No pre-committed prediction 63.47% vs full 75.09% | EvoSCM 2026 (c12, d14) | [C] (own benchmarks) |
| Self-judged progress is unreliable | 54 cycles; 56% had measured delta zero or negative while agent claimed improvement; strongest judge accepted 44% regressions, rejected 38% of real gains | Park and Choi 2026 (d07) | [S] |
| Only direct Kuhn-agent test is not supportive | 63 Kuhn runs, 33.5M of 229.0M tokens. Phase 1 stalled at 0.664 after 49 runs; Phase 2 0.846. Floor prompt 0.8896 vs full scaffold 0.7942. 7 of 10 arms did not beat best-of-15 | Smith 2026 (a26, a27, d04, d05) | [C] |
| Medical Einstellung items | 100 items; physicians 66%; DeepSeek-R1 52%, o1 48% | b19 | [S] |
| Mental-set few-shot | GPT-4o 0.33 to 0.66; six problems per cell | Haq 2025 (c08) | [S] weak |
| Paradigm shifts detectable from citation counts | AUROC 0.969 on 16 pairs; citation-only matches full workflow; semantic-only 0.844; funding-only 0.531 | c20 | [S] |

## 4. Mechanisms and models

Written so an engineer can build each one. Every threshold is [D] unless stated.

### 4.1 The Kuhn cycle as a state machine

States: NORMAL (puzzle-solving inside frame F), ANOMALY_LOGGED, CRISIS, REVISION, NORMAL(F').
- NORMAL: a failed check is a puzzle. Fix and continue. Do not question F.
- Each failure is logged with a record: the failing output (G2), the test that located it (code, not the model), a cause label (tool or setup error, auxiliary assumption, core assumption), and the response type (see 4.2).
- CRISIS fires when a counted signal crosses a threshold (4.3). It does not fire on the model's feeling of doubt (G1, K10).
- REVISION builds a candidate frame first (a07, K29), then compares it with F on held-out data (G3), then switches or stays.

### 4.2 Chinn and Brewer response log

Seven responses to anomalous data (a12): ignore, reject, exclude, abeyance, reinterpret, peripheral change, theory change. For an agent these map to: skip the failing case; blame the tool or the test; say it is out of scope; defer; re-read the output so it fits; patch the current approach; replace the frame. Log which one the agent used per failure. A run of "patch" entries with no new checkable prediction is the Lakatos degenerating signature (c06 reports models adding special cases, "epicycles", instead of dropping a hypothesis).

### 4.3 Trigger signals, ranked by evidence

1. Count of failures from an external check (tests, verifier, held-out score). Supported in direction by K10, K11, K27. Count only failures that are independent: different tests, different seeds, different inputs. Several lines of evidence are more persuasive than repeats of one test (a17).
2. Outcome stagnation: number of cycles or runs with no accepted improvement (Smith: configurable consecutive non-improving iterations; Park and Choi: days flat) (d04, d08). Precondition: check the signal is valid and the agent can see per-case failures. Smith's 49-run stall came from a mismatched benchmark and deleted diagnostics, not a wrong frame (d06, K26).
3. Lakatos progress signal: after a patch, did it predict a new checkable fact, and did that fact hold? Defined in philosophy (d03); no LLM test found (K30).
4. Prediction vs explanation gap: track an explanation score separately from fit; fit alone can be right while the law is wrong (c11, K17).
5. Learned detector for mistakes: a small classifier trained out of domain beat prompting GPT-4 on mistake finding (b06). Candidate only.

Do not use: the model's own doubt or verdict (b01, b02, d07, d13). Alderete's monitor is itself an LLM judgement (score at least 6.0 of 10, at least 10 steps, fires once per episode, d09), and its benefit was blocking early submission, not accuracy.

### 4.4 Dwell floor and gate

Reasoning models switch lines of thought too often (b10). A switch penalty helps and a prompt telling the model to persist does not (d12). So implement the gate as a mechanism: a minimum number of tokens or attempts in a frame before S6 may fire. Wang's best setting was strength 3, duration 600 tokens; strength 20 with duration over 300 hurt (d11). Tune per model.

### 4.5 Core versus auxiliary split

Dunbar: early surprise about an auxiliary assumption is ignored, about a core assumption is attended (a20). Implement a registry of core assumptions (Park and Choi design note, unvalidated, d08). A failure counts toward a frame switch only if it hits a registry item. Others are fixed locally.

### 4.6 Frame comparison in code

Explanatory coherence (a23): nodes for evidence and frame propositions, edges for explains and contradicts, solve for the accepted set. A simpler form: score old and new frame on Kuhn's values using held-out outcomes: accuracy first, then problems solved, then simplicity and scope (d01, a04). Fixed checklist, no weighting claim. The judge must not know which frame is favoured (a15, G5).

### 4.7 Competing-frame population and pre-commitment

EvoSCM keeps about four competing hypotheses, each making a falsifiable prediction before each experiment; recurring discrepancies become correction rules; revision prefers shallow edits (parameter, then mechanism, then structure) (c12, d14). Pre-commitment removed post-hoc rationalising (63.47% without it vs 75.09%). K=4 reaches almost the full gain (74.86% vs 75.09% at K=6).

### 4.8 Lessons memory with fresh context

Reflexion stores a short lesson after a failure and retries (b09). Smith's Kuhn agent restarted without history file and with an injected assumption and a cross-discipline inspiration (d04). Practitioner rule: restart fresh after 3 failed attempts carrying only lessons (c19; no measurement). Fresh context is the part to isolate.

### 4.9 Sunk-frame guard

Chinn and Brewer: more support for a theory means more resistance to anomalies (a13). Long success in one frame should not raise the bar for noticing failure. Implement by counting failures in absolute terms, not as a fraction of all attempts.

### 4.10 System dynamics view

A stock of confidence in the frame, reduced when anomalies exceed an acceptable level or progress slows (a24, unread). Closest formal match to S6, but parameters unknown.

## 5. What holds up

**Holds up.**
- Kuhn supplies no count (d01). [E]
- LLMs cannot self-correct without an external signal (b01-b03, d07, d13). Four sources. [E]
- Locating the error is the bottleneck; repair is easy once located (b05). [E]
- LLMs under-test hypotheses and favour confirming tests (c01, c05, c06). Three sources. [E]
- LLM agents seldom revise on contradicting evidence (c14, c15, c11, d15). [E] with the press-report caveat on 68%/26%.
- Scientists attend to surprise rather than explain it away, with timing and target as moderators (a19, a20). [E]
- Field-scale lock-in (b13, b14, b15). [E], correlational.

**Failed, mixed or contested.**
- Bruner and Postman resistance: the 2011 replication did not reproduce it (d02). We lack the sample sizes. Do not use the 1949 cards as evidence that agents or people cling to a frame (K28).
- Chinn and Brewer alternative-theory null (a14): contrasts with Kuhn. N=64, low stakes for students. Numbers not re-verified (critique item 10).
- Continued influence of retractions replicated in 1 of 3 experiments (b18). Belief perseverance is small and material-dependent.
- Smith 2026: abstract-level framing as success, body says non-load-bearing (critique). 7 of 10 loop arms did not beat one-shot best-of-15 (d05).
- BoxingGym: prior domain information often made things worse after 10 experiments, because the model did not revise strong assumptions (c16). Against EvoSCM's gain, this makes multi-frame benefit task-dependent (K20 [C]).
- Dual-Goal prompt hurt non-thinking models (c03).
- Self-judged triggers misfire both ways (d07).

**Moderators.**
- Model strength: opposite-test prompts help thinking models, can hurt non-thinking (c03). Code tools help weak models, hurt strong ones (c10).
- Noise: in a stochastic world the monitor gave no gain (c13); noise of 0.0001 cut GPT-5-mini accuracy 13-15% (c09). One failure should not switch a frame (c07).
- Order and load: under load the latest data wins; without load early expectations can win (b17).
- Whether the surprise hits a core or auxiliary assumption (a20).
- Task type: persistence helps on math with built-in switching (b11), but a trigger could help in open tasks. Unknown.

**Interventions that worked.**
- External-signal retry with lesson memory (b09).
- Forced thought-switch penalty (b11).
- "Wait" appended at stop: AIME24 50.0 to 56.7, GPQA 56.6 to 59.6 (b12). A schedule, not a signal; use as baseline arm.
- Think-in-Opposites prompt (c03).
- Blocking early commitment after regime change (d10).
- Competing causal models with pre-commitment (d14).
- A concrete scene clue raised discovery 16.7% to 28.6%; a 500-turn budget did not (d15).

**Interventions that did not work.**
- Intrinsic self-correction (b01).
- Prompt-only persistence (d12).
- Feedback content over feedback count: binary vs full error feedback made little difference in graph colouring (b07).
- Large judges as in-band evaluators (d07).
- Extra turns (c15, d15).
- Fresh-context Kuhn agent as isolated component: not tested; the paper's own ablation called the structure non-load-bearing (d04).

## 6. Language models

**No direct test of an N-failure frame-switch trigger exists** (b26, critique). The facts below are indirect.

**Smith 2026, The Little Scientist (a26-a28, d04-d06).** DNA motif discovery loop. A Kuhn agent fires after a configurable consecutive-non-improving count (N not reported), gets task instructions but none of the built-up artifacts or history file, plus an injected paradigm-shifting conjecture and a random cross-discipline inspiration. 63 Kuhn runs used 33.5M of 229.0M tokens (531K per run). Phase 1 stalled at 0.664 after 49 runs with no accepted improvement; Phase 2 reached 0.846 in 10 days. The authors trace the gap to infrastructure (a synthetic benchmark that did not match real performance, deleted per-instance diagnostics). The Kuhn side-agents were one of five changes made together. The paper says its ablation found the structure non-load-bearing. Ten preregistered arms vs best-of-15 fresh draws: pools H (n=114, mean 0.7644) and HG (n=88, mean 0.7802); expected best-of-15 0.8463 and 0.8455. Seven of ten arms did not beat HG. The full scaffold B used 111.4M tokens per run vs 15M, and scored below blind sampling (0.7942 vs floor prompt 0.8896 at the common horizon, n=10 per arm). Minimum detectable gap 0.063 at n=10. A framing-only rung gave best held-out 0.8819 and 0.8964 but its other draws were far below (a28), so reframing may raise variance more than mean.

**Park and Choi 2026 (d07, d08).** One frontier agent, three evaluator arrangements. The agent claimed improvement in all 54 cycles; 56% had measured delta zero or below; a self-verdict gate became accept-all and eroded the best deployed state by 19%. The strongest in-band judge accepted cycles of which 44% were real regressions and rejected 38% of real improvements. When success is checkable from the artifact, the mirage fell to 0. Sign-only external feedback gave similar output (110.0 vs 113.0). The authors' stagnation threshold and frame-adversarial review are unvalidated.

**Alderete 2026, Extended Blicket (c13, d09, d10).** 1,085 trials, Claude Sonnet 4.5 acting, Haiku 4.5 as judge. Hard post-switch rule, n=50 per agent. Reasoning-eligible accuracy: base 73.3% (22/30), context graph 93.9% (31/33), plus dynamic behaviours 95.3% (41/43). Exactly-N early submission 28.0% to 6.0% (Fisher p=.003, OR 6.09, h 0.62). Detection sensitivity 100%, PPV 90.5-100%. The gain is from not committing early. The accuracy gain from 93.9% to 95.3% is not significant, and the 73.3% vs 93.9% comparison has small counts. Stochastic condition: no advantage. Cost about 807 USD.

**EvoSCM 2026 (c12, d14).** GPT-5.4 pass@1 1.86% to 38.08%, pass@5 9.09% to 54.55%. GPT-5.5 pass@1 7.25% to 53.04%. Qwen3.6 baseline 0% at all k. Full system 75.09% explanation accuracy vs free-form text hypotheses 48.18%, random actions 47.45%, no correction rules 66.37%. The number of failures needed to trigger revision is not studied.

**Hypothesis testing (c01-c06, c25).**
- Jhaveri 2026: 11 LLMs, Wason-style, success 6% to 78% within 45 turns. Thinking mode raised success (Qwen3-8B 0.06 to 0.21; Qwen3-32B 0.33 to 0.41) but not by lowering confirmation bias. I:C correlated with success. Think-in-Opposites lifted all 11 model-mode scenarios (Qwen3-8B thinking 0.21 to 0.40; Qwen3-32B 0.41 to 0.61; Llama-3.3-70B 0.21 to 0.38); mean rate 42% to 56% with human-derived prompts. Distillation (training) moved 8B 0.21 to 0.35.
- FalsifyBench: 12 LLMs, 100 WordNet games, success GPT-5.2-Chat 75%, GPT-OSS-120B 68%, DeepSeek-V3.1 41%, others 33-35%, GPT-5-Nano 12%. Confirmation vs success rho -0.779 (p=.003); conclusive falsification rate rho -0.937; oracle error had no effect (OR 0.885). Failed games had more partial-overlap turns (+27.0 pp GPT-5.2-Chat, +22.3 GPT-OSS-120B, +21.4 GLM-5) and surface-feature hypotheses (97.6% of failed GLM-5 games). Near-miss frames are the trap.
- Numberwang pilot (blog, informal): mean success 11%, 4 of 11 models 0; o1-preview 3 of 10; some added special cases instead of dropping a hypothesis.

**Discovery under altered laws.**
- NewtonBench: GPT-5 72.9% symbolic accuracy, Gemini-2.5-pro 65.0%, o4-mini 47.5%, DeepSeek-V3 9.7%, GPT-4.1 5.3%; GPT-5 on complex-system hard 29.9% (c09).
- DiscoverPhysics: pass@1 / pass@5 26.4 / 50.0 for claude-opus-4-7, 21.7 / 36.4 gpt-5.5, 1.8 / 9.1 claude-sonnet-4-6 (c11). The judge was a Claude model; self-preference risk. Authors read gpt-5.5 as tuning parameters inside a failing law, which is normal science inside a failing paradigm.
- LongChang: one of 12 models discovered the altered law (16.7%); 36.1% of control reports were false anomaly claims; task guidance 16.7% to 28.6%; 500 turns 14.3%; apparatus disabled 4.8% (c15, d15). Model names unchecked.
- Rios-Garcia 2026 (press report): 619 tasks; ignored evidence in 68%; unsupported claims 53%; revised on contradiction in 26% (c14).

**Self-correction and switching (b01-b12).** See section 3. Older models (GPT-3.5, GPT-4, Llama-2) in Huang and Stechly; reasoning models in Wang. For GPT-3.5, 74.7% of GSM8K answers were kept after two intrinsic rounds, and changes more often turned right to wrong (b02, d13).

**Others.** Nova uses ten discovery methods as prompts, including Scientific Paradigm Shift and Explaining Anomalous Findings; 3.4 times more unique novel ideas; the Kuhn prompts were not ablated (a29). DuSAR: a fitness score decides when to revise the global plan; ALFWorld 37.1% vs 13.0%; trigger ablation not seen (c17). Medical Einstellung items: models below physicians (b19). Mental set: GPT-4o 0.33 to 0.66 (c08). Citation-based paradigm-shift detector AUROC 0.969 (c20).

**What changed behaviour, by how much (summary).** External signal vs none: GSM8K +8.4 for GPT-3.5 (oracle) vs -1.2 (intrinsic). Opposite-test prompt: +0.07 to +0.20 success. Switch penalty: +1.0 to +5.8 on AIME24 pass@1. Block early commitment: 28.0% to 6.0% premature submissions. Competing hypotheses: K=1 63.27% to K=4 74.86%. Persist-prompt: -1.4. Elaborate scaffold vs floor prompt: 0.7942 vs 0.8896.

## 7. What our agent should take

### Add now (established)

| Item | Part | Status | Evidence |
|---|---|---|---|
| Count failures from external checks (tests, verifier, held-out score), never from the model's own doubt or verdict | G1, G2, S6 | [E] | b01-b03, d07, d13; K10 |
| A failure must be located by code to a step or case before any revision | G2, S4 | [E] | b05, b06; K11 |
| Never trigger by schedule or token position; a "Wait"-style forced recheck is only a baseline arm | G1 | [E] | b12, b10; K14 |
| Force a counterexample test (one that could break the current hypothesis) before defending a frame; count the incompatible:compatible test ratio in code | S4, O-falsify (new candidate operator, tested under U-list) | [E] that models under-test | c01, c02, c05, c06; K15 |
| On a failed check, force revision from the actual output; models rarely revise on their own | G2 | [E] | c14, c15, c11, d15; K16 |
| Log every failure with cause label and Chinn and Brewer response type | S6, memory | [E] for the log's use as bookkeeping; the benefit is untested | a12, b22 |
| Score old and new frame on held-out outcomes only, in code | G3, G5 | [E] for the principle | a04, d01, a15 |
| Keep the failure count N as an explicit [D] parameter, not a Kuhn finding | S6 | [E] | d01; K07 |
| Do not use the 1949 card study as support for "agents cling to frames" | none | [E] | d02; K28 |
| Compare any S6 trigger with plain resampling at equal tokens | G7 | [E] | b08, d05; K12 |

### Test first

| Item | Part | Status | Evidence |
|---|---|---|---|
| Frame-switch at plateau with fresh context and lessons only, vs best-of-N | S6, memory | [C] | a26, d04, d05, c19; K21, K22 |
| Failure count N in {1,2,3,5}, independent vs repeated failures | S6 | [S], no measurement | a10 (human, contested), c19; K02 |
| Dwell floor before S6 may fire (mechanism, not prompt) | S6 | [S] | b11, d12; K14 |
| Offer a concrete candidate frame at the trigger | S6, O8 | [C] | d15, d14 vs a14; K04, K29 |
| Core-assumption registry; count only core failures | S6 | [S] | a20, d08; K05 |
| Lakatos signal (new-fact prediction rate of patches) vs failure count | S6 | [S] | d03, d08, c06; K30 |
| Hold about four competing frames with pre-committed predictions | S3, S6 | [C] | d14, c12 vs c16; K20 |
| Explanation score tracked separately from fit | S6, S8 | [S] | c11; K17 |
| Plateau precondition: check the signal is valid before blaming the frame | S6 | [S] | d06; K26 |
| Block commitment right after a detected regime change | S6, S8 | [S] | d10; K19 |
| Seven-response log: does naming the response lower "reject" and "reinterpret" use? | S6 | [S] | a12, b21, b22; K24 |
| Separate critic call (no authorship) vs self-revision | O, G5 | [S] | a21; K06 |
| Delay exploitation until k alternative frames have been tried | S6 | [S] | c10; K18 |

## 8. Concrete tests on our bench

All arms at equal total tokens (setup, trigger calls and reframing counted, G7). Report false-alarm rate with every trigger.

1. **Isolated plateau reframe.** Items: tasks where the first frame is plausible but wrong on some items (ARC-type programs, BrainTeaser-type puzzles, planted-anomaly tasks). Arms: (A) plain continue; (B) best-of-N fresh draws; (C) continue with fresh-context reframe after N external failures with lessons only; (D) same as C plus a concrete candidate frame. Metric: held-out solve rate and tokens per solved item. Expected: C beats A; C versus B uncertain, with Smith's result suggesting B may win. D beats C if the K29 hint effect holds (16.7% to 28.6% analogue).
2. **N sweep.** Same items as test 1, N in {1, 2, 3, 5}, each failure counted only if independent (different test inputs) vs counted if any repeat. Metric: solve rate, false switches (switching away from a frame that was correct), tokens. Expected: a middle N (2-3) wins; N=1 over-switches (c07, b01), N=5 wastes tokens.
3. **Self-judged vs external counter.** Same trigger, two signals: model says "this is failing" vs verifier or tests fail. Items with checkable answers. Metric: false-switch rate (correct-to-wrong) and solve rate. Expected: external wins; self-judged turns right answers to wrong ones (b02).
4. **Dwell floor.** Reasoning model with S6 fire allowed after 0, 300, 600 tokens in a frame; mechanism not prompt. Items: math with checkable answers, plus puzzles. Metric: accuracy, thought-switch count. Expected: floor of a few hundred tokens helps (b11), at +1 to +6 points on hard items.
5. **Planted anomaly uptake.** Insert a contradicting observation after the agent commits. Arms: no trigger; trigger on external failure; forced counterexample test. Metric: uptake rate (explicit note plus revision), log of Chinn and Brewer response type. Baseline from c14/c15: about 26% revision. Expected: forced revision raises uptake above 50%, with false-alarm rate on matched normal controls reported (c15: 36.1%).
6. **Core vs auxiliary.** Items with seeded setup errors (auxiliary) and seeded wrong assumptions (core). Arms: count all failures; count only registry-core failures. Metric: wrong-frame switches on auxiliary errors; correct-frame switches on core errors.
7. **Lakatos vs counter.** Same items; arm one switches after N failures; arm two switches when the last k patches predicted no new checkable fact that held. Metric: solve rate at equal tokens.
8. **Competing frames.** K in {1, 2, 4}, each with a pre-committed prediction before each test. Items: altered-rule tasks (NewtonBench-style, Blicket-style). Metric: held-out accuracy. Expected: K=4 about +10 points over K=1 (d14: 63.27% to 74.86%), unless BoxingGym-style prior-lock dominates.
9. **Plateau signal check.** Before reframing, verify the score matches a held-out set and per-case diagnostics are visible. Arms: reframe at plateau; signal-repair then reframe. Metric: solve rate; time to recover. Expected: repair first wins when the signal is broken (d06).

## 9. What does not transfer, and why

- **Kuhn's scale.** Paradigms are shared by a community over decades. One agent in one episode has no community, no funding or career pressure, and no sociology of attention. Chu and Evans lock-in (b13) is a crowding effect among many authors. It transfers only as a warning that correlated samples crowd out a rival frame (G4).
- **The 1949 cards.** Perception under tachistoscope is not theory choice, and the replication did not reproduce resistance (d02).
- **Students and low stakes.** Chinn and Brewer's null on alternatives (a14) used undergraduates with little stake. Agents have no stake either, which could cut both ways.
- **Dunbar's labs.** Surprise draws group reasoning in real labs (a19). A single agent has no group. G9 says debate adds little over voting, so a second agent is not a free critic (a21 vs G9).
- **Citation and field-level data.** Disruption, Gumbel curves, bibliometric AUROC (b15, c20) describe literatures, not a trigger inside one run.
- **Lab belief perseverance.** Continued influence of retractions is small (b18). Do not build a heavy anchoring guard on it.
- **Humans do not over-switch the way reasoning models do.** Wang's remedy (b11) is a decoding penalty for open models; for closed models only a mechanism in our own loop is available.
- **Training-based fixes.** Distillation of falsifying behaviour (c04) and fine-tuning for self-correction (b03) are outside our no-training rule.
- **Synthetic worlds.** Blicket, NewtonBench and DiscoverPhysics are small, curated, often LLM-judged. Effects may not carry to real tasks.
- **Many sources are 2026 preprints** with one author or no replication (critique).

## 10. Open questions

1. Does an isolated fresh-context reframe at plateau beat best-of-N at equal tokens? (Smith did not isolate it.)
2. What N is best, and does it depend on independence of failures? Gawali (d16) may bear on restart cutoffs; unopened.
3. Does an external failure signal beat a self-judged one in the same trigger? Direction is clear, no joint test.
4. Should only core-assumption failures count? No LLM study separates them.
5. Does supplying an alternative frame help LLMs, given the human null (a14)?
6. What are the sample sizes and thresholds in Horner and Tung 2011?
7. What does Kuhn say in ch. VII-VIII and in 1977 about number and kind of anomalies?
8. Does a trigger add anything on top of a switch penalty in reasoning models?
9. Can a Lakatos-style signal be run on an LLM, and does it beat a failure counter?
10. How often do the seven response types appear in LLM transcripts?
11. Do the Chinn and Brewer numbers hold (PDF not re-opened in the critique pass)?
12. Do the 68% and 26% figures hold in the Rios-Garcia paper itself (press report only)?

## 11. Sources

[V] opened, [M] snippet or memory only.

- [V] Stanford Encyclopedia of Philosophy, Thomas Kuhn (Bird). https://plato.stanford.edu/entries/thomas-kuhn/ (a01-a05)
- [V] Wikipedia, The Structure of Scientific Revolutions. https://en.wikipedia.org/wiki/The_Structure_of_Scientific_Revolutions (a06, a07)
- [V] Bruner and Postman (1949) On the perception of incongruity. https://psychclassics.yorku.ca/Bruner/Cards/ (a08-a10)
- [V] Horner and Tung (2011) Playing Cards with Thomas Kuhn, abstract via Crossref. https://doi.org/10.1037/a0023597 (d02; full text unread)
- [V] Chinn and Brewer (1993) Factors that influence how people respond to anomalous data. https://escholarship.org/uc/item/4tf7084b (a12-a17; not re-verified)
- [M] Chinn and Brewer (1993) Role of anomalous data, Rev Educ Res. https://ideals.illinois.edu/items/17657/bitstreams/63442/data.pdf (b21)
- [V] Dunbar (1997) How scientists think. https://chunk.cc.gatech.edu/AY2013/cs7601_spring/papers/Dunbar.pdf (a18-a22; a19 not re-verified)
- [M] Fugelsang, Stein, Green, Dunbar (2004). https://uwaterloo.ca/reasoning-decision-making-lab/sites/default/files/uploads/files/FugSteGreDun04.pdf (b20)
- [V] Wikipedia, Paul Thagard. https://en.wikipedia.org/wiki/Paul_Thagard (a23)
- [M] Sterman (1985) and Wittenberg and Sterman (1999) system-dynamics models. https://archives.albany.edu/description/catalog/ua435aspace_22d13cf704709562ae4e9d9fca152c3c (a24)
- [V] Schapiro, Black, Varshney (2025). https://arxiv.org/abs/2504.18687 (a25)
- [V] Smith (2026) The Little Scientist. https://arxiv.org/abs/2608.16951 (a26-a28, d04-d06)
- [V] Hu et al. (2024) Nova. https://arxiv.org/abs/2410.14255 (a29)
- [V] Wikipedia, Research program (Lakatos). https://en.wikipedia.org/wiki/Research_program (a30)
- [V] SEP, Imre Lakatos. https://plato.stanford.edu/entries/lakatos/ (d03)
- [V] Aerts and Aerts Arguelles (2022). https://arxiv.org/abs/2208.03726 (a31)
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (b01, b02, d13)
- [V] Kamoi et al. (2024) When can LLMs correct their own mistakes. https://arxiv.org/abs/2406.01297 (b03, b04)
- [V] Tyen et al. (2024). https://arxiv.org/abs/2311.08516 (b05, b06)
- [V] Stechly, Marquez, Kambhampati (2023). https://arxiv.org/abs/2310.12397 (b07, b08)
- [V] Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366 (b09, c18)
- [V] Wang et al. (2025) Thoughts Are All Over the Place. https://arxiv.org/abs/2501.18585 (b10, b11, d11, d12)
- [V] Muennighoff et al. (2025) s1. https://arxiv.org/abs/2501.19393 (b12)
- [V] Chu and Evans (2021). https://pmc.ncbi.nlm.nih.gov/articles/PMC8522281/ (b13, b14)
- [V] Singh et al. (2022). https://pmc.ncbi.nlm.nih.gov/articles/PMC9223313/ (b15)
- [V] Klein et al. (2023) Plausibility transition model. https://pmc.ncbi.nlm.nih.gov/articles/PMC10251660/ (b16)
- [V] Luhmann and Ahn (2011). https://pmc.ncbi.nlm.nih.gov/articles/PMC3491882/ (b17)
- [V] Ecker lab (2025) continued influence. https://pmc.ncbi.nlm.nih.gov/articles/PMC12058158/ (b18; shell only in critique pass)
- [V] Limits of LLMs in clinical problem solving (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12606185/ (b19)
- [M] Limon (2001) and PSA 1994 abstract. https://www.cambridge.org/core/journals/psa-proceedings-of-the-biennial-meeting-of-the-philosophy-of-science-association/article/scientists-responses-to-anomalous-data-evidence-from-psychology-history-and-philosophy-of-science/668FEBB13D35B22E47A57FD3487AC2CF (b23)
- [V] Student sensemaking with anomalous data (2024). https://pmc.ncbi.nlm.nih.gov/articles/PMC11659860/ (b22)
- [M] Kuhn (1962) from memory (b24, c21); ch. IX [V] at https://www.marxists.org/reference/subject/philosophy/works/us/kuhn.htm (d01)
- [M] Lakatos (1970), Langley et al. (1987), Thagard (1992) from memory (c22-c24)
- [V] Jhaveri et al. (2026) Failing to Falsify. https://arxiv.org/abs/2604.02485 (c01-c04)
- [V] Bertolazzi et al. (2026) FalsifyBench. https://arxiv.org/html/2606.04751 (c05, c25)
- [V] Alignment Forum Numberwang pilot (2025). https://www.alignmentforum.org/posts/RSqfcyAW9ZkveGQ5u (c06)
- [V] Li et al. (2025) Patterns Over Principles, abstract only. https://aclanthology.org/2025.findings-acl.1006/ (c07)
- [V] Haq et al. (2025) Mental Set. https://arxiv.org/abs/2501.11833 (c08)
- [V] Zhang et al. (2025) NewtonBench. https://arxiv.org/html/2510.07172v1 (c09, c10)
- [V] Wiemann et al. (2026) DiscoverPhysics. https://arxiv.org/html/2605.26087 (c11)
- [V] EvoSCM (2026). https://arxiv.org/abs/2609.01526 (c12, d14)
- [V] Alderete et al. (2026) Extended Blicket. https://arxiv.org/abs/2604.20039 (c13, d09, d10)
- [V] Rios-Garcia et al. (2026) via Science News (secondary). https://sciencenews.org/article/ai-ignore-evidence-trust-science (c14)
- [V] LongChang (2026). https://arxiv.org/abs/2610.37649 (c15, d15)
- [V] Gandhi et al. (2025) BoxingGym. https://arxiv.org/pdf/2501.01540v2 (c16)
- [V] Zhang et al. (2025) DuSAR, abstract only. https://arxiv.org/abs/2512.08366v1 (c17)
- [V] Understanding Data blog, clean-slate recovery (2025). https://understandingdata.com/posts/clean-slate-trajectory-recovery/ (c19)
- [V] Computational Kuhn benchmark (2026). https://arxiv.org/html/2605.22300 (c20)
- [V] Park and Choi (2026) When do agent loops mistake stagnation for progress. https://arxiv.org/abs/2607.25152 (d07, d08)
- [M] Gawali (2026) Restart, Don't Persist (title only). https://doi.org/10.13140/RG.2.2.21690.76483 (d16)

## Source audit (2026-11-20)

Fresh auditors re-opened the sources of 7 established claims: 6 confirmed as written, 1 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **F03.13-K23** (reworded: the sources support less). Haq numbers match (6 problems per condition, tiny); but only the best models scored 48-52% on mARC-QA, many were under 20%, so 'models scored 48-52%' is too broad. Corrected claim: Rigidity appears in LLMs as in people: in a six-problem-per-condition test (Haq et al. 2025), GPT-4o few-shot exact match went 0.33 to 0.66 with complex examples first; on Einstellung-style medical items (mARC-QA, 100 items) the best models scored 48-52% vs physicians 66%, and several models scored under 20%.
- **F03.13-K05** (now single-source: only one opened source, code check).
