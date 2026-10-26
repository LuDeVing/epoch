# Problem finding: deep document

*Subfield A10.08, psychology of creativity and expertise. Evidence: evidence_a to evidence_d.jsonl (ids a01 to d19), claims.jsonl (K01 to K37), critique.md. Schema parts refer to `research_notes/single_agent/SCHEMA.md` v0.2 (G1-G12, S0-S9, O1-O8, section 4b). Overlap with other subfields in this run (problem-solution co-evolution, question wording and presupposition, value of information, exploration and spontaneous experiments, novelty and atypicality, generation versus evaluation) is noted as links only.*

**Reading warning.** The human evidence for this subfield is thinner than its fame suggests. The founding book (Getzels and Csikszentmihalyi, 1976) and the 1971 paper were never opened by us. Every number about them is second-hand, and the second-hand sources disagree. The only meta-analysis is one 2016 dissertation. No LLM study runs the classic paradigm. Most LLM evidence is about neighbours: asking questions, spotting missing premises, rewriting questions, reframing with human users.

---

## 1. What it is

Problem finding is the part of creative work that happens before and during solving. The person decides what the problem is. They pick it, shape it, restate it, or notice that there is one. It is contrasted with problem solving, where the problem is handed over.

Getzels' split (a08):

- **Presented problem.** The formulation, the method and the solution are all known to someone.
- **Discovered problem.** None of the three is known. The person has to find all of it.
- Getzels (1982) lists 10 situations that vary which of the three are given.

Names are a mess. At least 13 labels are used across about 199 works (a19): problem finding 50.3%, problem posing 12.1%, problem construction 9.5%, problem formulation 9.1%, ill-defined problems 4%, problem generation 3.1%. Different fields pick their own label. The meta-analysis found the label did not change results (a19), so the literatures can be pooled.

How it is measured, in practice:

1. **Behaviour before commitment.** How many objects handled, how unusual the choice, how long the problem stays open (a01).
2. **Problem generation tests.** The person writes problems; scored for fluency, flexibility, originality. The Problem Generation test is reliable (alpha .816, k=43, N=2,029) with convergent validity r=.463 (k=125, N=2,573) (b11).
3. **Real-world tasks.** The person defines a problem from a messy situation (a11, b06).
4. **Restating a given problem in several ways** ("problem construction") (a22, b13).

For our agent, four different things hide under the name. Keep them apart:

| Sense | What the agent would do | Schema slot |
|---|---|---|
| A. Explore before committing | spend effort on many framings and objects before fixing one | open mode (S3), S1 |
| B. Restate or reframe a given problem | write the task in other terms, then solve | S1, O8, O6 |
| C. Notice what is missing or unsolvable | detect an underspecified or impossible task, ask or stop | S1 |
| D. Choose which question to ask | pick the question that splits the hypotheses best | S1, memory |

The human literature is mostly about A. The LLM literature is mostly about B and C. D is a separate line (active questioning) with strong scaffold results.

---

## 2. History and theories in depth

### 2.1 The founding study (1960s to 1976)

Getzels and Csikszentmihalyi began a project at the Art Institute of Chicago in 1963 (a06). Fine-art students composed and drew a still life under lab conditions. Reported design details, from secondary sources only:

- About 31 students, 27 objects on a table, roughly one hour each (b01, a27). The sample size and object count come from web summaries; the thesis summary does not give them (a01).
- Problem finding was coded at two stages (a01). Formulation stage: number of objects handled, interaction with them, uniqueness of the objects chosen, how they were arranged. Solution stage: how long the problem stayed open, exploration while drawing (switching medium, sketches), changes between the first arrangement and the final work. Drawings were photographed every 6 minutes. Students were interviewed afterwards.
- Five well-known artists and critics rated each drawing for craftsmanship, originality (regardless of craft) and overall aesthetic value (a04).

Findings, as reported second-hand:

- Both stages of problem finding correlated positively with rated creativity and originality. Students who kept the problem open and explored made work judged more original (a02).
- Concern for discovery at the formulation stage vs originality: r = .54, p < .01 (a04, d03; Abdulla, citing the 1971 paper).
- Grand total of process variables vs judged originality: r = .65, N = 31 (d02; via Moore 1985). Unusualness score vs originality: r = .42 (d02).
- Interviews: high scorers described the work as something that unfolded and changed meaning as they drew (a02; the book p.95 is quoted).

The three coefficients disagree about which pair they describe. Status: contested (K28). Safe summary: moderate positive, about .4 to .65, with N around 31.

The long-term follow-up is the famous claim: problem finders were more likely to stay working as artists and were judged more successful, and intelligence did not predict studio performance or later success (a27, b02). Secondary sources give the follow-up as 5, 6, 7, 11 or 18 years, and 27 of 31 or all 31 located. We never saw the primary text. Freeman (1994) says discovery-oriented artists produced work experts judged better and got early recognition, but also that problem finding was not the whole story: other traits such as being gregarious mattered (b03). **Do not cite exact follow-up numbers** (K24).

One more fact from the thesis: a study of secondary school students (Oostwoud Wijdenes, 1983) found some students do not engage in problem finding at all (a03).

### 2.2 Theory models

| Model | Idea | Source |
|---|---|---|
| Presented vs discovered (Getzels 1975, 1982) | problems differ by what is known: formulation, method, solution | a08 |
| Recognition, discovery, invention (Dillon 1982, 1988) | three levels of finding a problem or a solution | a09 |
| Arlin (1975, 1977) | needs a problematic situation, a chance to raise questions in it, and a post-formal mind; predicted adults beat children | a09 |
| Problem construction (Mumford, Reiter-Palmon, Redmond 1994) | built from stored problem representations; mostly automatic; people do not know they are defining a problem; instructions can make it active | a24 |
| Csikszentmihalyi and Getzels (1988) | metacognitive, mixes affect and motivation with logic; may be unconscious and knowledge-dependent | a25 |
| Creative Problem Finding Hierarchy (Abdulla and Cramond 2018) | five levels: discovery, formulation, construction, identification, definition; two dimensions (how ill-defined, how much ideation vs evaluation) | a20, a26 |
| Empathy proposal (Wakefield 1991) | artists find problems by empathy with themselves; problems start as conflicting feelings. Evidence preliminary | a07 |
| DISCOVER model (Maker et al. 2006) | reuses the problem/method/solution continuum | a08 |

