# Anomalies and paradigm change: deep document

Scope: how an observation that resists the current frame starts discovery, and what that means for an agent that must notice an impasse (S6) and reframe (O8). Evidence ids (a01 to d17) refer to evidence_a-d.jsonl in this folder. Claim ids (K01 to K24) refer to claims.jsonl. Status words: established, single-source, contested.

## 1. What it is

An anomaly is a result that the current theory or frame did not predict and cannot absorb without change. Kuhn (1962) made it the start of discovery: awareness of an anomaly, then a more or less long exploration of the anomalous area, then an adjustment of theory until the anomaly becomes the expected (a01). Anomalies are seen only against a paradigm. Normal science tightens expectations and so makes anomalies visible (a30).

Three questions follow, and each matters for an agent.
- Detection: does the system notice that a result clashes? This needs an expectation written before the result (K07).
- Response: what does it do with the clash? Ignore, blame the method, narrow the theory, patch it, or change the frame (K04).
- Timing: when does one clash justify dropping the frame? Real scientists hold on first, and change after replication (K01).

For our agent this maps to S6 (impasse trigger) and O8 (reframe the goal). The schema marks O8 as single-source with a null result for LLM reframing in one large test. This document adds what the anomaly literature says about when and how to trigger it.

Honest limit: Kuhn is a historical, interpretive account. No counted effect exists for the oxygen case itself. Nothing here tests a paradigm-level reframe in an LLM (K18, c25). All LLM evidence is a proxy: belief revision on simulated physics, falsification tasks, trace audits.

## 2. History and theories in depth

### 2.1 Kuhn 1962: the oxygen case and the discovery pattern
- Oxygen has no single discoverer or date (a02). Scheele made a fairly pure sample first but published late. Priestley heated red oxide of mercury in 1774, first called the gas nitrous oxide, and in 1775 called it dephlogisticated air. Lavoisier worked 1775 to 1777 and later and framed it as a new element in a new theory. The principle of acidity was not banished until after 1810 and caloric lingered to the 1860s.
- Kuhn's parallel (a03): before the red-oxide work Lavoisier had run experiments whose results the phlogiston paradigm did not predict. Roentgen's X-ray find began with a screen that glowed when it should not. Perceiving an anomaly prepared the way. The Leyden jar is the third case (a29): it came from an anomalous electrical effect and forced a revision of fluid theory.
- Ch. VIII, response to crisis (a05, a27): counterinstances alone never make scientists drop a paradigm. Rejecting a paradigm without a substitute is rejecting science. Every puzzle could be read as a counterinstance, so the line between puzzle and counterinstance is soft. In crisis, rules loosen and rival articulations multiply.
- Perception evidence Kuhn uses (a04): Bruner and Postman (1949) showed playing cards at growing exposure. Anomalous cards (red six of spades, black four of hearts) were first named as normal without hesitation. Kuhn reports that at 40 times the exposure needed for normal cards, over 10% of anomalous cards were still misidentified. Second-hand from Schindler 2024 (d10): threshold 114 ms versus 28 ms, and 10% still failed at 1 s. Original not opened.

### 2.2 Historians' critique
Hudson (2001), via Schindler (2024) (d09, d10): Priestley counts as discoverer of oxygen by a base description even with the wrong theory. X-rays were found by accident, with no clash with a held theory. So an anomaly is one route to discovery, not the only one (K24). Only a 2024 secondary chapter was opened. No primary source (Priestley 1775, Lavoisier memoirs, Scheele notebooks) was read.

### 2.3 Cognitive science of responses to anomalies
- Chinn and Brewer (1993) taxonomy (a06): seven responses when one holds theory A: ignore, reject (flaw, error, fraud), exclude from the theory's domain, hold in abeyance, accept and reinterpret to fit A, accept with a minor peripheral change, accept and change theory. The 1998 JRST test examined seven responses and added an eighth (d13). Frequencies not obtained.
- Chinn and Brewer (1993) Cogsci experiment (a07, a08): 64 undergraduates read about the meteor-impact theory of Cretaceous extinction, then anomalous data. Strong holders mostly discounted the data. 6 of 10 volcano proponents accepted the data against 4 of 32 meteor proponents (chi-square 7.04, p<.01). Offering an alternative theory did not reliably help (belief drop 0.97 versus 0.72, F<1). Reasons given for rejection fall in five types, from "scientists overlooked a factor" to "the theory is so well supported that the data must be wrong". The 4/32 and 6/10 counts are as extracted; the critique could not re-open the source.
- Brewer and Chinn (1994) (a10, d14): 72 undergraduates (24 per condition) read a strong case for warm- or cold-blooded dinosaurs. The same data were rated 8.0 believable when consistent with the read theory and 6.0 when inconsistent (control 7.8), F(2,66)=7.292, p<.001. Theory-ladenness of data is real but moderate.
- Boundary reports (a09, second-hand): adolescents kept a wrong displacement theory after anomalous data but changed once given the correct principle (Burbules and Linn 1988). Suggests a plausible substitute lowers resistance (K16, contested).

