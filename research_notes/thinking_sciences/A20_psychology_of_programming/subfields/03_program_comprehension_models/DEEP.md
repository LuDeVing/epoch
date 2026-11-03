# Program comprehension models: deep document

*Subfield A20.03. Evidence: evidence_a-d.jsonl (a01-a25, b01-b26, c01-c27, d01-d20), claims.jsonl (K01-K33), critique.md. Several evidence lines describe the same paper (Kaufman: b18, c01-c03, c24; Li: a16, c06; Kou: a17, b15; Paltenghi: a18, c07, c08; Richards and Wessel: a21, b17; Qiao: a23, b19, c10, c11, c25; Lehmen: a22, c04, c05, c26; Abdelsalam: b12, d17). Count each paper once when you count sources.*

## 1. What it is

Program comprehension models are theories of how a person builds an understanding of code. They are cognitive models of reading, not of writing. The question is: what does the reader hold in mind, and in what order does it get built?

The classic family has five parts.

- **Top-down (Brooks 1978, 1983).** The reader forms a global hypothesis about what the program does. They refine it into sub-hypotheses. They confirm or reject each one by looking for beacons: names, comments, tell-tale code patterns. Domain knowledge drives this.
- **Bottom-up (Shneiderman-Mayer, Pennington 1987).** The reader reads statements, groups them into chunks, and builds control flow (the program model) first. A situation model (data flow, goals, function) is built on top.
- **Opportunistic / integrated (Letovsky 1986/87, von Mayrhauser and Vans 1995).** The reader uses a knowledge base, a changing mental model, and an assimilation process. They switch between top-down, program and situation models as needed.
- **Reconstructive debugging (Gilmore 1991).** Understanding is not a finished model compared with the code. It happens inside the debugging loop and fires when expectation and code disagree.
- **As-needed vs systematic (Littman et al. 1986, Koenemann and Robertson 1991, Singer and Lethbridge 1998).** Read only the code the goal needs, or read it all in order.

Why it matters for our agent. In schema terms the reading states are S1 (understand) and S2 (represent). When the task is a repo or code, S1/S2 must decide what to read, in what order, how to hold hypotheses, and when a reading is trusted. The human models give a vocabulary (beacon, chunk, hypothesis, failure reason). The LLM studies give measured failure modes. The honest finding of this subfield: **the human models are descriptive, were built on tiny samples, and have never been tested as agent prompts** (K22, c27, d20). What survives is a small set of operators and guardrails, plus a lot of LLM-specific evidence about how models misread code.

## 2. History and theories in depth

### 2.1 Brooks: top-down hypothesis refinement (1978, 1983)

Brooks is the root of the top-down view. The reader forms a first hypothesis as soon as any information arrives. They refine it stepwise down to code. Beacons confirm or refute. If no beacon is found, the hypothesis is revised or dropped. Brooks first used the word "beacon" in 1983 (a01). Wiedenbeck (1985, 1986) later tied beacon recognition to expertise (d16).

Evidence status: Brooks ran no formal empirical test (d16). The primary paper was never opened here (a01, d16 are secondary). Treat Brooks as a theory, not a result.

### 2.2 Shneiderman and Mayer; Pennington: bottom-up

Bottom-up models say the reader builds understanding from the code up. Pennington (1987) found that experts form a **program model** first (control flow, procedural units) and only later a **situation model** (data flow, function, goal hierarchy). In her studies, control-flow questions were answered better than function questions after reading. After a modification task, function questions were answered better (a02, a14). A DTIC page mentions 80 programmers in her first study (a14, not opened). Her originals were not opened; the content comes via Wyrich 2023 and Detienne's survey.

Bottom-up reading is costly. Siegmund et al. 2014 forced bottom-up reading by obfuscating identifiers. It activated five left-hemisphere regions tied to working memory, attention and language (17 participants, FDR p<0.01, about 90% got the output right; b05).

### 2.3 Letovsky: the opportunistic processor (1986/87)

Letovsky models the understander as three parts: a knowledge base, an evolving mental model, and an assimilation process. The understander is "best viewed as an opportunistic processor" (a02). Readers ask three kinds of questions: **why** (trace up to the goal), **how** (from goal down to code), and **data description** (d15). Events are small and fragmented, lasting seconds to minutes. The primary text was never opened; the account is from a 1989 report (d15) and Wyrich.

### 2.4 Littman et al. 1986: systematic vs as-needed

Littman, Pinto, Letovsky and Soloway split readers into systematic (study the code fully, in order) and as-needed (opportunistic, incomplete). Systematic readers did better at modification. The as-needed approach produced error-prone changes. They also split programmers by static vs causal knowledge; the strong model has both (a02, a25). Littman's own numbers were not opened. Vans et al. note the systematic strategy is unrealistic for large programs (a25).

### 2.5 Koenemann and Robertson 1991: as-needed in a larger program

Twelve experienced Pascal programmers (4-15 years, mean 7.6) modified a 636-line formatter (main plus 39 procedures). Each did one of four tasks, 15-44 min. Code was served on request, one piece at a time (a08).

- They read an overview first, then looked for directly relevant code (focused top-down). Bottom-up reading was used only for directly relevant code or when hypotheses failed.
- On average they visited about one fifth of the procedures and under one third of the lines. None studied more than about half. On average 24% of procedures (21.3% of lines) were never encountered.
- Chart use fell linearly over time (F(1,11)=36.05, p<.001) while code use rose (p<.001).
- Relevance was judged from procedure names and domain knowledge. Subjects decoded abbreviated names (getcmd for getcommand) very well (a09). Different tasks led to different code being studied.

This qualifies Littman: in a larger program systematic reading is not what experts do. Limits: N=12 over four tasks; code shown on request is a lab artifact.

### 2.6 Gilmore 1991: reconstructive debugging

Gilmore argues debugging does not use a finished comprehension model built earlier. Comprehension runs inside the debug loop. The key event is a mismatch between expectation and code. Bugs deeper in the program structure were found more easily by both groups, "suggesting that they were being detected during an ongoing comprehension process" (a03). Ko and Uttl restate it as a reconstructive process in which perceived design decisions are compared with actual behaviour (a07). Gilmore 1991 was not opened; evidence is via Wyrich. No sample sizes are available.

### 2.7 von Mayrhauser and Vans: the integrated metamodel (1995, 1997, 1999)

The 1995 metamodel has four components: top-down model, program model, situation model, knowledge base. Any can be activated at any time (a04). The primary text was read (d14):

- Hypotheses fail for three named reasons: (1) code to verify the hypothesis cannot be found; (2) one piece of code satisfies different hypotheses (confusion); (3) code cannot be explained.
- Beacons index into knowledge (a swap in a loop signals a sort; the name "Sort").
- Keep the number of open hypotheses manageable.
- Quote: "No one model accounts for all behavior as programmers understand unfamiliar code."
- The experimental base was thin: of the experiments reviewed, only 1 used large-scale code, 2 medium-sized, 3 used C/Unix.

The field study (1997 conference, 1999 IJHCS): four professionals, code of 40,000+ lines, about 2-hour think-aloud sessions (a10, a11).