Arlin's age prediction was tested by the meta-analysis. The result went against it (children .297, adults .207), but the pattern is noise-prone (section 5.3).

### 2.3 The measurement tradition

Divergent thinking (DT) and problem finding were thought related, then found to be different:

- Runco and Okuda (1988): N=29 adolescents did three DT tests, each with presented problems and one self-discovered problem. Discovered problems drew significantly more ideas. Presented vs discovered r = .32. The authors call problem finding "by definition statistically independent" of solving (a10).
- Okuda, Runco and Berger (1991): N=77 elementary students, four tasks, criterion a checklist of creative activities. A real-world problem-finding task predicted creative accomplishments better than DT tasks, and added significantly in hierarchical regression (a11, b06). Coefficients not seen.
- Wakefield (1985): N=23 fifth graders; blank cards let children draw their own pattern and respond to it. Reliability of the creative performance score .82. DT vs WISC-R vocabulary r = .45 (a12).
- Hoover (1994): N=40 gifted fifth graders; scientific problem finding related more to flexibility (r = .41) than to fluency (r = .34) (a13).

### 2.4 Problem construction (Reiter-Palmon line)

Reiter-Palmon, Mumford, O'Connor Boes and Runco (1997): N=195 undergraduates, 6 real-life problems. Problem construction ability predicted solution quality and originality. Instructions could make construction more active. Cue consistency moderated it: high-ability people did best when the problem's cues were inconsistent; with consistent cues there is little to reconcile (a22, b07, b26). Effect sizes were not on the page we read.

### 2.5 The AI line

- Early: Lenat's AM (1976) and Eurisko (1983) proposed concepts and conjectures under interestingness heuristics. A later critique (Ritchie 1991) says they were hard to replicate or extend (c21).
- 2023 on: LLM work on questions and reframing. Rephrase and Respond (b22), step-back (b20), analogy prompts for design (c15), MacGyver (a32), QuestBench (a30), then missing-premise studies (c08), clarification benchmarks (d10, d11), research-question generation (a28, a29), and the large reframing test (b14). Details in section 6.

---

## 3. Core findings with exact numbers

