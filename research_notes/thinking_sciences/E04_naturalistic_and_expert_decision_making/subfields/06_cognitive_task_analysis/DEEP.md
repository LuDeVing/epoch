# Cognitive task analysis: deep document

*Subfield E04.06. Written from evidence_a-d.jsonl (ids a01-a28, b01-b25, c01-c27, d01-d16), claims.jsonl (K01-K24) and critique.md. Companion file: UNKNOWNS.md. Honest headline: the human-side evidence is real but small and inflated; the LLM-side evidence is one research group plus agent-memory papers; nobody has tested a CDM-style sweep on an agent's own failures.*

## 1. What it is

Cognitive task analysis (CTA) is a family of methods for getting out of an expert's head the knowledge they use but do not state: what cues they notice, what they expect, what options they drop, what a novice would miss. The best known method is the Critical Decision Method (CDM; Klein, Calderwood, MacGregor 1989, a01, b22). The expert retells one real, non-routine incident. The interviewer then sweeps through it several times with probes (cues, goals, options, expectations, what a novice would do). Output: cue-action patterns, decision points, pitfalls, strategies.

Related methods: ACTA (applied CTA, shorter, knowledge audit plus simulation interview, c24, b19), cued recall after a simulation (b10), eye-tracking replay (b11), procedural maps (b12). The review literature groups them with protocol analysis and repertory grids (a25, b20, a06).

Why it matters for our agent: a CTA is a method for building lessons. Our agent could use the same logic on its own hard cases: retell one failed case, probe cues, strategies and pitfalls, then store the result as a lesson. The question is whether that beats plain lessons, no lessons, or generic role prompts, at equal tokens.

Three things CTA claims to fix:
1. Experts omit most decision and knowledge steps when they explain unprompted (K01).
2. Retrospective reports are partly reconstruction, so anchor on a concrete incident with short delay (K11).
3. The useful content is cue and strategy knowledge, not option tables (K09, K18).

## 2. History and theories in depth

**Roots.** Nisbett and Wilson (1977, a07, not opened; cited 7,382 times) argued people often cannot report the true causes of their judgments and instead give plausible theories. Ericsson and Simon (1993, b25, not opened) hold that concurrent think-aloud is valid, retrospective reports less so unless close in time and well cued. Cooke (1994, a06) and Hoffman, Shadbolt, Burton, Klein (1995, a05) compared elicitation methods by efficiency and yield. None of these four was opened; all statements about them come from later sources.

**Fireground studies.** Klein, Calderwood and Clinton-Cirocco (1986) interviewed fire commanders about non-routine incidents (a27, retold in Klein 1991, a02, opened). Commanders did not compare options. They classed the situation, knew the typical action, and ran it in imagery to find flaws. This became the Recognition-Primed Decision (RPD) model. Klein and Wright (2016, a03, opened) say RPD accounted for 80 to 90 percent of firefighter decisions and was replicated with military leaders (Schmitt and Klein 1999), firefighters (Keren et al. 2013) and offshore oil managers (Skriver 1998). The 80-90% figure is the model author's own coding (K18). Klein 1991 reports RPD coding with 87% to 94% inter-rater reliability.

**CDM (1989).** Method paper, 718 citations (a01). No effect sizes. Structure taken from open later sources. Hoffman, Crandall, Shadbolt (1998, d14) discuss CDM reliability and utility, but only the abstract was reachable, so we have no reliability coefficient from the founders (K24).

**Use in training.** CTA became a way to design instruction. Two meta-analyses of CTA-based training exist: Tofel-Grehl and Feldon (2013, a11, g = 0.871, abstract only; the DOI in b23 was wrong, use a11) and a surgical one (Edwards 2021, a12, b01-b04). A 2026 update (a13) found 15 RCTs, 9 pooled. Scenario training from CTA: ShadowBox (Klein and Borders 2016, a16).

**Expert vs novice contrast.** CTA finds differences in strategies, pitfalls and links between steps, not in the count of decision points (b10, b12, a18; K09).

**Move to AI.** Early NLP tried to parse CTA transcripts into flowcharts (Du et al. 2019, a22/b18/c05). Bridge (Wang et al. 2023/2024, a19-a21) used CTA with four teachers to build a decision model that guides LLM replies, then Tutor CoPilot (c04) deployed it. Separately, agent-memory work (ExpeL, AWM, ReasoningBank, Dynamic Cheatsheet, SkillsBench) builds lessons from traces without expert interviews (c14-c19, d01-d05). Position papers propose LLM interviewers for tacit knowledge (a26, c21, c22) with no measured results.