### 2.4 Scientists at work
- Dunbar (1995/1997) (a11, a12): four weekly lab meetings in one lab, 6 experiments, 70 conditions: 22 expected, 18 unexpected, 30 exploratory findings. Group interactions 23 (expected) versus 176 (unexpected). Of 18 unexpected, 10 were inconsistent with the hypothesis and 8 consistent but of unexpected size; 8 of the 10 inconsistent ones led to new hypotheses. Timing matters: early in a project, a surprise that hits only an auxiliary is ignored; one that hits a core field assumption is pursued; late in a project both are attended. These timing analyses have no counts in the chapter.
- Fugelsang et al. (2004) (b01, b02): 3 molecular biology labs, 12 meetings, 28 projects, 165 experiments, 417 results. 223 (53%) were inconsistent with predictions. 196 of those 223 got a method explanation first and 27 (12%) a theory change. When the result was replicated (84 replications), theory change rose to 51 of 84 (61%). This is the key timing result.
- Trickett et al. (2001) (b04, d11): three scientists (2 astronomers, 1 physicist) analysing data. Astronomy 27 noticings (33% anomalous), physics 9 (44% anomalous). Later references per item: astronomy 7.6 for anomalies versus 1.5 for expected; physics 3.0 versus 1.25; t(28)=2.33. Hypotheses were proposed more for anomalies, chi2(1)=7.5. N=3.
- Alberdi, Sleeman and Korpi (2000) (d12): 5 botanists in plant taxonomy, same direction.
- Fugelsang student lab simulation (b03): N=32; data that clash with an implausible theory were discounted at first. Plausibility effect F(2,62)=21.87, eta2=.41; discounting fell as trials grew from 10 to 40.