Status: **established** = two or more independent sources agree; **single-source**; **contested**.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Exploring objects and keeping the problem open goes with rated originality of the drawing | r = .54 (concern for discovery vs originality, 1971 paper, via Abdulla); r = .65 N=31 total process; r = .42 unusualness (via Moore) | a02, a04, d02, d03 | single-source, coefficients contested (K01, K28) |
| Conceptual replications point the same way | Moore 1985: N=16 writers, formulation total 16.3 vs 3.0; process total vs originality r = .58; judge groups agree r = .92. van de Kamp 2021: 11 students, 196 portfolio events, 31% of event-level originality variance explained by 3 exploration types | d01, b04 | established (K02, K27) but tiny samples |
| Originality varies mostly inside a person | variance partition 0.89 at event level; student level not significant | b04, b05 | single-source (K03) |
| Problem finding relates modestly to creativity overall | random-effects r = .22 (CI .11 to .32); fixed .39; k=40, N=6,649, 196 effects; I2 = 98.74%; Q(195) = 15,480.27 | a16 | established (K04), one dissertation |
| One outlier and small-study bias inflate it | Frederiksen and Ward r = .99, N=2,636; removal gives .220 to .196; Egger t = 5.52, p < .001 | a17 | single-source |
| Moderators in the meta-analysis | age Q(2)=6.60: children .297, adolescents .113, adults .207; DT index Q(3)=10.95: fluency .314, originality .291, flexibility .149; domain Q(4)=18.44. Gender and measure type not significant | a18, d04 | single-source; fluency CI (-.084 to .625) includes zero |
| Problem finding is not divergent thinking | verbal flexibility vs PF r = .71 to .76 (N=90 sixth graders); verbal fluency .68 to .71; verbal originality .55 to .61; figural .14 to .31. Earlier studies: Arlin fluency r = -.18, flexibility .26; Artley verbal fluency .47; Lee and Cho -.17; Ambrosio quantity .41, quality -.08; Getzels and Smilansky verbal originality .23, flexibility .18, fluency ns | a21, b09, a14, a15, b10 | established (K05) |
| Problem generation test is reliable and moderately valid | alpha .816 (k=43, N=2,029); convergent r = .463 (k=125, N=2,573) | b11 | single-source (preprint) |
| Discovered problems draw more ideas than presented ones | N=29; presented vs discovered r = .32 | a10 | single-source |
| Real-world PF task beat DT tasks for creative accomplishment | N=77 children | a11, b06 | single-source (K06) |
| Problem construction predicts solution originality, only when cues conflict | N=195, 6 problems | a22, b07 | single-source (K07) |
| Telling teams to restate the problem first: no real gain | 65 teams (46 construction, 19 control); originality F(1,63)=2.06, reported p=.078 (two-tailed would be about .16), eta2 = .03; quality F=0.27, p=.30; less conflict, more satisfaction | a23, b08 | single-source (K08); treat as null on outcome |
| Reframing amplifies originality and harm | N=155; originality beta = .41; harmfulness beta = .29 | b13 | single-source (K09) |
| LLM did not help people reframe | N=280 (456 recruited), 4 conditions, 3 design problems, 15 expert raters; all p > .05 on novelty and usefulness | b14, c01 | single-source (K10) |
| LLM widened the skill gap | experts 12.54% more novel frames than novices with LLM (p=.01); free-form gap 20.84% (p=.06, not significant); structured: experts +15.69% agency (p=.02) | b15, c02 | single-source |
| Structured Dorst prompt picked as interesting | 29/189 vs 17/189 direct vs 17/189 all-content; top-3 picks 11 of 21 vs 7 vs 3; N=7 students | b16, c03 | single-source (K11) |
| LLM research ideas rated more novel than expert ideas | per idea 4.86 human, 5.62 AI, 5.78 AI reranked (49 ideas per arm); per review 4.84, 5.64, 5.81 (109 reviews each); 79 reviewers | b18, c11 | established (K13) |
| LLM idea generation saturates | of 4,000 seed ideas per topic about 200 non-duplicate (about 5%, cosine > 0.8); best LLM judge 53.3% accuracy | b19, c12 | established |
| LLM judges overrate generated research questions | 1,434 questions from 746 papers; experts gave the author question wins of 78% and 56%; LLM judges gave the model's best-of-five 82% | a28 | single-source (K12) |
| LLM judge vs humans on creativity | Kendall tau .31 elaboration, .23 creativity, .17 novelty, about 0 surprise; automatic metrics at or below .29 | d13 | single-source (K34) |
| Models rarely flag missing information | QuestBench "not sure" 1.4%, 4.6%, 0.7% on Planning-Q vs 41.8% truly underspecified; question choice over 80% on math, 40 to 50% or lower on logic and planning | a30, a31, c06, c07 | single-source (K14) |
| Models can label ambiguity but do not ask | answer rate above 95% across 10 models; Claude family asked up to about 5% | b17 | established with MacGyver, MiP (K15) |
| GPT-4 proposes solutions to unsolvable problems | 1,683 problems, 22% unsolvable; GPT-4 18.9% efficient, 37.5% infeasible on solvable ones; humans 79.3% (majority) vs GPT-4 73.3% | a32, c04 | established with b17, c08 |
| Reasoning models overthink missing-premise items | more tokens, rarely abstain; o1 an exception; early suspicion, no commit | c08, c09 | direction confirmed; the "2x to 4x" token figure was not found in the text |
| Separate detector for missing information beats a single prompt | SWE-bench Verified, hidden info, Sonnet 4.5: 54.8% hidden, 61.2% single prompt, 69.4% separate detector, 70.4% prompted interactive (detector vs interactive p=.621; vs single p<.001) | a33 | single-source (K16) |
| Non-code ask-or-answer structure beats plain prompting | ClarifyAgent 88.0 vs 57.9 (Qwen-2.5-7B), 88.4 vs 71.2 (Llama-3.1-8B) | d10 | single-source (K29) |
| Hidden requirements cost code accuracy | 7.8 to 19.8 pass@1 points; best model key-question rate 0.30 | d11 | single-source |
| A missing-info check in the main prompt costs success | average 28.6 to 27.8 to 27.0 over five benchmarks and five backbones; REAL 32.1 to 19.2; ALFWorld 57.5 to 58.9 | d09 | single-source, single-author preprint (K30) |
| Early stop on suspicion words is cheap and accurate | 47 to 75% of ill-posed items stopped; 1 to 6% false stops; 38 to 70% tokens saved on ill-posed items | d05 | single-source (K31) |
| Information-gain scoring of questions beats model-only questioning | Battleship targeting F1 0.367 to 0.764 (Llama-4-Scout), 0.450 to 0.782 (GPT-4o); EIG human mean 1.27 bits, k=1 LLM 0.65, k=5 matches human average; open spaces: sample candidate solutions and split them | c13, d07, d08 | established (K17), shrinks for stronger models |
| Identify-then-verify beats one-shot sufficiency judgement | explanation alignment 4.02 vs 3.89 of 5; FaithEval gain over 15% | c18 | single-source (K18) |
| Step-back helps knowledge tasks, not arithmetic | PaLM-2L MMLU Physics 66.4 to 73.2, Chemistry 70.9 to 81.8, TimeQA 41.5 to 68.7; GSM8K 84.3 vs 84; Physics fixed 20.5%, broke 11.9% | b20, b21 | single-source (K19) |
| Rephrase-and-respond | GPT-4 average over ten tasks 64.95 to 89.77; CSQA 84.09 to 85.45; Vicuna own rewrites vs GPT-4 rewrites: Sports 65.00 vs 73.64 | b22, b23, c10 | single-source (K20) |
| Rewording helps when the surface form is the obstacle | up to 15.5% accuracy (Granite, MultiArith); no resample control | d17 | single-source (K35) |
| Explore-first prompt gives more distinct high-utility tasks | 12 vs 8 at K=50 (Vendi); 96.67% of 20 blind novelty pairs; 3 experts; Qwen3-235B | d12 | single-source (K33) |
| MacGyver scaffolds | self-reflection: infeasible answers down 9.7%; divergent-then-convergent: efficient answers up 6.5%; 180 problems | c05 | single-source (K21) |
| GPT-3 analogy prompts for design | median helpfulness 4/5; about 80% changed the problem statement; up to 25% potentially harmful; one example beat zero or three | c15 | single-source (K22) |
| No LLM version of the Getzels paradigm exists | multiple searches (web, arXiv, Semantic Scholar, OpenAlex), tools limited | a35, d19 | established as absence, not proof |

---

## 4. Mechanisms and models

Written so an engineer can implement them. Nothing here is validated for LLM agents unless marked.

### 4.1 Two-stage problem finding (formulation, then solution)

Source model: Getzels and Csikszentmihalyi (a01).

Human mechanism: the person does not fix the problem at the start. During formulation they sample the material (objects). During solution they keep the problem open and let the work change it. Originality comes from this drift.

Implementation sketch (open mode only):

```
phase F (formulate):
  draws = N isolated attempts at stating the task in different terms   # fresh contexts (S3 rule)
  features = code extracts: count of distinct frames, rarity vs history, mid-task changes of frame
  commit = code picks the frame(s) by a non-same-family check or a downstream test (G8), not the generator
phase S (solve):
  solve under chosen frame; log whether the frame changed from F to final output
```

Log per run (matches SCHEMA section 6): frames tried, distinct frames after dedupe, time (tokens) before first commit, number of frame changes after commit, final-vs-first frame distance. These are the machine analogues of the 1976 scoring recipe (d02).

### 4.2 Problem construction with cue conflict

Source: Mumford and Reiter-Palmon (a24, a22). Model: construction is mostly automatic; active construction helps when the problem has inconsistent cues.

Implementation: a cheap code check for conflict in the prompt (two constraints that pull apart, a stated goal that disagrees with the examples, a requirement that cannot all be met). Fire reframing only on conflict or on a failed check (G1). With consistent cues, skip. Status: single human study; the gate is a hypothesis (U-test in UNKNOWNS).

