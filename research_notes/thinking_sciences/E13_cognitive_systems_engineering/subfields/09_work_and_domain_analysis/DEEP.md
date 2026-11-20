# Work and domain analysis: deep document

*Subfield E13.09. Sources: evidence_a-d.jsonl, claims.jsonl (K01-K26), critique.md in this folder. Evidence ids a01-a28, b01-b24, c01-c27, d01-d18. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested. Short summary: the human side is well described but thinly measured. The LLM side has no direct test at all.*

## 1. What it is

Work domain analysis (WDA) is the first phase of cognitive work analysis (CWA). It models the system the work happens in, not the person doing it (a01). It asks: what is this job for, what laws and limits bind it, what functions exist, what objects and forms carry them. The model it builds is the abstraction hierarchy (AH).

The AH has five levels (a03):

1. Functional purpose: why the system exists.
2. Abstract function: laws and priorities (mass, energy, value flow).
3. General function: processes that move things.
4. Physical function: what each component can do.
5. Physical form: what and where the components are.

Links run both ways. Down is "how". Up is "why". This is a means-ends structure.

The other four CWA phases are control task analysis (what must be done, independent of how or by whom), strategies analysis, social organisation and cooperation analysis, and worker competencies analysis (a01, a15, a26).

Ecological interface design (EID) is the design use of WDA. It makes work-domain constraints visible so people can reason at the knowledge level, even for events nobody planned for (a03, b10). It pairs the AH with Rasmussen's skills-rules-knowledge (SRK) split of behaviour.

Why it matters for our agent: schema state S0 is a problem-class gate. WDA is a worked, 40-year-old method for writing down goals, constraints and available actions of a job before acting. The question is whether a cheap text version of it helps a language model gate and route problems. No one has tested that (K02).

## 2. History and theories in depth

**1974: decision ladder.** Rasmussen (with Jensen) described mental procedures in real tasks. The decision ladder has seven stages: activation, observe, identify, interpret, define task, formulate procedure, execute. Experts take shortcuts and skip stages when the state is familiar (a08). Rasmussen and Goodstein (1987) used three ladders for cooperative decisions in nuclear control (a08).

**1983: SRK.** Rasmussen split behaviour into skill-based (automatic), rule-based (stored if-then) and knowledge-based (explicit reasoning from goal and model). Error types differ by level. Not opened; known through secondary text (a04, a02).

**1986: abstraction hierarchy.** Rasmussen's book on information processing and human-machine interaction. 1994: Rasmussen, Pejtersen and Goodstein, Cognitive Systems Engineering (a02, c27).

**1990-1992: EID.** Vicente and Rasmussen built EID at Risoe. A search snippet quotes them saying the first empirical tests gave only preliminary support (b18, not opened).

**1995-1998: DURESS II experiments.** A process simulator (a feedwater system). Students used either a physical-only interface (P) or a physical-plus-functional one (P+F, EID-based). Results are in section 5 (d01-d06).

**1999: Vicente's book.** Cognitive Work Analysis fixed the five phases and the claim that designs should support adaptation to unforeseen events (a01, a26).

**2000s: methods and artistry.** Reising and Sanderson found that moving from work-domain equations to display shape needed "open-ended artistry" (d08). Amelink (2010) said the AH has no rules for which fact belongs on which level and none for validating the model. Building it took significant time. The creative design step after the analysis drives success (b06, b07). Naikar's nine-step method is the usual patch. A 2021 surgical study said Rasmussen and Vicente give "comprehensive but somewhat conflicting" descriptions of how to do WDA (a10).

**2010s: extensions.** Degree-of-automation layer on the AH (Li and Burns 2017; a07). Work organisation possibilities diagram for adapting the organisation, not only behaviour (Naikar and Elix 2016; a14). Team CWA (Burns 2014; a15). Applications grew in medicine, sport, driving, manufacturing (a10-a13, b08-b15). The McIlroy and Stanton 2015 review found 40% of EID applications do not cite the SRK taxonomy, though EID rests on it (d07). It reports how EID was used, not how well it worked.

**2020s: the LLM turn.** Not WDA itself, but relatives:
- Task-analysis-derived scaffolds (Wang 2024, Figueiredo 2025, Kopka 2026).
- O*NET-based work benchmarks (TheAgentCompany, GDPval, WORKBank).
- Abstraction-first prompting (Step-Back, Self-Discover).
- Layered agent memory (STRATA).
- Perspective papers urging EID for GenAI interfaces (Simkute 2024; a06, c09, c10).