### 2.5 Models of anomaly handling
- KEKADA (Kulkarni and Simon 1988/1990) (a13 to a15): a program that modelled Krebs's urea-cycle discovery. It attaches an expected range to each experiment, so a surprise is a deviation from a stated expectation. It has five strategies for a surprise: magnify it by varying apparatus, divide and conquer, assess scope through taxonomies, find relevant factors by dropping variables, look for similar phenomena. A class with 3 or more negative instances inactivates the hypothesis. Only a hand-driven worked example; no baseline.
- Darden (1991, 1992): strategies for anomaly resolution (diagnosis then redesign of the theory). Not opened (a16).
- Gershman (2019) (b10, b11): Bayesian analysis of Duhem's problem. One anomaly is rationally shared between the core theory and the auxiliaries, so shielding a theory with auxiliaries can be rational. Example: Le Verrier's Neptune worked for Uranus; his Vulcan failed for Mercury, which general relativity later explained. He says a systematic empirical test "has yet to be undertaken".

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Scientists blame method first, theory after replication | 417 results, 223 (53%) inconsistent; 196 method explanations; 27 theory changes (12%); after replication 51/84 (61%) | Fugelsang et al. 2004 (b01, b02) | established (K01) |
| Experts dwell on unexpected results | 18 unexpected vs 22 expected; group interactions 176 vs 23; 8 of 10 inconsistent surprises gave new hypotheses | Dunbar 1997 (a11) | established (K02) |
| Same, in data analysis | Later references 7.6 vs 1.5 (astronomy), 3.0 vs 1.25 (physics); t(28)=2.33; N=3 | Trickett et al. 2001 (b04) | established, tiny N |
| Students discount data that clash with a strong theory | 4/32 meteor proponents vs 6/10 volcano proponents accepted the data; N=64 | Chinn and Brewer 1993 (a07) | established direction; counts unverified |
| Data rated less believable when they contradict a held theory | 6.0 vs 8.0 (0-10), F(2,66)=7.292; N=72 | Brewer and Chinn 1994 (a10) | established |
| Anomaly responses form a small taxonomy | 7 tested, 1 added (8 types) | Chinn and Brewer 1998 (d13) | single-source |
| Offering an alternative theory did not reliably cut discounting | belief drop 0.97 vs 0.72, F<1 | Chinn and Brewer 1993 (a07) | contested (K16) |
| Anomalous cards named as normal | 114 ms vs 28 ms threshold; 10% fail at 1 s (second-hand) | Bruner and Postman 1949 via d10 | single-source |
| LLM agents ignore contradicting evidence | 25,000+ runs: ignored 68%, no belief update 71%, refutation-driven revision 26%; per-model revision 0.17 (Claude-4.5-Sonnet), 0.07 (GPT-4o), 0.04 (GPT-OSS-120B) | Rios-Garcia et al. 2026 (b13, b14) | single-source (K10) |
| Frontier agents pass about half of altered-physics worlds | 22 worlds, 11 models, pass = normalised MSE <0.1; Opus 4.7 45%, GPT-5.5 64% on the 11 paper worlds | DiscoverPhysics (a17, b15) | single-source (K09) |
| Top failure cause is not considering the right kind of law | 15 of 50 failed runs (Opus 6, GPT-5.5 9); self-monitoring failures 10 of 50 | DiscoverPhysics App. F (d01, d02) | single-source; labelled by Opus 4.7 |
| More rounds do not buy frame change | GPT-5.5 pass rate and explanation score stop improving after round 4 of 16 while MSE keeps falling | DiscoverPhysics (d03) | single-source (K21) |
| Structured hypothesis scaffold lifts belief revision | Explanation 51.64 to 75.09%; pass@1 7.27 to 56.36%; GPT-5.4 39.80 to 65.30% | EvoSCM (a19, b17) | single-source (K08) |
| EvoSCM ablations (GPT-5.5, from 75.09%) | free-text hypotheses 48.18; random experiments 47.45; no pre-commit 63.47; no induction 66.37; no deduction 67.09; no abduction 69.58; free-form rewrite 70.73; K=1 63.27; K=4 74.86 | EvoSCM Table 11 (d04) | single-source; episode-matched, not token-matched |
| Pre-committing predictions matters | 75.09 vs 63.47; norm MSE 2.77e-4 vs 4.79e-3 | EvoSCM (d04) | single-source (K07) |
| Self-correction without an external signal hurts | GPT-3.5 CSQA 75.8 to 38.1; GPT-4-Turbo GSM8K 91.5, 88.0, 90.0; oracle GSM8K 95.5 vs 75.9 | Huang et al. 2024 (b21, c07, c08) | single-source (K11) |
| LLMs under-test hypotheses | success 6 to 78% across 11 models; counter-example prompt lifts discovery 42 to 56% on average | Jhaveri et al. 2026 (b20) | established (K12) |
| FalsifyBench | best instruction-tuned 41%; top reasoning 75%, 68%; confirmation bias 27.3% (GPT-5.2-Chat) vs 66 to 82% for instruction-tuned | Bertolazzi et al. 2026 (c16, c17) | established with b20 |
| Open discovery benchmarks are unsaturated | DiscoveryWorld 38% easy / 18% challenge vs humans 66% / 55%; NewtonBench GPT-5 75.9%, Gemini-2.5-pro 65.4%, non-thinking <10%; hardest setting 40.3% / 16.7%; LLM-SRBench 31.5% | a25, a23, b23 | established (K13) |
| Tools can hurt strong models | code interpreter helps models <40% symbolic accuracy, slightly hurts >=40%; exploration tokens drop | NewtonBench (a24) | single-source (K14) |
| Static-prior Bayesian surprise yields non-new surprises | 37.5% spurious; 25 to 30% of expert-surprising hypotheses derivable from prior results | AutoDiscovery line (a22, b18) | single-source (K15) |
| Models commit or abstain; rarely calibrate | Kimi committed in 92.3%; Astra abstained in 100%; clean controls accepted in 19/64 (29.7%); L3 perfect score 0.6% | DISCERN (d06, d07) | single-source (K19) |
| Altered defaults hurt GPT-4 even if stated | few-shot CoT narrows but does not close the gap | Wu et al. 2024 (d15) | single-source |

## 4. Mechanisms and models

