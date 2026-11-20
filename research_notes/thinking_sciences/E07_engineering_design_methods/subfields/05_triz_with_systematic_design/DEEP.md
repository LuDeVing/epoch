# TRIZ with systematic design: deep document

*Subfield E07.05. Key work: Fiorineschi, Frillici, Rotini (2018). Built from evidence_a-d.jsonl (a01-a29, b01-b25, c01-c29, d01-d19), claims.jsonl (K01-K27) and critique.md in this folder. Read with `../03_triz/DEEP.md` (TRIZ itself), `../01_systematic_design/DEEP.md` and `../02_functional_decomposition/DEEP.md`; this file does not repeat them. Evidence ids below are the lines in this folder.*

## 1. What it is

Systematic design (Pahl and Beitz, VDI 2221) builds a concept in stages. The designer clarifies the task. Then the designer splits the overall function into sub-functions (a function structure). Then the designer lists working principles for each sub-function in a morphological chart (rows = functions, columns = working principles). Then the designer combines one cell per row into a concept. This is "functional decomposition and morphology", FDM.

TRIZ is a separate method. It rests on technical contradictions (improve parameter A, parameter B gets worse), a 39 by 39 matrix that points to some of 40 inventive principles, an Ideal Final Result, and Subject-Action-Object (SAO) function models. About 40,000 patents were the source (a29).

"TRIZ with systematic design" is the attempt to join the two. The founding claim of this subfield (Fiorineschi, Frillici, Rotini 2018, a01) is:

1. FDM gives non-comprehensive support to creativity. Abstraction widens the problem but does not find its real crux, and psychological inertia anchors the task (b08).
2. Earlier TRIZ-FDM integrations ran into "non-negligible issues". The group's own review counted 10 integration proposals and 5 general issues (a03, a26; second-hand, review not opened).
3. So the authors propose a different join: build a Problem-Solution Network (PSN) of "How to verb + noun?" problems and solutions, and read SAO triads off its branches so that TRIZ tools can be picked per problem type (a04).

Plain status: the gap in point 1 is argued from literature and worked examples. There is no controlled experiment of the gap or the fix (K01, K20). The group's later papers are course suggestions (a07, b09) and one industrial case of task re-questioning (b07). The only quantitative work near this subfield is on TRIZ in general, in humans (2006-2022) and in language models (2024-2026). That is what Sections 3 to 6 record.

Why it matters to our agent. Our schema is a staged pipeline with typed reframes (O4 drop a constraint, O8 reframe the goal) that fire only on a signal (G1). The 2018 paper is the closest published argument that a staged pipeline needs a creativity step bolted on, and that bolting it on can cost more than it gives (a03). We must test it, not assume it.

## 2. History and theories in depth

**TRIZ origin.** Altshuller and colleagues in the 1960s studied over 40,000 patents and found repeated patterns of invention. The toolkit has 40 principles, 39 engineering parameters, the matrix, trimming, evolution trends and 76 standard solutions (a29, secondary statement). Industrial uptake stayed limited. Spreafico and Russo (2016) collected over 200 case studies from the TRIZ Journal and ETRIA venues; the contradiction matrix and 40 principles were the tools used most; sectors were energy and electrical 19%, home appliances 14%, generic mechanical 14% (b22, a25; snippet only). The cases are self-selected successes. Ilevbare et al. (2013) say detailed success and failure cases are seldom shared (a28, second-hand).

**Systematic design side.** Malmqvist et al. (1996) gave merging tips for Pahl and Beitz plus TRIZ, with no case study (b18). Later proposals: Dietz 2009, Nix 2011, Frillici 2014, Cascini 2011 (b08, names only).

**The group's argument, step by step (a01-a06).**
- Conceptual design is said to fix about 80% of product cost (Ullman 2010, cited).
- Two integration strategies. "Support": run TRIZ next to FDM, which makes the process more complex and onerous. "Merging": change FDM or TRIZ, which makes it unclear whether the original advantages survive (a03).
- Key technical blocker (K02): TRIZ performance problems (PP) and harmful-effect problems (HE) cannot be identified until a working principle is chosen for a function. The EMS (energy-material-signal) function model has no subject, so SAO triads cannot be built from a function structure (a02). Problems fall into three SAO classes: subject missing (SM), performance (PP), harmful effect (HE).
- The authors' verdict: forcing TRIZ into FDM is "destined to fail or, at least, to face many practical and theoretical issues" (a03).
- Their alternative: the PSN (Fiorineschi 2016). Six rules: main task, first-level problems, solution-independent decomposition, abstraction order, branch independence, completeness (a04). Problems and solutions co-evolve in a tree.
- Three academic examples, one per class (a05). SM: clothespin; the Ideal Final Result "clothes fasten by themselves" gave a new solution (clothes held between two twisted wires), used to break design fixation. PP: dishwasher; standard solution 1.1.2 (add a substance) gave particles in the jet. HE: aluminium anodising tub, about 1 m by 4 m at about 90 C, where the lid conflicts with bar movement; TRIZ tools sought non-lid solutions.
- Self-declared limits (a06): no guideline to feed TRIZ solutions back into the PSN, tool choice is subjective, case studies and surveys are needed. No N anywhere in the paper.