### 4.3 Missing-information detection as a separate step

Source: Edwards and Schuster (a33), ClarifyMT (d10), uncertainty decomposition (d09).

Mechanism: a detector call sees only the task and asks "what must be known that is not stated?" It returns a list. Code decides: empty list, proceed; non-empty, ask a question, or (no user available) state assumptions explicitly and branch.

Why separate: a check carried in the main prompt shares the reasoning budget and cost 1.6 points on average and up to 13 on hard tasks (d09); the separate detector reached the interactive ceiling (a33). Use a trigger, not a standing step, if tokens are tight (d05 keyword stop: 1 to 6% false stops).

Identify-then-verify variant (c18): list candidate missing facts, then verify each against the text. Small gain.

### 4.4 Early suspicion monitor

Source: MiP (c08, c09), statistical early stopping (d05).

Mechanism: reasoning models notice a missing premise early but keep going. A program watches the trace for uncertainty keywords ("missing", "cannot determine"), with a threshold calibrated on well-posed items to a target false-stop rate (5% nominal). On trigger, stop thinking and either ask one question or answer "underspecified". Missing in the literature: what the conversion to a question does to final answer quality.

### 4.5 Information-gain question selection

Source: Grand et al. (c13, d08), Kobalczyk et al. (d07).

When the hypothesis space can be listed (board positions, a bounded set of designs), compute expected information gain exactly: for each candidate question, run it over every hypothesis, partition them by answer, score by entropy of the partition. Pick the highest.

When the space cannot be listed: sample M of the model's own candidate solutions (d07 uses a few samples and M=5 candidate questions), score each question by how evenly it splits the sample, ask the best. The gain shrinks for stronger models and costs extra calls (K32).

### 4.6 Reframe operator (O8) with equivalence and harm checks

Sources: step-back (b20), Rephrase and Respond (b22), syntactic blind spots (d17), Linnell and Reiter-Palmon (b13).

Mechanism: a reframe slot returns a restated problem. Code runs:

1. Equivalence check: does the reframed problem keep the same answer set on test inputs? Logically nontrivial rewrites cut consistency (contrapositive 72.4% in a search summary, d18, not opened).
2. Constraint check: all original constraints still present (reframing raises harmful ideas, b13).
3. Selection: pick among frames by downstream test, not by a model's taste (G8).

Gate on: low confidence, weak model, varied or awkward phrasing, knowledge-heavy task. Do not apply on clean arithmetic (b21: GSM8K flat) or clean multiple choice (b23: CSQA +1.4).

### 4.7 Diverge then converge (explore-first)

Source: CreativeDC (d12). Stage 1: brainstorm unusual elements of the theme without the task constraints. Stage 2: choose one idea and build a valid task. The program counts distinct outputs (Vendi) and gates them on a quality check (d14). One model, one domain, tokens not matched.

---

## 5. What holds up

### 5.1 Replications

- **Direct replication of the still-life experiment: none found** (b25, K23). No failed direct replication either.
- **Conceptual replications**, all positive in direction, all tiny: Moore 1982/1985 writers (N=8 vs 8, then N=16) (a05, d01); van de Kamp 2021 (11 students) (b04); Okuda 1991 (N=77, no coefficients seen) (a11). These agree with each other, so "more exploration goes with more original products" has two independent lines (K02 established). The direct evidence on its size is weak.
- **Meta-analysis**: r = .22 with I2 = 98.7% (a16). "Modest, very heterogeneous" is the honest reading. After one outlier is removed, .196 (a17). Egger test significant, so small-study effects are likely. Fail-safe N 6,414 does not fix that.

### 5.2 Failures and nulls

- The restate-first instruction for teams: no quality gain, originality p reported .078 on what looks like a one-tailed test (b08). Treat as null.
- GPT-4o reframing aid: no gain in any mode (b14).
- Problem finding vs divergent thinking: links negative for quality in several studies (a15, b10). Fluency is not a good proxy (CI includes zero, a18).
- Step-back on GSM8K: no gain (b21).
- A check carried inside the main prompt: lowered success (d09).
- Structured agent hurt where the user had already supplied the detail (Qwen precise-user accuracy 96.6 to 85.3) (d10).

### 5.3 Moderators and boundary conditions

| Moderator | Direction | Strength of evidence |
|---|---|---|
| Cue consistency | benefit only when cues conflict | one human study (a22) |
| Domain | domain Q(4)=18.44, writing among the larger values | meta-analysis (a18) |
| DT index | originality (.291) and flexibility (.149) clearly positive; fluency (.314) CI includes zero | meta-analysis, corrected in critique |
| Age | children .297, adolescents .113, adults .207; but cell sizes 47, 26, 123 effects, nested, confounded with domain | treat as noise (d04, K36) |
| Verbal vs figural | verbal DT tracks PF far more than figural | N=90 (a21) |
| Task type for reframing | positive on knowledge tasks, null on arithmetic | b20, b21 |
| Surface-form obstacle | rewording helps when phrasing is the problem; weak models gain more | d17 |
| User expertise (LLM help) | experts gain, novices do not | b15 |
| Model strength | RaR: stronger models gain more; question-selection scaffolds: gain shrinks for stronger models | b23, d07 |

### 5.4 Interventions that worked and did not (human)

Worked or probably worked: giving people a real-world problem-finding task as a predictor (a11); active construction under inconsistent cues (a22). Did not clearly work: telling teams to restate the problem (b08). Training of problem finding as an intervention was not found in our sources.

### 5.5 Competing explanations

- **Selection**: problem finders may simply be more motivated or gregarious; Freeman notes other traits mattered (b03).
- **Measurement overlap**: if raters see the drawing process, exploration and originality ratings can bleed together. We could not check the original rating blinding.
- **Heterogeneity**: I2 near 99% means "r = .22" is an average of very different things.
- **Task familiarity**: the sample was art students on an art task; transfer to reasoning tasks is untested.

### 5.6 Source quality warning

Core human evidence rests on: one dissertation meta-analysis; secondary descriptions of a 1976 study; samples of 11 to 77 in the replications. Several LLM items are preprints (a28, a29, a33, b17, c19, c20, d09). Items not opened or snippet only: a27, b01, b02, c19, c22, d16, d18.