### 4.1 Anomaly ledger (from Fugelsang, Dunbar, KEKADA)
Implementable in code.
1. Before each experiment or check, the model writes a prediction with an expected range or class. Code stores it (pre-registered expectation).
2. After the result, code compares result to prediction. A miss is an anomaly record: id, prediction, observation, size of miss, round number, status.
3. Status moves open, then method-checked, then replicated, then explained, or retired as artefact.
4. Default policy: first miss goes to a method check (rerun, check units, inputs). Frame change is allowed only when the miss replicates, or when the miss is large and the check passes. Fugelsang's 12% versus 61% is the human rate of this policy, not proof it is optimal for an agent (K19 gap).
5. Count the open anomalies against the current frame. A class with 3 or more negative instances inactivates the hypothesis (KEKADA rule, a14).

### 4.2 Surprise detector and its flaw
Surprise is a deviation from an explicit expectation. A static LLM prior gives many false surprises (b18: 37.5% spurious). Add a derivability check: is this result already implied by the logged results? If yes, do not escalate.

### 4.3 Response menu (Chinn and Brewer)
Give the model the eight response types as a menu with a cost line each. Code tags which one it picked. Only "theory change" alters the core. The rest are cheap and often right (method errors are common in labs, so method blame is a good first guess, b01 limits). Untested whether showing the menu raises true theory-change rate (K04).

### 4.4 Impasse trigger options (S6)
Candidates, none compared in the literature (K20):
- Residual ratio over model noise (DiscoverPhysics trace: 6.7-fold unexplained near-field excess dismissed as noise).
- Flat refits: 3 refits plateau with no change of hypothesis class (trace: four plateaued refits at loss about 13).
- Committed-prediction miss rate.
Use an external signal. Self-rated confidence is not a safe trigger (b21).

### 4.5 Reframe, not refit
The failure audit says the main failure is never considering the right kind of law (d01). A frame change adds a structural entity (hidden source, new species, new dependency); a refit only moves parameters. Forced step: after poor residuals, name one structurally new entity and test it before refitting. Untested; HypoArena shows structured-skill prompts can swing ratings from +88 to about -58 depending on model (d17), so it must be measured.

### 4.6 Hypothesis population with discriminating experiments (EvoSCM)
Keep K competing hypotheses (K=4 gives 74.86% versus K=6 75.09%, so K=4 is enough). Each commits to a prediction. Choose the next experiment as the one where hypotheses disagree most. Turn each prediction-observation gap into a correction rule that edits dependencies, latent factors or functional forms. By ablation (GPT-5.5, from 75.09): free-text form and random experiments each cost about 27 points, pre-commit 11.6, induction, deduction and abduction 5 to 9.

### 4.7 Candidate frame before dropping (Kuhn, Burbules and Linn)
Require a named alternative frame before abandoning the current one. Contested: the Chinn and Brewer null on alternative theory, and Gershman's rational shielding, point both ways (K16).

### 4.8 Accident and side-effect entry route
Add an entry for results that were not predicted but are useful, even without a clash (X-rays, Priestley). Cheap: log unexpected side effects in the ledger and ask whether any is worth pursuing (K24).

## 5. What holds up

Holds up:
- Expert attention to unexpected results: Dunbar, Trickett and Alberdi point the same way. All are small and observational. No independent replication with computational scientists.
- Method-first, theory-after-replication timing: from Fugelsang's 3 labs; consistent with Dunbar's timing analyses.
- Theory-laden data ratings in students: Brewer and Chinn 1994 (2 points), Chinn and Brewer 1993.
- Confirmation-biased testing in LLMs and benefit of a counter-example prompt: two independent studies (b20, c16).
- Self-correction needs an external signal: Huang et al. 2024 (only Huang opened here).
- Frame-level failures in LLM science agents: three benchmarks agree that models do not revise (b13, a17, d06).

Failed, weak or contested:
- Alternative-theory help for students: null in Chinn and Brewer 1993 (F<1), but the authors guess students felt no need for a theory. Burbules and Linn reported the opposite.
- Experts versus students: opposite defaults, and Fugelsang's own work shows both at different times. Samples differ (3 labs; 3 scientists; 64 to 72 undergraduates).
- Dunbar's "unexpected" includes 8 of 18 findings consistent with the hypothesis, so attention to unexpected is not attention to contradiction.
- Method blame: 88% of inconsistent results (Fugelsang) versus little explaining away (Dunbar). Different labs and coding.
- Tools: NewtonBench says tools hurt strong models; EvoSCM says structure helps. Different mechanisms.
- Bruner and Postman: no replication found, original not opened.
- Kuhn's oxygen story as the only route: disputed (Hudson).
- Mental-set results (Haq et al., c20): in-context examples raise accuracy without cutting steps; no figures extracted. Vafa et al. (c12): orbit-trained models predict trajectories without recovering Newtonian force.