**Companion papers.**
- Frillici, Rotini, Fiorineschi (2016) re-question the task before FDM begins, using TRIZ functional modelling and the System Operator (nine screens). One case: a concrete slab plant. The firm asked for a conveyor belt to recover fallen mix; the analysis moved the task to a new dispenser that avoids leakage (b07). Quote: "the right problem may not be the one stated".
- Fiorineschi, Frillici, Rotini (2019) used OTSM contradictions and separation principles on their own course. Course: Florence, about 20-30 students a year, 12 of about 30 conceptual-design hours on the method, 5 hours of lectures. Output: six general problems, two physical contradictions, eight suggestions, four to be implemented. No outcome data (a07, a08, b09). Six years of experience: students see the advantages but find the project too onerous and abandon methods later. Industry rarely follows FDM (Maurer and Widmann 2012, cited).
- Fiorineschi, Frillici, Rotini (2018, J Eng Des 29(6)) is the full version of the PSN-plus-TRIZ proposal. Not opened (a27, d16).

**Competing explanations of why TRIZ helps people.**
- Forced problem-space time. In a protocol study, 11 teams of two seniors spent more reasoning on function and expected behaviour with TRIZ than with brainstorming; the gap faded in the second half (b06).
- Far stimulus. TRIZ principles act like far-domain analogies, which raise novelty and cut count (Chan et al., 153 students, second-hand in b02).
- Lower search load. 30 students, TRIZ needed less prefrontal activation than brainstorming or morphology (b23; snippet only).
- Concrete wording. Less abstract sub-principles gave about 1.5 times more ideas (b24; snippet, unverified).

## 3. Core findings with exact numbers

Status key: **E** established (two or more sources, read), **S** single source, **C** contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| FDM creativity gap and TRIZ fix are argued, not measured | 3 academic examples, no N, no control, no counts | a01, a05, a06, b08 | S (K01, K20) |
| TRIZ-FDM merges are hard: PP/HE problems need a working principle first; EMS has no SAO subject | 10 proposals, 5 issues (second-hand) | a02, a03, a26 | S (K02) |
| Full course on the matrix doubled feasible concepts | 8.94 vs 4.42 per team; 35 vs 16.3 per section; 21 vs 8 unique concepts; 16 TRIZ teams vs 24 | Ogot and Okudan 2006, b03 | C (K05); no significance test, quasi-experiment |
| One TRIZ lecture: novelty up at 2 of 3 sites, quantity no change | Novelty p=0.0004, 0.0145, 0.5786; quantity p=0.2879, 0.5409, 0.6291; one task | Hernandez 2012, b01 | S, authors call it a trend (K04) |
| Fluency and originality effects differ across studies | Dumas 2016 N=44 fluency -19.3%; Chang 2016 N=121 originality +1.5%; Dumas and Schmidt 2015 N=19 novelty +30.8%, 6-week course | b05 (second-hand) | C (K03, K25) |
| Simple TRIZ10 (30-min lecture) | N=13, no control, ideas +178%, novelty about +10% | Cano-Moreno 2022, b04 | S, weak |
| Simple ideation prompt: one gain, one null | Control about 2 dissimilar ideas (2014); later 5.03 vs 5.04 vs 4.20, no difference | b19-b21, d15 | C, snippet only (K06) |
| TRIZ shifts student reasoning toward the problem | 11 teams; second half difference gone, t(9)=-0.195, p>0.05 | b06 | S (K07) |
| Plain LLM TRIZ is unstable on contradiction pair | 100 runs per case; entropy 0 to 6.64; 7 of 10 cases match or half match in top 3; cases 5-8 have one dominant answer | AutoTRIZ, a09, c02 | E (K08) |
| CoT best for contradiction recall; few-shot collapses it | Recall/precision: basic 0.675/0.259, CoT 0.691/0.310, few-shot 0.245/0.333, CoT+FS 0.247/0.298; 34 cases | TRIZ-GPT, a14, b10, c06 | E (K09) |
| Post-cutoff drop | CoT recall 0.544 (GPT-4) vs 0.400 (GPT-3.5) on 10 cases; old cases 0.691 (different collections) | a15, c08 | E for the figures; drop cause unknown |
| Solution step insensitive to prompt style | Cosine to reference 0.829, 0.823, 0.824, 0.824 (SD about 0.03), 84 pairs | a16, b11, c07 | E (K10) |
| Detect contradiction easy, name the pair hard | HasF1 0.75-0.87 zero/few-shot, LoRA 0.88-0.90; pair F1 0.29-0.45; patent pair Hit@3 0.13-0.31; 590 docs, 734 cases with principles | TRIZBench, b15, d08 | E (K11) |
| Lookup nearly equals best LLM for principles | Hit@3 case/patent: matrix 0.67/0.48; TF-IDF 0.69/0.56; Qwen3-8B zero-shot 0.39/0.27; Gemini zero-shot 0.45/0.31; matrix-rerank 0.71/0.59 | b16, d11 | S (K12), one benchmark |
| GPT-4 over-detects contradictions | Zero-shot sentence recall 0.71, precision 0.46, F1 0.56, 3.19 false positives per patent; flagged 86 of 100 patents labelled contradiction-free (upper bound: labels doubtful); BERTScore 0.93 is not sentence F1 | Trapp and Warschat 2024, c20-c22, d09 | E for the numbers (K13) |
| Abstain instruction alone is not enough | Abstain in every TRIZBench arm; HasF1 still 0.75-0.87; no abstain vs no-abstain arm | d08 | S (K24) |
| LLM-TRIZ gives more ideas and variety than expert textbook answers | Ideas 20 vs 4, 7 vs 2, 18 vs 1-2; novelty means e.g. 2.42/3.41 vs 2.0/2.56; experts higher in 1 of 6 comparisons; function analysis accuracy 0.56-0.59 | Mohammadi and Zeng 2025, b14, c13 | S (K14) |
| LLM help did not lift student design quality overall | N=113 (62 vs 51); method F(1,108)=3.21, p=.076; wind turbine only F(1,108)=34.67, p<.001; contradiction-naming felt easier d=-0.78; time 40.3 vs 46.2 min | Cok et al. 2026, d01-d03 | S (K17) |
| Named contradiction moves a modern LLM off scaling | Claude Sonnet 4.5, one chair: vanilla mass -31.8%, stress +64.1%; TRIZ variants mass -4.0 to -14.7%, stress -0.1 to +40.7% | d05 | S (K21), N=1 |
| Plain GPT-3: feasible, less novel than crowd | 12 problems; 600 solutions expert-rated, two experts; embedding similarity 0.804 few-shot vs 0.746 "unique" | Ma et al. 2023, c23, c24 | S (K15) |
| Multi-agent TRIZ costs a lot, no control | 60-80 calls, 150k-250k tokens per run; one case, two runs; 6 links missed; specialist rarely used RAG | TRIZ Agents, c15-c17, d04 | S (K16, K26) |
| Typed TRIZ mutation vs untyped not isolated | TRIZa CICIoT2023 macro-F1 0.8325 to 0.8483; 43 of 45 groups improved; authors cannot assign cause | d06 | E that no ablation exists (K22) |
| Pre-LLM semantic TRIZ rarely reported benefits | 57 papers; 12 clear, 31 not addressed; 1,136 records screened | Ghane et al. 2023, a18 | E (K18) |
| Author-run case results | AutoTRIZ battery +24%, +64%, +26% from authors' own model | a11, b13, c04 | S (K19) |
| No independent-rater, post-cutoff, kappa study exists | arXiv search 2026-11-19: 7 relevant papers, none with all three | d17-d19 | S (K27) |