- Chunk-and-store counts: program model 115, situation model 107. Reading code in sequence: 102. Hypothesis generation: 76 top-down, 64 situation, 65 program.
- Domain knowledge was 23% of top-down actions (count 107). Three domain experts made 94% of top-down references. The language expert with no domain experience made 13% (1997) or 14% (1999) of his references at domain level.
- "Programmers work at all levels of abstraction about equally." Main questions are what the software does and how, not why.

Limits: N=4; each subject had a different task, language and software, so expertise is confounded with person and task. The authors call the conclusions working hypotheses.

### 2.8 Singer and Lethbridge 1998: just-in-time vs full coverage

One engineer, two years, meetings every 1-6 weeks (a12). For routine fixes he comprehended only the needed code and the partial model faded. For a new feature he went for full coverage and wrote analysis documents. "What determines usage is not 'SE-type,' but rather SE goal." N=1, a position paper. It is the best statement that strategy depends on the task, not the person.

### 2.9 Ko and Uttl 2003: individual differences in an unfamiliar system

The founding numbers (a06, a07, b01). 86 recruited, 75 analysed (11 dropped for poor English). A 10-minute tutorial, then 20 minutes debugging a Stata program with four planted bugs. Over 33,000 coded actions, Ward clustering, 3 clusters chosen from 2-7 tried.

- Cluster 1 (n=20): depth-first, information seeking. Mean bugs fixed 1.00.
- Cluster 2 (n=40): inactive, spec-focused. 1.65.
- Cluster 3 (n=15): breadth-first, most programming experience. 2.00.
- Cluster 1 lower than 2 and 3 (p<.05). Programming experience differed by cluster (p<.01). The inverted-axes bug was fixed by only 16 of 75 (21.3%).
- Bug-specific domain knowledge predicted success best.
- Quote: "The results presented here are largely inconsistent with studies on debugging in familiar programming systems."

Limits: exploratory, statistics domain, mostly undergraduates, one tool, cluster solution chosen by judgement, gender confounded with major. No replication was found.

### 2.10 Later human work

- **Reading order.** Busjahn et al. 2015: novices read code less linearly than prose (about 80% linear eye moves on text, 70% on code for novices, 60% for experts). Novices looked at 52.42% of code elements vs 41.27% for experts (U=84, p<0.01). Regression rate did not differ (p=0.97). Small samples, Java (b02). Peachock 2017 (C++) replicated "code less linear than text" but not the novice-expert difference (b04, via Peitek). Peitek, Siegmund and Apel 2020 (12 novices, 19 intermediates) replicated partly: experience effect on vertical moves (p=.003, .010, .008) but not the NW story-order score (p=.932). Code linearity (jumps in execution order) had a stronger effect than experience (p=.000). Strategy (top-down vs bottom-up, forced by meaningful vs obfuscated names) had a minor effect (b03).
- **Individual differences.** Wagner and Wyrich 2021: 117 students with complete data, two Java methods. Fluid intelligence beta 0.299, visual perception 0.261, speed 0.247; crystallised intelligence 0.188 (n.s.); personality not significant. Adjusted R2 .096 (b06).
- **Atoms of confusion.** Langhout and Aniche 2021 (Java, 132 students): 115 wrong of 315 answers with atoms vs 46 of 337 without; pooled OR 3.82 (95% CI 2.69-5.42); 7 of 14 atoms significantly confusing (b07). The original C study (Gopstein 2017, 220 professionals) was seen only via the replication (b08).
- **Complexity metrics.** Lavazza et al. 2023: three students, 32 methods; mean prediction error about 30%; Cognitive Complexity gave no gain (b09). A reanalysis of ten datasets found Cognitive Complexity no better than older measures (b10).

### 2.11 Methodological reality

Wyrich, Bogner and Wagner 2023 mapped 95 experiments (1979-2019): median 34 participants (range 5-277), 53.7% students only, 9.5% professionals only, 47% Java, only 6 of 25 between-subject designs balanced experience (24%), only one qualifying replication (b20). Of 409 threat mentions, 31 cited evidence; for experience, program length and comprehension measure, 17 of 18 cited studies did not meet evidence criteria (b21). Different comprehension measures hardly correlate (a01, critique). Feitelson 2021 warns subjects find shortcuts and obfuscation changes strategy (b22). Read every human result here with this in mind.

## 3. Core findings with exact numbers

Status key: E established (two or more independent sources), S single source, C contested, H human-only, O older models only.

### 3.1 Human studies

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Experts read as needed in a 636-line program | 12 experts; about 1/5 of procedures visited; 24% never encountered | Koenemann and Robertson 1991 (a08) | S, H |
| Professionals switch levels in 40k+ line code | N=4; chunk-and-store 115 (program) / 107 (situation); top-down hypotheses 76 | von Mayrhauser and Vans 1997 (a10) | S, H |
| Domain knowledge lifts reading to purpose level | 3 domain experts made 94% of top-down references; language expert 13% at domain level | von Mayrhauser and Vans 1997 (a10) | S, H |
| Strategy depends on goal, not person | N=1, 2 years | Singer and Lethbridge 1998 (a12) | S, H |
| Strategy clusters in unfamiliar system | N=75; bugs fixed 1.00 / 1.65 / 2.00 | Ko and Uttl 2003 (a06, b01) | S, H |
| Domain knowledge of the bug predicts success best | same study | Ko and Uttl 2003 (a06) | S, H |
| Program model before situation model | direction only; Pennington numbers not read | Pennington 1987 via a02, a14 | C, H |
| Situation questions answered better in OO code | N=51; 73.1 vs 59.4, F(1,46)=99.3 | Burkhardt et al. 2002 (a13) | C, H |
| Experts read less linearly | 60% vs 70% linear eye moves; partial replication | Busjahn 2015; Peitek 2020 (b02, b03) | C, H |
| Code linearity drives order more than experience | p=.000 on all measures | Peitek 2020 (b03) | S, H |
| Fluid ability predicts comprehension | beta 0.299 (Gf); R2 .096 | Wagner and Wyrich 2021 (b06) | S, H |
| Atoms of confusion raise errors | pooled OR 3.82; 7 of 14 atoms | Langhout and Aniche 2021 (b07) | E, H |
| Complexity metrics predict understandability poorly | error about 30%; no gain from Cognitive Complexity | Lavazza 2022, 2023 (b09, b10) | E, H |
| Programmers accept correct assertions but miss wrong ones | 73.9% vs 49.0%; N=86; OR 2.94 | Kaufman et al. 2026 (c01, b18) | S, H |
| With a docstring most responses are top-down | 31/50 top-down, 7/50 bottom-up, 10/50 as-needed (10 participants) | Kaufman 2026 (c02) | S, H |
| Intuition-only verdicts are mostly wrong | 7 of 12 wrong | Kaufman 2026 (c03) | S, H |
| Negative examples mostly confirm a hunch | 14 of 18 | Kaufman 2026 (c03) | S, H |
| Deeper bugs found more easily | no numbers | Gilmore 1991 via a03 | S, H |
| Human field is thin | 95 experiments; median 34; 1 qualifying replication | Wyrich et al. 2023 (b20) | E |