---

## 6. Language models

No study runs the Getzels paradigm on an LLM (a35, d19). What exists falls into five groups.

### 6.1 Reframing help for people

Shin et al. 2025 (b14, c01): GPT-4o as a reframing aid, N=280, no gain in novelty or usefulness in any of direct, free-form chat or structured (Dorst nine steps) modes. Experts did better with the LLM (+12.54% novel frames, p=.01), novices did not, and novices felt less agency. The title says it: "No evidence for LLMs being useful in problem reframing". Limits: one model, crowd workers, 3 problems, about 23 minutes, "submit the 2 best frames" may favour filtering.

Sood et al. 2026 (b16, c03): N=7; the Dorst-frame prompt was picked as interesting more often (29 vs 17 vs 17 of 189). Different outcome (interest, not rated novelty), tiny N, tastes differed. Does not contradict b14.

Ding et al. 2023 (c15): GPT-3 analogy prompts for design problems; about 80% led to a visible change in the problem statement; up to 25% potentially harmful; one example beat zero or three. Ratings only, no outcome test.

### 6.2 Rewriting the question before answering

- Rephrase and Respond (b22, b23, c10): GPT-4 zero-shot average 64.95 to 89.77 over ten tasks; Last Letter (2 words) 52.05 to 99.09; Last Letter (4 words) 21.36 to 86.82; Dates 69.92 to 75.88; CSQA 84.09 to 85.45. Stronger models gain more. A stronger model's rewrite helps a weaker one (Vicuna Sports 65.00 to 73.64; Last Letter 5.45 to 10.45). Gains are big where the question is oddly worded and tiny where it is clean. No equal-token control against best-of-2 was found.
- Step-back (b20, b21): PaLM-2L MMLU Physics 66.4 to 73.2; Chemistry 70.9 to 81.8; TimeQA 41.5 to 68.7 with retrieval; MuSiQue 35.5 to 42.6; GPT-4 Physics 69.4 to 84.5. GSM8K 84.3 vs 84 (no gain). Physics: fixed 20.5% of baseline errors but broke 11.9% newly; over 90% of remaining errors are in the reasoning, not the abstraction.
- Syntactic blind spots (d17): five open models, four math datasets; rewording failed questions recovered answers (2 to 210 per model-dataset pair) and accuracy up to 15.5% (Granite, MultiArith); weaker models gain most. No resample control, so part of this is luck on a second try.
- Logical rewrites: summary-level only (d18): surface rewrites keep consistency at 94 to 100%, logical ones such as contrapositive fall (72.4%). Not opened.

Take: reframing is a surface-form repair tool. It does not add a new problem. It helps when the first wording is what hurts.

### 6.3 Noticing that something is missing

- QuestBench (a30, a31, c06, c07): models above 80% on picking the right question in GSM-Q and GSME-Q, 40 to 50% or lower on Logic-Q and Planning-Q. When "not sure" was allowed, rates were 1.4% (Gemini Flash Thinking), 4.6% (Claude 3.5 Sonnet), 0.7% (GPT-4o) on Planning-Q, where 41.8% were truly underspecified. Gains over a random baseline at most 5% on Planning-Q.
- Su et al. 2026 (b17): 10 models; answer rate typically above 95%; 80 to 95% of responses were pure answers; extra retrieved context made them ask even less.
- MacGyver (a32, c04, c25): 1,683 problems, 22% unsolvable. GPT-4 often proposes solutions to unsolvable problems. Error types on solvable ones: wrong tool use 42.4%, not achieving the goal 17.7%, unnecessary or wrong steps 16.9%, unavailable tools 9.5%. Humans were all-or-nothing, GPT-4 sat in the middle.
- Missing Premise (c08, c09): reasoning models use far more tokens on ill-posed items and rarely abstain; many suspect early but do not commit; non-reasoning models answer shorter and spot the problem faster; o1 was an exception. (The token multiplier stayed unverified.)
- Clarification benchmarks (d10, d11): models answer too early and decline over turns; hidden requirements cost 7.8 to 19.8 pass@1 points in code; best model finds the key question 30% of the time.

### 6.4 What changed it

| Intervention | Result | Source |
|---|---|---|
| Separate detector step (code) | 54.8 to 69.4 resolve rate | a33 |
| Structured ask-or-answer agent (non-code) | 57.9 to 88.0; 71.2 to 88.4 | d10 |
| Identify-then-verify sufficiency | small (4.02 vs 3.89) | c18 |
| Keyword early stop | 38 to 70% tokens saved on ill-posed items | d05 |
| Same-prompt check | lower success | d09 |
| Program-side EIG question choice | F1 0.367 to 0.764 (Battleship) | c13 |
| Sample-then-split questions (open space) | beat model-only; gain shrinks for strong models | d07 |
| Self-reflection / div-conv on MacGyver | -9.7% infeasible / +6.5% efficient (GPT-4) | c05 |

### 6.5 Idea and question generation quality

- Si et al. (b18, b19, c11, c12): blind reviewers rated LLM research ideas more novel (5.62 vs 4.86 per idea, p=.03) and slightly less feasible (6.34 vs 6.61 per review). Generation saturates: about 5% of 4,000 seeds survive deduplication. LLM judges ranked ideas near chance (53.3%).
- Sinhahajari et al. 2026 (a28): LLM judges rate model-written research questions as more novel than the authors' own (novelty mirage); experts disagreed with the judges.
- AInstein (a29, b24): models solved over 70% of given research problems but rediscovered the published method under 19% of the time; they fail where the solution needs cross-domain analogy. Blind study of 20 researchers: LLM solutions preferred on solving 73.5% of decided pairs.
- Nova (a34): planning prompts that mine anomalies raised unique novel ideas 3.4 times. Thin.
- CreativeDC (d12): explore-first gave 12 vs 8 distinct high-utility tasks; 96.67% of 20 blind pairs.
- Judges: even a different-family judge (Llama-3.3-70B) had tau .17 on novelty and about 0 on surprise against humans (d13).
- Systems that mine problems: tree of problem-solution (c17), research-question certificate (c19, preliminary: 4.86 vs 4.38 by LLM rescore, single repeat), position paper on vocabulary growth (c20). All weak evidence.