**Competing views.** (1) The benefit of WDA is that the analyst learns the domain (b07). (2) The benefit is the design step, not the analysis (b06). (3) Gibsonian ecological design is narrower than Rasmussen's EID (a23, b04). This matters because the transfer claim to an LLM rests on the analysis itself, not on display design.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| In 56 display evaluations only iterative end-user evaluation separated successes | 14/14 positive with it vs 13/22 without (p<0.01) | Wright 2019 (b01, b02) | single-source |
| Two or more design processes did not reach significance | 17/20 vs 10/16 (p=0.15) | Wright 2019 (b02) | single-source |
| Making functional relationships visible (EID idea) was not a significant predictor | Fisher exact, not significant | Wright 2019 (b01) | single-source |
| Simulated gains larger than clinical gains | 27/36 (75%) simulated vs 9/17 (53%) clinical positive | Wright 2019 (b03) | single-source |
| Ecological helicopter-landing augmentation improved control | n=16; Cooper-Harper augmentation F(2,26)=4.87, partial eta2=0.27 | Morice 2021 (b04) | contested (Gibsonian, novices) |
| AR-HUD built from AH and SRK cut workload in some scenarios | n=25; DALI 21.45 vs 30.84; S2 18.91 vs 34.18 p<0.001; S3 p<0.01; S1, S4 ns (p=0.324, 0.391); perception time 62.96% shorter in the full-warning scenario | Zhang 2024 (b05) | contested ("3 of 5" not fully checked) |
| Six-month DURESS II study: ecological gain was consistency, not mean | little difference in average; P group up to 2x slower at times even at 5.5 months | Christoffersen 1996 (d01) | contested (N unobtained; critique printed) |
| DURESS fault report | faster detection, more accurate diagnosis, faster compensation | Christoffersen 1995 (d02) | contested |
| P+F interface lacked history information | deficiency found | Pawlak and Vicente 1996 (d04) | single-source, not opened |
| Of 49 nuclear workload-support studies only 11 tested workload empirically | 40 technical, 11 procedures, 3 training | Nuclear scoping review 2025 (b16) | single-source |
| 40% of EID applications omit SRK | 40% | McIlroy and Stanton 2015 (d07) | single-source |
| Expert decision model fed to GPT-4 | 700 conversations; +76% preferred, +80% useful; random decisions -97% vs expert; path entropy expert 6.00 vs gpt-4 3.37; p<0.05 | Wang 2024 (a16, c13) | single-source |
| Self-chosen decisions help strong models only | gpt-4, llama-2 gain up to +95%; gpt-3.5 does not (entropy 3.42); care score not improved for llama-2 and gpt-3.5 with expert decisions | Wang 2024 (c14, critique) | single-source |
| CWA-derived recipe prompt on GPT-4o-mini | 1,200 exchanges; d=0.225 [0.150, 0.300], t(2980)=6.16; question-count IRR 0.004 plain vs recipe, z=-22.71 | Figueiredo 2025 (a17, c01, c02) | single-source |
| Theory-shaped prompts for care-seeking advice | 63.3% default, 67.6% recognition-primed, 66.7% data-frame; self-care 13.4% to 29.8% and 24.6%; 45 vignettes, 13 self-care | Kopka and Feufel 2026 (a19) | single-source |
| Expert decision-ladder rule list in a quantum chemistry agent | coverage 24.9% to 44.1%; MAE 0.373 to 0.339 eV; doubles 0 to 14 of 30 | Chang Lee and Rondinelli 2026 (c11) | single-source, NOT re-verified |
| Full workflow given: agent reproduces results | MAE 23 meV; 75% resolved in 7 attempts | same (c12) | single-source, not re-verified |
| Abstraction-first prompting | PaLM-2L: MMLU physics +7, chemistry +11, TimeQA +27, MuSiQue +7; over 90% of residual errors in later reasoning | Zheng 2023 Step-Back (d13) | established (with Self-Discover) |
| Self-composed structure | PaLM 2-L T4D 69% vs 40% CoT; BBH 67 vs 60; MATH 50.5 vs 42; GPT-4 T4D 85 vs 52; structures right 87.5%; 74.7% of MATH failures computation | Zhou 2024 Self-Discover (d14) | established |
| Layered agent memory | Hermes flat 30.4/35.8 vs memoryless 62.8/66.9 (AppWorld Test-Normal); ScienceWorld 48.3/55.8 vs 75.7/80.6; 269 vs 201 nodes; 48.7 vs 23.3 injected lines; A-Mem leads STRATA on Test-Normal Flash (+0.4/+3.4) | Zhu 2026 STRATA (c03-c06, critique) | single-source |
| LLM hierarchical task analysis is limited by grounding | task accuracy ASHiTA 9.27 vs 4.88 vs 1.95; with ground-truth labels GPT 36.1 | Chang 2025 ASHiTA (c07, c08) | single-source |
| Best agent on a work-task benchmark | 30.3% complete, 39.3% partial (may come from different harness versions); Claude 3.7 26.3%, 3.5 24.0%, GPT-4o 8.6%; 175 tasks | TheAgentCompany (c20, c21) | established (benchmark) |
| Frontier model vs experts on work deliverables | Opus 4.1 47.6% win-or-tie (ties counted); gpt-5 39.0%, o3 35.2%, o4-mini 29.1%, gpt-4o 12.5%; 220 tasks, 44 occupations | GDPval (c22) | established (benchmark) |
| Check-your-work prompt and best-of-4 | +5 points win rate; egregious PowerPoint errors 86% to 64%; deliverable inspection 15% to 97% | GDPval (c23) | single-source |
| Workers want more human agency than experts think needed | 1,500 workers, 844 tasks, 104 occupations; 47.5% of tasks; H3 dominant in 45.2% of OCCUPATIONS (not tasks); 41.0% of startup mappings in low-priority or red-light zones | WORKBank (c15-c17) | single-source |
| Observed use below forecasts | about 57% of occupations use AI for 10%+ of tasks vs about 80% of workers forecast | Handa 2025 (c18, c19) | single-source, not re-opened |
| Padding alone hurts reasoning | mean accuracy 0.92 to 0.68 at 3000 tokens; visible past about 500 tokens | Levy 2024 FlenQA (d09) | single-source |
| LLMs label ambiguity near chance | Llama2-70B 50.37% acc; ChatGPT 54.25%; 81.97% of ChatGPT self-contradiction errors were false negatives | CLAMBER (d15) | single-source (2023 models) |
| Multi-agent failures | 1,642 traces: spec/design 41.8%, coordination 36.9%, verification 21.3%; role-spec fix +9.4%; human kappa 0.88 | MAST (d11, d12) | single-source |
| Expected gains did not materialise live | 246 tasks, 16 developers: forecast 24% faster, measured 19% slower | Becker 2025 (d16) | single-source |
| Sorting by order (Cynefin-style) before choosing a strategy | no test | ACTIVE 2026 (b17, a20) | single-source (no data) |