### 3.2 LLM and agent studies

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Removing names costs summaries | GPT-4o 87.3 to 58.7; Qwen3-Coder 87.2 to 72.1; DeepSeek V3 87.7 to 76.7; Llama 4 Maverick 86.2 to 66.4 | Le et al. 2025 (c12) | E |
| Removing names costs execution prediction | ClassEval 85.7 to 76.1; LiveCodeBench 85.4 to 71.2 | Le et al. 2025 (c12) | E (subsets of 37 and 96) |
| Neutral renaming cost by benchmark | CRUX about 1-9% relative; LCB up to 27% | CodeCrash (d07) | S |
| Meaning-preserving edits break fault localisation | 78% of correct localisations fail; 1.04% per step (Java), 1.93% (Python); 83% drop on function reordering | Haroon et al. 2026 (b13) | S (injected faults) |
| Mutations on code predicates | average effect up to 34% | Hooda et al. 2024 (a19) | O |
| Simulated execution is unreliable | avg 44.4% accuracy, IC 10.3 over 15 models | REval (c14) | E, O |
| Coherent is not correct | 81.42% coherent; 46.92% of those correct; 16 models | Liu et al. 2025 (c15) | E |
| Best model fully traces few tasks | 47% | CoCoNUT (a24, snippet only) | S |
| Reasoning LLMs make 9 kinds of trace error; tools fix some | 427 snippets; 85-98% accuracy; tool fixed 58% of computation errors | Abdollahi et al. 2025 (b14) | S |
| Comments are trusted for output prediction | 23.2% relative drop, 13.8% with CoT; about 24% for misleading comments and prints; 17 LLMs, 1,279 questions | CodeCrash (d06) | C |
| Comments do not shift security review | shifts -5% to +4%, p>0.21; 9,366 evaluations | Thornton 2026 (d08) | C |
| Fixed top-down pipeline matches agents | Agentless 32.00% (96 fixes) at $0.70; file localisation 78.67 / 70.33 / 81.67% | Xia et al. 2024 (c20) | E |
| Skeleton beats full file | 58.33% vs 53.67% | Agentless (c20) | S |
| View size changes success | 100-line viewer 18.0%; 30-line 14.3%; full file 12.7% | SWE-agent (c22) | S |
| Summarised search beats iterative | 18.0% vs 12.0% (none 15.7%) | SWE-agent (c22) | S |
| Last-5 observations beat full history | 18.0% vs 15.0% | SWE-agent (c22) | S |
| One failed edit hurts | eventual success 90.5% to 57.2% | SWE-agent (c22) | S |
| Graph tools help localisation | LocAgent file Acc@5 94.16% vs 90.15%; removing SearchEntity 88.32 to 68.98 | LocAgent (c21) | S |
| Graph-only tool loses to grep | Func@5 0.595 vs 0.832 (n=274) | Lin et al. 2026 (d10) | S |
| Graph views as extra help | +20, +35, +46 resolved of 731 | DualView (d11) | S |
| Call/inheritance hints as comments | Func@5 +2.2, variance about halved, +10% input tokens | Lin et al. 2026 (d09) | S |
| Failure is long and in fine localisation | file match 92-97% (success) vs 59-81% (fail); steps 54.05 vs 98.62 (OpenHands Verified) | Majgaonkar et al. 2025 (c18) | E |
| Agents recall few lines | line recall 0.15-0.23 vs oracle 0.953; CoSIL 0.788 | SWE-Explore (c19) | S |
| Failed runs repeat actions | repeats 13.6% vs 6.1% (RepairAgent); iterations 40 vs 22 | Bouzenia and Pradel 2025 (c17) | S |
| Stage-wise code reasoning adds resolution | +10.53, +6.29, +8.34 points on SWE-bench Pro (731); tokens +7.6% | DeskCheck (d02) | S |
| DeskCheck ablation | 53 to 68% on 100 instances | DeskCheck (d03) | S |
| Structured simulation vs 28 reproduction tests | method recall 0.66 vs 0.23 | DeskCheck (d04) | S |
| Certificate beats free CoT | patch equivalence 78.2% to 88.8%; 2.8x steps | Ugare and Chandra 2026 (d05) | S |
| One re-plan at first edit | +16.8% / +14.7%; matches periodic review at 11-15% of planner cost | PAUSE (d13) | S |
| Debugger loop gives little repair gain | Defects4J v1.2 87 vs 76 fixes; v2.0 110 vs 113 | AutoSD (c16) | S |
| Hallucinated debugger output hurts | about 11 points less likely plausible | AutoSD (c16) | S |
| Human-model attention weakly aligned | at most 22% of methods significant; summary quality not predicted | Li et al. 2024 (a16, c06) | E |
| Metrics do not predict LLM success | AUROC 0.63 vs 0.86 for a shadow model | Beyond Accuracy 2026 (a20) | S |
| Perplexity spike tracks confusion at region level | rho 0.47 vs 0.05 (24 participants); snippet-level fails (largest 0.373, n.s.) | Abdelsalam 2025; Rong 2026 (d17, b11) | C |
| LLM explanations help but contain errors | 90.2% vs 65.0%; 50% had an incorrect statement | via Qiao et al. 2025 (c11) | C |

## 4. Mechanisms and models

Each model below is written so that code could implement it. These are our reading of the literature, not tested designs (K22).

### 4.1 Hypothesis store (Brooks, von Mayrhauser and Vans)

State: a list of open hypotheses H. Each has: statement, level (code / algorithm / domain), evidence list, status (open / confirmed / failed).

Loop (the program runs it; the model fills slots):
1. Model writes one hypothesis about the code or failure in a fixed slot ("This function does X because Y").
2. Program checks `len(open) <= CAP`. The sources say "manageable" and give no number; start with 3. If over cap, the program asks the model to close or merge one.
3. Model names the beacon it expects (a name, a call, a pattern) and where to look. Program runs a search (grep, outline) for it.
4. If a beacon is found, the model quotes it with file and line. Program stores it. If not found, the program assigns a failure reason.
5. Failure reason is one of three labels (d14): NOT-FOUND (no verifying code), AMBIGUOUS (the code fits several hypotheses), UNEXPLAINED (code cannot be explained). Next action: NOT-FOUND, widen the search or drop; AMBIGUOUS, add a discriminating test; UNEXPLAINED, switch to bottom-up on this unit.
6. Confirmed means a beacon plus a check that could have refuted it (G3; see c03 on confirm-only checks).

### 4.2 Bottom-up chunking and the program/situation split (Pennington)

Two passes over a unit of code. Pass A (program model): list the steps in execution order; for each branch or loop, name what changes. Pass B (situation model): after pass A, write what the unit is for and what data flows out. Run pass B once a task is set (a14: function questions were better after a modification task). Burkhardt shows the task changes what is built: a reuse task pushed novices toward a situation model (a13).

For an agent, pass A must not be a free-text mental run. Models trace poorly (c14, c15). Pass A should be a structural outline from a parser, with real execution for values (K08).

### 4.3 As-needed reading with a coverage ledger (Koenemann, Singer)

State: ledger L of code units with status (seen-full, seen-skeleton, never-seen) and a relevance guess with a reason (name-based, per a09).

Procedure:
1. Overview first (skeleton, outline, file tree; Agentless 58.33% vs 53.67%).
2. Pick directly relevant units by name and goal. Read those fully.
3. Expand only on failure: when a hypothesis fails, widen to callers or callees.
4. Before editing, the program lists units the answer depends on that are still never-seen. The model must read them or write why they cannot matter. This is our proposed fix for the known risk of as-needed reading: partial models and error-prone changes (a25). It is a design, not a finding.
5. Strategy switch by task type (Singer): narrow fix means as-needed; new feature or refactor means broader coverage. Task type is a code-checked label.