Moderators found: timing (early versus late), what is hit (core versus auxiliary), strength of prior belief, plausibility of theory (b03), replication, number of trials, availability of a substitute (contested), model strength (tools), external signal (oracle versus none).

Interventions that worked (LLM): counter-example prompt (42 to 56%); structured hypothesis population plus pre-commit; agent-chosen over random experiments (Opus 4.7, GPT-5.5). Did not work or unproven: intrinsic self-correction; more rounds; more experiments (BoxingGym saw error rise sometimes, c10); other labs' scaffolds (GEPA, ReasoningBank, ModelSMC, PiEvo did not clearly beat baseline, pass@1 0 to 10.91%).

## 6. Language models

How they behave:
- They rarely revise. 25,000+ runs: 68% of traces ignored evidence, 71% never updated, 26% showed refutation-driven revision (b13). Variance explained: base model 41.4%, environment 30.1%, scaffold 1.5%. The small scaffold share applies to the scaffolds tested, not to all possible ones. Outcome scores hide this.
- They lock in. NewtonBench traces show an early shift from exploration to exploitation in strong models (a24). GPT-5.5 stops improving after round 4 of 16 (d03).
- They fail where the fix is structural. DiscoverPhysics: best models pass about half; GPT-5.5 never proposed hidden sources in the dark-matter world (K09). Failure cause "never considered the right kind of law": 15 of 50.
- They miss signals they logged: 6.7-fold excess called noise; refits that plateau (d02).
- They confirm. FalsifyBench and Jhaveri: confirming tests dominate and success tracks falsifying tests.
- They normalise defaults. Wu et al.: GPT-4 drops when a familiar default is altered even if stated. This is the nearest analogue to Bruner and Postman.
- They are miscalibrated both ways on revision: commit (92.3%) or abstain (100%), and only 29.7% of clean controls accepted (DISCERN).
- Self-correction without outside feedback hurts: GPT-3.5 CSQA 75.8 to 38.1.

What changed it, by how much:
- Counter-example prompt: discovery 42 to 56% average (b20).
- EvoSCM scaffold: explanation 51.64 to 75.09; pass@1 7.27 to 56.36 (GPT-5.5). Not token-matched. Token use is higher than baseline on DiscoverPhysics and lower than GEPA, ReasoningBank, ModelSMC (bar chart only).
- Reasoning models over non-thinking on NewtonBench: under 10% to 30 to 80%.
- Oracle feedback: GPT-3.5 GSM8K 75.9 to 95.5 (inflated by stopping when correct).
- Evidence-informed priors cut spurious surprisal (b18).

Caveats: almost all of this is 2026, on three benchmarks, much of it single-lab preprints. LLM judges grade several scores (possible Claude-on-Claude favouritism in DiscoverPhysics). The failure labelling was done by Opus 4.7. Rios-Garcia c15 is a news restatement, not a separate source; b13, b14, b27, c15 are one study. Likewise Huang (b21, c07, c08), EvoSCM (a19 to a21, b17, c18, c19), DiscoverPhysics (a17, a18, b15, b16).

## 7. What our agent should take

### Add now (established)
1. **Pre-registered expectation and anomaly ledger** [E on the human side, K01/K07]. Part: S4 logging and S6 input. Code compares prediction to result and records misses. Evidence: b01, b02, a11, a13, d04. The EvoSCM drop (75.09 to 63.47) is single-source, so only the ledger itself is "add now"; the policy on top goes to tests.
2. **Disconfirming test before commit** [E, K12]. Part: G (extends G3). Evidence: b20, c16, c17. Require at least one test designed to fail the leading hypothesis.
3. **Do not trigger on self-rating** [E in effect, K11 with schema G1/G2]. Part: S6 trigger. Evidence: b21, c07, c08. The trigger must rest on code-measured signals (residual, failed prediction, repeated error).
4. **Believability guard** [E, K03]. Part: G (bias guard). Evidence: a10, a07, b03. Do not rate a result lower because it contradicts the current frame. Rate data credibility from method facts first (rerun, noise level), then compare to theory.
5. **Method check before reframe on a first miss; reframe allowed after replication** [E for humans, K01]. Part: S6/O8. Evidence: b01, b02, a11, b04. This is the human pattern. Its value for an agent is untested, so ship it as the default but keep the first-clash arm on the bench (section 8).