### 6.6 Safety side of reframing

Benign-reframing harm rate in agents: not measured (K37). Nearest: verse rewrite lifted attack success from 8.08% to 43.07% on 1,200 prompts, 25 models (d15); tool-call framing cut refusals 10.9 to 40.2 points (d16, abstract only). Human data: reframing amplified harmful ideas (beta .29, b13). Treat O8 as a possible risk until measured.

---

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory. Status marks match SCHEMA.md: [E] established, [S] single-source, [C] contested.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| 1 | Do not expect a big lift from a "problem finding" step. Use r about .2, heterogeneity high, as the prior. Keep O8 at [S]. | O8 | [E] | a16, a17, b14, K04 |
| 2 | Score reframes on flexibility (distinct frames) and downstream success, not on count of ideas. | eval / logging | [E] | a18, a21, b09, K05 |
| 3 | Dedupe generated frames or ideas before counting. Track unique frames per token. About 5% of bulk ideas survive. | S3 open mode, logging | [E] | b19, c12, K13 |
| 4 | Never let the generating model pick the best frame or idea; never use a same-model judge for novelty. Judges are near chance and show a novelty mirage. | G8, G5 | [E] | a28, b19, d13 |
| 5 | Models do not ask or abstain on their own, even when they can label ambiguity. If we want S1 to catch missing information, code must force the step; it will not happen by default. | S1 | [E] | b17, a32, c04, c08, c09, a31 |
| 6 | When the hypothesis space is enumerable, choose clarifying questions by program-side expected information gain. | S1 / S7 | [E] | c13, d08, d07 |
| 7 | Treat reframing as a repair for awkward surface form, not a default. Do not apply on clean arithmetic or clean multiple choice. | O8, G1 | [E] on direction (b21, b23, d17 agree) | b21, b23, d17 |
| 8 | Keep the theory hierarchy (presented/discovered; Dillon; Abdulla-Cramond) out of the schema as extra states. Labels did not change results, and none is tested as an agent design. | section 4b candidate | [E] | a19, K25 |
| 9 | Do not cite exact follow-up numbers or one Getzels coefficient. Use "moderate positive, about .4 to .65, N about 31". | notes only | [E] (as a caution) | K24, K28 |

### Test first (single-source or contested)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | A separate cheap missing-information detector in S1, not carried in the main prompt. Raised resolve rate to the interactive ceiling on code; costs accuracy if bundled. | S1 | [S] | a33, d09, d10, K16, K29, K30 |
| T2 | Trigger-based early stop on uncertainty keywords, converted to one clarifying question or an explicit "underspecified" answer. | S1, S6 | [S] | d05, c09 |
| T3 | Explore-first open mode: brainstorm without constraints, then commit, vs commit-first, at equal tokens, blind human ratings. | S3 open | [S] | d12, a02, d01, K33 |
| T4 | Gate O8 on cue conflict, low confidence, weak model or awkward phrasing; skip when cues agree. | O8, G1 | [S] | a22, d17, b21 |
| T5 | O8 with an equivalence check and a constraint check on the reframed problem. | O8, G3 | [S] | b13, d18, d15 |
| T6 | Identify-then-verify listing of missing facts. | S1 | [S] | c18 |
| T7 | Sample-then-split clarifying questions in open spaces. | S1 | [S] | d07, d08 |
| T8 | Structured Dorst-style template vs plain "restate". | O8 | [C] | b14 (null) vs b16 (N=7) |
| T9 | Log exploration features in open mode (frames tried, tokens before commit, frame changes) and check that they predict blind originality. | logging | [S] | d01, b04, K27 |
| T10 | Rephrase-and-respond as a cheap first slot, compared to best-of-2 at equal tokens. | O8 | [S] | b22, c10 |

---

## 8. Concrete tests on our bench

All arms at equal total tokens (including detector and reframe calls). Report setup cost (G7). Run each at least 3 seeds.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 Missing-info detector | underspecified variants of existing bench items (remove one premise or constraint); plus the fully specified originals; mix 50/50 | plain; detector in the same prompt; separate detector call; separate detector only on keyword trigger | rate of correct "ask/underspecified" on removed-premise items; false-alarm rate on specified items; final accuracy on the mix | separate detector > same-prompt; same-prompt may fall below plain on hard specified items (d09: -1.6 average) |
| B2 Early stop to question | MiP-style ill-posed items plus well-posed controls | let model finish; keyword stop then "underspecified"; keyword stop then one question | tokens; abstain/ask rate; final correctness when an answer to the question is supplied; false stops | 38 to 70% token saving on ill-posed (d05); final quality unknown |
| B3 Explore-first open mode | open-ended tasks (NoveltyBench-style prompts, design problems) | commit-first; explore-first (brainstorm without constraints, then pick one); explore-first with code-dedupe and selection | blind human novelty and usefulness; distinct count after dedupe at fixed token budget; quality-gated count | explore-first higher distinct count (d12: 12 vs 8); human rating gain uncertain |
| B4 O8 gating | ARC and BRAINTEASER items where first attempt fails | no O8; O8 ungated; O8 only on failed check; O8 only on cue conflict | solve rate; fixed vs broken answers (as in b21); tokens | gated > ungated; ungated breaks answers (11.9% in b21) |
| B5 Reframe safety | benign tasks with explicit constraints (budget, format, rules) | plain; O8 ungated; O8 plus constraint check | constraint-violation rate by program check; unsafe content rate | O8 ungated raises violations; check removes them (unmeasured) |
| B6 Rephrase vs resample | items with awkward wording | rephrase-and-respond; best-of-2 plain; plain | accuracy | gain on awkward items only; compare to d17's missing resample control |
| B7 Question selection | 20-questions style hidden-rule tasks (ARC rule discovery, Zendo-like); enumerable and open versions | model picks question; program EIG over enumerated rules; sample-then-split | questions to correct rule; final accuracy | EIG fewer questions; edge shrinks for strong models (d07) |
| B8 Frame template | design problems | plain restate; Dorst nine steps; Abdulla-Cramond levels | blind expert novelty and usefulness; downstream solution success | null expected on rated novelty (b14); template may raise interest |
| B9 Process features | logs from B3 | none (analysis) | correlation of frames-before-commit, frame changes, rarity with blind originality | positive, around .4 to .6 if the 1976 pattern transfers |
| B10 Proxy validity | small set of 30 to 50 reframes rated by 2 humans | n/a | rank correlation of quality-gated distinct count, and of downstream solve rate, with human ranks | needed before using any proxy as the metric (d13, d14) |