## 4. Mechanisms and models

### 4.1 Abstraction hierarchy as a fill-in template

An engineer can implement it as a structured S0 prompt with five slots and link checks.

```
PURPOSE     (why does this task exist; what counts as success)
LAWS/LIMITS (what must hold; what cannot be broken; resources)
FUNCTIONS   (processes that must happen; what flows)
ACTIONS     (what the agent and tools can do; owner: program or model)
FORMS       (the concrete objects: files, tests, inputs, units)
```

Link check in code: every item at a lower level must name at least one item above (why). Every item above must be served by at least one below (how). Orphans are flagged. This means-ends check is the only part of the AH with a mechanical pass/fail test. The method itself gives no pass/fail rule (K01, K14).

### 4.2 Decision ladder as a skip rule

Seven stages. Experts shortcut from "observe" or "identify" straight to "execute" when the state is familiar (a08). Implement as: if S0 finds a class with a high recorded plain pass rate, take the direct mode and skip S1-S2 work. This matches SRK: familiar goes to a cheap rule path, novel goes to the full schema. Weak point: SRK is the least-used part of EID in practice (d07).

### 4.3 Boundary and facet step

Real studies found the system boundary hard to fix and modelled facets instead (a10). Implement as an explicit first line in S0: what is in scope, what is not. Typical method: documents, observation and expert interviews, then iterate and review (a11).

### 4.4 Degree-of-automation layer

Shade each function with its owner: program or model (a07). In the trading case, high automation took over upper levels (purpose, abstract function), not only physical ones. For our agent this is the section 1 split: code decides transitions and checks; the model fills slots.

### 4.5 Stable or open-ended test

WDA was designed for stable, well-bounded technical systems (K15). Extensions exist for automation, organisation, teams. Implement as a gate bit: are the constraints stable and knowable, or open? Route by it. Untested.

