# Systematic design: deep document

*Subfield E07.01. Staged process: Pahl and Beitz, VDI 2221. Schema links: S1 (understand), S2 (represent). Built from evidence_a-d.jsonl (a01-a28, b01-b27, c01-c26, d01-d16), claims.jsonl (K01-K26) and critique.md. Evidence ids below refer to those files. Status marks: [E] established, [S] single-source, [C] contested.*

## 1. What it is

Systematic design is the German-school view that engineering design should run as a fixed sequence of stages. Each stage has a named result. The main texts are Pahl and Beitz, *Engineering Design* (first German edition 1977, English 1984/1996/2007), and the guideline VDI 2221 (1993; revised 2019 as VDI 2221-1/-2). The classic stages are:

1. Clarify the task. Result: a requirements list (specification).
2. Determine functions and structure. Result: a function structure (overall function broken into sub-functions).
3. Search solution principles and combine them. Result: principal solutions (often via a morphological table).
4. Divide into realisable modules. Result: module structures.
5. Develop layouts of key modules, then the overall layout. Result: preliminary then definitive layouts.
6. Prepare production and operating documents.

VDI 2221 groups these as 7 stages in 4 phases (planning/clarifying, conceptual, embodiment, detail). Backward and forward iteration is allowed, and the requirements list is revised throughout (a03).

Core claim, quoted second-hand from Pahl and Beitz: intuition rarely gives good results, and a systematic method raises the chance of success significantly (b23). The method is a "road to follow" (b24, a16).

Why it matters for our agent: S1 (restate the task and say what makes an answer correct) and S2 (represent the problem, find structure) are close cousins of stage 1 (clarify) and stage 2 (function structure) of Pahl and Beitz. Stage 3 (search principles, combine) maps to S3 in open mode. So this literature is the oldest large body of "staged thinking" advice, and the question is whether the staging itself helps, or only what is done inside each stage.

Short answer from the evidence: the stages describe good content, but strict order is not shown to help humans, and no one has tested the full sequence against a plain prompt on a frontier LLM at equal tokens (K01, K02, K19).

## 2. History and theories in depth

**Lineage of the guideline (a01-a04, Jaensch and Birkhofer 2006).**
- Kesselring 1954: a list of 10 items of advice, mostly about the inventor's own thinking.
- Hansen 1965: a stepped system.
- VDI 2222 (1973): 4 phases, 52-page white print. Every step has a decision box (go on, or repeat earlier steps). It carries advice on thinking, for example abstract the task first to free the designer from fixation on a solution (a04).
- VDI 2221 (1993): 7 stages in 4 phases, 42 pages, about one third on CAD and data processing. The decision boxes and the thinking advice were dropped. The figure shows only instructions and results.
- The authors link this loss to the reserved uptake by practitioners (a02). They measured nothing. It is an insider interpretation.

**Pahl and Beitz view.** Four phases: task clarification, conceptual design, embodiment design, detail design. The key moves in the conceptual phase are abstraction (formulate the problem solution-neutrally), function structure, search for physical effects and principles per sub-function, and combination (morphological matrix), then rating. They allow slack: if a flash of insight gives the best solution fast, skip steps, though they say this seldom happens, especially while learning (a17, 1988 foreword).

**Descriptive versus prescriptive.** Prescriptive models say how to design. Descriptive studies say how designers behave. The critique line:
- Jensen and Andreasen (2010) (a16): in firms, steps are skipped, reordered and reinterpreted. In a 12-step branding method, the full sequence was the exception. One firm had about 30% of projects arising outside its formal technology planning. About 50 master students per year over 3 years did the case studies. Qualitative.
- Pahl and Beelich 1981 survey of 14 companies (a15): practice was opportunistic and the formal model generally not followed. Firms that introduced it reported more protective patents and shorter total time. Self-report, proponent-authored.
- Dorst, Eder, Frost (via b23): methods ignore differences in objective, context and actor. Methods emerge from the design process rather than precede it.
- Daalhuizen et al. (2012) (b24): effect of a method depends on objective type, context and actor. Analysis methods are more algorithmic and suit the "road" view; synthesis methods do not.

**Kannengiesser and Gero (2017) (a18, a19, b01-b03).** They coded the four Pahl and Beitz phases into the Function-Behaviour-Structure (FBS) schema as a process model: 87 elementary steps, 235 with assumed iteration (task clarification and detail once, conceptual and embodiment twice). They compared this with student protocols: Study 1, 15 two-student sessions of 45 min; Study 2, 31 sessions (brainstorming 10, morphological analysis 11, TRIZ 10). Result: requirement, function and expected-behaviour issues come early in both model and students. Structure and structure-behaviour issues come late in the model but early in students. So real designers sketch structure from the start.

**Evidence standard.** Cash, Daalhuizen and Hekkert (2023) (b11), a systematic review with a chain of evidence from motivation to claims: no paper reports every link or follows best practice. The field lacks standards for claiming a design method works. (Abstract page only.)

**Teaching reality.** Dillenhofer et al. (2025) (b12) analysed curricula at 3 of 19 German universities mapped to the VDI 2221 activity model. Design-oriented courses are 14-26% of bachelor workload (210 CP) and 27-33% of master. About 50% of product-development workload is "shaping the modules" (embodiment). Other activities average under 10% each. So even where taught, the early stages get little practice.