## 4. Mechanisms and models

Each mechanism is written so an engineer can build it as a step in a program that calls a model.

**4.1 Problem-Solution Network (PSN), the 2018 model (a04).**
Data structure: a tree with two node types, Problem ("How to ... ?") and Solution. Each Solution may open child Problems. Rules the code can check:
1. One root node: the main task, phrased as a how-to question.
2. First-level children come from the main task only.
3. Decomposition is solution-independent: child problems of a node must not name a solution.
4. Siblings are ordered from abstract to concrete.
5. Branches are independent (a problem appears in one branch).
6. Completeness: every leaf is a Solution or is marked open.
Implementation: store nodes as JSON with type, text, parent, status. A validator in code checks that problem text starts with "How to", that no problem node contains a solution token from its sibling Solutions, and that no leaf is empty. The model proposes nodes; code accepts or rejects. Untested in any experiment (K20).

**4.2 Problem typing by SAO class (a02).**
Classify each node as SM (a subject, i.e. an actor, is missing), PP (an action performs poorly) or HE (an action causes harm). The class picks a tool: SM goes to Ideal Final Result ("the thing does the job by itself"); PP goes to standard solutions (add a substance, change a field); HE goes to trimming or contradiction handling (a05). The blocker the authors name: PP and HE cannot be typed until a working principle exists. So the order must be: pick a working principle per function first, then type problems, then call TRIZ. A program can enforce this order by refusing to run the typing step on a node with no working principle recorded.

**4.3 Contradiction-then-lookup in code (AutoTRIZ, a09, c01, d10).**
Four modules: restate problem (LLM), name the contradiction as two of the 39 parameters (LLM), look up principles in the 39 by 39 matrix (code, a fixed table), write solutions from the listed principles (LLM). The program owns control flow. One contradiction per run; randomness is kept on purpose to widen the idea set. To stabilise the naming step: run it N times, count pairs, keep the top by frequency. Frequency predicted match to textbook (higher-probability outputs matched better, b12). Entropy of the pair distribution (0 to 6.64 over 100 runs) is a usable instability score.

**4.4 Detect, then name (TRIZBench, b15).**
Two separate slots. Slot 1: "is there a conflict that can be grounded in the text? yes/no/unknown". Slot 2: "name the improving and worsening parameter". Score and gate them separately because detection F1 is 0.75-0.87 and pair F1 is 0.29-0.45. A none-found exit is needed because a model with no such exit will report a contradiction almost always (86 of 100 flagged, d09).