### 4.4 Reconstructive debug loop (Gilmore, AutoSD)

Keep an expected-behaviour line. Run something real. Compare the output to the expectation. A mismatch triggers deeper reading of the code that produced that output. Hypothesis, prediction, run, conclude (c16). The observation must be real tool output: AutoSD shows hallucinated debugger output lowers plausible-patch odds by about 11 points.

### 4.5 Breadth-first survey vs depth-first dive (Ko and Uttl)

Breadth-first: list all modules (names, one-line purpose), then dive. Depth-first: dive on the first hit. Ko and Uttl: breadth-first cluster 2.00 bugs vs depth-first 1.00, but it is a single exploratory human study. As an agent policy it is untested (K03).

### 4.6 Skeleton, graph, and hints

Three structure aids were tested. (1) Skeleton before full code (Agentless). (2) Preview then load on demand (SWE-Adept; roughly 10-15% fewer localisation tokens at equal or slightly higher accuracy; table layout ambiguous). (3) Call and inheritance links as hints (Lin et al.: +2.2 Func@5, variance halved; prefer who-calls-me links on hub-heavy repos). A graph as the only tool lost to grep. So structure is added beside text search, not instead of it.

### 4.7 Stage-wise code reasoning and certificates

DeskCheck: four stages of explicit code reasoning (localise, repair-refine, audit against the issue text, validate by simulating input and expected output). Ugare and Chandra: a fill-in certificate with premises, per-test execution traces and a conclusion. Both force the model to follow actual call paths; the certificate caught a shadowed function (d05). These are the closest studies to a comprehension scaffold for LLMs, but neither names bottom-up or top-down.

### 4.8 Anchor control

Kaufman et al.: with a docstring present, people read top-down and confirm. They accept correct claims 73.9% but catch wrong ones only 49.0%. CodeCrash: LLMs treat comments as authoritative. Mechanism: read the code first and write what it does, then compare with the comment or spec as a claim. Schema S1 already has input hygiene that moves suggestive material into a marked block.

### 4.9 Surprise flag

Region-level perplexity spikes of a code model track human EEG confusion (rho 0.47, 24 participants; d17). A detector hit 64% of labelled atoms but flagged 85 other regions in confusing snippets and 69 in clean ones (b12). Mechanism: score tokens, flag top spans, force a real-execution check on those spans. Snippet-level perplexity is not useful (b11).

## 5. What holds up

### 5.1 Replications and failures

- **Only one qualifying replication in 95 human experiments** (Wyrich et al. 2023; b20). The whole subfield rests on single studies.
- **Reading order (Busjahn 2015).** Peachock 2017 (C++): "code less linear than text" replicated; the experience difference did not (experience p-values .41-.49; b04). Peitek 2020: partly replicated (vertical moves yes, NW score no; b03). The expert/novice gap is fragile.
- **Atoms of confusion.** Replicated in Java with novices (b07): 7 of 14 atoms significant; some C atoms did not replicate; perceived confusion disagreed with Gopstein for some atoms.
- **Pennington's order.** Burkhardt et al. 2002 found the reverse in OO code (situation 73.1 vs program 59.4). The authors say question difficulty cannot be calibrated, so the two models are not comparable. Neither a clean replication nor a refutation (a13).
- **Koenemann vs Littman.** Koenemann qualified Littman (as-needed in a bigger program). Nobody tested them head to head.
- **Ko and Uttl.** No replication found. They say their results are "largely inconsistent" with studies in familiar systems.
- **Kaufman 2026.** Pre-registered, N=86, but the strategy coding comes from 10 think-aloud participants and two coders.

### 5.2 Meta-level

- Experience as a moderator is not firmly backed (b21: 17 of 18 cited studies fail the criteria).
- Comprehension measures hardly correlate. Numbers across studies are not additive.
- Complexity metrics have not delivered (b09, b10).

### 5.3 The "novice bottom-up, expert top-down" slogan

Reviews state it (Qiao et al.: a23, c10, c25). The measured data do not support it simply.
- Ko and Uttl: the most experienced cluster was breadth-first.
- Busjahn/Peitek: experts read less linearly, but the effect is fragile and partial.
- Kaufman: with a docstring most people went top-down regardless.
- Peitek: strategy had only a minor effect on reading order (b03).
The slogan is a textbook line, not a measured result. Singer's "goal, not person" fits better but is N=1.

### 5.4 Interventions that worked for agents

- Coarse-to-fine reading with a skeleton (Agentless): 32.00% at $0.70.
- A 100-line window (SWE-agent): 18.0% vs 12.7% full file.
- Summarised search results and last-5 observations (SWE-agent).
- Structured code reasoning at four stages (DeskCheck): +6 to +10 points at +7.6% tokens (single paper, not peer reviewed).
- Certificates (Ugare and Chandra): 78.2% to 88.8% at 2.8x steps (not equal compute).
- One re-plan at the first edit (PAUSE): +16.8% / +14.7%, weak executor with a strong planner.
- Call hints as comments: small but stable.

### 5.5 Interventions that did not work, or whose gain is unclear

- **Hypothesis-experiment loop for repair (AutoSD):** repair accuracy about equal to the plain LLM (87 vs 76 on v1.2, 110 vs 113 on v2.0). The benefit was explanations for humans.
- **Graph-only tool:** lost to grep (0.595 vs 0.832).
- **Iterative search (SWE-agent):** 12.0% vs 18.0% for summarised search; agents stepped through every match.
- **Mimicking human attention:** alignment does not predict summary quality (Li: rho -0.128, p=0.386 for accuracy).
- **Theory-of-mind assistant (Richards and Wessel):** overall null (0.05, p=0.61). The +0.34 / -0.28 split is a post-hoc subgroup on 28 observations; not a finding.
- **Natural-language explanations for judging assertions (Kaufman):** no net benefit; poor ones hurt.
- **Complexity metrics for triage (b09, b10, a20).**

### 5.6 Moderators that matter

- Task: comments anchor output prediction but not security review (K14/K27 contested).
- Code length: name-hiding costs 1-9% on short CRUX code and up to 27% on LCB.
- Language familiarity: Ko and Uttl's unfamiliar-system results differ from familiar-system studies.
- Paradigm: procedural vs OO may reverse the program/situation order (unresolved).
- Whether a spec or docstring is present (Kaufman).
- Executor strength: PAUSE gains are for a weak executor.

## 6. Language models

No LLM study uses von Mayrhauser-Vans or Letovsky as a prompt (c27; search-based negative with rate-limited APIs; absence is not proven). What exists is indirect.

### 6.1 How models behave on comprehension tasks