**Competing views.**
- CTA as content source (the expert knows, we extract it) versus CTA as structure (any well-formed lesson helps). Not separable in current data (b04, K24).
- Heavy CTA versus streamlined CTA for linear procedures (b14, c24). No head-to-head on learning outcomes (K19).
- Self-report skepticism (Nisbett and Wilson) versus careful elicitation (Ericsson and Simon). For LLMs, the skeptical view has fresh support (d10-d12).

## 3. Core findings with exact numbers

Status: E established, S single-source, C contested (claims.jsonl).

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Experts teaching unprompted omit most steps | 3 experts: omitted 71% (10/14) clinical knowledge steps, 51% (14/27) action steps, 73% (3.6/5) decision steps; said "how" for 13% of action steps | Sullivan 2014 (a08, b05), abstract | S (K01) |
| Prompted CTA recovers part, not all | steps described 44% (20/46) free recall to 66% (31/46) with CTA; about a third still missing | Sullivan 2014 (b06) | S (K01) |
| One CTA interview beat free recall | 10 trauma surgeons (4 free, 5 free+simulation, 1 CTA); CTA ~70% more complete and accurate; unaided omitted nearly 70% of decision steps | Clark 2012 (a09, b07), abstract | S, same lab as Sullivan |
| CTA course beats usual training (RCT) | 26 interns; checklist 12.6 vs 7.5 of 14, P<0.001; MCQ 11 vs 8.64, P=0.03; attempts 3.3 vs 6.4, P=0.046; time 15.4 vs 20.6 min, P=0.149 n.s. | Velmahos 2004 (a10) | S |
| Overall CTA training effect | Hedges g = 0.871 | Tofel-Grehl and Feldon 2013 (a11) | E direction, inflated (K02) |
| Surgical meta-analysis | 2205 records, 12 studies (10 RCTs), 327 participants; knowledge SMD 1.36 (0.67-2.05), 4 studies, I2 60%; technical (trainees) SMD 2.06 (1.17-2.96), 4 studies, I2 61%; all 5 pooled 1.58 (0.31-2.85); I2 87% overall | Edwards 2021 (a12, b01, b02) | E direction, size unreliable |
| Benefit gone for novices | two medical-student studies: no difference in technical performance; only trainees gain | Edwards 2021 (b03) | C (K03) |
| Updated review | 15 RCTs, 9 pooled; trainee knowledge SMD 2.08 (1.46-2.71); not in medical students | 2026 update (a13), abstract | E direction |
| Method quality weak | only 7 of 12 studies described the CTA method; 3 gave no detail; no funnel plot; risk of bias "some concern" | Edwards 2021 (b04, d13) | E (K23) |
| CTA studies are mostly routine events | 81 articles; CDM 36, CTA interviews 30; routine 64, challenging 13, rare 3 | Systematic review 2022 (a15) | E (K08) |
| ICU CDM study | 11 of 23 residents interviewed; median 7 days after event; 71 cues; 9 of 11 (82%) guideline-concordant; Fleiss kappa 0.64; saturation after interview 7, none new by 10 | Mansoori 2025 (a14, b08, b09) | S (K12) |
| Expert vs novice, VR cardiac arrest | 7 experts, 5 novices; decision points 48 vs 45; pitfalls 46 vs 33; strategies 77 vs 44; communications 23 vs 20 | b10 | E (K09) |
| Surgical procedural maps | 6 attendings vs 6 residents; steps 29.67 vs 23.3 (p=0.04); crosslinks 3.2 vs 1.0 (p=0.005); total 90.2 vs 63.2 (p=0.015); no difference in factor counts | Hashimoto 2019 (b12) | E (K09) |
| ShadowBox | Marines N=59: match .59 vs .44, d=.63 (printed groups 29+31 do not sum to 59); soldiers N=30 d=.38 no control; fire officers 86.9 vs 73.6 | Klein and Borders 2016 (a16) | S (K10) |
| Bridge: CTA decision model helps GPT-4 | 700 sessions, 4 teachers, 40 pairs per model, 3 raters; GPT-4 none 0.51, expert 0.83, self 0.84, random 0.26; expert-written replies 1.02; prefer +76%, useful +80% | Wang 2024 (a19, b15, c01) | S (K04) |
| Bridge: weaker models | Llama-2 none 0.53, expert 0.49, self 0.70, random 0.35; GPT-3.5 none 0.28, expert 0.45, self 0.16, random 0.17 | c02, critique | S (K04, K06) |
| Random decisions hurt | GPT-4 0.26 vs 0.83. Paper says -97% in abstract and -67% in intro; table gives about -69% | Bridge (b16, c03) | S (K05) |
| LLM paths narrower than expert | entropy 6.00 expert vs 3.37 GPT-4 | Bridge (a21) | S (K06) |
| Tutor CoPilot RCT | 900 tutors randomised, 783 analysed, 1,013 students, 4,136 sessions, 350,000+ messages; pass 62% to 66% (+4 pp, p<.01); +9 pp for lower-rated tutors; ~$20 per tutor per year; test-score effect ~0.024 SD | c04 | S (K07) |
| Transcript parsing before LLMs | span accuracy 47.1% (fuzzy), 38.18% (sequence labelling); relation F1 74.4% | Du 2019 (a22, c05) | E (K17) |
| LLM applies a codebook | kappa GPT-4 0.97/0.75/0.56 vs human 0.97/0.83/0.63 on tasks A/B/C | Kirsten 2024 (d08) | E (K22) |
| Agreement understates LLM quality | Jaccard human-LLM 0.30 vs human-human 0.52; blind expert preference 51.5% human vs 48.5% LLM, p=0.537, 855 pairs | Liu 2026 (d09) | E (K22) |
| LLM interviewers under-probe | 88% of follow-up violations by AI; 72 vs 64 violations per interview; pretest behaviour broke after prompt edits | Wuttke 2024 (c09, c10) | E (K14) |
| Learned questioning tied to respondent | win rate 72% falls to 65% and 62% with other roleplayers | STaR-GATE (c08) | E (K14) |
| GATE elicitation | 388 participants; beat user-written prompts in 6/10 settings absolute, 7/10 time-normalised | Li 2023 (c06) | E |
| Persona prompts | 162 personas, 4 families, 2,410 questions: no average gain | Zheng 2024 (c12) | C (K16) |
| Reasoning-mode templates | GPT-3.5 MedQA CoT 46%, analytic 40% (p=.001), differential 38%, Bayesian 42%; GPT-4 CoT 76%, differential 78% | Savage 2023 (c11) | C (K16) |
| Machine-mined lessons | WebArena: Gemini-2.5-flash none 40.5, ReasoningBank 48.8, +MaTTS 51.8; Claude-3.7 41.7 / 46.3 / 48.8; AWM 44.1 / 47.6 / 40.8 | ReasoningBank (c18) | E, task-dependent (K15) |
| Failure lessons | ReasoningBank 46.5 to 49.7 (+3.2 pp, no memory 39.0); AWM 44.4 to 42.2 | d01 | S (K21) |
| Self-written skills fail | no skills 33.9% to curated 50.5% (+16.6 pp, range +4.1 to +25.7); self-generated -8.1 (Opus 4.7 43.0 to 34.9), -11.3 (GPT-5.5 46.8 to 35.5) | SkillsBench (d04) | C (K20) |
| Lesson count and length | 1 skill +18.0 pp, 2-3 +19.0, 4+ +10.1; compact +19.0, standard +21.5, detailed +14.5, comprehensive +0.7 | d05 | S (K12) |
| Agents ignore condensed lessons | empty, shuffled, irrelevant, corrupt, filler lessons often match real ones; raw trajectories matter | Zhao 2026 (d03) | C (K20) |
| Self-explanations omit the true cause | accuracy drops up to 36.3% with unmentioned bias; reasoning models verbalise hints 25% (Claude 3.7) and 39% (R1) | d10, d12 | E (K11) |
| Larger model less faithful | 13B changed answer after CoT more than 175B on 7 of 8 tasks | Lanham 2023 (d11) | S |
| LLM analyst agent | water-jug puzzles, GPT-3.5/4, one run each, $3 total; CTA-agent spec executable in Soar | Wray 2024 (d06) | S, feasibility only |
| LLM expert interviewer | 8 experts; 58-71% annotation overlap with a human interviewer; +4 annotations per group | Data Therapist (d07) | S |