**4.5 Retrieve, then rerank (d11).**
Principle candidates come from code: matrix cell, or TF-IDF over principle descriptions. The model reranks the top candidates and does not generate freely. Hit@3 0.71/0.59 against 0.69/0.56 for TF-IDF alone: the model adds about 0.02 to 0.03.

**4.6 Task re-questioning before decomposition (b07).**
Before building the function structure, run a short pass over the requirement list with nine screens (system level x past, present, future; super-system; sub-system). Ask for each: what function is actually needed, what does the requirement hide? Output: a revised task statement. In the case, a "conveyor belt" request became "dispenser that avoids leakage". The agent version would be an S1 step that rewrites the task, then a code check that the new statement is no longer a solution word.

**4.7 Mohammadi and Zeng's loop (c11).**
Environment-based design questions, then interaction network, then functional analysis, then an idea prompt that loops 40 times, one per principle, temperature 1. 12 prompts. Function analysis accuracy 0.56-0.59, so a verify step is needed before the contradiction is trusted.

**4.8 Multi-agent TRIZ (c15).**
Manager agent plus TRIZ, mechanical, control, safety, electrical specialists; six-step workflow; matrix step deterministic. Failure modes: a specialist never called leaves a solution class unexplored (circuit breaker missed); the manager never sent work back; behaviour depended on profile prompts. The fix for the first is a coverage check over roles in code.

**4.9 Typed-mutation search (TRIZa, d06).**
Evolutionary loop. Each mutation must instantiate a named principle and a matrix entry. Promotion gate: a candidate is withheld if it fails a gain threshold or if harm (false-positive rate) worsens. The gate style is reusable; the TRIZ benefit is not isolated.

## 5. What holds up

**Holds up (read, two or more sources).**
- LLM TRIZ contradiction naming is unstable and over-generates (K08, K09, K13). AutoTRIZ entropy, TRIZ-GPT precision 0.26-0.33, Trapp precision 0.46.
- Detecting that a conflict exists is much easier than naming it (K11).
- Few-shot examples do not help and can cut contradiction recall to about 0.245 in GPT-4 (TRIZ-GPT). TRIZBench few-shot changes are small and sometimes negative. Ma 2023 found few-shot pulls ideas toward the example set. Direction agrees across three sources (c06, c24, d08).
- Embedding similarity to a reference solution does not separate prompt styles (0.82-0.83) (K10).
- Pre-LLM literature seldom reported benefits or limits (K18).

**Contested.**
- Quantity of ideas under TRIZ. Gain (Ogot 8.94 vs 4.42; TRIZ10 +178%), no change (Hernandez), loss (Dumas -19.3%). Units differ (feasible concepts per team vs ideas per person). Pattern in the table: full course or per-team count gives gains, one lecture gives nothing or a loss. Not tested; two of five numbers are second-hand (K25, d14).
- Novelty. +30.8% (Dumas and Schmidt, N=19), +1.5% (Chang, N=121), significant at 2 of 3 sites (Hernandez). Range of more than an order of magnitude (K03).
- Belski simple ideation: a gain by the originators (2014, 2015) and a null replication (2017). Originator replication is not independent. Snippet-level only (K06).

**Failures and weak spots.**
- The central claim has no experiment. The 2018 paper has no N and no control.
- Human TRIZ studies are student samples, one task, short training, whole-section assignment.
- Ogot 2006 had no significance test and measured quantity only. Instructors saw students drift off the principles without monitoring (b03).
- Hernandez 2012: TRIZ group had a first no-method session; Penn State quantity cell 16.286 vs 4.100 looks like a team-vs-individual unit mismatch; sample sizes UTEP 21 vs 9 and Maryland 20 vs 21 were not re-found in the PDF text (critique item 9).
- LLM studies compare to textbook answers likely in training data. TRIZ-GPT's 0.691 to 0.544 drop is across different collections, so memory versus difficulty is unseparated.
- Mohammadi idea-count wins favour a generator against fixed textbook answers (experts printed 1-4 ideas).
- TRIZBench labels are partly made by Gemini-2.5-Pro (74% agreement before adjudication); labels are inventors' principles, not best principles. Its 5-case human and frontier calibration (Sonnet-4.6 HasF1 1.00, pair 0.60; GPT-5.2 0.80/0.60; Gemini-3-Pro 0.50/0.40; TRIZ-familiar humans 1.00/0.60) is too small to use.
- AutoTRIZ results are all self-reported with no plain-LLM baseline arm (K19).
- TRIZ-RAGNER (F1 84.2 vs 76.9; ablation each part 4 to 8 points) has stray unrelated text and no N or variance. Weak (K23).

**Moderators seen.**
- Training length and what is counted (K25).
- Problem difficulty and tool skill: Cok 2026, gain only on the wind turbine problem whose group was AI-specialised; method x problem F(2,108)=7.58, p=.001; Levene p=.018 so variances differ.
- Model strength: GPT-3.5 gained from few-shot structure, GPT-4 did not (c08).
- Monitoring: gains came with guided practice (b03).