- **Names are beacons for models too.** Hiding identifiers drops class-summary accuracy from 86-88% to 59-77% across four models (c12). Execution prediction also drops, by 9.6 points on ClassEval (85.7 to 76.1) and 14.2 on LiveCodeBench (85.4 to 71.2), although these tasks should not need names. Llama 4 Maverick with ambiguity renaming went 80.2 to 56.4. The execution subsets are small (37 and 96) and GPT-4o is the summary judge.
- **Comments are trusted.** CodeCrash (17 LLMs, 1,279 questions): relative drop 23.2% direct and 13.8% with CoT; misleading comments and prints about 24%. GPT-4o-Mini fell -32.6% (CRUX) and -40.4% (LCB). Four "reasoning collapse" events, all QwQ-32B. But in security review, adversarial comments shifted detection by -5% to +4% (p>0.21; d08). Task-dependent.
- **Simulated execution is poor.** REval: average 44.4%, IC 10.3 over 15 models; GPT-4-Turbo path 57.7, average 75.0, IC 42.5. Models often get the output right without the right intermediate states. CoT on CodeLlama-7B: path 10.8 to 21.4, output down 6.8. Liu et al.: of 81.42% coherent simulations only 46.92% were correct (16 models, HumanEval). Consistency across different-path tests: strong 5.76%, weak 45.37%, random 48.87%; 361 correct outputs were suspicious. Reasoning models are better (85-98% in Abdollahi et al.) but still make nine kinds of error; tools fixed 58% of computation errors.
- **Brittle to meaning-preserving edits.** 78% of previously correct localisations fail after mutations; 56% of correct localisations lie in the first 25% of lines vs 6% in the last 25%; function reordering gave an 83% drop (b13; injected faults, spec given). Hooda et al.: mutation effect up to 34% (2023-era models).
- **Failure is not where humans fail.** Complexity metrics: AUROC 0.63 vs 0.86 for a shadow model (a20). Attention: at most 22% of methods align with human gaze (Li et al.). Paltenghi et al. found a partial match (CodeGen +0.22 Spearman; next line 47% vs 42.3%) and models answered at 36-39% vs about 70% for developers (2022-era open models). Kou et al.: 27% of 211 wrong programs fit five attention patterns on the task text. Reasoning-tuned models find the same obfuscation tiers hard as humans; instruction- and coder-tuned models show near-zero alignment (c13, abstract only).
- **Confusion signal.** Perplexity spikes track EEG at the region level (rho 0.47 vs 0.05) but not at the snippet level.
- **Human response modelling.** Centaur predicts human comprehension answers slightly better than its base (NLL 1.63 vs 1.85, effect 0.172; 7 of 9 studies). Prior answers in context bias the base model more than the code (c05).

### 6.2 Agents reading repositories

- Agents spend about 29% of actions on reading (search 15% plus explore 14%; c17).
- File finding is not the bottleneck; fine-grained line recall is. File match 92-97% for successes vs 59-81% for failures. Function-level match in successes only 21-34% (c18). SWE-Explore line recall: Oracle 0.953, CoSIL 0.788, AutoCodeRover 0.233, Codex 0.194, OpenHands 0.179, Claude Code 0.154, BM25 0.021. Resolve rate Random 4.7%, Claude Code 48.0%, CoSIL 59.3%, Oracle 59.7% (c19). Ground truth is what earlier agents read, so alternative paths are missed.
- Code reasoning appears unguided in 66.95% of 7,955 trajectories; resolution 69.84% with vs 50.81% without. Correlational (d01).
- Failures run about twice as long (OpenHands Verified 98.62 vs 54.05 steps; RepairAgent 40 vs 22 iterations) and repeat actions more (13.6% vs 6.1%).
- Thought-action misalignment is rare (1.3-3.7%) but a single one can cause failure (c17).

### 6.3 What changed results, and by how much

| Change | Effect | Source |
|---|---|---|
| Fixed top-down pipeline instead of open agent | 32.00% at $0.70 on SWE-bench Lite; matches complex agents of its time | c20 |
| Skeleton instead of full file | 58.33% vs 53.67% | c20 |
| 100-line window | 18.0% vs 12.7% (full) vs 14.3% (30-line) | c22 |
| Summarised search | 18.0% vs 12.0% iterative | c22 |
| Stage-wise code reasoning | +6.29 to +10.53 points, +7.6% tokens | d02 |
| Certificates | 78.2% to 88.8%; +9 to +11 on code QA; 2.8x steps | d05 |
| Call hints | Func@5 +2.2; variance halved; +10% input tokens | d09 |
| Graph views | +20 to +46 of 731 | d11 |
| Preview-first loading | 10-15% fewer tokens, accuracy equal or slightly higher | d12 |
| Re-plan at first edit | +14.7 to +16.8 (weak executor) | d13 |
| CoT on output prediction with misleading comments | loss 23.2% to 13.8% | d06 |
| Tools for trace errors | 58% of computation errors fixed | b14 |

Caveats: most of these studies use different token budgets per arm; few are at equal tokens. Most numbers come from one benchmark, mostly SWE-bench or HumanEval-like, and contamination is mostly not discussed.

## 7. What our agent should take

Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested. "Part" is the schema part (G guardrail, S state, O operator, memory).

### Add now (established)

| # | Item | Part | Status | Evidence | Claim |
|---|---|---|---|---|---|
| A1 | Do not trust identifier names as proof of behaviour. Derive what code does from structure and checks; treat names as claims to verify. Comments: same rule, but anchoring is task-dependent, so only the name part is established. | G (extends G10) and S1 input hygiene | [E] names; [C] comments | c12, b13, a19, c15, d07; boundary d06, d08 | K07 |
| A2 | Do not rely on model-simulated execution for facts about behaviour. For values and traces, use real execution or tools. A plausible trace is not evidence. | S2, S4 (G2, G10) | [E] | c14, c15, b14, a24, d05 | K08 |
| A3 | Read coarse to fine. Skeleton or overview first, then only the relevant lines, in windows of about 100 lines rather than whole files. | S1/S2 | [E] skeleton and pipeline; [S] window size | c20, c21, c22, d09, d11, d12 | K09, K29 |
| A4 | Measure agent reading failure by fine localisation and run length, not file finding. A long run with repeats is a failure signal counted by code. | S6 impasse trigger | [E] | c17, c18, c19 | K11 |
| A5 | Keep text search as the base reading tool. Add structure (skeleton, who-calls-me links, graph views) as hints beside it, not instead of it. | S1 | [E] | d09, d10, d11, c21 | K29 |
| A6 | Use the von Mayrhauser-Vans primitives as slot types: state a hypothesis; seek a beacon; on failure label the reason (not found / ambiguous / unexplained); cap open hypotheses; switch model on unrecognised code. | S1 operators | [E] as description of human practice; effect on LLMs untested, so ship as logging labels first | d14, d15, a04, a05, a10 | K32 |
| A7 | Do not model the agent's reading on human attention, and do not triage by human complexity metrics. | none (negative) | [E] | a16, c06, a20, b09, b10 | K12, K13 |
| A8 | Treat human findings as provisional. Do not hard-code "experts read top-down" or an expert reading order as a rule. | none (negative) | [E] | b20, b21, b04, b03 | K16, K02 |

A2 overlaps SCHEMA G2 and G10 in spirit; the new content is the specific code-simulation evidence. A6 is established only as a description of what people do; the Add-now step is to use the labels, not to claim they raise accuracy. No item conflicts with section 4b.

### Test first (single-source, contested, or untested)