**Neighbouring tools inside the method.**
- Morphological analysis and functional decomposition (Fiorineschi et al. 2018, a20): known flaw is weak support for innovation; attempts to bolt on TRIZ clash on how function is defined. Cites Ullman (2010): early decisions affect about 80% of product cost.
- Roth's corkscrew (a14): full function synthesis plus a separate search of physical effects found all solution principles (3.2.1.1 to 3.2.2.2). Searching effects together with embodiment found only 3.2.1.1 to 3.2.1.5. A worked example, not an experiment.
- Systems-engineering descendants: VDI 2206 V-model (c25, c11), originating in software.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| No controlled evidence that whole-method design beats intuitive design | More than 30 industrial applications 1971-2014, all reported successful, but written by proponents or their students (Collin under Rodenacker; Schmidt, Hoehn under Beitz; Derhake under Roth; Hales under Wallace); no matched controls | Motte 2015 (a05, a06) | [E] weak evidence |
| Lever exercise: abstraction, principle search and selection cut cost | About 540 designers, 21 seminars; 90% drew solution b1 first; final cost 43% (f2) and 31% (f3) of the first solution | Pahl 1990 via Motte (a07) | [S], confounded with second try and extra time, no control |
| Coordinate table: with vs without method | One product, systematic version better mainly via fewer parts; in two variant-design cases the method helped much less | Birkhofer 1991 via Motte (a08) | [S] n=1 |
| Strict VDI 2221 followers did worse than flexible ones | N=15 engineers; good quality went with adequate decomposition, several variants, assessment, solution-neutral requirements | Fricke and Pahl 1991, Fricke 1993/1999 via Motte (a09) | [S]; no effect sizes |
| Experience beat method training | Pahl: 4 of 21 observed; 2 experienced got among the best, 2 inexperienced method-trained among the worst; experienced intuitive designer took half the time of the experienced-and-trained best. Ehrlenspiel and Dylla: no effectiveness difference among 6 designers with different strategies | Pahl 1992; Ehrlenspiel and Dylla 1991 via Motte (a10) | [S] tiny N |
| Flexible > none > strict | 16 student groups (79 students), semester industrial project; no link between adherence and quality in first report; follow-up order flexible > no method > strict; one flexible group with little field experience failed and needed the strict method first | Rueckert, Schroda, Gaedeke 1997/98 via Motte (a11) | [S] no statistics |
| Systematic education gave no conceptual-design advantage | Group sizes A1 n=47; VG A2 9, A3 5; KG A2 13, A3 9; embodiment better only in educated plus experienced (n=5 vs 9), p=.04 median test; by actual style only 8 students followed VDI 2221 top-down and they had the poorest quality | Bender 2004; Bender and Blessing 2004 via Motte (a12) | [S] small cells |
| Process quality did not predict result quality | 30 master students, embodiment; Eisentraut (N=15): result-oriented student took half the time of a thorough systematic one and built a better product; the systematic one missed central requirements | Motte, Bjoernemo, Andersson 2005; Eisentraut 1999 (a13) | [S] |
| Teaching a structured process helped specification, decomposition, criteria; no link between process and result | Before/after course plus untaught cohort; the heuristic "think in standard components" mattered more than adherence; solution search and evaluation needed most teaching improvement | Motte, Andersson, Bjarnemo 2005 (b06, b07, b25) | [S] abstract-level |
| Systematic method raised felt pressure, no gain in rating | N=213 (systematic 118, heuristic 95). Time pressure 4.03 (SD 1.33) vs 3.23 (SD 1.40), t(211)=4.27, p<.001, d=.59. Effort 4.77 vs 4.49, d=.29. Motivation lower, d about .20. Self-rated effectiveness heuristic 5.09 higher. Design rating, confidence: n.s. Clusters: 31 (14.55%) on top of things, 70 (32.86%) swamped yet striving, 64 (30.04%) indifferent, 48 (22.54%) lost faith | Daalhuizen, Person, Gattol 2012 (b08, b09) | [S] self-report outcomes |
| System-level morphological step lifted quality in crossover trial | 7 teams of 2 per group. Golf ball 0.584 to 0.853 (+46%, p=.028); mouse 0.433 to 0.740 (+71%, p=.027). Group A +26% p=.142 n.s.; group B +97% p=.004. Problem difficulty n.s. (p=.331, .366) | Sobek and Ruder 2006 (b04) | [S] run 2 always the treatment; order confounded |
| Method gains larger on new than variant design | Birkhofer's cases; plus CoT evidence that gains concentrate in formal tasks | a08, b24, d03 | [S] |
| Real behaviour departs from the staged model | Requirement, function, expected behaviour early as predicted; structure and structure-behaviour early in students, late in model. 46 sessions (15 + 31) | Kannengiesser and Gero 2017 (a18, a19, b01-b03) | [S] |
| FBS-chain prompting of ChatGPT beat free ChatGPT for human designers | 80 designers (60 novice, 20 professional), 20 per group. Mean concept score: FBS 3.31 (SD .58), fixed-prompt 2.94 (.55), free 2.90 (.47), search engine 2.63 (.53). Novices: feasibility 3.64 vs 2.85, usability 3.58 vs 2.49, functionality 3.26 vs 2.40. Professionals' novelty: free 3.73, fixed 3.60, FBS 3.53. Kappa .66 | Chen et al. 2024 (a22, a23) | [S]; p=1.7e-9 inflated; ordering FBS > fixed > free > search only |
| Nine-role staged pipeline lost requirements | 60 runs. Coverage 0% all Llama; best 20% (R1, MAS, T=0). Executability Llama MAS 40.2/46.8/49% vs 2AS 62.9/94.7/5% at T=0/.5/1; R1 MAS 34.8/1.3/5% vs 2AS 100/66/4%. R1 MAS about 6 nodes, about 650 s; 2AS 1 node, under 40 s. JSON validity 100% | Massoudi and Fuge 2025 (a24, c01-c04, d02) | [S] |
| Much of that coverage loss is bookkeeping | Empty linked_reqs and ID drift (SR01, SR-001 for SR-01) counted as misses by exact-match regex | Same (d01, d16) | [S] |
| Waterfall role pipeline beat single-step code generation | Completeness/executability/consistency/quality: GPT-Engineer .5022/.3583/.7887/.1419; MetaGPT .4834/.4145/.7601/.1523; ChatDev .5600/.8800/.8021/.3953. Ablation quality: coding .2512, +code-complete .3690, +review .3717, +testing .3953; no roles: executability .58, quality .2212; no dehallucination .3094 | Qian et al. 2024 (b18, c19, c20) | [S] tokens not controlled |
| MetaGPT SOP pipeline | Executability 3.75/4 on SoftwareDev (70 tasks), 503 s; HumanEval Pass@1 85.9, MBPP 87.7; executable feedback +4.2 and +5.4 points; human revisions 2.25 to 0.83 | Hong et al. 2024 (c21, c22) | [S] |
| Staged multi-agent systems fail often | Over 1,600 annotated traces, 7 frameworks, failure 41%-86.7%. Categories: system design 41.8%, misalignment 36.9%, verification 21.3%. 14 modes from 150 traces; annotator agreement 94%. ChatDev role fix +9.4%; verification topology +15.6% | Cemri et al. 2025 (b19, b20) | [S] |
| LLM does single early stages about as well as students | Functional decomposition completeness 3.96 GPT-4o vs 3.91 students vs 3.53 with MCTS; logic 4.00/3.87/3.69; creativity 3.12/3.48/3.32. Error-free: 16% GPT-4o vs 42% MCTS-FD, Llama 405B 10%, Llama 8B 0% | Haddad and Seibel 2025 (b16) | [S] |
| Fine-tuned small model wrote better requirements lists | ReqGPT 7B 77% (IQR 69-86) vs GPT-4 69% (62-75) vs base Mistral 34%; p<1%; 107 training lists; 18 student raters | Schiller et al. 2025 (b22) | [S] |
| LLM concepts feasible but unoriginal | GPT-3, 12 problems, 600 rated solutions; nearest-sample cosine few-shot .804, zero-shot "unique" .746; convex hull best LLM .266 | Ma et al. 2023 (a21, c14, c15) | [E] with d08, d09 |
| LLM fixation | Unique-term share 67.4% vs 78.2% human Red Dot entries (N=10 novices). Professionals anchored on LLM's first design (18 pairs) | Chen 2025; Jackson 2026 (d08, d09) | [S] |
| LLM dropped promising concept | NERF hackathon: 116 prototypes; ChatGPT 15 prototypes, 14.8 m vs winner 37 m (then 8.1, 6.6, 5.1, 0.1) | Egea et al. 2024 (b13, b14) | [S] one run |
| TRIZ automation | Top-3 contradiction match or half-match 7 of 10 textbook cases; entropy flags low agreement | Jiang et al. 2025 (a26, c17) | [S] |
| DSM generation | Reproduced 357 of 462 entries (77.3%); correctness 82.6/54.5/40.0% by source; direct ChatGPT 66.7-85.7% | Koh 2023 (c16) | [S] |
| Morphological LLM pipeline diversity | Diversity 0.64 (SD .13) with guidance vs 0.27 (SD .07) without | Lang2Morph (c23) | [S] author metric |
| Reliability needs repeats | Clopper-Pearson at 95%: 5 passes for p=.50, 29 for .90, 299 for .99; their 10/10 is below B-basis | DUCTILE (c06, c07) | [S] |
| CoT helps formal tasks only | Gains: symbolic 14.2, math 12.3, logic 6.9 points; other categories 56.8 vs 56.1; up to 95% of MMLU gain from equals-sign questions; 20 datasets, 14 models | Sprague et al. 2025 (d03) | [E] |
| CoT cost and weak gain on strong models | GPQA Diamond, 198 questions x 25 trials; 35-600% more time (non-reasoning), 20-80% (reasoning); Gemini Flash 2.0 RD -.131, Pro 1.5 -.172 (both p<.001) at 100%-correct metric | Meincke et al. 2025 (d04, d07) | [S] |
| Rich structured prompt lifted a strong model on formal planning | o1 Blocksworld Random 31.5% to 97.33%; Mystery 74.3 to 83.3; Classic 95.7 to 98.5; GPT-4o Classic 35.5 to 45.3; o1-mini Mystery 19.1 to 16.83 | Goh et al. 2026 (d05) | [S] |
| Model-chosen structure beat fixed CoT | GPT-4 BBH/T4D/MATH: direct 58/51/70.5; CoT 75/52/71; plan-and-solve 73/53/70; Self-Discover 81/85/73 | Zhou et al. 2024 (d06) | [S] |
| Structure gain shrinks with strength | Llama3.1-8B consistent gain; GPT-3.5 mostly; GPT-4o-mini about half the time and smaller | Zhang et al. 2025 (d14) | [S] |