### Test first
| Item | Part | Status | Evidence |
|---|---|---|---|
| Forced "name one structurally new entity before refitting" | O8 | [S] K09 | a17, d01, d02 |
| Hypothesis population K=4 with discriminating experiment and pre-commit | S4-S6/O8 | [S] K08, K22 | a19, a20, d04, d05 |
| Impasse trigger comparison (residual ratio, 3 flat refits, prediction-miss rate) | S6 | [S] K20 | d02, d16 |
| Hold-then-replicate versus reframe-at-first-clash | S6 | [S] K19 | b01, d06, d07 |
| Derivability check on a surprise before reframe | S6/memory | [S] K15 | a22, b18 |
| Named alternative frame before dropping the old | O8 | [C] K16 | a05, a07, a09, b10 |
| Response menu (8 types) in the ledger | S6/O8 | [S] K04 | a06, d13 |
| Forced exploration burst when residuals stall | S6 | [S] K14, K21 | a24, d03 |
| Accident or side-effect entry route | O8 | [S] K24 | d09, d10 |
| Set-breaking cue after N same-method failures | G | [C] K17 | c20, c12 |
| Normalisation test: contradictory item in familiar template | none | [S] K06 | d15, a04 |

## 8. Concrete tests on our bench

All arms at equal total tokens (including setup, G7). Report mean and spread over at least 5 seeds.

1. **Trigger ablation.** Item type: DiscoverPhysics hidden-source worlds or NewtonBench shifted laws. Arms: plain; trigger = residual ratio; trigger = 3 flat refits; trigger = prediction-miss rate; trigger = self-rated confidence. Metric: pass rate (normalised MSE <0.1) and tokens to pass. Expected: code-based triggers beat plain; self-rated no better than plain.
2. **Hold versus reframe.** Item type: dossiers with injected anomalies, some real and some noise artefacts (DISCERN style with real controls). Arms: reframe at first clash; method check then reframe after one replication; never reframe. Metric: missed reframes on real anomalies plus false reframes on artefacts. Expected: replicate-first wins on mixed sets; first-clash wins only if artefacts are rare.
3. **Forced new entity.** Item: latent-structure worlds. Arms: think-longer; forced "propose one structurally new entity" step at S6; refit only. Metric: pass rate and false-reframe rate on worlds where the frame is right. Expected: gain on hidden-source worlds, small cost on plain worlds.
4. **Population K=4 and pre-commit.** Item: held-out anomaly worlds. Arms: single hypothesis; K=4 with discriminating experiment; K=4 without pre-commit. Metric: explanation score and pass@1. Expected: a gain that survives equal tokens, probably smaller than the reported 24-point explanation gain (EvoSCM was episode-matched, not token-matched).
5. **Counter-example prompt.** Item: 2-4-6 style rule items, then our own rule items. Arms: plain; counter-example prompt. Metric: success rate. Expected: about +14 points on average (42 to 56%).
6. **Derivability check.** Item: logged discovery runs with injected surprises, some implied by earlier logs. Arms: reframe on any surprise; reframe only if not derivable by code. Metric: wasted reframes and final pass rate. Expected: fewer wasted reframes with no loss in pass.
7. **Believability gap.** Item: identical result under two opposite primed frames. Arms: plain; credibility-first prompt. Metric: rating gap on a 0 to 10 scale. Expected: the human gap is 2 points; the credibility-first prompt narrows it.
8. **Normalisation.** Item: familiar templates with one stated or unstated contradictory item. Arms: plain; "list anything that conflicts with the template" step. Metric: rate of silent normalisation. Expected: unstated cases show more normalisation; the step cuts it.
9. **Entry-route test.** Item: tasks with a useful side effect and no clash. Arms: anomaly-only; anomaly plus side-effect log. Metric: discovery rate. Expected: gain only if side effects are present.

## 9. What does not transfer, and why