| # | Item | Part | Status | Evidence | Claim |
|---|---|---|---|---|---|
| T1 | Strategy-labelled reading prompt (bottom-up / top-down / as-needed) vs plain read-then-fix at equal tokens. | S1/S2 | [S] never tested | c27, d20 | K22, K01 |
| T2 | Stage-wise code reasoning (trace, simulate patch, audit against issue, predict inputs/outputs). | S1/S2, S4 | [S] | d01-d03 | K24 |
| T3 | Fill-in certificate for "does this code do X". | S1/S2 | [S] | d05 | K25 |
| T4 | Coverage ledger before edit (as-needed reading with a never-seen list). | S2 to S3 boundary | [S] design, no study | a08, a25, a12 | K01 |
| T5 | Breadth-first survey before dive vs depth-first. | S1 | [S] human only | a06, b01, d12 | K03, K30 |
| T6 | Code-first pass, then spec or comments as claims (anchor guard). | G / S1 | [C] | c01-c03, d06, d08 | K14, K27 |
| T7 | Two-pass reading: names masked, then unmasked. | S1 | [S] | d07, c12 | K28 |
| T8 | Simulate-only vs run-only vs simulate-then-run. | S2, S4 | [S] | d04, c16, c14 | K26, K06 |
| T9 | One plan-check at the first edit. | S2 to S3 | [S] | d13 | K31 |
| T10 | Token-level surprise as a "re-read here" flag. | S1 | [S]/[C] | d17, b12, b11 | K19, K33 |
| T11 | Task-type switch: narrow fix gets as-needed, feature or refactor gets broad coverage. | S0/S1 | [S] N=1 | a12 | K01 |
| T12 | State the reading goal before reading code (purpose shapes what is stored). | S1 | [S] human, second-hand | a13, a15 | K04 |
| T13 | Force a counter-example attempt before accepting a reading. | S4 | [S] human | c03, b18 | K14 |
| T14 | List confusing micro-patterns before tracing. | G | [E] for humans; LLM transfer untested | b07, b08, b12 | K18 |

Nothing in T1-T14 goes into SCHEMA.md until its test passes (see UNKNOWNS.md).

## 8. Concrete tests on our bench

All arms use equal tokens (G7), counting the setup cost of any scaffold. If an arm needs more tokens, give the control extra samples or a longer limit up to the same total. Log trajectory length and tool calls.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 strategy prompt | Repo bug-fix and code-QA items (SWE-bench Lite-like, 100+ items) | (a) plain read-then-fix; (b) top-down hypothesis prompt; (c) bottom-up chunking prompt; (d) as-needed with ledger | Resolve rate; line recall of localisation; tokens | Small, 0 to +4 points. Likely no label beats the others by much; finding that is still useful. |
| T2 stage-wise reasoning | Same | plain vs four-stage reasoning, same token cap | Resolve rate | +3 to +8 points if DeskCheck holds at equal tokens |
| T3 certificate | Patch equivalence and "does this do X" QA | free CoT vs certificate, same total tokens | Accuracy | +5 to +10 points; shrinks at equal steps |
| T5 breadth vs depth | Multi-module bug items with decoy hits | survey-all-then-dive vs dive-on-first-hit | Bugs found; tokens to first correct localisation | Breadth wins with decoys; ties otherwise |
| T6 anchor guard | Output prediction and review items with wrong-comment variants | normal read vs code-first then comment check | Accuracy on wrong-comment items; accuracy on right-comment items | Recovers part of the 13.8-23% drop; no loss on correct comments |
| T7 names masked first | Items where names mislead (function named the opposite of its behaviour) | single pass vs masked pass then unmasked pass | Accuracy on misleading items; cost on normal items | Gain on misleading names; cost about 1-9% on normal items |
| T8 simulate vs run | Localisation and output items in an executable environment | simulate-only; run-only; simulate-then-run | Method-level recall; accuracy | Run beats simulate on value-heavy items; simulate-then-run best |
| T9 first-edit check | Repo bug-fix | no check vs one check at first edit vs step-count trigger | Resolve rate; tokens | +2 to +5; cheaper than periodic review |
| T10 surprise flag | Atoms-of-confusion and clean snippets | no flag vs top-K token-surprise flag with forced execution | Accuracy; false-flag rate on clean code | Gain on confusing code; waste on clean code; judge the net |
| T4 coverage ledger | Large-repo items | plain vs never-seen dependency list before edit | Wrong-patch rate; tokens | Fewer wrong patches by a few points; about +5% tokens |
| T13 refute step | Assertion/postcondition judgment (Kaufman style) | accept-by-reading vs forced counterexample run | Catch rate on wrong items | Rises from the human-like 49% toward the model's own rate |
| T14 confusion list | Atoms-of-confusion output prediction | plain vs "list the confusing constructs first" | Error rate on atom snippets | Small |

Analysis rules: item-matched pairs; at least 100 items for repo tasks; report the equal-token accounting; run each arm at least twice. DeskCheck shows run noise is real: re-running baselines recovered only 16/97, 7/49 and 14/74 of the wins, so most of the gain was not noise, but some was.

## 9. What does not transfer, and why

- **Working-memory load story for bottom-up reading.** Humans pay in working memory when names are removed (fMRI, 17 participants, b05). An LLM has no such limit in the same form, though it pays in accuracy (c12). The symptom (names matter) is shared; the mechanism is not.
- **Expert skimming and reading order.** Eye-movement linearity (Busjahn, Peitek) is a property of human eyes and short snippets. Model attention is only weakly aligned (Li: at most 22% of methods). An order that works for humans is not shown to work for the agent.
- **"Novice bottom-up, expert top-down."** Not measured cleanly even for humans (5.3). Do not map "agent without domain knowledge" to "novice" as a design rule (c25 suggests it; no data).
- **Individual-differences findings** (fluid intelligence, personality). Not a scaffold lever (K17).
- **Atoms of confusion as an error-rate result.** Error rates were measured on novices or C professionals. The LLM overlap is a perplexity correlation with EEG, not an error-rate result.
- **Complexity metrics.** Weak even for humans, and AUROC 0.63 for LLM success.
- **Tools that need training or a human user** (EyeMulator fine-tuning, c23; ToM assistants). Outside our no-training scope.
- **Think-aloud strategy labels.** Kaufman's labels come from 10 participants judging assertions with a spec in hand. A repo agent has a different task.
- **The N=1 and N=4 field studies.** They describe how some people behave in some firms. They cannot give effect sizes.
- **Outcome mismatch.** Human studies score answers to questions; agent success is a passing patch.

## 10. Open questions

1. Does a named reading strategy in the prompt change agent outcomes at equal tokens? Nobody has tested it (K22).
2. Is Ko and Uttl's breadth-first advantage real, for humans in a larger sample or for agents? No replication.
3. Does Pennington's order hold for agents, and does it reverse in OO code?
4. Execution versus simulation on the same scaffold. DeskCheck beat a 28-test executor on localisation (0.66 vs 0.23), but the scaffolds differ in many ways.
5. Is a two-pass "names masked, then unmasked" read better than a single pass, and what does it cost on normal code?
6. Which reading unit is best at equal tokens: skeleton, 100-line window, or call graph? Needs one benchmark.
7. What triggers re-planning best: first edit (PAUSE), step count, repeats, or model uncertainty? Only the first has data; uncertainty triggers were seen in snippets (d19).
8. Do wrong comments anchor agents as they anchor humans, in repo tasks? Output prediction says yes (d06); security review says no (d08).
9. Does token-level surprise work as a re-read trigger, and what is the false-flag cost?
10. What do Brooks 1983, Letovsky 1986 and Littman 1986 actually report? Never opened.
11. Does stage-wise code reasoning (DeskCheck) reproduce outside its authors and at equal tokens?
12. Do comprehension gains show up as better patches or only as better explanations? AutoSD suggests the latter (repair equal; explanations helped humans).