## 4. Mechanisms and models

These are written so an engineer can build them. Each is a hypothesis about why staging helps or fails.

**M1. Solution-neutral abstraction (anti-fixation).** Rewrite the task so that it names a function, not a solution ("increase manual force to remove a cork", not "design a corkscrew").
- Implementation: S1 produces two fields, `task_literal` and `task_abstract`. A check in code rejects `task_abstract` if it contains nouns that name the first solution (keyword list from the first attempt). S3 attempts are generated from `task_abstract` only.
- Evidence: Roth corkscrew (a14, worked example), VDI 2222 advice (a04), lever (a07), Fricke solution-neutral requirements (a09). LLM link: fixation is shown (d08, d09, b14). Untested for LLMs. [S]

**M2. Function structure as a typed graph.** Overall function split into sub-functions, each with input and output flows (energy, material, signal).
- Implementation: JSON graph; code checks that every sub-function has at least one input and output and the graph is connected. Haddad and Seibel (b16): GPT-4o error-free graphs only 16%; with MCTS 42%; fully connected 44% to 72%. So the code check matters: a model-made graph needs code validation and repair loops.

**M3. Separate search of principles per sub-function, then morphological combination.**
- Implementation: table of rows = sub-functions, columns = candidate principles (3 to 5 per row, each generated in a fresh context). Code enumerates combinations, filters by compatibility rules (a pair table, may be model-filled once), and scores by a code-checkable criterion. Evidence: Roth (a14), Sobek and Ruder (b04), Lang2Morph diversity (c23). Combinations explode (product of row sizes); cap in code.