### 4.6 Expert decision path as scaffold (Wang 2024)

Cognitive task analysis with four experts gave a three-step model: infer the error, pick a strategy, state an intention (a16). The model gets the expert's decision as context, or picks its own. Context-sensitivity is what matters: random decisions gave -97%. Design implication: a wrong label is worse than no label.

### 4.7 Recipe by mode (Figueiredo 2025)

CWA found three functions (School, Discovery, Entertainment). Each became a structured conversation recipe. Implement: classify mode first, apply the mode's recipe. The strong effect was behaviour (question count). The weak one was similarity to the gold answer (d=0.225). Style change is not accuracy change.

### 4.8 Layered memory (STRATA)

Three typed layers (skills and code, task workflows, meta workflows), bounded, with forgetting and contrast edges between directionally opposite goals (c03-c06). Contrast edges lifted ScienceWorld 78.7 to 89.8 (hand-placed) to 96.7 (rule-based) and ALFWorld 89.5 to 98.6. Flat memory of concrete procedures was worse than none. Not Rasmussen's hierarchy, but the same idea: store at several abstraction levels and link them.

### 4.9 Check loop on the analysis

Wright 2019 says iterative evaluation with real users was the only separating factor (b02). Translation: S0 output must be tested against something outside the analysis, and revised (G3, G2).

## 5. What holds up

**Holds up (weakly).**
- WDA is usable. Many application studies built models: ICU nurses (32 h observation, 20 interviews, 2 hospitals; a11), telemedicine (20 interviews; a10), spacewalk (a13), netball (13 experts; b11), biofoundry (b15). None reports an outcome measure. They show it is usable, not that it is useful.
- Revising the model against real feedback is the best-supported moderator (14/14 vs 13/22), though confounded with team resources (b02).
- Abstraction-first prompting works for LLMs on STEM and multi-hop tasks, with the same sign in two independent papers (K22, established).
- Task-level work taxonomies now define LLM evaluation (K11, established).

**Failures, nulls and boundary conditions.**
- EID (functional relationships visible) was not a significant predictor in Wright 2019 (b01).
- Gains shrink in real settings: 75% to 53% (b03). In the one randomised trial, AI tools were forecast +24% and measured -19% (d16).
- DURESS: the gain came from consistency and fault handling, not mean speed. A critique of the longitudinal study was printed (d01, d05). A later paper is summarised as benefiting only if users actively reflect on feedback (d06, not opened). No independent replication was found (K17).
- A Gibsonian helicopter task (n=16) does not show Rasmussen EID works (b04).
- Mixed results inside one study: AR-HUD significant in S2, S3, not S1, S4 (b05).
- Even in nuclear control, 11 of 49 workload studies tested workload (b16).
- Perspective papers (Simkute, Mussi, Jalaeian) recommend EID or several abstraction levels for GenAI but did not measure it (a06, a21, a28, c09, c10).

**Moderators.**
- Novel versus routine events: gains show in complex or novel cases (b24, weak cross-source pattern).
- Analyst skill: the analysis depends on the analyst; no level-assignment rules; no inter-rater figure for humans (b07, d08, d18).
- Model strength: self-chosen decisions help gpt-4 and llama-2, not gpt-3.5 (c14).
- Class rarity: prompt gains landed mostly on the rare self-care class (a19).
- Setting: simulator versus clinical.

**Interventions that worked (LLM side).** Expert decision given as context (Wang). Recipe by mode (Figueiredo, small). Theory-shaped prompts (+3 to +4 points). Abstraction-first (Step-Back, Self-Discover). Check-your-work prompt plus best-of-4 (+5 points). Role-specification fix (+9.4%, MAST).

**Did not work.** Random decisions (-97%). Flat memory of concrete procedures (below memoryless). Unbounded memory. Chain of thought or few-shot for ambiguity labelling (d15). Temperature (no effect, Figueiredo). Filler tokens in commercial LLMs (d10). Pure length (d09).

**Corrections from the critique.** Wang's expert decisions did not raise the "care" score for llama-2 and gpt-3.5. On STRATA Test-Normal, A-Mem leads STRATA on Flash; STRATA's lead is on Test-Challenge, which the authors flag as confounded. TheAgentCompany's 39.3% and 30.3% may come from different harness versions. The Wright 2019 figure says n=35 while counts sum to 36.

## 6. Language models