## 4. Mechanisms and models

**4.1 CDM as a procedure (implementable).**
1. Pick one concrete incident (non-routine, hard, or failed).
2. Sweep 1: timeline. List events in order.
3. Sweep 2: decision points. Mark where the actor chose or could have chosen.
4. Sweep 3: deepening probes at each decision point: cues noticed, what was expected, goals, alternatives considered and dropped, information missing, what a novice would have done.
5. Sweep 4: what-if probes: what would have changed the choice.
6. Output a table: cue pattern, situation class, action, pitfall, link to other steps.

Recency matters: the ICU study ran at median 7 days after the event (b08). For an agent the trace is available at zero delay, so the recall problem is replaced by the faithfulness problem (4.4).

**4.2 RPD as retrieval.** The agent recognises a situation class from cues, retrieves the typical action, runs it mentally for flaws, and only then tries another. Engineering form: lessons keyed by cue pattern; value is action plus known failure mode. This differs from an option table (a02, K18).

**4.3 Bridge decision model (the one tested LLM mechanism).** Three steps before the reply: A infer the error type, B pick a strategy (11 options), C pick an intention (11 options). Built by 4 teachers; two built it, two validated it, options refined until experts agreed (a20). Variants: none, expert decisions, self-chosen decisions, random decisions. Pattern: content must fit the case (random hurts); strong models can choose for themselves (GPT-4 0.84); weak models cannot (GPT-3.5 0.16); self-chosen paths are narrower than expert paths (entropy 3.37 vs 6.00).