- Lab-meeting timing: human scientists face replication cost and social review; an agent can rerun cheaply. The 61% figure may not be the right threshold.
- Student studies (64 and 72 undergraduates, theories held for 10 minutes) do not describe how an agent holds a frame. The agent has no stake in a theory. The nearest effect is prompt-induced priming.
- Kuhn's sociology (community, crisis, generational change) has no agent counterpart. Only the logic transfers: expectation, anomaly, substitute.
- Bruner and Postman is human perception at millisecond exposure. Only the "normalise to the default" pattern might apply, and Wu et al. is the only analogue.
- Brain imaging (b06) is unread and not actionable.
- KEKADA's hand-driven example had no baseline; it informs design, not expected gain.
- EvoSCM's gains come from a benchmark tied to its own scoring and are not token-matched.
- DiscoverPhysics-style worlds have a simulator that gives a clean external signal. Many of our items (ARC, brainteasers) have a checker but no residual, so the residual trigger may not apply; use failed-check counts instead.
- Reframe on ARC-style items has a null result in the schema; anomalies there are test-output mismatches, not physical misses.

## 10. Open questions

1. Does any LLM study measure frame change with a clean contrast of structure-adding versus parameter-adding fixes? Closest is DiscoverPhysics hidden-source worlds; per-world numbers are only in a heatmap.
2. What does EvoSCM's gain cost at equal tokens, part by part?
3. Which impasse trigger works without an oracle? No comparison exists.
4. Is hold-then-replicate better for an agent than reframe-at-first-clash, with noisy anomalies?
5. Chinn and Brewer 1998: N, response frequencies and which factors moved theory change.
6. Replications of Dunbar, Trickett, and Bruner and Postman with other fields, computational scientists and LLMs.
7. Primary-source check of the oxygen case against historians' critiques.
8. Does a forced "propose one new entity" step raise reframe rate, and what does it do to false reframes?
9. How often is surprise already implied by logs?
10. Do LLMs normalise contradictory items in familiar templates, and what removes it?
11. Does any benchmark test a true paradigm-level anomaly in an LLM? None found (K18).

## 11. Sources

[V] opened (this session or an earlier pass of this study); [M] snippet, metadata or second-hand only.