**Interventions that worked.**
- Code-fixed matrix lookup with the model confined to naming and writing (AutoTRIZ; TRIZBench lookup baseline).
- Chain-of-thought over few-shot for contradiction recall.
- Retrieval over free choice for principle selection (single benchmark).
- Naming a contradiction and a principle moved Sonnet 4.5 from scaling to structure (N=1).

**Interventions that did not work, or are not shown.**
- Few-shot examples for naming contradictions.
- Embedding similarity as a creativity or quality score.
- LLM support for students on complex tasks (Cok 2026): no overall quality gain; it eased effort only (contradiction difficulty d=-0.78; satisfaction, usefulness and reuse unchanged: p=.133, .541, .307).
- Multi-agent TRIZ at matched budget: never tested (K16).

## 6. Language models

**What was measured, by model.**
- GPT-4 and GPT-3.5 (2024): TRIZ-GPT. Contradiction recall best under CoT, 0.691 on 34 classic cases and 0.544 on 10 post-April-2023 cases. GPT-3.5 0.400 on the new set. Consistent reasoning in 85.3% (basic) and 88.2% (CoT) of cases. Solution step: no difference by prompt.
- GPT-4: AutoTRIZ. Unstable contradiction pairs; fixed chain in code; no baseline arm; battery case +24, +64, +26% by the authors' own model. Plain ChatGPT told to use TRIZ "always included apparent errors, such as mismatched contradictions and inventive principles" (anecdote, c03).
- gpt-4-1106: Trapp and Warschat. Matches best fine-tuned classifiers on sentence extraction (F1 0.56 vs weighted 0.54). Over-detects.
- GPT-3.5 in LangChain: Mohammadi and Zeng. 20 vs 4, 7 vs 2, 18 vs 1-2 ideas; novelty higher than experts in 5 of 6 comparisons.
- GPT-3 (davinci-003): Ma 2023. More feasible, less novel than crowd.
- GPT-4o multi-agent: TRIZ Agents. Physical contradictions matched exactly; engineering contradictions near but different; 6 useful links missed; one principle matched.
- Qwen3, LLaMA3.1, Gemini-2.5-Pro: TRIZBench. See Section 3. Best LoRA detection 0.90.
- Claude Sonnet 4.5: text-to-CAD. One chair; contradiction-carrying prompts changed structure instead of scaling.
- Embedding retrieval plus rerank: TRIZ-RAGNER (weak).

**What changed behaviour, by how much.**
- CoT vs few-shot on contradiction recall: 0.691 vs 0.245 (GPT-4). Large, one study.
- Structure and retrieval on principle Hit@3: roughly 0.39-0.45 free to 0.67-0.71 with matrix or rerank on cases; 0.27-0.31 to 0.48-0.59 on patents. Lookup alone nearly equals rerank.
- Prompt wording "unique" vs few-shot: embedding similarity 0.746 vs 0.804.
- Model size: GPT-4 vs GPT-3.5 recall gap 0.144 on the new cases.
- Naming the contradiction: vanilla mass -31.8% by shrinking dimensions; TRIZ prompts -4.0 to -14.7% with different structure. Not a novelty score.

**What no one measured.** Blind-rated novelty at equal tokens, plain model vs TRIZ scaffold, on post-cutoff problems, with independent raters and kappa (K27, gap 1, gap 8). Tokens per novel idea (K26). Single agent vs multi-agent TRIZ at matched budget (K16). A none-found exit versus no exit (K24). Any LLM test of the PSN or of task re-questioning (K20, K01).

**How these results sit against our schema.** G8 says models are poor judges of novelty; every LLM TRIZ study here either used embedding similarity, expert textbook comparison, or author judgement, so none supports a model-judged novelty claim. G9 (no debate) matches the finding that TRIZ Agents had no control. G6 (never abstain on the first pass) conflicts at face value with a none-found exit for contradictions; see Section 7.

## 7. What our agent should take