**Direct tests of WDA or the AH as an agent method: none found.** Three search passes returned zero hits. The one EID hit is Simkute 2024, a perspective (K02, [E] for absence within the sources searched; not proof).

**Nearest relatives, with measured results.**

| Study | What it tests | Result |
|---|---|---|
| Wang 2024 (c13, c14) | expert decision model, GPT-4 | +76% preferred, +80% useful; random -97%; weak model gains nothing from self-chosen path |
| Figueiredo 2025 (c01, c02) | CWA-derived recipes, GPT-4o-mini | d=0.225 similarity; question count IRR 0.004; no child outcomes |
| Kopka and Feufel 2026 (a19) | recognition-primed and data-frame prompts | 63.3 to 67.6 / 66.7; self-care 13.4 to 29.8 |
| Chang Lee and Rondinelli 2026 (c11) | decision-ladder rule list, quantum chemistry agent | coverage 24.9 to 44.1; not verified, paper not found again (d17) |
| Step-Back (d13) | one abstraction step first | MMLU chemistry +11, TimeQA +27; residual errors over 90% in reasoning |
| Self-Discover (d14) | self-composed reasoning structure | T4D 69 vs 40 (PaLM 2-L), 85 vs 52 (GPT-4) |
| STRATA (c03-c06) | typed three-layer memory | beats flat on harder split; flat can be worse than none |
| ASHiTA (c07, c08) | LLM hierarchical task analysis | grounding, not decomposition, is the limit |
| TheAgentCompany, GDPval (c20-c23) | work tasks from O*NET | 30.3% completion; 47.6% win-or-tie; check prompt +5 |
| WORKBank, Handa (c15-c19) | what people want automated | 47.5% mismatch; observed use below forecast |
| MAST (d11, d12) | multi-agent failure map | spec/design 41.8%; role-spec fix +9.4% |
| CLAMBER (d15) | ambiguity labelling | near chance, 50 to 54% |

**What changed behaviour and by how much.** Structured task-analysis context gives mid-size effects on judged quality (+76%) and small effects on accuracy metrics (d about 0.2; +3 to +4 points). Behaviour counts move a lot, accuracy little (Figueiredo).

**Where errors live.** Step-Back: over 90% of residual errors in later reasoning. Self-Discover on MATH: 74.7% computation. So abstraction at the front fixes little of the remaining error. Execution dominates. MAST puts 41.8% of multi-agent failures in specification and design, but those categories are not keyed to abstraction levels.

**Self-labelling is the risk.** 2023-era models label ambiguity near chance (d15). A wrong decomposition is worse than none (-97% for random decisions). Both come from older models or other tasks. Neither tests current models labelling problem classes.

**Length control is missing.** Pure padding lowers accuracy (0.92 to 0.68; d09). So a content effect is plausible, but no scaffold paper above ran a length-matched generic-advice control (K21). The +5 check-prompt gain in GDPval and the +4.3 reasoning-prompt gain in Kopka do not separate WDA content from "more reasoning text".

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

| Item | Part | Status | Evidence |
|---|---|---|---|
| Fix the system boundary and name what the job is for, one line each, before solving. Already close to S0 and S1; this only cites the method. | S0/S1 | [E] as method description; value unproven | a01, a03, a10, a26, K01 |
| Keep a one-step abstraction ("what principle or class is this?") as an S0/S2 option to test. Two independent LLM papers show gains from abstraction-first. | S0/S2 | [E] for the prompt family; our version unmeasured | d13, d14, K22 |
| Report results by task type and class, not only overall. Gains concentrate in rare classes and vary by grade. | logs (schema section 6) | [E] pattern across studies | a18, a19, c20, c22 |
| Use a work-task benchmark as held-out check, and keep a live-task holdout; expect smaller live gains. | bench | [E] benchmark facts; shrinkage [S] | c20-c22, b03, d16 |
| Do not claim the S0 gate is proven by the WDA literature. | G7 | [E] | a12, b16, K26 |

None of these adds a new operator or guardrail. All fit inside S0 and S1 as written.

### Test first