**M4. Requirements ledger.**
- Implementation: S1 writes requirements with fixed IDs (R01...). Code owns the IDs and the list, never the model. After each later stage, a checker lists unmet IDs and the next stage must either satisfy or explicitly waive each one. Coverage is measured on the final output with a semantic or per-ID judge, not exact-match regex. This answers the Massoudi and Fuge failure (d01, d16). No study has tested the ledger (K25, conjecture).

**M5. Stage-end decision gate (the VDI 2222 box).** At each stage end, a check outputs one of: go on, repeat the stage, go back to stage k. Code evaluates the check where it can (graph connectivity, requirement coverage, code runs). VDI 2222 had these; VDI 2221 lost them (a02). MAST finds verification is where staged systems fail (b19, b20: a verification loop +15.6%).

**M6. Flexible ordering.** Allow skipping and reordering, but log it. Human evidence: flexible followers beat strict ones (a09, a11). Self-Discover shows model-chosen structure beats fixed (d06), but only once per task. Implementation: a stage menu; code picks the next stage from the failing check, not from the model's wish (G1 compatible).

**M7. Early structure sketch allowed.** Students raised structure issues early (b03). Implementation option: allow a "provisional structure" note inside S1/S2, flagged as a hypothesis, kept out of the S3 context to avoid anchoring (d09). Untested (gap 8).

**M8. Cost cap per stage.** Each stage gets a token cap. A stage stays only if the arm with it beats the arm without it at equal total tokens (G7). Evidence for the cost: d04, d07, b08, c03.

**M9. Pass^k reporting.** Report the chance of k passes in a row, not single-run pass (c06, c07).

## 5. What holds up

**Replications and agreement.**
- Humans, adherence vs quality: five lines agree on "no positive link between strict adherence and quality": Fricke (a09), Rueckert (a11), Bender (a12), Motte et al. (a13, b06), Pahl 1992 (a10). All second-hand via Motte (2015), so one reviewer's reading. Independent groups: about 4. [E] that strict adherence is not shown to help.
- Experience over method: Pahl, Ehrlenspiel, Rueckert, Daalhuizen (clusters), and the LLM analogue (gain shrinks with model strength, d04, d14). [E] for humans.

**Failures and non-replications.**
- No controlled test shows the whole method beats intuition (Motte 2015). The positive cases (about 30) are non-independent and from proponents. Counted as one source (K01).
- Education effect null (Bender): no difference in conceptual-design quality between taught and untaught students.
- Daalhuizen: the systematic route felt worse (d=.59 more time pressure) and did not raise rated quality.
- The Sobek and Ruder group A effect was n.s. (+26%, p=.142). Only group B (+97%, p=.004) was significant. Run 2 was always the treatment, so learning is confounded.
- Lever: confounded with a second attempt.

**Moderators.**
- Task novelty: larger gains in new design than variant design (Birkhofer, a08). [S]
- Designer experience: novices with little field experience needed the strict method first (a11); experts do fine without. [S]
- Task type for LLMs: staged/CoT structure pays on formal, verifiable tasks (symbolic +14.2, math +12.3, logic +6.9) and about nothing elsewhere (+0.7) (d03). Open-ended design was not in that set.
- Model strength: gains shrink with stronger models on generic structure (d04, d14), but a rich task-method-knowledge prompt lifted o1 most on formal planning (31.5% to 97.33%) (d05). Too weak a model breaks the pipeline (Llama MAS crashes, d15). So the shape is task-dependent.
- Designer's analysis vs synthesis: analysis methods suit staging better than synthesis methods (b24).