## 11. Sources

[V] = opened and read this session (full text, or abstract page where the evidence line says so). [M] = snippet or secondary citation only.

**Classic models and human studies**
- [V] Ko and Uttl (2003) Individual differences in program comprehension strategies in unfamiliar programming systems. https://www.cs.kent.edu/~jmaletic/cs69995-PC/papers/Ko'03.pdf (a06, a07, b01)
- [V] Koenemann and Robertson (1991) Expert problem solving strategies for program comprehension. https://www.cs.kent.edu/~jmaletic/cs69995-PC/papers/koenemann-1991.pdf (a08, a09)
- [V] von Mayrhauser and Vans (1995) Program comprehension during software maintenance and evolution. https://www.cs.kent.edu/~jmaletic/cs69995-PC/papers/von_mayrhauser-1995.pdf (d14)
- [V] von Mayrhauser and Vans (1997) Program understanding behavior during debugging of large scale software. https://www.cs.kent.edu/~jmaletic/cs69995-PC/papers/von_mayrhauser97.pdf (a10)
- [V] Vans, von Mayrhauser and Somlo (1999) Program understanding behavior during corrective maintenance of large-scale software. https://www.cs.colostate.edu/~somlo/pubs/ijhcs99.pdf (a11, a25)
- [V] Singer and Lethbridge (1998) Just-in-time comprehension vs. the full-coverage strategy. https://www.site.uottawa.ca/~tcl/papers/WESS/WESS98SingerLethbridge.pdf (a12)
- [V] Burkhardt, Detienne and Wiedenbeck (2002) Object-oriented program comprehension. https://arxiv.org/pdf/cs/0612004 (a13)
- [V] Detienne, What model(s) for program understanding? https://arxiv.org/pdf/cs/0702004 (a14, a15; Pennington 1987a and Mills et al. 1995 second-hand)
- [V] Tiemens (1989) Cognitive models of program comprehension. https://sites.cc.gatech.edu/reverse/repository/cogmodels.pdf (d15; Letovsky, Brooks, Soloway second-hand)
- [V] Wyrich (2023) Source code comprehension: a contemporary definition and conceptual model. https://arxiv.org/pdf/2310.11301 (a01-a04; Brooks, Pennington, Letovsky, Littman, Gilmore, Koenemann second-hand)
- [V] Fekete and Porkolab (2020) A comprehensive review on software comprehension models. http://publikacio.uni-eszterhazy.hu/6320/1/103_111_Fekete.pdf (a05)
- [M] Brooks (1983) Towards a theory of the comprehension of computer programs. https://www.st.cs.uni-saarland.de/edu/empirical-se/2006/PDFs/brien03.pdf (d16, b25)
- [M] Letovsky (1986), Littman et al. (1986), Pennington (1987), Gilmore (1991): primary texts not opened; known via the secondary sources above.
- [V] Busjahn et al. (2015) Eye movements in code reading: relaxing the linear order. https://huang.isis.vanderbilt.edu/cs8395-f23/paper/linear-order-eye.pdf (b02)
- [V] Peitek, Siegmund and Apel (2020) What drives the reading order of programmers? https://www.se.cs.uni-saarland.de/publications/docs/PSA20.pdf (b03)
- [M] Peachock et al. (2017), via Peitek 2020 (b04)
- [V] Siegmund et al. (2014) Understanding understanding source code with fMRI. https://www.se.cs.uni-saarland.de/publications/docs/SKA+14.pdf (b05)
- [V] Wagner and Wyrich (2021) Code comprehension confounders. https://arxiv.org/pdf/2109.13546 (b06)
- [V] Langhout and Aniche (2021) Atoms of confusion in Java. https://arxiv.org/pdf/2103.05424 (b07)
- [M] Gopstein et al. (2017) Understanding misunderstandings in source code, via b07 (b08)
- [V] Lavazza, Morasca and Gatto (2023) Software understandability and code characteristics. https://link.springer.com/content/pdf/10.1007/s10664-023-10396-7.pdf (b09)
- [V] Lavazza et al. (2022) Cognitive Complexity as a predictor of understandability. https://osf.io/2mbwe/download (b10)
- [V] Wyrich, Bogner and Wagner (2023) 40 years of designing code comprehension experiments. https://arxiv.org/pdf/2206.11102 (b20)
- [V] Munoz Baron et al. (2023) Evidence profiles for validity threats. https://arxiv.org/pdf/2301.10563 (b21)
- [V] Feitelson (2021) Considerations and pitfalls in controlled experiments on code comprehension. https://arxiv.org/pdf/2103.08769 (b22)
- [V] Bexell et al. (2024) How do developers approach their first bug in an unfamiliar code base? https://www.ppig.org/files/2024-PPIG-35th-bexell.pdf (b23)
- [V] Lin and Robles (2023) registered report on vocabulary difficulty and naturalness. https://arxiv.org/pdf/2308.13429 (b26; protocol only)
- [M] Casalnuovo, Devanbu, Morgan (2020) Does language model surprisal measure code comprehension? https://cognitivesciencesociety.org/cogsci20/papers/0102/index.html (d18)