| Item | Part | Status | Evidence |
|---|---|---|---|
| Five-level AH prompt (purpose, laws, functions, actions, forms, with why/how orphan check) vs plain vs goals-only S0 | S0 | [S] none measured | K01, K02, a03 |
| Expert-decision scaffold vs length-matched generic advice vs none | S0/O | [S] | a16, a17, a19, K06, K21 |
| Given problem-class label vs self-chosen vs random (harm from a wrong label) | S0 | [S] | c13, c14, d15, K07, K23 |
| Stable-or-open routing bit at S0 | S0 | [S] | K15, a07, a14 |
| Four-way Cynefin-style class label | S0 | [S] no data | b17, K18 |
| Owner tag (program or model) per function | S0/section 1 | [S] modelling only | a07 |
| Check loop on the S0 analysis (revise against examples) | S0/S5/G3 | [S] | b02, K04 |
| Layered notes (purpose, workflow, unit) vs flat at equal injected lines, with contrast notes | memory | [S] | c03-c06, K10 |
| Ask-or-act gate (desire vs capability) | S0 | [S] | c17, d15, K13 |
| Decision-ladder shortcut: skip S1-S2 when class record shows high plain pass rate | S0 | [S] | a08, a04 |
| Agreement between independent S0 samples as a reliability probe | S0 | [S] no human figure | b07, d18, K14 |

## 8. Concrete tests on our bench

All arms at equal total tokens (S0 tokens count against the budget; G7). Items: a mixed set of problem classes where plain pass rate varies (ARC-style, BRAINTEASER-style, NoveltyBench-style open items, plus a short work-task set in the style of TheAgentCompany or GDPval if available). At least three seeds. Report per class.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Mixed-class items | A plain; B goals-and-constraints S0; C five-level AH S0 with orphan check; D generic advice of the same token length as C | pass rate by class; tokens | C over B small (0 to 3 points); C vs D shows the content effect; D near A. If C equals D, no content effect. |
| T2 | Items with a known expert decision list (tutoring remediation, triage style) | expert decisions; self-chosen; random; length-matched generic | pass rate; rare-class recall | expert beats generic by more than d 0.2; random worse than none |
| T3 | Same items, class labels | gold class; self label; random label; no label | pass rate; label accuracy | wrong label costs; if self-label accuracy is below about 75%, disable the gate |
| T4 | Items marked stable or open | route by bit vs fixed mode | pass rate at equal tokens | small gain if bit accuracy is high |
| T5 | S0 analysis sampled 5 times per item | 5 independent S0 outputs | kappa of level assignments | below 0.6 means S0 content is noise |
| T6 | Failures from T1 | tag by MAST category and AH level | share the S0 gate could catch | if most failures are execution, S0 gain is capped (Step-Back: over 90%) |
| T7 | Memory notes | flat vs 3-layer, equal injected lines; with and without contrast notes | pass rate on a later split | layered not worse; contrast notes help on opposite-goal pairs |
| T8 | Work tasks with missing information | act always; ask at ambiguity; ask by desire/capability tag | task success; wasted asks | unknown |
| T9 | S0 check loop | S0 with and without a check against examples | pass rate | per Wright 2019, the check loop matters more than the analysis alone |

Reporting rules: include a live-task holdout and expect a smaller gain there. Report tokens spent on S0.

## 9. What does not transfer, and why

- **Display effects.** EID is about how a human sees a display. Our agent has no perceptual system. The Morice, Zhang and DURESS effects (b04, b05, d01) are about perception and workload. They give no number for an LLM.
- **Gibsonian examples.** Tau-dot for helicopter landing is a perceptual variable, not an abstraction hierarchy (a23, b04).
- **Human learning over months.** The DURESS benefit comes through months of practice and reflection on feedback (d01, d06). An LLM does not learn inside a run.
- **Analyst benefit.** One acknowledged benefit of WDA is that the analyst becomes familiar with the domain (b07). A model reading a prompt does not.
- **Stable physical systems.** WDA was built for stable, bounded technical systems (K15). Open puzzle problems have few physical forms.
- **Preference ratings.** Wang's +76% is human preference on tutoring responses, not correctness.
- **Single-domain results.** Each positive LLM result is one domain with rater or proxy metrics.
- **Older models.** CLAMBER and Step-Back numbers use older models. Current ones may differ either way.
- **Expert time cost.** Building a WDA takes significant time (b07). Our budget is tokens, so an S0 template must be written once per class and cached, not rebuilt per item.
- **Team and organisation layers.** Possibilities diagrams and team CWA (a14, a15) concern human organisations. Our agent is a single agent (G9).

## 10. Open questions