**4.4 Retrospective report validity.** Nisbett and Wilson: reports are reconstruction. For LLMs this is measured: stated reasoning omits the hint that changed the answer (d10, d12). Implementation rule: a cue the agent claims to have used is a hypothesis. Verify by removing the cue and rerunning (counterfactual removal). A lesson whose cue does not change behaviour on removal is dropped.

**4.5 Lesson store design.** From SkillsBench and ReasoningBank (d01, d04, d05): keep 2 to 3 compact lessons per task, not comprehensive manuals (comprehensive +0.7 pp). Retrieve by relevance; random sampling hurt in ExpeL (d16, snippet only). Check that the agent actually reads and cites the lesson (d03).

**4.6 Saturation.** Themes saturated at interview 7, none new by 10, in the ICU study (b09). Engineering form: add traces per task type until a new case adds no new cue cluster.

**4.7 Coding reliability.** Fleiss kappa 0.64 for cue-influence ratings (b09). LLM coders match humans on mechanical codes and lag on interpretive ones (d08). Use blind pairwise expert preference as well as overlap (d09).

## 5. What holds up

**Holds (several sources):**
- Unaided experts omit decision knowledge; prompted probes recover more (K01 direction). Weak: one lab.
- CTA-designed training beats conventional training in surgical trainees; direction is consistent across 12 and 15 RCT sets (a12, a13). Size is not trustworthy.
- Experts differ from novices in strategies, pitfalls and links, not counts (b10, b12, a18).
- CTA literature covers routine events; rare events 3 of 81 (a15).
- Machine-mined lessons can help (ReasoningBank, AWM, Dynamic Cheatsheet: Claude 3.5 Sonnet AIME 2024 23.3% to 50.0%, c19) but are task dependent and sometimes fall below no memory (AWM 40.8 vs 41.7 on Claude-3.7).
- LLM interviewers under-probe (c09) and learned question skill is respondent-specific (c08).
- Retrospective self-explanation is unreliable, for people and for LLMs (d10-d12).

**Does not hold up or is weak:**
- Effect sizes of g 0.87 to 2.06. Four studies per outcome, I2 60-87%, no funnel plot, undocumented CTA methods, CTA content confounded with delivery medium (Touch Surgery app) (b04, d13). The authors call the effects large; the inflation caveat is ours (critique item 6).
- Medical students: no gain (b03). Tutor CoPilot shows the reverse split (largest gain for weakest tutors, +9 pp), so the "needed base" is topic grounding, not general skill (K03).
- ShadowBox outcome is agreement with an expert panel, evaluated by its own authors; group sizes inconsistent (critique item 10).
- RPD 80-90% share is author coding (a03).
- No equal-length, same-format, non-expert-content control exists in any CTA study (K24).
- Self-written lessons: -8.1 to -11.3 pp in SkillsBench, against ReasoningBank and ExpeL gains (contested, K20).
- Role labels: no average gain (c12), but ExpertPrompting reports gains by GPT-4 judge only (c13). Different outcome measures.