Judging rule for all: judges never see authorship, are not of the generator's family, and scores are length-normalised (G5). Prefer program checks and downstream success.

---

## 9. What does not transfer, and why

- **Art studio exploration.** Handling physical objects and sketching is bodily sampling of a real environment. An LLM has no table; its "objects" are tokens it generates. Exploration costs tokens and, by the model's own fixation, tends to repeat (b19).
- **Years-long outcomes.** Follow-up claims about careers (a27) concern person-level traits; agents have no career and the claims are contested.
- **Motivation and affect.** Csikszentmihalyi's account involves feeling and drive (a25); Wakefield's empathy (a07). No analogue to build.
- **Age effects.** Meaningless for agents, and noisy anyway (d04).
- **Teams.** The restating-in-teams effect (less conflict, more satisfaction) is a social benefit (b08); G9 says no debate for agents.
- **Rated novelty in LLM idea studies.** Research-idea novelty ratings (b18) are about idea generation judged by outsiders, not about finding better problems. Also a judge mirage (a28).
- **Tests where the user can answer.** Clarification gains (a33, d10) assume a user or simulator replies. In our bench, if no user exists, the detector can only force an explicit assumption list or abstain, which G6 limits.
- **Expertise moderation.** In b15 the LLM helped experts and not novices. Our agent has no "user skill" variable; the analogue may be prompt quality, untested.
- **Autonomous problem discovery** (new research directions, AM-style) has only weak LLM evidence (a34, c17, c19, c20, c21). Not a benchmark we can score now.

---

## 10. Open questions

1. What do the 1976 book and the 1971 paper actually report (coefficients, N per cell, blinding, how problem finding was scored)? We never opened them (gap 5). The three second-hand coefficients conflict.
2. Does an explicit open-mode phase beat commit-first at equal tokens on open-ended agent tasks rated blind by humans (gap 1)? Only CreativeDC points that way.
3. When does an O8 reframe help? Candidate boundaries: cue inconsistency, task type, weak model, user skill (gap 2).
4. Is the missing-information check worth its tokens? What is the false-alarm rate on fully specified items at first turn (gap 3)? No first-turn false-alarm figure was found.
5. How can reframe quality be scored without a same-model judge (gap 4)? Candidate proxies: downstream solve rate, quality-gated distinct count, expert panel. None is validated.
6. Does reframing raise harmful output or constraint violations in agents as it did in people (gap 6)?
7. Is the meta-analytic age pattern real or confounded (gap 7)? Low value.
8. Do structured frame templates beat a plain restate at equal tokens (gap 8)? One N=7 positive, one N=280 null.
9. Can information-gain scoring of questions work on open design problems (gap 9)? Partly, via sampling; not tested on truly open design.
10. Can the early-suspicion stop be turned into a clarifying question without losing final answer quality (gap 10)?
11. Does problem finding in the human sense (choosing what is worth solving) show up in any LLM benchmark at all? No found.
12. Does the missing-premise token cost multiplier of "2x to 4x" hold? Unverified in the text we read (c08).
13. Why do LLM-help studies split (Si positive on rated ideas, Shin null on reframing)? Different tasks and different raters; no study bridges them (c23).

---

## 11. Sources

[V] = opened and read this session (full text or substantive page). [M] = search snippet or summary only.

**Human studies and reviews**

- [V] Groenendijk (2012) thesis ch.2, describing Getzels and Csikszentmihalyi 1976: https://pure.uva.nl/ws/files/1856164/105340_06.pdf (a01 to a03)
- [V] Abdulla (2016) dissertation, UGA, with the meta-analysis (Abdulla, Paek, Cramond, Runco) and reports of Csikszentmihalyi and Getzels 1971, Moore 1982, Runco and Okuda 1988, Hoover 1994, Dillon, Arlin, Abdulla and Cramond 2018: https://openscholar.uga.edu/record/21269/files/abdulla_ahmed_m_201612_phd.pdf (a04, a05, a08 to a10, a13, a16 to a20, a25, d03, d04)
- [V] Wakefield (1991) Problem Finding and Empathy in Art: https://archive.org/details/micro_IA41152961_0557 (a06, a07)
- [V] Wakefield (1985) Towards creativity: problem finding in a divergent-thinking exercise: https://archive.org/details/micro_IA41152959_0143 (a12)
- [V] Okuda, Runco and Berger (1991): https://scholarship.claremont.edu/cgu_fac_pub/340 (a11, b06)
- [V] Abdulla Alabbasi et al. (2021) Which divergent thinking index is most related to problem finding: https://www.frontiersin.org/articles/10.3389/fpsyg.2021.671146 (a14, a15, a21, b09, b10, b12)
- [V] Reiter-Palmon, Mumford, O'Connor Boes and Runco (1997): https://digitalcommons.unomaha.edu/psychfacpub/52 (a22, b07, b26)
- [V] Reiter-Palmon and Murugavel (2018) problem construction and team creativity: https://www.frontiersin.org/articles/10.3389/fpsyg.2018.02098 (a23, a24, b08)
- [V] van de Kamp et al. (2021) exploration types and originality: https://pure.uva.nl/ws/files/116325938/Journal_of_Creative_Behavior_20 (b04, b05, b25; full URL in evidence_b.jsonl)
- [V] Moore (1985) originality of essays and problem-finding variables: https://files.eric.ed.gov/fulltext/ED258186.pdf (d01, d02)
- [V] Freeman (1994) Finding the Muse, appendix: https://www.cambridge.org/core/books/abs/finding-the-muse/appendix-the (b03)
- [V] Linnell and Reiter-Palmon (2026) malevolent creativity and problem construction: https://www.frontiersin.org/articles/10.3389/fpsyg.2026.1788182 (b13)
- [V] Problem Generation test meta-analysis (2024 OSF preprint): https://osf.io/preprints/psyarxiv/wkzhq (b11)
- [V] Wikipedia, Problem finding: https://en.wikipedia.org/wiki/Problem_finding (a26)
- [M] MIT Press Reader and Project MUSE summaries of The Creative Vision and follow-ups: https://thereader.mitpress.mit.edu/the-1960s-art-school-experiment-tha... ; https://muse.jhu.edu/article/599015/summary (a27, b01, b02)
- [M] Getzels and Csikszentmihalyi (1976) The Creative Vision; Csikszentmihalyi and Getzels (1971) J Pers Soc Psychol. The primary texts were not opened; used only through the sources above.