1. Does a five-level AH prompt beat plain, or goals-only, at equal tokens? Nobody has measured it (critique gap 1).
2. What did the DURESS experiments measure (N, effect sizes, novel faults), and did anyone replicate? Not obtained; full texts were blocked (gap 2).
3. Is the gain of expert-decision scaffolds a content or a length effect? (gap 3)
4. How much does a wrong class label cost, and how often does a current model produce one? (gap 4)
5. Do analysts, or LLM samples, agree on level assignment? No inter-rater figure exists for humans either (gap 5).
6. Is there a scaffold counterpart to simulated-versus-clinical shrinkage (75% vs 53%)? (gap 6)
7. What is the pooled EID effect? None found. McIlroy and Stanton cover usage, not effect (gap 7).
8. Do the Chang Lee and Rondinelli numbers (24.9% to 44.1%) hold? Paper not found again (gap 8).
9. Do work-task failures cluster on problem-class misreading or on execution? No taxonomy keyed to work-domain levels (gap 9).
10. When should the agent ask rather than act? No agent-side test (gap 10).
11. Links to other subfields in this run, notes only: Naturalistic decision making (recognition-primed prompts, Kopka), Resilience engineering, Cognitive ethnography, Coordination and common ground, Expert-novice differences, Debiasing, Design-space exploration.

## 11. Sources

[V] opened this session or in the earlier passes. [M] snippet, citation or abstract only.

**Founding and method**
- [M] Rasmussen (1983) Skills, rules, knowledge. https://doi.org/10.1109/TSMC.1983.6313160 (a04)
- [V] Wikipedia bibliography of Rasmussen (1986; 1994 with Pejtersen and Goodstein). https://en.wikipedia.org/wiki/Jens_Rasmussen_(human_factors_expert) (a02; the books themselves not opened)
- [M] Vicente (1999) Cognitive Work Analysis. https://www.routledge.com/Cognitive-Work-Analysis-Toward-Safe-Productive-and-Healthy-Computer-Based-Work/Vicente/p/book/9780805823974 (c27)
- [V] Wikipedia: Cognitive work analysis. https://en.wikipedia.org/wiki/Cognitive_work_analysis (a01)
- [V] Wikipedia: Ecological interface design. https://en.wikipedia.org/wiki/Ecological_interface_design (a03, b10)
- [M] Vicente and Rasmussen (1990, 1992), snippet (b18)
- [M] McIlroy and Stanton (2015). https://doi.org/10.1109/THMS.2014.2369372 (a05, d07; abstract level)

**DURESS and EID experiments**
- [M] Christoffersen, Hunter, Vicente (1996). https://doi.org/10.1518/001872096778701917 (d01, abstract)
- [M] Christoffersen et al. (1995). https://doi.org/10.1177/154193129503900912 (d02, abstract)
- [M] Christoffersen et al. (1997). https://doi.org/10.1177/001872089703900309 (a25)
- [M] Christoffersen et al. (1998). https://doi.org/10.1006/ijhc.1998.0190 (d06)
- [M] Vicente, Christoffersen, Pereklita (1995). https://doi.org/10.1109/21.370186 (d03, abstract)
- [M] Pawlak and Vicente (1996). https://doi.org/10.1006/ijhc.1996.0028 (a24, d04)
- [M] Maddox (1996) critique. https://doi.org/10.1518/001872096778701971 (d05)
- [M] Jungk et al. (1999). https://doi.org/10.1023/a:1009909229827 (b21)
- [M] Militello et al. (2009), cited in Amelink (b22)
- [V] Reising and Sanderson. https://doi.org/10.1518/0018720024497952 (d08, abstract)
- [V] Wright et al. (2019). https://pmc.ncbi.nlm.nih.gov/articles/PMC6696941/ (b01-b03; re-checked)
- [V] Morice et al. (2021). https://europepmc.org/article/PMC/PMC8357182 (a23, b04)
- [V] Zhang et al. (2024) AR-HUD. https://europepmc.org/article/PMC/PMC11679450 (b05)
- [V] Amelink (2010). https://repository.tudelft.nl/file/File_e1248dac-ccd4-4f25-af66-3a94465f5695 (b06, b07)
- [V] Boyce et al. (2015). https://xcdacademy.s3.amazonaws.com/iitsec/2015/2015_15130.pdf (b08)
- [V] Upton and Doherty (2008). https://link.springer.com/content/pdf/10.1007/978-0-387-36792-7_2.pdf (b09)
- [M] Flexible manufacturing EID study. https://doi.org/10.1177/15553434221118978 (b19, snippet)
- [V] Designing for confidence (2022). https://europepmc.org/article/PMC/PMC9263374 (a22)
- [V] Nuclear workload scoping review (2025). https://europepmc.org/article/PMC/PMC12107347 (b16)