**Interventions that worked.**
- A function-first (FBS) prompt chain for novices (feasibility +0.8 on a 5-point scale) (a23).
- System-level morphological step (+46%, +71% pooled) (b04).
- Verification loop in a staged LLM pipeline: +15.6% (b20). Better role prompts: +9.4%.
- Executable feedback in MetaGPT: +4.2 and +5.4 points (c22).
- Testing phase in ChatDev: executability .74-.81 to .88 (c20).
- Diversity guidance in a morphological pipeline: 0.27 to 0.64 (c23).
- Self-chosen reasoning structure: GPT-4 T4D 85 vs 52 for CoT (d06).

**Interventions that did not work.**
- Telling students to "consider architecture" without a tool (b05).
- Novelty wording in the prompt (c15). Few-shot examples shrank diversity.
- MCTS on function decomposition: lowered rated completeness (3.96 to 3.53) and logic (4.00 to 3.69) though it raised structural validity (b16).
- More stages without verification: staged pipeline lost requirements (a24).
- Generic CoT on strong reasoning models (d04).

**Known flaws in the staged-LLM evidence** (critique.md): ChatDev compared against weak single-step baselines with no token control; the two-agent loop's 100% executability came with a collapse to one node; coverage of 20% is partly an exact-match artefact; Chen et al. p-values look inflated.

## 6. Language models

**Single stages.** LLMs do early stages roughly at student level.
- Functional decomposition: GPT-4o completeness 3.96 vs students 3.91; creativity lower (3.12 vs 3.48) (b16). Only 16% of GPT-4o graphs were error-free by graph rules; 100% format-correct.
- Requirements: fine-tuned 7B beat GPT-4 (77% vs 69%) (b22).
- DSM: 77.3% of published entries reproduced (c16).
- TRIZ: 7 of 10 contradictions matched in top 3 (a26).

**Concept generation.** Feasible, useful, less novel than crowds (Ma, GPT-3) (a21). Repeats itself after a few outputs. Few-shot raised closeness to human concepts and shrank spread; novelty wording did not help (c15). GPT-4o shows fixation (67.4% vs 78.2% unique terms) (d08). Professionals anchor on the model's first design (d09). Egea: strong concept generation, but dropped the promising pneumatic concept at a small hitch and fixated on detail; ranked 2nd of 6 (b13, b14).

**Staged vs unstaged.**
- Software (ChatDev): staged beats single-step: quality .3953 vs .1523 and .1419; executability .88 vs .41 and .36 (b18). Confounded with roles and dialogue, tokens uncontrolled.
- Systems design (Massoudi and Fuge): staged 9-role pipeline vs two-agent loop on 70B models. Staged gave finer decomposition (about 6 nodes vs 1) at 17 times the time (650 s vs 38.6 s) and lost requirements (max 20%); the loop was more often runnable but partly by collapsing to a trivial design (a24, d02). With the reasoning model, the staged system beat the loop on coverage and graph size; the loop won on executability, completion and runtime. The non-reasoning model failed to finish in the staged pipeline (d15).
- Failure causes (MAST): 41-86.7% failure; spec, misalignment and weak verification dominate (b19). Verification loop +15.6%.
- FBS chain with humans in the loop: 3.31 vs 2.90 (a22). Not LLM-only.
- Generic structure: gains on formal tasks only (d03). Cost 35-600% more time for non-reasoning models (d04).
- Self-chosen structure beats fixed (d06). Rich method prompt lifts strong models on formal planning (d05).

**What is not known.** No study runs a Pahl-and-Beitz or VDI 2221 prompt sequence against a plain prompt on a frontier model at equal tokens (K19; the search was not exhaustive because APIs were rate-limited). No stage-order vs stage-content ablation. No frontier replication of Egea.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | Treat any stage list as unproven. Keep the G7 rule: every stage must beat the plain arm at equal tokens. Never add a stage on authority alone. | G7 | [E] | K01; a05, a06, a12, a13, b23 |
| A2 | Do not force one fixed order for all items. The schema's S1-S9 order is a default; skipping must be allowed by code when a check already passes (this agrees with S0 gating and G1). | G7, S0 | [E] | K02; a09, a11, a13, b06, b07 |
| A3 | Make the gate depend on difficulty and novelty: easy/routine items go direct; staged flow where a check exists or the item is new. | S0 | [E] for formal-vs-open split; [S] for novel-vs-routine | K21 (d03); K04 (a08) |
| A4 | S1 output should be a short requirement list with fixed IDs, kept by code, plus the original wording. (The ledger itself is in "Test first".) | S1 | [E] that LLMs can do the stage at student level | K14; b16, b22, c16 |
| A5 | A plain LLM gives feasible but repetitive concepts. Open mode needs forced alternatives plus code-based selection (already in S3). This evidence agrees; no change needed. | S3, O1 | [E] | K15; a21, c14, c15, d08, d09, b13 |

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Requirements ledger with code-owned IDs and unmet-ID listing after each stage. | G4, S1 | [S] conjecture | K25, K11; d01, d16, c02 |
| T2 | Stage-end decision gates (VDI 2222 style) computed by code. | S4, G2 | [S] | K13, K20; b19, b20, a02 |
| T3 | Solution-neutral abstraction step before generating (M1). | S1, S3 | [S] | K05; a14, a04, a07 |
| T4 | Function-structure typed graph with code validation (M2). | S2 | [S] | K10, K14; b16, a22 |
| T5 | Morphological table of sub-function by principle, code-enumerated combinations (M3). | S2, S3 | [S] | K07; b04, c23 |
| T6 | Flexible vs fixed stage order; agent or check-chosen subset. | G7, S0 | [S]/[C] | K23, K02; d06, a09, a11 |
| T7 | Persistence rule: keep a rejected concept alive until a check fails twice. | G6, S5 | [S] | K17, K26; b14, d08 |
| T8 | Early structure sketch allowed in S1/S2, flagged. | S1 | [S] | K08; b03, d09 |
| T9 | Stage token caps and pass^k reporting. | G7 | [S] | K09, K18, K24; b08, d04, d07, c07 |
| T10 | Repeat-run agreement (entropy) as a confidence signal at S2 decisions. | G5 | [S] | K16; a26, c17 |
| T11 | Scaffold gain on weak vs strong base models. | S0 | [S]/[C] | K03, K22; d04, d05, d14, d15 |
| T12 | Memory: log which stage was decisive per problem class. | memory | [D] | indirect |