**LLM and AI studies**

- [V] Shin, Polyanskaya, Lucero, Oulasvirta (2025) No evidence for LLMs being useful in problem reframing: https://arxiv.org/abs/2503.01631 (b14, b15, c01, c02, c23)
- [V] Sood, Wan, Paris, Grace (2026) ICCC: https://computationalcreativity.net/iccc26/papers/ICCC26_paper_78.pdf (b16, c03)
- [V] Si, Yang, Hashimoto (2024) Can LLMs generate novel research ideas: https://arxiv.org/abs/2409.04109 (b18, b19, c11, c12)
- [V] Sinhahajari, Majumder, Poria (2026) limits of LLM-as-judge for scientific novelty: https://arxiv.org/pdf/2606.12071 (a28)
- [V] Mishra, Sahu et al. AInstein: https://arxiv.org/pdf/2510.05432 (a29, b24)
- [V] Li, Kim, Wang (2025) QuestBench: https://arxiv.org/abs/2503.22674 (a30, a31, c06, c07)
- [V] Tian et al. MacGyver: https://arxiv.org/abs/2311.09682 (a32, c04, c05, c25)
- [V] Edwards and Schuster (2026) Ask or assume: https://arxiv.org/pdf/2603.26233 (a33)
- [V] Hu et al. (2024) Nova: https://arxiv.org/pdf/2410.14255 (a34)
- [V] Su et al. (2026) Knowing but not showing: https://arxiv.org/abs/2605.25284 (b17)
- [V] Zheng et al. (2023) Take a step back: https://arxiv.org/html/2310.06117v2 (b20, b21)
- [V] Deng et al. (2023) Rephrase and Respond: https://arxiv.org/pdf/2311.04205 (b22, b23, c10)
- [V] Fan et al. (2025) Missing premise exacerbates overthinking: https://arxiv.org/abs/2504.06514 (c08, c09)
- [V] Grand et al. Shoot first, ask questions later (authors unverified): https://arxiv.org/abs/2510.20886 (c13, c14)
- [V] Grand, Pepe, Andreas, Tenenbaum (2024) Loose LIPS Sink Ships: https://arxiv.org/pdf/2402.19471 (d08); [M] earlier snippet c22
- [V] Ding et al. (2023) Fluid transformers and creative analogies: https://arxiv.org/abs/2302.12832 (c15)
- [V] Sabbah and Li (2025) augmented problem finding: https://doi.org/10.1080/14479338.2025.2504428 (c16)
- [V] Tree-based problem-solution exploration (2024): https://arxiv.org/abs/2402.06053 (c17)
- [V] Jain and Garimella (2026) Knowing what's missing: https://arxiv.org/abs/2512.06476 (c18)
- [M] Wang (2026) FirstResearch: https://arxiv.org/abs/2607.05682 (c19)
- [V] Vocabulary and verifier gaps position paper: https://arxiv.org/abs/2607.09560 (c20)
- [V] Lenat AM and Eurisko; Ritchie (1991): http://www.dai.ed.ac.uk/papers/documents/rp522.html (c21, abstract only)
- [V] Xie et al. (2026) statistical early stopping: https://arxiv.org/pdf/2602.13935 (d05)
- [V] Wang et al. (2026) EAT entropy early exit: https://arxiv.org/pdf/2509.26522 (d06)
- [V] Kobalczyk et al. (2025) active task disambiguation: https://arxiv.org/pdf/2502.04485 (d07)
- [V] Matsnev (2026) uncertainty decomposition for clarification: https://arxiv.org/pdf/2606.19559 (d09)
- [V] Luo et al. (2025) ClarifyMT-Bench: https://arxiv.org/pdf/2512.21120 (d10)
- [V] Fang et al. (2026) ClarifyCodeBench: https://arxiv.org/pdf/2607.00711 (d11)
- [V] Nguyen, Tschiatschek, Singla (2026) diversity of LLM-generated educational tasks: https://arxiv.org/pdf/2512.23601 (d12)
- [V] Tutone, Franceschelli, Musolesi (2026) limits of automatic evaluation of creativity: https://arxiv.org/pdf/2608.23705 (d13)
- [V] Shypula et al. (2025) diversity and quality of LLM output: https://arxiv.org/pdf/2504.12522 (d14)
- [V] Bisconti et al. adversarial poetry: https://arxiv.org/pdf/2511.15304 (d15)
- [M] Tool-framing and refusal rates (ICML 2026 abstract): https://icml.cc/virtual/2026/76855 (d16)
- [V] Williamson, Ji, Dwyer (2025) syntactic blind spots: https://arxiv.org/pdf/2510.01831 (d17)
- [M] CRTBench logical reformulation consistency (search summary): https://www.alphaxiv.org/abs/2607.14528 (d18)
- Search records of absence: a35, d19 (no LLM test of the Getzels paradigm; no paired open-mode, harm-rate or template tests found).

## Source audit (2026-10-27)

Fresh auditors re-opened the sources of 7 established claims: 6 confirmed as written, 1 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A10.08-K05** (now single-source: the sources are not independent). Numbers verified (N=90, verbal flexibility r=.71-.76, figural .14-.31, fluency moderator CI -.084 to .625) but both the Frontiers 2021 study and the meta-analysis dissertation are by the same author (Abdulla Alabbasi), and the mixed/negative earlier links (Arlin, Getzels and Smilansky, Lee and Cho, Ambrosio, Runco and Okuda) were only read second-hand through them; also r up to .76 means verbal DT and problem finding overlap heavily.
- **A10.08-K13** (now single-source: only one opened source, code check).