**Moderators found:**
- Learner or model strength (Bridge, surgical data; contradicted by the SkillsBench small-model result, d05).
- Match between lesson and case (random hurts).
- Task type: insights beat retrieval on HotpotQA (36 vs 31) but not ALFWorld (50 vs 55) (c14).
- Lesson count and length (d05).
- Domain: SkillsBench gains Natural Science +28.8, Media +24.1, Cybersecurity +18.9, Software Engineering +11.6, Math/OR +9.7.
- Generic reasoning-style templates versus domain content (c11 vs Bridge): generic styles hurt GPT-3.5 and are flat for GPT-4; domain-specific CTA decisions help GPT-4.

**Interventions that worked:** CTA decision model for GPT-4 (Bridge); deployed Tutor CoPilot; curated compact skills; failure-aware extraction built for it (ReasoningBank).
**Did not work:** random decisions; GPT-3.5 self-decisions; self-written skills; failure lessons bolted onto AWM; generic clinical reasoning-mode templates on GPT-3.5.

## 6. Language models

**No study runs a full CDM sweep with an LLM and scores it against expert knowledge** (a28, c27, d15, K13). What exists:

1. **CTA output used as prompt content (Bridge, c01-c03).** GPT-4: 0.51 none, 0.83 expert decisions, 0.84 self decisions, 0.26 random. Llama-2: 0.53, 0.49, 0.70, 0.35. GPT-3.5: 0.28, 0.45, 0.16, 0.17. Expert-written replies 1.02. One group, 4 experts, 40 pairs per model; the expert arm uses gold labels (an upper bound). No outside replication found (d15).
2. **Deployed (Tutor CoPilot, c04).** +4 pp mastery, +9 pp for lower-rated tutors, $20 per tutor per year; test-score effect about 0.024 SD, tiny.
3. **LLM as analyst or coder.** Wray 2024 (d06): feasibility on puzzles. Kirsten 2024 (d08): GPT-4 kappa 0.97/0.75/0.56 vs human 0.97/0.83/0.63; GPT-3.5 0.74-0.85 / 0.56-0.60 / 0.34-0.43; few-shot examples barely mattered for GPT-4. Liu 2026 (d09): blind preference 51.5% human vs 48.5% LLM. So applying a given codebook is near human level; building a cue-action protocol from raw CDM transcripts is untested.
4. **LLM as interviewer.** GATE beats user-written prompts in 6/10 settings (c06); model-simulated respondents track humans in 2 of 3 domains (c07). Wuttke 2024: AI skipped follow-up probes (88% of those violations). Data Therapist: 58-71% annotation overlap with a human. None of these is an expert-cue interview.
5. **Agent lessons.** ReasoningBank +8.3 pp (Gemini-flash 40.5 to 48.8), +7.2 (pro 46.7 to 53.9), +4.6 (Claude-3.7 41.7 to 46.3). AWM +12.0 points on WebArena with GPT-4, but 40.8 vs 41.7 no-memory on Claude-3.7 in the ReasoningBank table. Dynamic Cheatsheet GPT-4o Game of 24 10% to 99%. SkillsBench curated +16.6 pp, self-written -8 to -11 pp; a small model with skills (34.9%) beat stronger no-skill baselines.
6. **Faithfulness.** Models do not name the cue that moved them (up to -36.3% accuracy with an unmentioned bias; hints verbalised 25% by Claude 3.7 Sonnet, 39% by R1). An agent's own "why I did it" is weak evidence of the real cue.
7. **Role prompts.** No average gain from personas (c12); reasoning-mode templates flat or harmful (c11).
8. **Content versus structure.** Zhao 2026 finds corrupt, irrelevant or filler condensed lessons often match real ones, which suggests structure or mere presence may carry part of the gain. ReasoningBank with random judge labels (50% accuracy) still scored about 47.6 vs 39 to 40 with no memory (d02, d01).

## 7. What our agent should take

### Add now (established)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Treat the agent's stated reason for a past action as a hypothesis. Verify any cue claimed as a lesson by removing it and rerunning. Never store a lesson on the strength of the explanation alone. | G10, memory | [E] | K11; d10-d12 |
| When mining lessons, sample failed and rare cases deliberately, not only typical successes. | memory | [E] | K08; a15 |
| Store lessons as cue / strategy / pitfall triples with cross-links, not as option tables or counts. | memory | [E] | K09; b10, b12, a18 |
| Test every lesson on its own, whatever its source. Confirm the store does not fall below no-memory on the target model. | G7, memory | [E] | K15; c16, c18, d01 |
| Keep lessons compact and few (about 2 to 3 per task), retrieved by relevance. | memory | [E] direction (size from one paper) | d05, d16; fits G12 |
| Rule-check any probing operator after every prompt edit; evaluate against several respondents or traces. | O | [E] | K14; c08-c10 |
| Do not plan test power on SMD above 1; expect small effects. | G7 | [E] | K02, K23 |
| Include a role-label-only control and a length-matched irrelevant control in every lesson test. | G7 | [E] method | K16, K20; c12, d03 |
| Score any LLM-built protocol by blind pairwise preference as well as overlap with a human. | memory | [E] | K22; d08, d09 |