## 8. Concrete tests on our bench

All arms at equal total tokens (stage tokens count). Report pass^k (k=3 or more seeds), not single pass. Items: our open-design and novelty items (NoveltyBench style) and our code or constraint items with a checker; ARC and Brainteaser items serve as routine controls.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1. Staged P&B prompt vs plain | Open design briefs with 8-12 requirements and constraint-checkable parts | (a) plain; (b) generic extra steps (verify, alternatives); (c) staged in order: clarify, abstract, function graph, principles, evaluate; (d) staged in shuffled order | Requirement coverage (per-ID judge, code-run constraints), distinct-concept count, pass^3 | Staged > plain on coverage by 10 or more points; (c) vs (d) tells order from content; (b) tells staging from generic effort |
| B2. Requirements ledger | Same briefs | Staged with and without code ledger | Coverage of requirement IDs in final output (semantic judge, blind) | Ledger +15 points or more; Massoudi baseline was at most 20% |
| B3. Stage-end gates | Code tasks with unit tests; constraint design tasks | Staged without gates vs with code-computed gates | Pass rate on held-out tests | Gates +10 points (MAST: +15.6) |
| B4. Fixed vs flexible order | Mixed easy and hard items | Fixed S1-S9 vs check-chosen subset vs plain, equal tokens | Accuracy and tokens used | Flexible >= fixed; saves tokens on easy items |
| B5. Abstraction step | Open design items with a known typical-solution trap | Generate from literal task vs abstract task | Distinct solution principles (code clustering by function or effect); share of typical answer | +1 to 2 principles per item |
| B6. Morphological table | Open design | Free list of 5 concepts vs table-and-combine | Distinct concepts, best concept's checker score | More distinct combos; quality gain uncertain |
| B7. Weak vs strong model | Same items on a small and a frontier model | Scaffold vs plain per model | Gain per model and token ratio | Larger gain on the weaker model for generic structure; possible reversal on formal planning (d05) |
| B8. Novel vs routine | Item pool tagged novel or routine | Route routine to plain, novel to staged vs always-staged | Accuracy at equal tokens | Routing wins by saving tokens on routine items |
| B9. Persistence rule | Multi-step design tasks with a hitch (a component fails once) | Drop on first fail vs keep alive until two fails | Final task success; abandonment rate | Persistence +10 points on tasks with transient failures |
| B10. Early sketch | Open design | Blocked order vs sketch allowed in S1/S2 (kept out of S3 context) | Distinct concepts; anchoring share (first concept's share of final picks) | Unknown; risk of anchoring |
| B11. Entropy signal | Repeated runs of S2 decisions | Entropy of decision vs correctness | AUROC of entropy for error | AUROC above .65 |

## 9. What does not transfer, and why

- **The human evidence is about people with skills, time and motivation.** Daalhuizen found felt time pressure and lost motivation (d=.59, d about .20). An LLM has no motivation. What may transfer is cost (tokens), not the feeling.
- **Experience beats method.** For a frontier LLM the "experience" is in the weights. The human finding that experts do fine without method maps only loosely to model strength, and the LLM data are mixed (d04, d14 vs d05).
- **Physical embodiment stages (layouts, production documents)** have no counterpart in a text agent. Stages 4-7 of VDI 2221 (modules, layouts, production) do not map to S-states. Dillenhofer shows human teaching also concentrates on embodiment (b12), which is out of scope here.
- **Iteration across drawings and prototypes.** Egea's prototypes cost 0.7 h each (b13); our agent tests by running code, not by building.
- **Industrial positive cases** are proponent-authored and not independent; they transfer nothing (a06).
- **The Pahl and Beitz stance (intuition is rarely good) is a human claim.** For LLMs the plain model is already a strong baseline on routine items; extra thinking can hurt on easy items (G11).
- **ChatDev and MetaGPT results are software.** Executable tests exist there. Open mechanical design lacks such checks, so the gains may not carry to tasks without a checker (d03).
- **Role-play (nine roles).** The Pahl and Beitz stages do not need nine agents; the role dialogue confounds staging (b18). G9 (no debate) applies.
- **Student studies at one university** (Kannengiesser and Gero, Daalhuizen, Bender) have small cells and one task each.

## 10. Open questions

1. Does a Pahl-and-Beitz staged prompt beat a plain prompt on a frontier LLM at equal tokens, and on which tasks? (d11, K19)
2. Is the gain from stages, or from generic extra work (verification, alternatives, requirement checking)? An ablation of stage order vs stage content is missing.
3. Does a code requirements ledger fix requirement loss (K25)? How much of the 20% coverage ceiling is bookkeeping (d01)?
4. Does flexible, check-chosen ordering beat fixed order inside one problem for LLMs (Fricke, Rueckert analogue)? Self-Discover tested a once-per-task choice only (d06).
5. Does the staged gain depend on base-model strength? Evidence mixed (d04, d05, d14, d15).
6. Is the gain larger for novel than routine design? No benchmark found.
7. What do the original German studies (Fricke 1993/1999, Ehrlenspiel and Dylla, Bender 2004, Rueckert 1997) report in effect sizes? Only Motte's summary was read.
8. Do early structure sketches help or hurt an LLM inside clarify and function stages?
9. How should stage cost be bounded so stage tokens pay for themselves?
10. Do frontier models reproduce Egea's concept abandonment, and does a persistence rule help?
11. Does the 2019 revision VDI 2221-1 restore decision gates? It was not read (a03).
12. What share of design-method papers meet each link of the Cash et al. (2023) chain of evidence? Only the abstract was read.

## 11. Sources

[V] opened (page or PDF text read this session); [M] snippet or abstract-level only.

- [V] Jaensch and Birkhofer (2006), development of VDI 2221. https://www.designsociety.org/download-publication/18983/the_development_of_the_guideline_vdi_2221-the_change_of_direction (a01-a04)
- [V] Motte (2015), Effectiveness of the systematic engineering design method. https://asiachapter.designsociety.org/download-publication/37712/ (a05-a15; also carries second-hand Pahl 1990/1992, Birkhofer 1991, Fricke and Pahl 1991, Fricke 1993/1999, Ehrlenspiel and Dylla 1991, Rueckert et al. 1997/98, Bender 2004, Motte et al. 2005, Eisentraut 1999, Roth 1995, Pahl and Beelich 1981). The originals are [M], not opened.
- [V] Jensen and Andreasen (2010), Design methods in practice. https://www.designsociety.org/download-publication/29347/design_method (a16, a17)
- [V] Kannengiesser and Gero (2017), Can Pahl and Beitz' systematic approach be effective. https://www.cambridge.org/core/journals/design-science/article/can-pahl-and-beitz-systematic-approach (a18, a19, b01-b03)
- [V] Fiorineschi, Frillici, Rotini (2018). https://designsociety.org/download-publication/40519/ (a20)
- [V] Ma, Grandi, McComb, Goucher-Lambert (2023), conceptual design with LLMs. https://arxiv.org/abs/2306.01779 (a21, c14, c15)
- [V] Chen et al. (2024), FBS ontology for controllable generative design. https://spiral.imperial.ac.uk/bitstreams/fe8fedb0-8313-4557-8035-9b15c (a22, a23)
- [V] Massoudi and Fuge (2025), Agentic LLMs for conceptual systems engineering and design. https://arxiv.org/abs/2507.08619 (a24, b17, c01-c05, c26, d01, d02, d15, d16)
- [M] Bhattacharya, Majumder, Chakrabarti (2024), SAPPhIRE with reference knowledge. https://arxiv.org/pdf/2407.00396 (a25; abstract level, weak)
- [V] Jiang et al. (2025), AutoTRIZ. https://arxiv.org/abs/2403.13002 (a26, c17)
- [V] Marini and Krus (2026), context operations for architecture modelling. https://arxiv.org/abs/2609.10132 (a27, c18; skimmed)
- [M] Search notes of this run (a28, d10-d13). Searches were not exhaustive.
- [V] Sobek and Ruder (2006), improved design method experimental validation. https://peer.asee.org/849.pdf (b04, b05)
- [V] Motte, Andersson, Bjarnemo (2005), teaching a structured design process. https://lup.lub.lu.se/record/578369 (b06, b07, b25; abstract-level record page)
- [V] Daalhuizen, Person, Gattol (2012), ambiguous role of methods. https://cognitive.designsociety.org/download-publication/32172/ (b08-b10, b23, b24)
- [M] Cash, Daalhuizen, Hekkert (2023), evaluating efficacy and effectiveness of design methods. https://researchportal.northumbria.ac.uk/en/publications/evaluating-th (b11; abstract only)
- [V] Dillenhofer et al. (2025), competencies in higher education. https://www.cambridge.org/core/product/37C2FB50A71936A0AA59E4595EE46FA (b12)
- [V] Egea et al. (2024), ChatGPT as an inventor. https://arxiv.org/pdf/2404.18479 (b13-b15)
- [V] Haddad and Seibel (2025), functional decomposition with LLMs. https://www.cambridge.org/core/product/35FEB974215FB807A317AF662EA29EA (b16)
- [V] Qian et al. (2024), ChatDev. https://arxiv.org/abs/2307.07924 (b18, c19, c20)
- [V] Cemri et al. (2025), MAST. https://arxiv.org/pdf/2503.13657 (b19, b20)
- [M] Otten et al. (2026), generative AI in systems engineering. https://arxiv.org/pdf/2602.04358.pdf (b21; body unreadable)
- [V] Schiller, Haddad, Seibel (2025), ReqGPT. https://www.cambridge.org/core/product/B39D357BB32F8F87C75CF5CFC639AEC (b22)
- [M] Three-team brake study, VDI 2221. https://www.designsociety.org/publication/33181/school_culture_through (b26; snippet)
- [M] Diamond of Thought. https://arxiv.org/pdf/2410.06972 (b27; snippet)
- [V] Pradas-Gomez, Brahma, Isaksson (2026), DUCTILE. https://arxiv.org/abs/2603.10249 (c06-c08)
- [V] Guo et al. (2025), MDO agent. https://arxiv.org/abs/2511.17511 (c09)
- [V] Kumar and Karniadakis (2025), knowledge-guided multi-agent design. https://arxiv.org/abs/2511.03179 (c10)
- [V] de Payrebrune et al. (2024), AI in VDI 2206 procedures. https://arxiv.org/abs/2412.12230 (c11, c25)
- [V] Chiarello et al. (2024), generative LLMs in engineering design. https://doi.org/10.1017/pds.2024.198 (c12, c13)
- [V] Koh (2023), LLM generating a Design Structure Matrix. https://arxiv.org/abs/2312.04134 (c16)
- [V] Hong et al. (2024), MetaGPT. https://arxiv.org/abs/2308.00352 (c21, c22)
- [V] Qiao et al. (2025), Lang2Morph. https://arxiv.org/abs/2509.18937 (c23)
- [M] DRS 2024 LLM-augmented morphological analysis. https://dl.designresearchsociety.org/drs-conference-papers/drs2024/research (c24; snippet)
- [V] Sprague et al. (2025), To CoT or not to CoT. https://arxiv.org/abs/2409.12183 (d03)
- [V] Meincke, Mollick, Mollick, Shapiro (2025), Prompting Science Report 2. https://arxiv.org/pdf/2506.07142 (d04, d07)
- [V] Goh, Kos, Goel (2026), Knowledge Model Prompting (TMK). https://arxiv.org/pdf/2602.03900 (d05)
- [V] Zhou et al. (2024), Self-Discover. https://arxiv.org/pdf/2402.03620 (d06)
- [V] Chen et al. (2025), design fixation in generative AI. https://arxiv.org/pdf/2502.05870 (d08)
- [V] Jackson, Cha, Prikladnicki, van der Hoek (2026), LLMs in collaborative design. https://arxiv.org/pdf/2604.09120 (d09)
- [V] Zhang et al. (2025), SR-LLM. https://arxiv.org/pdf/2502.14352 (d14)

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 4 established claims: 1 confirmed as written, 3 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E07.01-K03** (reworded: the sources support less). In Pahl's 4-designer case the best result went to the experienced designer who was also method-educated, and the review concludes the method was 'all in all positive' but inseparable from experience; only one of the two experienced designers worked without the method, so 'experienced designers without method got top results' and 'experience beats method training' overreach an N=4 anecdote (the LLM papers d04/d14 listed as evidence are unrelated). Corrected claim: In a small observation of 4 of 21 designers (Pahl 1992, via Motte 2015), the two experienced designers got among the best results and the two inexperienced method-trained ones among the worst; the best result came from the experienced and method-educated designer, and the intuitive experienced designer was as good in half the time; the author concluded the method helps but cannot be separated from practical experience. One flexible student group with little experience failed until it followed the strict method (Rueckert et al.).
- **E07.01-K14** (reworded: the sources support less). Only the functional-decomposition study (12 student groups, GPT-4o lower on creativity) compares with students; the ReqGPT 77% vs 69% result is LLM vs LLM with no student baseline, so 'individual early stages about as well as students' is wider than the sources. Corrected claim: In one early-stage test, GPT-4o functional decompositions were rated about as complete as those of 12 student groups (3.96 vs 3.91; lower on creativity, 3.12 vs 3.48); separately, a fine-tuned 7B model (ReqGPT) beat GPT-4 on requirements lists in rater similarity scores (77% vs 69%), without a student comparison.
- **E07.01-K15** (reworded: the sources support less). Repetition, feasible-but-less-novel, unique-adjective and few-shot results all come from one GPT-3 study (Ma et al. 2023, listed three times); the other cited sources (Egea: ChatGPT team placed 2nd; Chen: unique-term share) do not show repetitiveness, so 'a plain LLM' and independence are overstated. Corrected claim: In one 2023 study with GPT-3 (Ma et al.), LLM concepts were rated more feasible and useful but less novel than crowdsourced ones; GPT-3 repeated itself after a few outputs, adding a 'unique' adjective gave the smallest convex-hull volume (0.186) and few-shot examples also lowered coverage (0.2) versus 0.294 for the crowd; a separate small chair-design study found a lower share of unique terms for ChatGPT (67.4%) than for human designs (78.2%).
- **E07.01-K01** (now single-source: only one opened source, code check).
- **E07.01-K21** (now single-source: only one opened source, code check).