Tags: schema part G/S/O/memory; status [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Put the matrix or principle lookup in code; the model only names parameters and writes the idea.** O8/O4, S5. [E for the design; the lookup benefit on principle choice is [S]] Evidence: a09, c01, c02, d10, d11, b16, K08. Why: contradiction naming is unstable (entropy up to 6.64) and free principle choice does not beat lookup (0.39-0.45 vs 0.67). Cost is near zero, so it passes G7.
2. **Do not use few-shot examples in a naming or reframe prompt; prefer a short stepwise prompt.** O8. [E] Evidence: b10, c06, c24, d08. Recall 0.691 vs 0.245; "unique" lowered embedding similarity to 0.746 vs 0.804 for few-shot.
3. **Split contradiction work into detect and name, and score them separately.** O8, S1. [E] Evidence: b15, d08, K11. Detection 0.75-0.87, naming 0.29-0.45.
4. **Never score creativity by similarity to a reference solution.** G8, G5. [E] Evidence: a16, b11, c07. Flat at 0.82-0.83 across prompts. Reinforces the existing rule.
5. **Test any TRIZ step on post-cutoff or private problems only.** G7, bench rule. [E] Evidence: a15, c10, c08. Textbook cases are probably memorised.
6. **Pre-register metrics (fluency, feasible count, blind novelty, tokens per novel idea) before testing any reframe operator.** G7. [E] Evidence: K18, a18, b01, b03. Quantity and novelty move in different directions across human studies.
7. **Report the strict metric.** Meta-rule for our own bench notes. [E] Evidence: c20 (0.93 is BERTScore, not F1).

### Test first

1. **Task re-questioning step before decomposition (Frillici 2016).** S0/S1, O8. [S] Evidence: b07, K01. One industrial narrative case. Test T1.
2. **Contradiction-named reframe vs plain "improve it" prompt at equal tokens, blind novelty.** O8/O4. [S] Evidence: d05, K21, K03. The one modern-model signal is N=1. Test T2.
3. **None-found exit plus second-pass check on contradiction claims.** G6 exception inside O8, G1. [S] Evidence: d09, d08, K13, K24. Must not violate G6: the exit only governs the reframe slot, never the final answer. The final answer still submits the best attempt. Test T3.
4. **Frequency vote over 5 to 10 contradiction namings as a confidence gate.** G4/G5. [S] Evidence: b12, c02. Higher-probability outputs matched better, but G4 says one model's samples are not independent, so frequency is a hint. Use it only to decide whether to fire O8, never as proof. Test T4.
5. **Problem-Solution Network (how-to tree) versus plain decomposition (O3).** S2/O3. [S] Evidence: a04, K20. Never tested. Test T6.
6. **Typed reframe (SM/PP/HE) routing versus untyped reframe.** O8, S0. [S] Evidence: a02, a05, d06, K22.
7. **Order test: contradiction step before versus after a working principle exists.** S1. [S] Evidence: a03, K02. Test T7.
8. **Single-agent TRIZ chain vs multi-role at matched budget.** G9, S5. [S] Evidence: c15-c17, d04, K16. Prior is "no gain" per G9; test only to confirm. Test T8.
9. **Lookup alone vs LLM rerank vs LLM free choice.** O8, memory. [S] Evidence: d11, K12. Test T5.
10. **Principle wording: concrete sub-principles vs abstract.** O8. [S, snippet] Evidence: b24. Low priority until verified.
11. **Store which principle or reframe worked on which problem class.** memory. [S] No source tests learned principle retrieval. Candidate only after T2 and T5 pass.

## 8. Concrete tests on our bench

All arms use equal total tokens including setup (G7). Items are post-cutoff or private design and puzzle prompts. Two blind raters, kappa reported, order randomised. Use at least 3 problem families and report per-family results (Cok 2026 saw a method-by-problem interaction).

| ID | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | 30 open design briefs where the stated task hides the real need (conveyor-belt style) | A plain decomposition; B plain plus task re-questioning step; same total tokens | Blind-rated fit of final concept to the hidden need; share of runs that change the task statement | B wins on briefs with hidden needs; no change or loss on routine briefs. Add only if B wins on at least 2 of 3 families |
| T2 | 20 contradiction-type design problems (strength vs weight style), 5 samples per arm | A "improve X"; B same plus named contradiction and one code-picked principle; C B without the principle | Blind structural novelty (two raters, kappa); feasible count; tokens per novel idea | B above A on novelty; fluency may fall (Hernandez pattern); C between |
| T3 | 50 problems with a real conflict plus 50 with none | A one-pass naming; B naming with none-found exit; C B plus independent checker (no authorship shown) | False-positive rate on no-conflict items; detection F1; pair accuracy against human-labelled pairs | A near 80%+ false positives (Trapp 86%); B and C lower. Add if false positives fall by 20 points with detection F1 unchanged |
| T4 | 100 repeated runs of naming on 10 cases | A free LLM naming; B naming with parameter list grounded in the 39 fixed names | Entropy of pair distribution; match to labelled pair in top 3 | B lowers entropy; match rises (TRIZ-RAGNER direction, weak) |
| T5 | TRIZBench cases, principle task | A matrix lookup; B TF-IDF; C LLM free; D lookup plus LLM rerank | Hit@3 and downstream idea novelty | A about B about D; C lower. Confirms K12 and shows if rerank earns its tokens |
| T6 | 20 decomposition-hard problems | A O3 plain decomposition; B PSN tree with code validator (six rules) | Solved rate; blind novelty; token cost | Unknown. First test of the 2018 proposal |
| T7 | Same items as T2 | A principle then typing then TRIZ; B reverse order | Idea validity; wasted calls | A better if Fiorineschi's blocker binds LLMs |
| T8 | 10 cases | A single chain; B manager plus specialists, matched tokens | Novelty; coverage of solution classes; tokens | Expect no gain (G9). Run once |
| T9 | Post-cutoff and textbook problems, same format | Same arm on both sets | Recall drop between sets | Shows how much of any TRIZ gain is memory |
| T10 | Ideation mix | A plain; B principle-prompted | Fluency, variety, novelty scored separately | Reproduces novelty up, fluency flat or down, or not |

Rule for all: report per-family numbers, tokens per blind-rated novel idea, and the cost of arms that failed.

## 9. What does not transfer, and why

- **Training length and student drift.** Human effects depend on a course versus a lecture and on instructors monitoring drift (b03, K25). An agent has no training length; its drift is prompt adherence, which code can check.
- **Learning cost and abandonment.** The 2019 course finding (students drop methods as too onerous, a08) is about human effort. The agent analogue is token cost per step, which we measure directly.
- **Psychological inertia.** The 2018 argument for a creativity gap rests on human fixation. LLM fixation is different: embedding collapse toward similar outputs, few-shot anchoring (c24). The fix may differ. A named contradiction may break a default, as in d05, but that is not the same mechanism.
- **EMS function models lacking a subject.** A human function-structure blocker. An LLM can state a subject freely, so the blocker may not bind; it may reappear as a hallucinated subject. Untested.
- **Textbook-answer comparisons.** Fine for humans on unseen tasks; for LLMs, classic cases are in training data (a15).
- **Idea-count wins.** Mohammadi and Zeng's 20 vs 4 compares a generator to a printed answer. Do not read as a gain from TRIZ.
- **Industrial success cases.** Self-selected venues (b22). No transfer evidence.
- **Matrix coverage.** The matrix points to only some principles; AutoTRIZ lists only 40 principles as a limit (c05). A fixed table restricts the idea space, which may help focus and hurt breadth.
- **G6.** A none-found exit for contradictions must not become a first-pass abstention on the final answer.

## 10. Open questions

1. Is the FDM creativity gap measurable at all with a task-questioning arm against plain FDM? (gap 4)
2. Does the PSN beat plain decomposition in any experiment? (gap 5)
3. Does a TRIZ step raise blind-rated novelty of a current model at equal tokens, on post-cutoff problems, with kappa? (gaps 1 and 8)
4. Does LLM TRIZ cost more tokens per novel idea than plain sampling? (gap 6)
5. Single versus multi-agent TRIZ at matched budget. (gap 9)
6. Does a none-found exit or second pass cut false contradictions, and at what loss of detection? (gap 3)
7. Why human quantity effects disagree: training length, unit, task. (gap 7)
8. Cok 2026 cell means and per-cell n were not read. Is the wind-turbine gain a skill effect or a problem effect?
9. TRIZBench principle labels are inventors' choices; is a better-than-recorded principle penalised?
10. The Fiorineschi 2018 reviews (Computers in Industry, J Eng Des) were not opened; their counts (10 proposals, 5 issues) are second-hand.
11. Valentine 2017, Belski 2014/2015, Dumas 2016, Chang 2016 originals not opened; K06 and part of K25 stay unverified.
12. Hernandez per-site sample sizes and table order remain uncertain.

## 11. Sources

[V] opened and read; [M] snippet or abstract only.

1. Fiorineschi, Frillici, Rotini (2018) Supporting systematic conceptual design with TRIZ, DESIGN 2018. https://doi.org/10.21278/idc.2018.0135 [V] (a01-a06; b17 [M])
2. Fiorineschi, Frillici, Rotini (2018) Enhancing functional decomposition and morphology with TRIZ: literature review, Computers in Industry 94. https://doi.org/10.1016/j.compind.2017.09.004 [M] (a26)
3. Fiorineschi, Frillici, Rotini (2018) Exploiting TRIZ tools for enhancing systematic conceptual design activities, J Eng Des 29(6). https://doi.org/10.1080/09544828.2018.1473558 [M] (a27, d16)
4. Fiorineschi, Frillici, Rotini (2019) Teaching and learning design methods: facing the related issues with TRIZ, ICED19. https://doi.org/10.1017/dsi.2019.63 [V] (a07, a08, b09)
5. Frillici, Rotini, Fiorineschi (2016) Re-design the design task through TRIZ tools. https://collaborative.designsociety.org/download-publication/38830/RE-DESIGN+THE+DESIGN+TASK+THROUGH+TRIZ+TOOLS [V] (b07, b08)
6. Frillici, Fiorineschi, Cascini (2015) Linking TRIZ to conceptual design engineering approaches. https://re.public.polimi.it/retrieve/e0c31c09-5d82-4599-e053-1705fe0aef77/1-s2.0-S1877705815043052-main.pdf [M] (b18)
7. Hernandez, Schmidt, Okudan Kremer (2012) Experimental assessment of TRIZ effectiveness in idea generation. https://peer.asee.org/21369.pdf [V] (b01, b02)
8. Ogot and Okudan (2006) Integrating systematic creativity into first-year engineering design curriculum. https://www.ijee.ie/articles/Vol22-1/IJEE1618.pdf [V] (b03)
9. Cano-Moreno et al. (2022) Using TRIZ10 for enhancing creativity in engineering design education. https://link.springer.com/article/10.1007/s10798-021-09704-3 [V] (b04, b05)
10. ICDC 2012, Design cognition differences when using structured and unstructured concept generation creativity techniques. https://collaborative.designsociety.org/download-publication/32457/Design+Cognition+Differences+When+Using+Structured+and+Unstructured+Concept+Generation+Creativity+Techniques [V] (b06)
11. Valentine, Belski, Hamilton (2017) Can idea generation techniques impede effective ideation. https://aaee.net.au/wp-content/uploads/2018/09/AAEE2017-Valentine_Belski_Hamilton-Can_idea_generation_techniques_impede_effective_ideation.pdf [M] (b19, d15)
12. Belski et al. (2014) Simple ideation: enhancing idea generation. https://aaee.net.au/wp-content/uploads/2018/10/AAEE2014-Belski_Hourani_Valentine_et_al-Simple_ideation_enhancing_idea_generation.pdf [M] (b20)
13. Belski et al. (2015) Simple ideation influencing idea generation. https://aaee.net.au/wp-content/uploads/2018/10/AAEE2015-Belski_Belski_Berdonosov_et_al-Simple_ideation_influencing_idea_generation.pdf [M] (b21)
14. Spreafico and Russo (2016) TRIZ industrial case studies: a critical survey. https://doi.org/10.1016/j.procir.2016.01.165 [M] (a25, b22)
15. Ilevbare, Probert, Phaal (2013) A review of TRIZ and its benefits and challenges in practice. https://doi.org/10.1016/j.technovation.2012.11.003 [M] (a28)
16. Neuro-cognitive comparison of brainstorming, morphological analysis and TRIZ (Design Science 2020). https://doaj.org/article/c688ff81d54e4049a4d229b61d2eeab0 [M] (b23)
17. Livotov group modified TRIZ principles. https://unpaywall.org/10.1007%2F978-3-030-32497-1_41 [M] (b24)
18. Comparison of ideation techniques for beginning designers, 102 students. https://typeset.io/pdf/comparing-ideation-techniques-for-beginning-designers-59jvnmbrz6.pdf [M] (b25)
19. Jiang, Li, Qian, Zhang, Luo (2025) AutoTRIZ. https://arxiv.org/abs/2403.13002 [V] (a09-a12, a29, b12, b13, c01-c05, d10)
20. Chen, Song, Ding, Sun, Childs, Zuo (2024) TRIZ-GPT. https://arxiv.org/abs/2408.05897 [V] (a13-a17, b10, b11, c06-c10, d18)
21. Trapp and Warschat (2024) LLM-based extraction of contradictions from patents. https://arxiv.org/abs/2403.14258 [V] (a24, c20-c22, d09)
22. Wang and Uzzi (2026) TRIZBench. https://aclanthology.org/2026.findings-acl.1798/ [V] (a19, b15, b16, c18, d08, d11); repository https://github.com/ellenzhuwang/trizbench [M] (c19)
23. Mohammadi and Zeng (2025) Enhancing TRIZ through environment-based design supported by an LLM. https://doi.org/10.1017/S0890060425000083 [V] (b14, c11-c14, d19)
24. Szczepanik and Chudziak (2025) TRIZ Agents. https://arxiv.org/abs/2506.18783 [V] (a23, c15-c17, d04)
25. Cok et al. (2026) Evaluating TRIZ with and without LLM support, PDS 2026. https://www.cambridge.org/core/product/identifier/S2732527X2610409X/type/journal_article [V] (a20, d01-d03)
26. Xu, Wu, Zhao (2026) TRIZ-RAGNER. https://arxiv.org/abs/2602.23656 [V] (a21, d07)
27. Lee et al. (2026) TRIZ-inspired text-to-CAD. https://arxiv.org/abs/2606.21378 [V] (a22, d05)
28. Liu, Huang, Wang (2026) TRIZa. https://arxiv.org/abs/2610.04555 [V] (d06)
29. IdeaForge (2026). https://arxiv.org/abs/2605.13311 [V] (c29)
30. Ma, Grandi, McComb, Goucher-Lambert (2023) Conceptual design generation using LLMs. https://arxiv.org/abs/2306.01779 [V] (c23, c24)
31. Zhu and Luo (2022) GPT for design concept generation. https://doi.org/10.1017/pds.2022.185 [M] (c25)
32. Sankar and Sen (2024) Idea generation tool using structured conversational AI. https://arxiv.org/abs/2409.05747 [V] (c26)
33. Chen, Tsang, Jing, Sun (2024) LLM-augmented morphological analysis, DRS 2024. https://dl.designresearchsociety.org/drs-conference-papers/drs2024/researchpapers/152 [M] (c27, d12)
34. Owen and Roberts (2024) Design contradictions: help or hindrance? https://arxiv.org/abs/2409.02823 [V] (d13)
35. Ghane et al. (2023) Semantic TRIZ systematic review, Heliyon 10(1). https://pmc.ncbi.nlm.nih.gov/articles/PMC10788813/ [V] (a18)
36. arXiv listing search "TRIZ LLM", 2026-11-19. https://arxiv.org/search/?query=TRIZ+LLM&searchtype=all&order=-announced_date_first [V] (d17)
37. Dumas 2016; Chang 2016; Dumas and Schmidt 2015 (via Cano-Moreno Table 1, b05). [M] second-hand