- [V] Kuhn (1962) ch. VI and VIII, a01 to a03, a05, a27, a29, a30: https://home.csulb.edu/~cwallis/382/readings/690/Kuhn/kuhn.structure.pt4.pdf and https://home.csulb.edu/~cwallis/382/readings/690/Kuhn/kuhn.structure.pt5.pdf
- [M] Bruner and Postman (1949), a04, via Kuhn and Schindler 2024. No original URL.
- [V] Chinn and Brewer (1993) Cogsci, a06 to a08: https://escholarship.org/uc/item/4tf7084b
- [M] Burbules and Linn 1988, Stavy 1991, Samarapungavan 1992, a09, via Chinn and Brewer.
- [V] Brewer and Chinn (1994), a10: https://escholarship.org/uc/item/0q23c07n
- [V] Dunbar (1995/1997), a11, a12: https://chunk.cc.gatech.edu/AY2013/cs7601_spring/papers/Dunbar.pdf
- [V] Kulkarni and Simon (1988/1990) KEKADA, a13 to a15: https://ntrs.nasa.gov/api/citations/19920016497/downloads/19920016497.pdf
- [M] Darden (1991, 1992), a16: https://www.cambridge.org/core/books/reasoning-in-biological-discoveries/strategies-for-anomaly-resolution-diagnosis-and-redesign/76374D9CBB522A32B6F789E3809D0867
- [V] Wiemann et al. (2026) DiscoverPhysics, a17, a18, b15, b16, d01 to d03: https://arxiv.org/pdf/2605.26087
- [V] Zhao et al. (2026) EvoSCM, a19 to a21, b17, c18, c19, d04, d05: https://arxiv.org/pdf/2609.01526
- [V] Agarwal et al. (2025) AutoDiscovery, a22: https://arxiv.org/pdf/2507.00310
- [V] Agarwal et al. (2026) evidence-informed beliefs, b18: https://arxiv.org/pdf/2606.29182
- [V] Zheng et al. (2026) NewtonBench, a23, a24: https://arxiv.org/pdf/2510.07172
- [V] Jansen et al. (2024) DiscoveryWorld, a25, b22, c04 to c06: https://arxiv.org/pdf/2406.06769
- [M] Chinn and Brewer (1993) RER, a26: https://ideals.illinois.edu/items/17657/bitstreams/63442/data.pdf (not opened as PDF)
- [V] Fugelsang et al. (2004), b01 to b03: https://uwaterloo.ca/reasoning-decision-making-lab/sites/default/files/uploads/files/FugSteGreDun04.pdf
- [V] Trickett et al. (2001), b04, b05, d11: https://conferences.inf.ed.ac.uk/cogsci2001/pdf-files/1054.pdf
- [M] Fugelsang and Dunbar (2005), b06: https://uwaterloo.ca/reasoning-decision-making-lab/sites/default/files/uploads/files/FugDun2005a.pdf
- [M] Chinn and Brewer (1993) summary, b08: https://www.causeweb.org/cause/node/6957 ; (1998) b09: https://acnpsearch.tweb-dev.unibo.it/singlejournalindex/57109705
- [V] Gershman (2019), b10, b11: https://www.psychologie.uzh.ch/dam/jcr:c71d5674-6d7f-418f-89cf-d03d56618f52/Gershman_PBR_2019.pdf
- [V] Rios-Garcia et al. (2026), b13, b14, b27: https://arxiv.org/pdf/2604.18805 ; news restatement c15 (secondary): https://sciencenews.org/article/ai-ignore-evidence-trust-science
- [V] Trehan and Chopra (2026), b19: https://arxiv.org/abs/2601.03315
- [V] Jhaveri et al. (2026) Failing to falsify, b20: https://arxiv.org/pdf/2604.02485
- [V] Huang et al. (2024) self-correction, b21, c07, c08: https://arxiv.org/pdf/2310.01798
- [V] Shojaee et al. (2025) LLM-SRBench, b23: https://arxiv.org/pdf/2504.10415
- [M] Banatt et al. (2024) WILT, b24: https://arxiv.org/pdf/2410.10998
- [M] Alberdi, Sleeman and Korpi (2000), b26, d12 (Crossref metadata): https://api.crossref.org/works/10.1207/s15516709cog2401_2
- [V] Anomaly-detection perspective (2023), c01, c02: https://arxiv.org/abs/2307.11085 (not about science; low relevance)
- [V] Nova (2024), c03: https://arxiv.org/abs/2410.14255
- [V] Wang et al. (2024) Hypothesis Search, c09: https://arxiv.org/abs/2309.05660
- [V] Gandhi et al. (2025) BoxingGym, c10: https://arxiv.org/abs/2501.01540
- [V] Majumder et al. (2024) DiscoveryBench, c11: https://arxiv.org/abs/2407.01725
- [V] Vafa et al. (2025), c12: https://arxiv.org/abs/2507.06952
- [V] Denario project (2025), c13: https://arxiv.org/abs/2510.26887
- [V] Survey "From Automation to Autonomy" (2025), c14: https://arxiv.org/abs/2505.13259
- [V] Bertolazzi et al. (2026) FalsifyBench, c16, c17: https://arxiv.org/abs/2606.04751
- [V] Haq et al. (2025) mental set, c20: https://arxiv.org/abs/2501.11833 (no accuracy figures extracted)
- [M] Langley et al. (1987); Thagard (1992); Kulkarni and Simon (1988) from memory: c21 to c24, no URL.
- [V] Huang et al. (2026) DISCERN, d06 to d08: https://arxiv.org/pdf/2609.33357
- [V] Hudson (2001) via Schindler (2024), d09, d10: https://philsci-archive.pitt.edu/23718/1/Kuhn%20on%20Scientific%20Discovery.pdf
- [V] Chinn and Brewer (1998) abstract via ERIC, d13: https://api.ies.ed.gov/eric/?search=title%3A%22taxonomy+of+responses+to+anomalous+data%22&format=json&fields=id,title,description
- [V] Brewer and Chinn (1994) PSA, d14: https://www.cambridge.org/core/journals/psa-proceedings-of-the-biennial-meeting-of-the-philosophy-of-science-association/article/scientists-responses-to-anomalous-data-evidence-from-psychology-history-and-philosophy-of-science/668FEBB13D35B22E47A57FD3487AC2CF
- [V] Wu et al. (2024) Reasoning or Reciting, d15: https://arxiv.org/pdf/2307.02477
- [V] HypoArena, d17: https://www.alphaxiv.org/abs/2607.15766.md