### Test first (single-source or contested)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| CDM-style retrospective sweep (cues, alternatives, novice pitfalls) on the agent's own solved or failed cases, versus unprompted summary | memory, S9 | [S] | K01, K13, K24; a08, b05, b06 |
| Notice-strategy-intention step before answering | S2/S3, O | [S] | K04; a19, c01 |
| Lessons gated by model strength | G, memory | [C] | K03; b03, c04, d05 |
| Case-matched lesson retrieval; random well-formed lessons may hurt | memory | [S] | K05; b16, c03 |
| Self-written versus externally written lessons | memory | [C] | K20; d03, d04 vs c14, c18 |
| Failure-derived versus success-derived lessons at equal count | memory | [S] | K21; d01, d02 |
| Commit first, then see expert reasons (ShadowBox style) | memory | [S] | K10; a16 |
| Cheap versus deep extraction on branching versus linear tasks | memory | [S] | K19; b14, c24 |
| Interview-count saturation (7 to 10 traces per task type) | memory | [S] | K12; b09, d05 |
| RPD-style retrieval of cue-action cases versus option comparison on time-pressured items | memory, S3 | [S] | K18; a02, a03 |
| LLM-run CDM sweep scored against human-run sweeps | memory | [S] | K13, K17, K22 |

## 8. Concrete tests on our bench

All arms at equal total tokens (lesson text and any extraction cost counted, per G7). Held-out items. Report by model strength.

1. **Three-arm lesson test (K24, K02).** Items: held-out hard cases the plain model failed. Arms: (a) CDM-style lessons, (b) same-length same-format lessons with non-expert content, (c) no lesson, (d) length-matched irrelevant lessons, (e) role label only. Metric: pass rate on held-out items. Expected: (a) minus (c) small, +2 to +6 pp; (a) minus (b) smaller; (d) and (e) near zero or slightly negative.
2. **Unprompted versus probed summary (K01).** Items: 30 solved hard cases. Arms: free summary versus summary with 3 CDM probes (cues, alternatives, novice pitfall), same token cap. Metric: coverage of a gold step list built from the full trace, decision steps scored separately. Expected: probes raise decision-step coverage by 15 to 25 points; about a third still missing.
3. **Notice-strategy-intention step (K04).** Items: open-judgement items. Arms: structured three-field step, same-length neutral planning step, none. Metric: blind pairwise preference plus task score. Expected: gain only on the strong model; none or negative on the weak one.
4. **Self versus external lessons (K20).** Arms: lessons the agent wrote, lessons from a stronger model, hand-curated, none. Metric: pass rate plus a trace check that the lesson was cited. Expected: self-written at or below none for the weak model.
5. **Failure-only versus success-only versus mixed (K21).** Equal lesson count; strong and weak model. Metric: held-out pass rate. Expected: mixed at or above success-only by about 2 to 3 pp; failure-only unknown.
6. **Matched versus random lessons (K05).** Metric: pass rate. Expected: random well-formed lessons at or below none.
7. **Counterfactual cue verification (K11).** For each lesson cue, remove it from the case and rerun. Metric: fraction of cited cues that change the answer when removed. Expected: well under 100%.
8. **Saturation sweep (K12).** Mine lessons from 1 to 12 failed cases per task type. Metric: new lesson clusters per added case, and held-out gain per added case. Expected: saturation at 7 to 10 cases; gain flattens at 2 to 3 lessons used.
9. **Commit-first (K10).** Agent ranks cues on a held-out case, then sees expert reasons, versus reading reasons directly. Metric: match to gold ranking on a second held-out case. Expected: small gain.
10. **Cheap versus deep extraction (K19).** Branching task and linear task. Expected: deep wins only on branching.

## 9. What does not transfer, and why