**Applications and extensions**
- [V] Li and Burns (2017). https://pmc.ncbi.nlm.nih.gov/articles/PMC6187463/ (a07-a09, b14)
- [V] Telemedicine WDA (2021). https://europepmc.org/article/PMC/PMC8485199 (a10)
- [V] ICU nurse mobility (2022). https://europepmc.org/article/PMC/PMC9555320 (a11, b12)
- [V] Patient treatment AH (2017). https://europepmc.org/article/PMC/PMC5554354 (a12)
- [V] Miller, McGuire, Feigh (2017). https://europepmc.org/article/PMC/PMC5410855 (a13)
- [V] Naikar and Elix (2016). https://europepmc.org/article/PMC/PMC4924480 (a14)
- [V] Burns et al. (2014). https://europepmc.org/article/PMC/PMC4066876 (a15, a26)
- [V] Netball organisation (2019). https://europepmc.org/article/PMC/PMC7739835 (b11)
- [V] Payyanadan and Lee (2021). https://europepmc.org/article/PMC/PMC8395743 (b13)
- [V] Kim et al. (2025) biofoundry. https://europepmc.org/article/PMC/PMC12214803 (b15)
- [V] ACTIVE (2026). https://europepmc.org/article/PMC/PMC13602259 (a20, b17)
- [V] Mussi et al. (2025). https://europepmc.org/article/PMC/PMC12454906 (a21)
- [V] Jalaeian, Morey, Rayo (2025). https://arxiv.org/abs/2512.08036 (a28)

**LLM and AI studies**
- [V] Wang et al. (2024) Bridge. https://arxiv.org/abs/2310.10648 (a16, c13, c14; re-checked)
- [V] Figueiredo (2025). https://arxiv.org/abs/2508.21209 (a17, a18, c01, c02; re-checked)
- [V] Kopka and Feufel (2026). https://europepmc.org/article/PMC/PMC13061108 (a19; abstract re-checked)
- [V] Chang Lee and Rondinelli (2026). https://arxiv.org/abs/2609.13357 (c11, c12; not re-verified, d17)
- [V] Zhu et al. (2026) STRATA. https://arxiv.org/abs/2610.19386 (c03-c06; re-checked)
- [V] Chang et al. (2025) ASHiTA. https://arxiv.org/abs/2504.06553 (c07, c08)
- [V] Simkute et al. (2024). https://arxiv.org/abs/2402.11364 (a06, c09, c10)
- [V] Shao et al. (2025) WORKBank. https://arxiv.org/abs/2506.06576 (c15-c17)
- [V] Handa et al. (2025). https://arxiv.org/abs/2503.04761 (c18, c19; not re-checked)
- [V] Xu et al. (2025) TheAgentCompany. https://arxiv.org/abs/2412.14161 (c20, c21)
- [V] Patwardhan et al. (2025) GDPval. https://arxiv.org/abs/2510.04374 (c22, c23)
- [V] Motoura et al. (2018). https://arxiv.org/abs/1806.07037 (c24)
- [V] Di Matteo et al. (2024). https://arxiv.org/abs/2405.13918 (c25)
- [V] Levy, Jacoby, Goldberg (2024). https://arxiv.org/abs/2402.14848 (d09)
- [V] Pfau, Merrill, Bowman (2024). https://arxiv.org/abs/2404.15758 (d10)
- [V] Cemri et al. (2025) MAST. https://arxiv.org/abs/2503.13657 (d11, d12)
- [V] Zheng et al. (2023) Step-Back. https://arxiv.org/abs/2310.06117 (d13)
- [V] Zhou et al. (2024) Self-Discover. https://arxiv.org/abs/2402.03620 (d14)
- [V] Zhang et al. (2024) CLAMBER. https://arxiv.org/abs/2405.12063 (d15)
- [V] Becker et al. (2025) METR trial. https://arxiv.org/abs/2507.09089 (d16)

**Search notes**
- [V] arXiv listing queries, 0 to 1 hits for work domain analysis and related terms. https://arxiv.org/search/?query=%22work+domain+analysis%22&searchtype=all (a27, c26, b23)
- [M] Gap searches for Chang Lee and Rondinelli and for inter-rater agreement (d17, d18)
