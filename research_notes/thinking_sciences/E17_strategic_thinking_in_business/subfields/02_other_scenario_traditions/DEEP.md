# Other scenario traditions: deep document

*Subfield E17.02. Scope: Kahn's stories at RAND, La Prospective (Berger), morphological analysis (Zwicky, Ritchey), Delphi and its hybrids (cross-impact, Policy Delphi), and financial stress tests. Source files in this folder: evidence_a-d.jsonl, claims.jsonl (K01-K24), critique.md. Role for the agent: background, plus a small set of testable protocol ideas. Almost all human-tradition evidence is second-hand (Wikipedia, one Ritchey PDF, Fed documents). Almost all LLM evidence is 2024-2026 preprints, mostly single-team and small-sample.*

## 1. What it is

Four families of foresight method sit beside the Shell-style scenario planning covered in subfield 01. They share one idea: do not predict one future. Build structured pictures of several futures, or structured sets of expert estimates, and reason from them.

- **Kahn's stories at RAND.** Herman Kahn (RAND in the 1950s, Hudson Institute from 1961) wrote futures "from inside": narrative paths, war-game style, for nuclear war and escalation. He also wrote The Year 2000 (1967, with Wiener) with branching baseline scenarios and a list of 100 technical innovations judged very likely. [a01, a02, a03, b04, d09]
- **La Prospective (Berger, France).** Gaston Berger's French school built normative scenarios from the 1950s, book in 1964. Normative means: start from a desired or required future and ask what leads to it. Only a Wikipedia mention was read. [a03]
- **Morphological analysis (Zwicky; Ritchey's general version, GMA).** List the parameters of a problem. Give each parameter a set of values. Every combination is a configuration. Then prune combinations whose value pairs cannot co-exist (cross-consistency assessment, CCA). What is left is the solution space. [a06-a09, b05, c18, c19]
- **Delphi and hybrids.** Developed at RAND by Helmer, Dalkey and Rescher. Experts give estimates anonymously, see a summary of the group's answers and reasons, and revise over rounds. Variants: real-time, Policy Delphi, Argument Delphi, Disaggregative Policy Delphi, fast-track, and Delphi plus cross-impact analysis. [a10, a11, a13, b03]
- **Financial stress tests.** A regulator or bank fixes a baseline and a more adverse macro scenario, then computes losses and capital need. Large banks ran them from the early 1990s, a 1996 Basel I amendment required them, and regulators ran their own after 2007. [a14, a15, a16]

Why it matters for our agent: these traditions give a few concrete protocol patterns (enumerate a space then prune by pairwise checks; anonymous independent estimates then feedback; stated baseline plus adverse case with probability anchors). Each can be tested at equal tokens. None is a proven forecaster on its own record (K23).

## 2. History and theories in depth

**Kahn and RAND (1950s-1967).** Kahn studied nuclear war survivability. On Thermonuclear War (1960) sold 14,000 copies in two months. His escalation ladder grew from 16 steps (1962) to 44 steps (On Escalation, 1965). Note: one Wikipedia page dates Thinking About the Unthinkable to 1965; the Kahn page says 1962, and 1965 probably belongs to On Escalation (critique correction 4, mostly settled). The Year 2000 (1967) lists 100 technical innovations (Table XVIII) and predicted Japan passing the US in per-capita income by 1990. The sources read give no hit-rate count for any of this. Reception was mixed; critics called On Thermonuclear War a moral tract on mass murder. [a01, a02, b04, d09]

**Berger and Wack.** Berger's La Prospective ran in France at the same time as Kahn. Wack at Shell London (from 1971, pushed on by the 1973 oil shock) turned scenarios into a corporate strategy tool; two HBR articles in 1985 carried Kahn's ideas into business. The claim that Shell anticipated two oil shocks needs a citation. An early-1980s Shell review under de Geus reportedly found weak implementation came from decisions after the scenarios, not the scenarios themselves. Evidence for the value of scenario planning is called "largely anecdotal and mostly from Shell". Diffenbach (1983): alternate scenarios were the third most popular long-range technique, used by 68% of large firms (adoption, not accuracy). [a03, a04, a05, d08]

**Zwicky and Ritchey.** Zwicky generalised morphology from anatomy and geology to relations among ideas, calling it totality research, and worked on it about 30 years from the 1940s to 1974 (Discovery, Invention, Research, 1969). Ritchey (1998, 2006, rev. 2013) made it general and computer-supported (Swedish Defence Research Agency, since 1995; over 100 computer-aided projects). CCA allows three kinds of inconsistency: logical contradiction, empirical implausibility, normative constraint. Normative judgments must be held back until the possible set is found. Scale examples: a 5x5x3 box has 75 cells; a Swedish shelter-policy field 4x4x4x3x3x4 has 2,304 configurations; the original 10-parameter field had over 500,000; a field of 100,000 configurations needs only a few hundred pairwise judgments. A Wikipedia bread example has 6 categories with 4 options each (5^6 = 15,625 in the page's raw count). Applications: engineering design, technology forecasting, organisation design, policy analysis. The method suits problems that cannot be quantified where causal models and simulation fit poorly. No accuracy or outcome study was found; Ritchey is the main advocate and the source of most claims. [a06-a09, b05, d10]

**Delphi.** Origin: a 1944 US Army Air Corps report on future military technology; RAND project Delphi (Dalkey and Helmer 1962 RM-727/1, 1963 Management Science paper; Gordon and Helmer 1964). The authors disliked the name for sounding occult. Primary papers were blocked (RAND 403), so no respondent or round numbers were read. Variants and critiques: strong personalities may dominate; self-rated expertise weighting may breed overconfidence; non-expert panelists "only add confidence to ignorance"; Sackman (1974) is the standard critic. Cross-impact analysis (Gordon and Helmer 1966) gives each of 10-40 events a prior and pairwise conditional probabilities, then simulates; it began as a card game (Future, UCLA 1968); Institute for the Future added time series in 1972; Delphi plus cross-impact was combined in 1984. It needs exact probabilities and can yield impossible values with negative impacts. Speed: a three-round human Delphi takes 3-4 months (Gordon 2009); fast-track about 3 weeks; eLAC ran 5 rounds with 1,454 contributions; TechCast about 100 experts. [a10-a13, b03, d06, d07]

**Stress tests.** The key design: two scenarios (consensus baseline and a "more adverse" case that is explicitly not a worst case but severe and plausible) and disclosed assumptions. In SCAP 2009 the baseline was the average of Consensus Forecasts, Blue Chip and SPF (Feb 2009). The adverse path had probability anchors: about a 10% chance of 2010 unemployment this high (Blue Chip history); about 15% joint GDP and unemployment (survey subjective probabilities). Authors admit forecasts moved: consensus for 2010 unemployment was 9.3% by results time. Taleb's critique: arbitrary-number tests can be gamed. Borio, Drehmann and Tsatsaronis (2014): macro stress tests are poor early-warning devices in calm times but work for crisis management and resolution. Scenarios are only as good as the designers' imagination: EBA 2009 and 2010 adverse euro-area growth was -0.6%, revised to -4.0% for 2011. [a14-a17, d16]

## 3. Core findings with exact numbers

Status key: single = single-source (one paper or team); established = official primary document or several sources; thin = second-hand or abstract only.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| LLMs ranked 30 live Kickstarter ventures better than managers | Spearman: Gemini 2.5 Pro 0.74; GPT-5 family 0.67-0.71; best of 3 MBA investors 0.45; 346-manager aggregate 0.19; human range 0.04-0.45; 870 pairwise comparisons per model; 20 LLMs, temp 0.5 | Csaszar, Peterson, Wilde 2026 (a18) | single; one domain, single calls |
| Human 0.04 and 0.19 are not distinguishable from zero | Gemini vs Expert 3 diff 0.29 (p=0.063); vs crowd 0.55 (p=0.001); CIs wide | same (a18, critique) | single |
| Replication of the tournament | 26 projects (3 removed), LLM-only, lower correlations, model-rank consistency about 0.54 over 19 models | same (a19) | single; not a human-vs-LLM replication |
| Ensembles did not beat best single LLM | Best human + Gemini 0.67 < 0.74; Gemini + GPT-5 Mini 0.77 (+0.03, n.s.); GPT-5 variants inter-correlate 0.80-0.97 | same (a19, a20) | single |
| LLM Delphi panel tracks benchmark truth only with evidence | r 0.91-0.98; MAE 4.5-6.1 pp; ECE 1.6-4.1 pp; GPT-5.1 r 0.97/0.97/0.91, Opus-4.1 0.95/0.98/0.93; anonymised r 0.30, -0.22, -0.40; plausibility ranges hold truth 39-80% | Lorenz and Fritz 2026 (a21, a22, b09, b10) | single; no rounds ablation (d13) |
| LLM panel vs human panels | Human A vs B 16.6 pp mean abs diff; GPT-5.1 vs A 5.0; Opus-4.1 vs A 12.8; persona-set swap MAD 3.0 (GPT-5.1), 1.9 (Opus) | same (b11, d13) | single |
| LLM panels diverge on long horizons | 2050 high-warming sea level: LLM about 65 mm vs human 120 mm; at 2300 two LLMs differ 2.6x; post-2018 evidence moved GPT-5.1 medians down 11-28% | same (b12) | single; contamination possible |
| Base model beats persona | Persona effect 2.4 pp vs model effect 4.8 pp (after mediation 0.5 vs 4.4) | same (a23, b13) | single; same direction in Sela |
| LLM panelists conform | Rationales citing panel mean: humans 0.6%, GPT-5.1 +45.4 pts, Opus +49.4; numeric convergence Opus 0.49 to 0.19, humans 0.73 to 0.55, GPT 0.10 to 0.08 | same (a24, b13) | single |
| Mixed-model panels keep disagreement | First-choice share child welfare 70.9% to 46.1% (p<0.001, r=0.58); housing 46.0% to 22.9% (p<0.001, r=0.50); 120 deliberations; 7-9B models | Sela 2026 (a26, b23) | single; small models |
| Feedback and self-confrontation failed on small models | Two exposure rounds compounded sycophantic flips; self-confrontation changed 0 votes in 10 runs | Sela 2026 (c17, d14) | single |
| LLM Delphi run-to-run variance | 12 runs; fragmentation theme in 7 of 12; run 1 has 9 of 14 topics, run 9 has 10 of 14 | Bertolotti and Mari 2025 (a25, b06, b07) | single; no ground truth |
| LLM Delphi vs Metaculus | 50 experts, temp 1.5, stop at SD<10%; spread vs correctness p=0.053 over 100 scenarios | Barrett et al. 2025 (b08) | single, weak |
| LLM vs human experts on a risk model | Probabilities within 6% (never over 15%); quantities lower by up to 70%; extra LLM rounds said not to help (a remark, not a test) | Barrett et al. 2025b (b14, b15) | single |
| One feedback round helps only mixed models | Log loss diverse/shared 0.501 to 0.481 (p 0.017); diverse/distributed 0.475 to 0.453 (p 0.18); homogeneous 0.517 to 0.525 and 0.525 to 0.545 (n.s.); 202 Metaculus questions; min detectable effect about 0.047 vs observed 0.022 | Schneider and Schramm 2025 (d01, d02) | single; underpowered, no token match |
| Round count in a Delphi agent | Brier/acc: 1 round 0.206/74.1%; 2 rounds 0.178/77.9%; 3 rounds 0.196/75.7%; no rationale sharing 0.211/70.4%; 375 Polymarket markets | InfoDelphi 2026 (d03, d04) | single; zero-shot 0.201 beats most baselines |
| InfoDelphi baselines | Zero-shot 0.201, CoT 0.216, self-consistency 0.221, debate 0.202, crowd 0.245, MoA 0.220; Llama-4-Scout 0.209 to 0.204 | same (d04) | single |
| Story-framed prompt hurt forecasts | Median Brier direct vs narrative: o3 0.1352 vs 0.1985; GPT-4.1 0.1542 vs 0.1842; DeepSeek-v3 0.1798 vs 0.2689; Claude 3.6 Sonnet 0.1810 vs 0.2345; GPT-4o 0.1883 vs 0.1940; Qwen3-235B better 0.1871 vs 0.1923; worse for 11 of 12 models; experts 0.1573 | arXiv 2507.04562 (d05) | single; not Kahn-style |
| Scenario severity follows prompt wording | Prompt partial eta-sq 0.87 (GPT), about 0.40 (Llama); removing severity bands: recession 1.6 pp milder (-3.85 to -2.20), VaR multiple -17%, CVaR -15%; 2,420 G7 scenarios | Soleimani 2026 (b17, d12) | single; eta-sq inflated by design |
| Small model contradicts itself in scenarios | Llama-3.1-8B 4-7x more dispersed; contradicts own stated changes in 90%; 744 accepted (11.4% rejected); GPT 838 of 840 accepted; repeat run agrees on aggregate within 0.007x | same (b18, d12) | single |
| Narrative and number severity decouple | Association about zero in severe and systemic tiers (three quarters of corpus); unanchored r +0.014; retrieval null in every run | same (b19) | single |
| Futures Wheel agents broaden coverage | 30 runs; 86-110 consequences cut to 27-47 unique risks; theme similarity over 0.95; 290 domain experts and 7 leaders rated; systemic share agents 84-100% vs human-only 24-63%; expert-rated systemic 93%; over 90% negative; labelling F1 0.86 | Fruhling et al. 2026 (b20, b21) | single |
| Paired counterfactual scenarios are plausible | n=234 raters; severity 3.66, plausibility 3.94; severity change -0.38 (SD 1.01, p<0.001); 40% of scenarios lower in severity; GPT-4 failed to depict 39 impact types | Barnett et al. 2024 (b22) | single |
| Persona panel with grounding tracks humans | r: single judge 0.716, prompt-ensemble 0.789, full 0.922; no dynamics 0.891; no grounding 0.811; UI ratings task | 2026 UI panel paper (b24; arXiv id not re-verified) | single; unverified |
| Morphological box shrinks a space | 4x4x4x3x3x4 = 2,304; original field over 500,000; 100,000 configurations need a few hundred pairwise judgments | Ritchey 2006 (a06, c18) | thin; advocate source; no accuracy test |
| 2009 US stress test (SCAP) | 19 BHCs (two-thirds of assets); adverse: 2010 unemployment 10.3%, GDP -3.3% (2009) and +0.5% (2010); losses about $600B (loans about $455B, trading and securities $135B); 10 of 19 short; $185B buffer before Q1 actions, $74.6B after; Treasury preferred equity $216B | Federal Reserve 2009 (a15, a16, c20) | established (official); estimates, not realised outcomes |
| Stress test information value | Market moved only at the results release (significant abnormal returns for gap banks); not at announcement or method events; aggregate gap $75bn vs market guess $100-200bn; tied to a government backstop clarification | Peristiani, Morgan, Savino 2010 (b16, c21) | single episode |
| Adverse cases set too mild | EBA adverse -0.6% (2009, 2010), -4.0% (2011); 25 banks failed 2014 EBA test | Wikipedia (a14, d16) | thin |
| Delphi vs other groups (human labs) | Delphi beat statistical groups 12 to 2 (2 ties); beat interacting groups 5 to 1 (2 ties); no consistent edge over other structured methods | Rowe and Wright 1999 (b01, d06) | thin; abstract only |
| Delphi single business case | 3-4% error on two-year sales vs 10-15% quantitative vs about 20% unstructured | Basu and Schroeder 1977 via Wikipedia (a10, b02) | thin; one case |
| Macro stress tests as early warning | Poor in calm times; useful for crisis management | Borio et al. 2014 (a17) | abstract only |

## 4. Mechanisms and models

Each is written so an engineer could build it. None is validated on our agent; see section 7 for status.

**4.1 Morphological box with pairwise pruning (Zwicky/Ritchey).**
1. The program asks the model for 4-8 parameters of the problem and 3-5 values each (slot call). Code deduplicates values.
2. Code builds the full product. For 6 parameters of 4 values this is 4,096.
3. For every pair of values from different parameters, code sends one short slot call: "Can these two coexist? Answer logical / empirical / normative / ok". The pair count is the sum over parameter pairs of (ni x nj): for 6 parameters of 4 values, 15 x 16 = 240 calls, not 4,096. This is the point of CCA: judgments are pairwise, configurations are many.
4. Code marks a pair forbidden only for logical or empirical conflict. Normative conflicts are stored but not applied until the feasible set exists (Ritchey's rule).
5. Code enumerates configurations with no forbidden pair. Output: the remaining set, with counts before and after pruning.
6. Choosing which configuration to try is done by code (run or check), not by the model's taste (G8).
Risk: model pair labels are noisy and correlated. Run each pair twice and keep disagreements as "uncertain", not "forbidden" (G4: same-model samples are not independent).

**4.2 Delphi round (LLM version).**
Round 1: K independent drafts, all with the same evidence package (identical evidence is what matters: Lorenz). Code computes the median and spread. Round 2 (optional): each draft sees an anonymous summary (median, range, 2-3 short rationales). Revised answers are aggregated by code. Stop rules in the literature: spread below a threshold (Barrett: SD<10%) or a fixed round count (InfoDelphi best at 2). Known failures: LLMs cite the panel mean (conformity), spread shrinks, small models flip to wrong answers. The variant that fared best: rationale sharing among mixed models (d01, d03).
Arm design that isolates the mechanism: the same K calls, with or without the feedback step, aggregated by code.

**4.3 Scenario set with stated anchors (stress-test pattern).**
Code fixes a baseline from a reference (numbers, not model opinion). The model writes the adverse path only as narrative; the severity path is prescribed by code with a stated probability anchor ("about 10% chance", SCAP style). Output must give both levels and changes. A reconciler (code) checks that stated changes equal level differences against the fixed baseline, and flags a scenario whose narrative tone and number disagree. Soleimani's authors advise exactly this: prescribe severity, use the model for story.

**4.4 Cross-impact.**
Event list of 10-40 events with priors and pairwise conditional probabilities. Code samples joint outcomes by simulation and returns scenario frequencies. Code does all arithmetic. The model only proposes events and conditional numbers. Guard against impossible values with negative impacts (clamp and flag).

**4.5 Futures Wheel.**
Start from a change. Level 1: the model lists consequences. Level 2: for each, list second-order consequences. Condense by embedding similarity (threshold set in code). Fruhling used 6 agents per wheel and got 86-110 items per run, reduced to 27-47 unique. Add a forced benefits pass because agent output was over 90% negative.

**4.6 Kahn-style branch then probability (untested).**
Write 3-5 branch narratives from inside the future. For each, the model states the key event chain and a weight; code normalises weights to sum 1 (G5) and combines branch-conditional answers into one probability. Compare with a direct probability. This differs from the narrative prompt that failed in d05, which was one scripted discussion.

## 5. What holds up

**Holds up (several sources or official record).**
- LLM panels conform and compress spread. Seen in Lorenz (citing panel mean: humans 0.6% vs +45 pts), in Sela (70.9% single-model concentration), and as a stated limit in Barrett. The direction is consistent across teams, even though each number is single-study. [K04]
- Model choice matters more than persona for estimates (4.8 vs 2.4 pp). Sela finds the same shape on policy choices. Heterogeneous models reduce artificial consensus. [K05]
- LLM-run Delphi output is run-dependent. Bertolotti and Mari show themes appear in only some of 12 runs; Soleimani shows per-scenario variation with aggregate agreement. [K06]
- LLM estimates diverge from human experts on quantities and long horizons while bounded probabilities agree (within 6%). Reconciliation of Lorenz (5.0 pp for GPT-5.1) with Barrett (quantities up to 70% lower): agreement holds on bounded percentages with evidence; divergence on unbounded quantities and long horizons. [K16]
- The stress-test design pattern is documented in the official record (SCAP). The market learned at the results release, not at the method announcement. [K09]
- Morphological enumeration arithmetic is exact and the pairwise structure suits batch labelling. [K11] The accuracy of the method for decisions is not tested.

**Single-source, not yet reliable.**
- Csaszar: LLMs beat humans at ranking ventures. The human comparison is thin (3 investors; 0.04 and 0.19 are indistinguishable from zero), the replication was LLM-only, and the authors do not claim a general strategy result. [K01, K02]
- Evidence-dependence in Lorenz: without benchmark and agent identity the panel is noise. Strong and plausible, but there is no round ablation and training-data contamination is possible. [K03]
- Severity set by prompt (Soleimani). The authors call eta-sq 0.87 inflated by design. [K07, K08, K22]
- Futures Wheel breadth (one team, GPT-4.1 mini). [K13]

**Failures and moderators.**
- Feedback rounds: small or none. Schneider and Schramm found one significant cell of four (0.501 to 0.481), none for same-model groups, and worsening for homogeneous groups (0.525 to 0.545, n.s.). InfoDelphi found 2 rounds better than 1 but 3 worse, mostly from rationale sharing. Sela found two rounds of exposure compounded flips on 7-9B models. Barrett says extra rounds did not help. Lorenz has no round data. No study matches tokens against independent samples plus averaging. [K15, K20]
- Delphi helps in Lorenz, yet the Barrett spread-vs-correctness test is only p = 0.053 and no source ablates rounds, so rounds are not shown to add value over one evidence-rich pass.
- Story framing: a scripted narrative hurt 11 of 12 models (o3 0.1352 to 0.1985). [K21]
- Persona-only diversity is weak. [K05]
- Ensembles: averaging did not beat the best single LLM in Csaszar, since same-family models correlate 0.80-0.97. Lorenz and Sela say model diversity helps against consensus; these measure different targets (ranking accuracy vs spread), not necessarily a conflict. [K02]
- The traditions' own forecasting record was not recovered. RAND papers were blocked; no hit-rate count for Kahn Year 2000, Shell or La Prospective. Shell evidence is anecdotal and self-reported. [K17, K19, K23]
- Stress-test adverse cases were too mild before the 2011 euro crisis (-0.6% vs -4.0%). [d16]

**Interventions that worked (weakly).** Mixed-model groups with shared information plus one round (d01). Rationale sharing and two rounds in one agent system (d03). Grounding the panel in evidence (b24, a22). Reconciling levels with changes against a fixed baseline (d12).

**Interventions that did not work.** Self-confrontation (0 vote changes in 10 runs). Persona variety. Rounds beyond 2. Retrieval added to a prompt that already fixed macro anchors (null in every run). Narrative prompts. Debate-like designs are already banned by schema guardrail G9.

## 6. Language models

- **Ranking and judgment (Csaszar).** Frontier models beat humans on a 30-venture pairwise task. Gemini 2.5 Pro 0.74, GPT-5 family 0.67-0.71. Claude models ranked near the bottom of the 20 LLMs. Size did not predict (Gemma-3-4b beat 27b). Reasoning mode had inconsistent effects (Grok-4 reasoning beat non-reasoning; DeepSeek Chat beat Reasoner). The replication on 26 projects gave lower correlations and rank consistency about 0.54 over 19 models, so model rank is unstable. [a18-a20, d15]
- **Delphi simulation.** Panels of 5 personas with a mediator reproduce benchmark success rates (r 0.91-0.98) when given the benchmark description and the agent identity; anonymised, r falls to 0.30/-0.22/-0.40. Rationales are long (GPT 736 chars, Opus 414, humans 234). Panel spread is compressed. Plausibility ranges hold truth only 39-80%, so they are not calibrated intervals. The cost claim (months of human Delphi replaced by a run) has no figures. [a21-a24, b09-b13, d13]
- **Forecasting rounds.** Gains of 0.02 log loss or 0.02-0.03 Brier at best, in one cell or one run, sensitive to the backend (DeepSeek-V3.2 0.184 to 0.163; Llama-4-Scout 0.209 to 0.204). Cost per run $12.66 (GPT-5.4-mini), $3.51 (DeepSeek), $0.51 (Llama). Zero-shot (0.201) beats most elaborate baselines, so the Delphi margin over zero-shot is 0.023. [d01-d04]
- **Stories.** A story-first prompt hurt. A direct range-first prompt is the strong baseline. [d05]
- **Scenario generation.** Severity follows the prompt. Small open models contradict their own stated changes 90% of the time. Narrative severity and numeric severity decouple. [b17-b19, d12]
- **Foresight breadth.** Agents list more risks and more systemic ones than humans, but skew negative; humans judge their own, fewer risks more likely. [b20, b21]
- **Counterfactual scenarios.** GPT-4 pairs show a small rater-perceived severity shift (-0.38) but failed to depict 39 impact types. [b22]
- **Not tested at all.** Kahn-style stories, La Prospective, LLM-run morphological analysis (cross-consistency) and probability-anchored adverse scenarios on agent decisions. Searches were negative but recall was low because APIs were rate-limited. [K12, K24, d11]

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory = section 5 of SCHEMA.md. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **If diversity is needed at an estimate or scenario step, vary the model, not the persona.** Part: G4 (extends "no persona voters" to scenario and estimate steps) and O (diversify). [E] K04, K05; evidence a23, a24, b13, a26, b23, c16.
2. **Log run-to-run variation of any scenario or estimate step and report the aggregate, not one run.** Part: G (reproducibility; section 6 run log). [E] K06; a25, b06, b07, c02, b18.
3. **Treat bounded probabilities as more reliable than raw quantities and long horizons; check monotonicity of numeric estimates across difficulty.** Part: G (calibration). [E] K16; b14, b15, c07, b12.
4. **Pairwise-pruned enumeration of an option space (section 4.1) as an optional S/O helper**, only when the option space is a product of a few parameters and each pair is cheap to label. Mechanism [E]; benefit for decisions unproven, so it stays behind G7 and trial T5. Part: O (enumerate options) / S. [E] for mechanism, [S] for benefit; K11; a06, a07, c18, c19.
5. **Record scenario assumptions with a baseline and an adverse case with a stated probability anchor** (design pattern from SCAP). Part: memory/log. [E] as official practice (K09; a15, a16, c20); agent benefit untested.

### Test first (not established)

| Item | Part | Status | Evidence |
|---|---|---|---|
| Rationale-sharing round among a mixed-model set vs K independent samples averaged | O (ensemble), G9 | [S], weak, partly [C] | K20; d01-d04 |
| Identical evidence package supplied before any scenario or estimate step | G (ground) | [S] | K03, K18; a22, b10, b24 |
| Branch-then-probability (Kahn style) vs plain probability | S0/O1 | [S], open | K21, K12; d05 |
| Prescribed severity path plus text-to-number reconciliation in code | G5 | [S] | K07, K08, K22; d12 |
| Futures Wheel consequence tree vs single-pass list | O (enumerate consequences) | [S] | K13; b20, b21 |
| Paired counterfactual scenarios (with/without an action) | O4 analogue | [S] | K14; b22 |
| LLM cross-consistency labels for morphological boxes | O/S | [S] | K11 |
| Pairwise ranking task at equal tokens, agent vs plain single call | S0 | [S] | K01, K02; a18-a20 |

Do not add: Delphi as a default round process, narrative prompts for forecasting, persona panels. These conflict with G9, G4, 4b and the d05 result.

## 8. Concrete tests on our bench

All arms at equal total tokens (calls x length). Report setup cost (G7).

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Delphi round vs independent average | Resolved binary forecasting questions (100+) | A: K independent samples, mean by code. B: same K samples plus one anonymous rationale-sharing round, mean by code | Brier; paired difference with CI | 0.00-0.02 gain in mixed-model, none in single-model. Add only if B beats A by 0.01 Brier with CI excluding zero |
| T2 Kahn branches vs plain | Same questions | A: direct probability. B: 3-5 branches with weights, code-normalised, conditional answers combined | Brier | Likely no gain (narrative hurt in d05); may help on multi-path questions |
| T3 Severity anchor | 100 macro or risk scenarios | A: free severity. B: severity prescribed by code plus reconcile check | Contradiction rate (stated change vs level); severity variance over 5 runs | Contradictions down sharply for small models; small gain for large |
| T4 Evidence ablation | Estimation items with known answers | A: model alone. B: same evidence package injected | Correlation with truth; MAE | Large gain from evidence (Lorenz: r about 0 to about 0.95) |
| T5 Morphological pairwise pruning | Design tasks with a human-labelled valid-configuration set | A: free brainstorming. B: box plus pairwise labels | Coverage of valid configurations; share of invalid kept; agreement with human pair labels | Coverage up; label agreement unknown; about 30 pairs per task |
| T6 Model vs persona diversity | Scenario generation, forecasting | A: 5 personas on one model. B: 5 models, one prompt. C: 5 samples, one persona | Distinct-branch count; Brier | B wins on distinct branches; accuracy unknown |
| T7 Futures Wheel | 20 change events | A: single-pass list. B: two-level wheel plus benefits pass | Unique risks; expert-rated systemic share | Breadth up; check negative skew |
| T8 Ranking | Pairwise ranking of fresh ventures or papers | A: plain single call. B: our agent | Spearman with later outcome | Unknown; Csaszar-scope replication |
| T9 Run variance | Our scenario step | 5 repeats | Theme recall across runs; aggregate stability | Per-run theme recall well below 100% (Bertolotti pattern) |

## 9. What does not transfer, and why

- **Human consensus building.** Delphi's value in humans is partly social: anonymity blocks dominant personalities and experts bring private knowledge. LLM panelists share one training set, so independent knowledge is missing and conformity is written into the text (+45 points citing the mean). Same-model samples are not independent (G4).
- **Narrative as a thinking aid.** Kahn's "from inside the story" shakes human assumptions. A model already writes fluent stories; the tested story framing worsened Brier for 11 of 12 models.
- **Workshop morphology.** Human CCA is a group judgment. Model pair labels are cheaper but correlated and untested against human workshops.
- **Stress-test legitimacy.** Part of the SCAP effect came from the government backstop and the public release. An agent has no market to inform.
- **Scenario as organisational learning.** Shell's value was said to come from changed managers' mental models. A single agent has no managers; the Shell audit blamed post-scenario decisions anyway.
- **Csaszar ranking.** One domain and single calls; not evidence for an agent scaffold.
- **Long-horizon quantities.** LLM estimates diverge from experts here, so "Delphi replaces experts" is unsafe for numbers.
- **Cost claims.** "Three orders of magnitude cheaper than human Delphi" has no figures.

## 10. Open questions

1. Does a feedback round add accuracy beyond independent samples averaged at equal tokens? No study matches tokens.
2. Do Kahn-style branches then probabilities beat direct probabilities? Untested.
3. What were the primary Delphi numbers (Dalkey and Helmer 1963 error by round), and what did Sackman 1974 and Rowe and Wright 1999 find in full? RAND and ScienceDirect were blocked.
4. Can an LLM do cross-consistency labelling reliably (agreement with human workshops; share of valid configurations kept)?
5. How well did Kahn's Year 2000, Shell and La Prospective forecast (hit rates)? None found.
6. Does the Csaszar ranking result hold in other domains and for scaffolds at equal tokens?
7. How to anchor severity so it follows numbers; does text-to-number reconciliation fix it?
8. Do stress-test-style adverse scenarios with probability anchors improve agent decisions?
9. Does model heterogeneity beat persona heterogeneity on accuracy (not only spread) at equal tokens?
10. Does the persona-panel UI result (b24) exist as stated? arXiv id 2607.28439 returned a page but no API record.

Links to parallel subfields (not covered here): Retrieval and ensembles for LLM forecasts; Debiasing; Structured analytic techniques; Search theory; Imprecise credences; Probabilistic programming; Collective intelligence factor c; Weick's organisational sensemaking.

## 11. Sources

[V] = opened and read (page text); [M] = snippet or abstract listing only.

- [V] Wikipedia: Herman Kahn. https://en.wikipedia.org/wiki/Herman_Kahn (a01, a02, b04, d09)
- [V] Wikipedia: Scenario planning. https://en.wikipedia.org/wiki/Scenario_planning (a03, a04, d08)
- [V] Wikipedia: Pierre Wack. https://en.wikipedia.org/wiki/Pierre_Wack (a05)
- [V] Ritchey (2006, adapted 1998; rev. 2013) General Morphological Analysis. https://www.swemorph.com/pdf/gma.pdf (a06-a08, c18, c19)
- [V] Wikipedia: Morphological analysis (problem-solving). https://en.wikipedia.org/wiki/Morphological_analysis_(problem-solving) (a09, b05, d10)
- [V] Wikipedia: Delphi method. https://en.wikipedia.org/wiki/Delphi_method (a10, a11, b02, b03, d07)
- [M] Dalkey and Helmer (1962) RM-727/1, catalogue page only. https://www.rand.org/pubs/research_memoranda/RM727z1.html (a12)
- [M] Dalkey and Helmer (1963) Management Science. https://doi.org/10.1287/mnsc.9.3.458 (b26)
- [M] Ritchey (1998) GMA. https://www.swemorph.com/ma.html (b25)
- [V] Wikipedia: Cross-impact analysis. https://en.wikipedia.org/wiki/Cross-impact_analysis (a13)
- [V] Wikipedia: Stress test (financial). https://en.wikipedia.org/wiki/Stress_test_(financial) (a14, d16)
- [V] Federal Reserve (2009) SCAP design and implementation. https://www.federalreserve.gov/newsevents/pressreleases/files/bcreg20090424a1.pdf (a15, c20)
- [V] Federal Reserve (2009) SCAP overview of results. https://www.federalreserve.gov/newsevents/pressreleases/files/bcreg20090507a1.pdf (a16)
- [M] Borio, Drehmann, Tsatsaronis (2014) BIS WP 369, abstract page. https://www.bis.org/publ/work369.htm (a17)
- [V] Peristiani, Morgan, Savino (2010) NY Fed SR 460. https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr460.pdf (b16, c21)
- [V] Csaszar, Peterson, Wilde (2026) Strategic foresight of LLMs. https://arxiv.org/pdf/2602.01684 (a18-a20, d15)
- [V] Lorenz and Fritz (2026) Scalable Delphi. https://arxiv.org/abs/2602.08889 (a21-a24, b09-b13, d13)
- [V] Bertolotti and Mari (2025) LLM-based Delphi study. https://arxiv.org/abs/2502.21092 (a25, b06, b07)
- [V] Sela (2026) Preserving Disagreement. https://arxiv.org/abs/2604.26561 (a26, b23, c17, d14)
- [V] Barrett et al. (2025) Confidence in frontier AI safety cases. https://arxiv.org/abs/2502.05791 (b08)
- [V] Barrett et al. (2025) Quantitative modeling of cybersecurity risks due to AI misuse. https://arxiv.org/abs/2512.08864 (b14, b15)
- [V] Soleimani (2026) LLM-generated counterfactual stress scenarios. https://arxiv.org/abs/2512.07867 (b17-b19, d12)
- [V] Fruhling et al. (2026) Agent-supported foresight, Futures Wheel. https://arxiv.org/abs/2602.08565 (b20, b21)
- [V] Barnett, Kieslich, Diakopoulos (2024) Generative scenario writing. https://arxiv.org/abs/2405.09679 (b22)
- [V, id unverified] Evidence-grounded social-weighted persona panel for generative UI evaluation (2026). https://arxiv.org/abs/2607.28439 (b24)
- [V] Schneider and Schramm (2025) Wisdom of Deliberating AI Crowds. https://arxiv.org/html/2512.22625v1 (d01, d02)
- [V] InfoDelphi (arXiv 2607.01661) via AlphaXiv. https://www.alphaxiv.org/abs/2607.01661.md (d03, d04)
- [V] Evaluating LLMs on real-world forecasting against expert forecasters (2025). https://arxiv.org/html/2507.04562v3 (d05)
- [M] Rowe and Wright (1999) Delphi as a forecasting tool. https://econpapers.repec.org/RePEc:eee:intfor:v:15:y:1999:i:4:p:353-375 (b01, d06)
- [M] arXiv searches for LLM plus morphological analysis (negative). https://arxiv.org/search/?query=morphological+analysis+LLM&searchtype=all (a27, d11)

## Source audit (2026-11-20)

Fresh auditors re-opened the sources of 6 established claims: 4 confirmed as written, 2 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E17.02-K09** (reworded: the sources support less). SCAP numbers (19 BHCs, about 600B losses, 185B need, 10 of 19 short) verified, but NY Fed SR 460 says announcement and methodology were nonevents while the clarification event was highly informative and results were also informative, so the market did not learn only at the results release. Corrected claim: The 2009 US bank stress test (SCAP) used a baseline and a more adverse scenario on 19 BHCs: about $600B two-year losses, $185B capital needed, 10 of 19 short. In the NY Fed event study the announcement and methodology events produced no significant abnormal returns, while the clarification event and the results release both did for banks with capital gaps; the market had largely guessed which banks had gaps beforehand.
- **E17.02-K11** (reworded: the sources support less). Ritchey PDF confirms 4x4x4x3x3x4 = 2,304, the 500,000+ original field and pairwise cross-consistency; Wikipedia agrees on CCA but is derivative of Ritchey. The sentence that pairwise judgments suit batch LLM labelling is not stated in any source. Corrected claim: General morphological analysis shrinks a large option space by pairwise cross-consistency checks: example 4x4x4x3x3x4 = 2,304 configurations; the original 10-parameter field exceeded 500,000. (Inference, not from the sources: the pairwise judgments could be labelled in batch by an LLM.)