- **Surgical effect sizes.** Small trials, weak controls, inflated. Humans also learn from lessons by practice, which an agent does not do.
- **Interview recall problems.** Human experts forget and reconstruct after days. The agent has the full trace at zero delay. The remaining problem is faithfulness of its explanation, not memory.
- **Rapport and probing skill.** Human interviewers adapt to the expert. LLM interviewers under-probe and are respondent-specific (c08, c09).
- **Expert panel as ground truth.** ShadowBox, Bridge and Tutor CoPilot depend on experts. Our bench has verifiers, not teacher panels. Bridge's expert arm used gold labels, an upper bound.
- **Tutoring-style open judgement.** Bridge gains were rated by teachers. Exact-answer items with checks (G3) may behave differently and may favour SkillsBench-type procedural skills.
- **Medical students versus trainees.** The novice-base finding maps to model strength only loosely. Tutor CoPilot and SkillsBench contradict a simple gate.
- **RPD "first workable option".** Author coded. Our agent can sample cheaply and test (G3, G11), so recognition-only is not our constraint.
- **Training transfer to later practice.** Human outcomes are exam and checklist scores; there is no direct agent analogue.

## 10. Open questions

1. Does an LLM-run CDM sweep on an agent's own failed traces beat plain-structure lessons and no lesson at equal tokens? No published test (K13, K24).
2. Is Bridge replicated by anyone outside the original group or outside tutoring? Not found (d15).
3. Does lesson content matter beyond structure? No equal-length non-expert control in any CTA study; Zhao 2026 suggests filler often matches.
4. How accurate is a modern LLM at building cue-action protocols from CDM transcripts versus human analysts? Open; only codebook application is measured (d08, d09).
5. Where does the model-strength gate flip? Bridge says strong models only; SkillsBench says a small model with skills can beat stronger ones.
6. Failure-derived versus success-derived lessons at equal count, across model sizes.
7. Saturation point on agent traces.
8. Corrected surgical effect sizes (funnel plot, trim-and-fill, larger RCTs).
9. Does an agent's retrospective self-explanation match the counterfactually verified cause?
10. Reliability numbers for CDM from Klein 1989 and Hoffman 1998 (not reached).
11. Forward citations of Bridge could not be pulled (APIs rate limited), so 2025-2026 LLM-CTA work may exist.

## 11. Sources

[V] opened (full text or HTML, as recorded in the evidence files); [M] snippet, abstract only, or not opened.