**LLM and agent studies**
- [V] Kaufman, Brun, Murali and Endres (2026) Programmers are poor and overconfident judges of LLM-generated assertions. https://arxiv.org/abs/2607.08885 (b18, c01-c03, c24)
- [V] Lehmen et al. (2026) Predicting program comprehension with foundation models of human cognition. https://arxiv.org/abs/2607.11372 (a22, c04, c05, c26)
- [V] Li et al. (2024) Do machines and humans focus on similar code? https://arxiv.org/abs/2402.14182 (a16, c06)
- [V] Kou et al. (2024) Do LLMs pay similar attention like human programmers when generating code? https://arxiv.org/pdf/2306.01220 (a17, b15)
- [V] Paltenghi et al. (2024) Follow-up attention. https://arxiv.org/abs/2210.05506 (a18, c07, c08)
- [V] Hooda et al. (2024) Do large code models understand programming concepts? https://arxiv.org/pdf/2402.05980 (a19)
- [V] Beyond Accuracy (2026) Characterizing code comprehension capabilities in LLMs. https://arxiv.org/html/2601.12951v1 (a20)
- [V] Richards and Wessel (2024) Theory of mind for an LLM-based code understanding assistant. https://arxiv.org/pdf/2408.04477 (a21, b17)
- [V] Qiao, Shihab and Hundhausen (2025) Systematic review of GenAI assistants for code comprehension. https://arxiv.org/abs/2510.17894 (a23, b19, c10, c11, c25)
- [M] CoCoNUT (ICSE LLM4Code 2025). https://conf.researchr.org/details/icse-2025/llm4code-2025-papers/19/CoCoNUT-Structural-Code-Understanding-does-not-fall-out-of-a-tree-Virtual-Talk- (a24)
- [V] Rong et al. (2026) Can perplexity serve as a cognitive signal for code understandability? https://arxiv.org/pdf/2608.00624 (b11)
- [V] Abdelsalam et al. (2025) How do humans and LLMs process confusing code? https://arxiv.org/abs/2508.18547 (b12, d17)
- [V] Haroon et al. (2026) Impact of code changes on LLM fault localizability. https://arxiv.org/pdf/2504.04372 (b13)
- [V] Abdollahi et al. (2025) Demystifying errors in LLM reasoning traces: code execution simulation. https://arxiv.org/pdf/2512.00215 (b14)
- [V] Tang et al. (2024) Developer behaviors for validating and repairing LLM-generated code. https://arxiv.org/pdf/2405.16081 (b16)
- [M] Chain of Understanding (2025). https://arxiv.org/abs/2504.04553 (b24)
- [V] Le et al. (2025) When names disappear. https://arxiv.org/abs/2510.03178 (c12)
- [V] Le, Nguyen, Nguyen (2026) Do machines struggle where humans do? (abstract page only). https://arxiv.org/abs/2606.31725 (c13)
- [V] Chen et al. (2025) Reasoning runtime behavior of a program with LLM (REval). https://arxiv.org/abs/2403.16437 (c14)
- [V] Liu, Chen and Jabbarvand (2025) Coherency and consistency of code execution reasoning. https://arxiv.org/abs/2510.15079 (c15)
- [V] Kang et al. (2023) Explainable automated debugging via LLM-driven scientific debugging (AutoSD). https://arxiv.org/abs/2304.02195 (c16)
- [V] Bouzenia and Pradel (2025) Understanding software engineering agents. https://arxiv.org/abs/2506.18824 (c17)
- [V] Majgaonkar et al. (2025) Understanding code agent behaviour. https://arxiv.org/abs/2511.00197 (c18)
- [V] Zhang et al. (2026) SWE-Explore. https://arxiv.org/abs/2606.07297 (c19)
- [V] Xia et al. (2024) Agentless. https://arxiv.org/abs/2407.01489 (c20)
- [V] Chen et al. (2025) LocAgent. https://arxiv.org/abs/2503.09089 (c21)
- [V] Yang et al. (2024) SWE-agent. https://arxiv.org/abs/2405.15793 (c22)
- [V] Zhang et al. (2025) EyeMulator (abstract page only). https://arxiv.org/abs/2508.16771 (c23)
- [V] Alebachew (2025) AI-guided exploration of large-scale codebases (no evaluation). https://arxiv.org/abs/2508.05799 (c09)
- [V] Liu et al. (2026) DeskCheck. https://arxiv.org/abs/2610.23782 (d01-d04)
- [V] Ugare and Chandra (2026) Agentic code reasoning. https://arxiv.org/abs/2603.01896 (d05)
- [V] Lam et al. (2025) CodeCrash. https://arxiv.org/abs/2504.14119 (d06, d07)
- [V] Thornton (2026) LLM code reviewers are harder to fool than you think. https://arxiv.org/abs/2602.16741 (d08)
- [V] Lin et al. (2026) How much static structure do code agents need? https://arxiv.org/abs/2606.26979 (d09, d10)
- [V] Zhang et al. (2026) DualView. https://arxiv.org/abs/2607.01929 (d11)
- [V] He and Roy (2026) SWE-Adept. https://arxiv.org/abs/2603.01327 (d12, d20)
- [V] Patel et al. (2026) PAUSE. https://arxiv.org/abs/2610.29870 (d13)
- [M] Uncertainty-aware self-correction for coding agents (ICLR 2026); Ask or Assume. https://arxiv.org/abs/2603.26233 (d19)

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 11 established claims: 6 confirmed as written, 5 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A20.03-K01** (reworded: the sources support less). Mixed top-down/bottom-up switching is supported (von Mayrhauser and Vans 1997/1999, N=4). But 'as-needed reading is the common pattern in large programs' rests on Koenemann and Robertson (12 programmers, a 636-line program), a single-engineer case study (Singer and Lethbridge, who also report a full-coverage strategy for development work), and a statement in von Mayrhauser and Vans; strategy depends on the goal. Corrected claim: Human code reading is mixed, goal-driven switching between top-down hypotheses and bottom-up chunking, not one fixed strategy; as-needed reading of only the relevant code is typical of maintenance work in larger programs (small lab studies and one longitudinal single-engineer case), while development tasks can call for fuller coverage.
- **A20.03-K08** (number corrected). Chen et al. (15 models, average accuracy 44.4%, IC 10.3) and Liu et al. (81.42% coherent, 46.92% of those correct output) verified, but 'best model fully traced 47% of tasks' appears in none of the opened sources (Chen, Liu, Abdollahi); GPT-4-Turbo, the best in Chen, has average 75.0 and IC 42.5. Corrected claim: LLM mental simulation of execution is unreliable: across 15 models the average accuracy is 44.4% with Incremental Consistency 10.3 (Chen et al.), and of the 81.42% of HumanEval simulations that are coherent only 46.92% give the right output (Liu et al., 16 LLMs).
- **A20.03-K11** (reworded: the sources support less). Majgaonkar et al. report the file-level match numbers (success 92-97%, failure 59-81%) but conclude that on SWE-bench Lite failures usually find the right file, whereas on Verified 35-40% of failed trajectories miss the file and file localisation is 'a bottleneck for a successful outcome'; so 'not file finding' holds only for Lite. SWE-Explore line recall (AutoCodeRover 0.233, Codex 0.194, Claude Code 0.154, Mini-SWE-Agent 0.151 vs oracle 0.953) verified; CoSIL scores 0.788. Corrected claim: Agent failure on SWE-bench Lite is mostly fine-grained localisation and long trajectories rather than file finding (file-level match 92-97% for successes vs 59-81% for failures, with failures matching the file 79.8-81.4% on Lite), but on SWE-bench Verified file-level localisation is itself a bottleneck (failures match the gold file only 59-63% of the time); in SWE-Explore, agent line recall is 0.15-0.23 against an oracle 0.95.
- **A20.03-K12** (reworded: the sources support less). Li et al. (at most 22% of 68 methods significant; 85% between two models; negative results on summary quality) verified. But Paltenghi et al. report 47% vs 42.3% as a positive result (follow-up attention has the highest model-human agreement and beats the baseline), not as evidence that alignment is weak. Corrected claim: Human-model attention alignment on code is weak in code summarization: at most 22% of methods show a significant human-model rank correlation (vs 85% between two models), and alignment does not predict summary quality; attention-derived follow-up predictions of a developer's next line reach 47% accuracy vs 42.3% for a history baseline, a modest but positive result.
- **A20.03-K32** (reworded: the sources support less). von Mayrhauser and Vans (1995) verified: hypotheses fail for three reasons and the key is to keep open hypotheses manageable. But in Tiemens (1989) the why/how/data-description classes are the question types answered by Letovsky's CPU program, not Letovsky's general question taxonomy (which also has other types), and Tiemens is a secondary technical report. Corrected claim: Von Mayrhauser and Vans name three reasons a hypothesis fails (no verifying code found; one code satisfies several hypotheses; code cannot be explained) and say to keep open hypotheses manageable; Tiemens' summary of Letovsky's CPU program lists three question classes it answers: why, how, and data description.
- **A20.03-K21** (now single-source: only one opened source, code check).