- [M] Klein, Calderwood, MacGregor 1989 CDM. https://doi.org/10.1109/21.31053 (a01, b22)
- [V] Klein 1991 Naturalistic Decision Making. https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.191.833&rep=rep1&type=pdf (a02, a27)
- [V] Klein and Wright 2016 Macrocognition. https://www.gary-klein.com/_files/ugd/2360d8_2a8ed920b0ca45c7955a4e88fac00cc5.pdf (a03)
- [M] a04, record only (see evidence_a.jsonl)
- [M] Hoffman et al. 1995. https://doi.org/10.1006/obhd.1995.1039 (a05)
- [M] Cooke 1994. https://doi.org/10.1006/ijhc.1994.1083 (a06)
- [M] Nisbett and Wilson 1977. https://doi.org/10.1037/0033-295x.84.3.231 (a07, b24)
- [M] Sullivan et al. 2014. https://pubmed.ncbi.nlm.nih.gov/24667500/ and https://doi.org/10.1097/ACM.0000000000000224 (a08, b05, b06)
- [M] Clark et al. 2012. https://pubmed.ncbi.nlm.nih.gov/22099596/ and https://doi.org/10.1016/j.jss.2011.09.003 (a09, b07)
- [M] Velmahos et al. 2004. https://pubmed.ncbi.nlm.nih.gov/14706600/ (a10)
- [M] Tofel-Grehl and Feldon 2013. https://doi.org/10.1177/1555343412474821 (a11; b23 DOI wrong)
- [V] Edwards et al. 2021. https://doi.org/10.1093/bjsopen/zrab122 and https://pmc.ncbi.nlm.nih.gov/articles/PMC8669793/ (a12, b01-b04, d13)
- [M] Updated meta-analysis 2026. https://doi.org/10.1016/j.jsurg.2026.104129 (a13)
- [V] Mansoori et al. 2025. https://doi.org/10.34197/ats-scholar.2025-0009oc and https://pmc.ncbi.nlm.nih.gov/articles/PMC12712819/ (a14, b08, b09)
- [V] CTA systematic review 2022. https://doi.org/10.1186/s40814-022-01002-6 (a15)
- [V] Klein and Borders 2016 ShadowBox. https://www.gary-klein.com/_files/ugd/2360d8_f10a0dd34a20429a9e130284001b5fd5.pdf (a16-a18)
- [V] Wang et al. Bridge. https://arxiv.org/abs/2310.10648 (a19-a21, b15, b16, c01-c03)
- [V] Du et al. 2019. https://arxiv.org/abs/1906.11384 (a22, b18, c05)
- [V] Verostek et al. 2022. https://arxiv.org/abs/2204.13652 (a23, c25)
- [V] Irons et al. 2024. https://arxiv.org/abs/2411.07406 (a24, b21)
- [V] Leu and Abbass 2018. https://arxiv.org/abs/1802.09669 (a25, b20, c26)
- [V] Benderoth et al. 2025. https://arxiv.org/abs/2508.19942 (a26, c22)
- [V] arXiv search gap check. https://arxiv.org/search/?query=%22critical+decision+method%22&searchtype=all (a28)
- [V] Cardiac arrest VR cued recall 2025. https://pmc.ncbi.nlm.nih.gov/articles/PMC11878170/ (b10)
- [M] White et al. 2018. https://doi.org/10.1016/j.annemergmed.2018.03.005 (b11)
- [M] Hashimoto et al. 2019. https://doi.org/10.1016/j.amjsurg.2018.11.011 (b12)
- [M] Hegde et al. 2020. https://doi.org/10.1007/s00464-019-06822-x (b13)
- [M] Riggle et al. 2014. https://doi.org/10.1007/s40037-013-0100-1 (b14)
- [V] Stanik et al. 2022. https://arxiv.org/abs/2108.05622 (b19, c24)
- [V] Wang et al. Tutor CoPilot. https://arxiv.org/abs/2410.03017 (b17, c04)
- [M] Ericsson and Simon 1993. https://mitpress.mit.edu/9780262550239/protocol-analysis/ (b25)
- [V] Li et al. GATE. https://arxiv.org/abs/2310.11589 (c06, c07)
- [V] Andukuri et al. STaR-GATE. https://arxiv.org/abs/2403.19154 (c08)
- [V] Wuttke et al. 2024. https://arxiv.org/abs/2410.01824 (c09, c10)
- [V] Savage et al. 2023. https://arxiv.org/abs/2308.06834 (c11)
- [V] Zheng et al. 2024. https://arxiv.org/abs/2311.10054 (c12)
- [M] Xu et al. ExpertPrompting. https://arxiv.org/abs/2305.14688 (c13)
- [V] ExpeL. https://arxiv.org/abs/2308.10144 (c14, c15); [M] d16 snippet figures
- [V] Agent Workflow Memory. https://arxiv.org/abs/2409.07429 (c16, c17)
- [V] ReasoningBank. https://arxiv.org/abs/2509.25140 (c18, d01, d02)
- [V] Dynamic Cheatsheet. https://arxiv.org/abs/2504.07952 (c19)
- [M] Selby et al. 2024. https://arxiv.org/abs/2402.07770 (c20)
- [V] Cervera 2026 Expert Mind. https://arxiv.org/abs/2603.14541 (c21)
- [V] Joyner and Vaughn-Cooke 2026 DECIDE-CTA. https://europepmc.org/article/PMC/PMC13659902 (c23)
- [V] Zhao et al. 2026, not-always-faithful self-evolvers. https://arxiv.org/abs/2601.22436 (d03)
- [V] SkillsBench. https://arxiv.org/abs/2602.12670 (d04, d05)
- [V] Wray, Kirk, Laird 2024. https://arxiv.org/abs/2405.12147 (d06)
- [V] Data Therapist 2025. https://arxiv.org/abs/2505.00455 (d07)
- [V] Kirsten et al. 2024. https://arxiv.org/abs/2403.06607 (d08)
- [V] Liu et al. 2026, Agreement Is Not Quality. https://arxiv.org/abs/2607.28890 (d09)
- [V] Turpin et al. 2023. https://arxiv.org/abs/2305.04388 (d10)
- [V] Lanham et al. 2023. https://arxiv.org/abs/2307.13702 (d11)
- [V] Chen et al. 2025. https://arxiv.org/abs/2505.05410 (d12)
- [M] Hoffman, Crandall, Shadbolt 1998. https://doi.org/10.1518/001872098779480442 (d14, abstract only)
