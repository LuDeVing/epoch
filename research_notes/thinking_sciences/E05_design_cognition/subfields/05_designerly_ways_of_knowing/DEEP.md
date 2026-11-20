# Designerly ways of knowing: deep document

*Subfield E05.05. Sources: evidence_a-d.jsonl (a01-a29, b01-b25, c01-c26, d01-d19), claims.jsonl (K01-K20), critique.md. Evidence ids use those file letters. Marks: [V] opened this session, [M] snippet or citation only.*

## 1. What it is

"Designerly ways of knowing" is Nigel Cross's 1982 claim that design is a third culture of knowledge, next to the sciences and the humanities. It has its own subject matter, methods and values. It is a conceptual programme paper, not an experiment. Seven pages, Design Studies 3(4):221-227 (a01, [V] abstract page and reference list only).

Cross's five aspects, as recalled and not verified against the full text (a02, opened:false):
1. Designers tackle ill-defined problems.
2. Their mode of problem solving is solution-focused.
3. Their thinking is constructive, not only analytic.
4. They use codes that translate abstract requirements into concrete objects, and back.
5. They use non-verbal media: sketches, models, drawings.

Why this matters for one LLM agent with a scaffold:
- It names a family of moves (conjecture a solution first, translate between abstract and concrete, externalise a sketch, revise the problem after seeing a solution) that our schema does not yet treat as one family.
- It warns that when no check exists (wicked problems), there is no stop rule from inside the problem (a06, a21).
- Its testable parts have separate literatures: solution-first conjecturing (Lawson 1979), co-evolution of problem and solution (Dorst and Cross 2001), fixation (Jansson and Smith 1991), reflection in action (Schon 1983, covered in subfield 02).

Honest status: the founding claim has no replication and no failed replication in what we could read (b19, d17). That is a search limit (APIs returned 429; Cross 1982, Lawson 1979, Dorst and Cross 2001 full text, and Sio 2015 are paywalled), not proof of absence. No study we found tests an LLM on Cross's core claims (b20, c21, d19).

Links to parallel subfields (not covered here): 01 design as problem solving, 02 reflection in action, 03 problem-solution co-evolution, 04 framing and reframing, 07 fixation and ideation, 09 expert-novice designers, TRIZ with systematic design, Computational design, Design-space exploration.

## 2. History and theories in depth

**Pre-history.** Simon 1969 (The Sciences of the Artificial) framed design as the science of how things ought to be, and as satisficing search in a space of alternatives (a23, [M]). Rittel and Webber 1973 defined wicked problems: no definitive formulation, no stopping rule, solutions are good or bad, not true or false (a21, [M]; a06 [V] secondary). Darke 1979 described the "primary generator": an early guiding idea that architects test against constraints (a24, [M] citation). Cross, Naughton and Walker 1981 contrasted design method with scientific method (a26, [M]). Ferguson 1977 (non-verbal thought in technology), Ryle 1949 (knowing how vs knowing that), Alexander 1964/1979 and March 1976 appear in Cross's reference list (a28, [V]).

**Lawson 1979 (the empirical base).** Cognitive strategies in architectural design, Ergonomics 22(1):59-68 (a03, citation [V]; content not opened). As recalled (a04, opened:false): final-year architecture students and postgraduate science students arranged coloured blocks to meet hidden rules. Scientists tended to probe the problem to find the rule. Architects proposed arrangements and learned the rule from the rejections. Wikipedia confirms only the direction (a05, b02, secondary). Group sizes and scores are not obtained.

**Cross 1982.** Argues design deserves a place in general education beside science and the humanities. Its value lies in "designerly ways of knowing" (quote, a01). Proposed as an axiomatic touch-stone theory for design as a discipline. Wikipedia says it helped found design as an academic discipline (b01).

**Institutional growth.** Cross started with computer-aided-design studies in the 1960s and helped found the Design Thinking Research Symposia in 1991 with Delft. DTRS2 (Delft, 1994) produced the shared protocol data set behind many co-evolution studies (a07). Books: Designerly Ways of Knowing (2006, 2nd ed 2025), Design Thinking (2011, 2nd ed 2023). Rowe 1987 Design Thinking described architects' methods. Lawson's 1980 book How Designers Think generalised the claim (a06). IDEO was founded by David Kelley in 1991.

**Dorst and Cross 2001.** Protocol study of nine experienced industrial designers on one realistic task, concept quality rated by a panel of educators. Creative moments came when a bridge formed between a problem frame and a solution idea after repeated moves between the two. The reprint abstract adds that in creative design the solution space may be structured BEFORE the problem space, using precedents (d16, [V] abstract only). So solution-first is one pattern, not the rule (K20). Full tables not read.

**Cross 1999/2024 review.** Lists solution focusing, co-evolution, fixation, opportunism and expert-novice differences from protocol studies across domains (d17, [V] abstract and references). It is a self-review. No independent critique of the five aspects was found.

**Splits and critiques.** Cross 2023 separates Design Thinking 1 (design-based) from Design Thinking 2 (business-based). Critics (Kimbell, Vinsel, Iskander) say business design thinking is under-theorised and gives creative confidence without skill. Wikipedia reports no quantitative evidence that design thinking works; the only pro-effectiveness citation named is Liedtka 2018 (b02, secondary). Micheli et al. 2019 review was not readable (b15).

**Computational descendants.** Maher and Poon 1996 modelled co-evolution with genetic ideas (c18, [M]). Jiang et al. 2021 surveyed data-driven design by analogy, 47 papers (c17, [V]).

**LLM era (2023-2026).** Three kinds of work:
1. Does LLM help change human designer behaviour (fixation, reframing, co-evolution)? Studies a12, a09, c01.
2. Does the LLM itself fixate or lack variety? Studies a15, b05, b12, c09, d15.
3. Do scaffolds based on design process (diverge/converge, monitors, typed fragments, method prompts) help? Studies a16, b07, b08, c14, d07.

## 3. Core findings with exact numbers

Status key: E established (2+ independent sources agree), S single source, Fnd founding claim (no test), K = claim id in claims.jsonl.

| Finding | Numbers | Source (evidence id) | Status |
|---|---|---|---|
| Design is a third culture of knowing; five aspects | No data; conceptual, 7 pages | Cross 1982 (a01, a02) | Fnd, K01 |
| Architects work solution-first, scientists problem-first | Group sizes not obtained | Lawson 1979 via Wikipedia (a04, a05, b02) | Fnd, secondary |
| Nine experienced designers: co-evolution of problem and solution; solution space may be structured first | N=9, one task | Dorst and Cross 2001 (d16, c19) | S, K20 |
| Example images raise fixation | Midjourney +.32 (89% CI .11-.55, BF 124); image search +.27 (BF 42.5); N=60, 20 per cell | Wadinambiarachchi 2024 (a12, b03, c07) | S, K02 |
| AI image help lowers fluency and originality slightly | Fluency GenAI total effect BF 3.2; originality -.03 (CI -.06 to .00); 44% (206/468) AI images showed humanoid robots like the example | same | S |
| Fixation can move from the example to the AI output | 92 sketches; 39 prompts held no brief words | a13 | S |
| LLM output repeats itself (chairs) | Unique terms 67.4% ChatGPT vs 78.2% Red Dot; chair keywords per 100 cases 208.57 Red Dot vs 142.71 ChatGPT; N=10 users | Chen 2025 (a15, b04, c08) | E (K03) |
| Models repeat across models too (UI) | Cross-model originality 0.592 vs 0.764 human-model; creative range 0.581 vs 0.902; appropriateness over 90%; 15 models, 80 tasks | d15 | S, supports K12 |
| GPT-3 sets less varied than crowd | 12 prompts, 600 solutions; cosine to crowd 0.804 few-shot, 0.746 zero-shot with "unique"; lower convex hull | Ma 2023 (c09, c24) | E (K12) |
| Chatbots match mean human originality on AUT | B=-0.21, p=.218; 100 humans; 32.8 humans beat best chatbot averaged | Haase and Hanel 2023 (c10) | E (K12) |
| Anchoring on last option in a prompt list | Anecdotal, no counts | Egea 2024 (b23) | S |
| ChatGPT-4 directing a hackathon team placed 2nd of 6 | Dart range 14.8 m vs winner 37.66 m; 97 prompts, 108 codes | Egea 2024 (b05) | S |
| Frontier LLMs show action fixation on MUTATE | Claude Sonnet 4.6 30/56 (53.6%), GPT-5.4 25/56 (44.6%), Qwen3-235B 22/56, Llama-4-Maverick 13/56, Scout 7/56, humans 44.75/56 (79.9%) | b12 | S, K03 |
| Splitting diverge from select helps | GPT-5.4 base 27/56 (48.2%) to ReDNA 38/56 (67.9%); Self-Refine 29/56; EscapeAgent 35/56 | b12 | S |
| LLM helps reframing? No | GPT-4o, 3 modes; 456 recruited, 280 analysed; all p>0.05; 93 of 218 reported problems (31 not novel, 14 repetitive, 12 not useful) | Shin 2025 (a09, a11) | S, K05 |
| LLM widens expert-novice reframing gap | Experts +12.54% novel frames, t=2.70, p=.01; free-form gap 20.84% (p=.06) | a10 | S |
| Experts reject AI output, novices copy it | 7/10 and 8/10 noticed repetition; only 2 of 10 edited prompts | Chen 2025 (c22, b22) | E (K11) |
| Separate monitor beats self-monitor beats plain loop | Capacity Ah: RWL 72.07 (SD 20.52), SRL 106.08 (45.60), CRDAL 141.17 (48.45); F(2,86)=21.606, partial eta2 .334; RWL vs CRDAL d=1.846; RWL vs SRL d=.956; SRL vs CRDAL d=.746, p=.005; 30 runs each; steps 9.07/9.10/9.37, p=.97 | Xu 2026 (b06, c11, d01; a16 corrected) | S, K04 |
| CRDAL changes where designs land | Over 6048 cells: RWL 0, SRL 9, CRDAL 20/30 (mode 8100) | c26, c11 | S |
| CRDAL cost not compared at equal tokens | Matched on steps; monitor adds a call per step | d01 | S |
| Divergent persona raises self-rated creativity; convergent persona does not | 3.65 vs 2.76, g=.69, p=.003; convergent 2.70 vs 2.76, p=.837; N=101 logs (69 vs 32); originality (cosine) .34 vs .28; within-person diversity .59 vs .59 | Rosenbaum 2025 (b07, d06) | E in claims file (K06); see caveats in section 5 |
| Two-mode diverge/converge tool beat ChatGPT | N=24; CSI p<.002; UMUX 81.25 vs 64.24; clusters 2.88 vs 2.04 (p=.021) | Wen 2026 (c14) | K06 |
| Diverge-then-converge prompt, no human | ~12 vs ~8 distinct high-utility tasks at K=50, Wilcoxon p<.001; novelty win rate 96.67%; validity 1.00 vs 0.78; Qwen3-235B | d07 | S, K17 |
| Naming a design method beats control on novelty | Top-5 novelty roughly +10% to +41% (TRIZ +35.6, C-K +40.3, read from a figure; approximate) | IDEAFix (b08, b17) | S, K07 |
| Simple "avoid the obvious" matches methods; C-K, SCAMPER, brainstorming did not beat control | Novelty p: AI-specific 1.16e-34, TRIZ 2.24e-44, Design Thinking 2.16e-2, Scenario 1.18e-2, C-K .104, SCAMPER .281, Brainstorming .082; method prompts cut list length to ~10 vs 19-24 | d05 | S, K15 |
| Design-thinking pipeline with retrieval | IO < CoT < DoT; vs humans p=0.89; 6 raters (Kendall W .90-1.00); 4 tasks; 1,603 prototypes, 1,129 products | Miao 2024 (a17, b11) | S, K08 |
| Problem-driven vs solution-driven prompts shift process | Formulation 31.7% vs 16.3% (t=8.489); Structure 10.6 vs 29.3; 10 runs per cell; coders agree 79.5% | Zhang 2025 (c03, c04) | S, K09 |
| Abduction mediates AI creativity gain | Midjourney +27.2 abduction units (p<.01); +0.058 creativity per unit; direct effect after control -0.833; N=20 (5 per cell) | Guo 2024 (c01, c02) | S, K10 |
| Fragmenting, delaying AI output makes it material | NexusAI N=14 out-degree 0.98 vs 0.30, p=.004; frustration 2.43 vs 4.36; friction study 6 designers | b09, c15, c16 | S, K13 |
| Editable reasoning units help | N=20; controllability t(19)=3.65, p=.002; SUS 77.6 vs 69; expert quality p=.004 and .006 | DesignerlyLoop (b10, a19) | S |
| Models judge better than they generate | Weak model choosing from pool +1.04 to +1.09; own best-of-4 only 4.16 to 4.57 vs 4.43 random pool pick | RE-SEARCH (d09) | S, K18 |
| Option map as external input | Up to +1.25 points, largest for lowest scorers (r=-0.74) | d10 | S |
| Typed recombination beats prompted GPT-4o on novelty | 3.53 vs 3.146 (p=.0009); 3.612 vs 3.141 (p=9.2e-8); similarity .387 vs .659 | Dish COVER (d11) | S |
| Same-model peer debate costs more, gains little | 2.1 to 3.4 times tokens; Ministral GSM-Hard base 24.7%, debate 20.7%, self-correction 48.3% | d03 | S (matches G9) |
| At 16 generations, sampling beats loops and debate on maths | Qwen2.5-7B MATH500 SC 81.3 vs SR 71.5 vs MAD 78.1 | d04 | S |
| Reflection gains need knowing the answer was wrong | Baseline .786, Retry .827 (+.041), Explanation .876, Solution .925; 1,000 questions, 9 LLMs | Renze and Guven (d02) | S |
| LLMs anchor too | 22% to 61% of questions anchored | d12 | S |
| Many AI examples widen group diversity, not individual creativity | 800+ people, AUT | d13 | S |
| Order of AI use shapes uptake | Final designs covered 90.7% human-derived concerns vs 68.8% AI-derived; N=21 | d14 | S, K19 |
| LLMs frame gaps narrowly | Bridge framing 47.1% to 64.2% vs 12.1% human | d08 | S |
| AutoTRIZ contradiction match | 7/10 textbook cases in top 3; BTMS efficiency up over 60%, one co-author check | Jiang 2025 (c13) | S |

## 4. Mechanisms and models

Each model below is written so an engineer could build it. None is verified as a gain for our agent; see section 7.

**M1. Solution-first conjecture loop (Lawson, Darke, Cross).**
1. Take the brief. Do not enumerate requirements fully.
2. Pick a "primary generator": one concrete candidate solution.
3. Test it against the check (code or validator). Record which constraints it broke.
4. Use the broken constraints to restate the problem (add a requirement, drop one, split one).
5. Generate the next candidate under the restated problem.
Stop by budget or by a passing check. This is propose-and-test with problem learning from feedback. It maps to S3, S4, S5 and O8. Boundary: needs a check. Without one, step 3 is empty and the loop has no stop rule (a06, a21).

**M2. Co-evolution state (Dorst and Cross; Maher and Poon).** Keep two stores: problem frame (list of requirements and the current reading of them) and solution set. Tag each move P->S or S->P. A "bridge" is a candidate that satisfies the current frame in a way that also changes the frame. Zhang 2025 coded GPT-4o runs this way (Function-Behaviour-Structure coding, P-S index): the model held focus on one space and did not shuttle like humans (c03, c25). So code must force the cross-space move, not hope for it.

**M3. Anchor control for generation (Jansson and Smith; Wadinambiarachchi; Egea).**
1. Before generating, have code list the features of any example or prior candidate.
2. Generate each new attempt in a fresh context that shows no other attempt (already S3).
3. After generation, code computes feature overlap with the example and with ALL earlier attempts, not only the first (a13: fixation moved to the AI output).
4. Shuffle or summarise option lists in the prompt (b23: model fixated on the last item).
5. Re-sample if overlap is above a threshold.

**M4. Separate monitor (CRDAL, Xu 2026).** A second agent, with a different role and its own view of the trajectory (trend, design-space region), reads progress after each step. It names fixation and pushes exploration. An external validator, not the agent, decides success (c12). Costs one extra call per step (d01). Risk: tension with G1 (doubt only on a signal) and G9 (no debate). Resolution to test: make the monitor fire only on a code-detected plateau, and compare at equal tokens.

**M5. Diverge/converge separation (ReDNA, Geneplore, HAICo, CreativeDC).** Two phases with different prompts. Phase 1: wide, no judging, remote associations. Phase 2: narrow, apply constraints, select. ReDNA moved GPT-5.4 from 27/56 to 38/56 (b12) and CreativeDC from ~8 to ~12 distinct good items (d07). Rosenbaum's convergent null (p=.837) and the unablated stage in d07 are the caveats. In our schema the selection step stays in code (G5, G8).

**M6. Typed idea fragments (NexusAI).** Store each idea as What / How / Value, at several abstraction levels. Recombine fragments by code. Dish COVER (d11) did the code-side version: typed trees, code recombination, text rewrite; within-model similarity fell from .659 to .387. Maps to memory and O7 (map an analogue). Not tested as agent memory.

**M7. Design codes (Cross aspect 4; Canvil).** Two-way translation between an abstract requirement and a concrete artefact. Implement as two checked functions: requirement -> concrete spec, and artefact -> list of requirements it satisfies. A mismatch between the two is the revision signal (a20, [V]; formative interviews only).

**M8. Method labels vs plain constraint (IDEAFix).** Compare: control; one line "go beyond obvious answers, include wild directions"; TRIZ script; C-K; SCAMPER. In IDEAFix the one-liner and TRIZ gave the large gains, C-K and SCAMPER did not beat control on novelty, and method scripts halved the list length (d05). So length is a confound; test per token.

**M9. Option map import (RE-SEARCH).** Give the agent a map of the space (5 to 7 dimensions, 4 to 6 approaches each; 20-42 candidates) or candidates from another model. Weak models gain most (d10). Models judge better than they generate (d09), which supports "generate with many draws, select by code".

## 5. What holds up

**Replications and failed replications of the founding claim.** None found (b19, d17, c21). Cross's own review is the only support for the set of five aspects. Dorst and Cross (N=9) qualifies solution-first. Treat the five aspects as design hypotheses (K20).

**Fixation.**
- Held: example exposure raises copying of the example's features. Jansson and Smith 1991 (four experiments, described second-hand, a14) and Wadinambiarachchi 2024 (N=60, BF 124) agree in direction.
- Not constant: when many AI examples were shown to 800+ people, group diversity rose and individual creativity stayed flat (d13). The AI-example effect depends on example type, measure and how many examples.
- Not checked: Sio, Kotovsky, Cagan 2015 meta-analysis (paywalled, effect sizes unknown, d18). The counterweight that examples can inspire is unread. Do not quote effect sizes from it.
- LLMs fixate too: chairs (a15), last-item anchoring in prompts (b23), numeric anchoring in 22% to 61% of questions (d12; reasoning models least affected), action fixation (b12).

**Reframing.** One large crowd test (a09, 456 recruited, 280 analysed, sized for 95% power at a medium effect) found no gain from GPT-4o for novelty or usefulness in three modes. It is laypeople with an LLM, not an LLM alone (K05). The structured Dorst steps gave no higher helpfulness. Process prompts in an LLM-alone setting did change process share (c03), but that is a different measure.

**Monitors and reflection.**
- One study (CRDAL, three evidence lines, one source) gives d=1.85 over a plain loop. Matched on steps, not tokens (d01). One task, one model.
- Counter-evidence: reflection gains depend on knowing the first answer failed (d02: Retry alone +.041); same-model debate loses at 2.1-3.4 times tokens (d03); parallel sampling beats loops at 16 generations on maths (d04). Together these match schema G2, G9, G11. A monitor is credible only if it is a different role, sees different information, or uses a code check (K16).

**Diverge/converge.**
- Direction holds across four studies (K06, marked established in claims.jsonl): Rosenbaum, Wen, ReDNA, CreativeDC. Caveats: Rosenbaum's divergent result is a self-rating and the human chose the persona (d06); the convergent persona showed nothing; CreativeDC had no stage ablation; HAICo compared a two-mode tool with plain ChatGPT, so interface and structure are confounded.

**Method prompts.** All method prompts beat control in one reading (b08) and several did not in the table re-read (d05). Do not treat method names as the active ingredient. The "long method script cuts list length" effect is a token-efficiency issue.

**Experts vs novices.** Experts reject, novices copy (c22). AI help widens the gap (a10). Consistent across three studies (K11, established). For an agent, the analogue is a code-side critic that forces reject-or-revise, since the model lacks an expert's judge (G5).

**Human-LLM creativity level.** Mean originality parity (c10: B=-0.21, p=.218) but lower variance in space coverage (c24, d15) (K12, established). The right use is wide sampling plus code selection, not trust in one draw.

**Interventions that worked:** structured diverge/converge, separate monitor (one study), typed fragments (human tools), option maps, process prompts for shifting problem/solution focus, ordering of AI input.
**Interventions that did not:** LLM reframing for laypeople, convergent persona, combining two AI tools (lower feasibility, c01), method scripts beyond the one-liner, same-model debate.

**Weak spots of the whole literature (critique.md):** most LLM studies are N=6 to 24 or single-paper; Wikipedia lines (a05-a07, a27, a29, b01, b02) are secondary; Guo 2024 has 5 per cell; Egea 2024 is a single run (rank 2 could be chance). Several IDEAFix numbers were read from a garbled figure and are approximate. a16 had swapped SRL and RWL means; the corrected table values (RWL 72.07, SRL 106.08, CRDAL 141.17) are used here.

## 6. Language models

**How they behave on design tasks.**
- Level: match humans on mean originality of divergent answers (c10), rated above crowd on feasibility and usefulness and below on novelty (c09), appropriateness over 90% in UI design (d15).
- Variety: lower than humans. Cross-model originality .592 vs .764; creative range .581 vs .902 (d15). GPT-3 convex hull lower (c24). Sets repeat after a few items (c09).
- Fixation: repeated themes in chairs (a15); last-listed option anchoring (b23); plateau fixation in a hackathon until told to pivot (b05); action fixation under blocking, 12.5% to 53.6% of path slots found by models vs 79.9% for humans (b12).
- Process: GPT-4o holds focus in one of problem or solution space; it does not shuttle like humans (c03, c25).
- Framing: LLM-alone gap framing is narrow (bridge 47% to 64% vs 12.1%, d08).
- Judging: models judge better than they generate (d09).
- Domain: AutoTRIZ found the right contradiction in 7/10 textbook cases within top 3 (c13).

**What changed behaviour, and by how much.**

| Change | Effect | Source |
|---|---|---|
| ReDNA diverge/select split (GPT-5.4) | 27/56 to 38/56 (+19.7 pts); Self-Refine +3.6 | b12, b18 |
| Separate monitor agent (Gemini 3.1 Pro, battery pack) | 72.07 to 141.17 Ah, d=1.85; steps same | b06 |
| Self-monitor | 72.07 to 106.08, d=.96 | b06 |
| Two-stage diverge/converge prompt (Qwen3-235B) | about 8 to about 12 distinct good items at K=50 | d07 |
| One-line "go beyond obvious" prompt | novelty p=1.16e-34 vs control; method scripts cut list length | d05 |
| Problem-driven process prompt (GPT-4o) | Formulation share 16.3% to 31.7%; novelty and completeness above baseline | c03, c04 |
| Typed recombination in code (GPT-4o recipes) | novelty 3.146 to 3.53 | d11 |
| Option map as input | up to +1.25 points, weaker models most | d10 |
| Candidates from another model, own choice | +1.04 to +1.09 vs 4.16-4.57 for best-of-4 on self | d09 |
| DoT design-thinking pipeline with retrieval | IO < CoT < DoT, equals humans (p=.89); retrieval confounded | b11 |
| Reasoning models vs anchoring | least anchored, but 36.7% anchored for DeepSeek-R1 | d12 |
| Same-model debate (10 small agents) | 2.1-3.4 times tokens; no gain over self-correction | d03 |

**Nobody has tested:** an LLM on Lawson's puzzle (d19); a reframing operator for an LLM alone (K05); typed fragments as agent memory (K13); CRDAL at equal tokens (K04).

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory = S9 and the problem-class store. Marks: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Anchor control on options and examples** [E that LLMs fixate and anchor; K03]. Part: S1 input hygiene, G4. Shuffle or summarise option lists; keep examples in a marked block; compute feature overlap with the example and ALL earlier attempts by code. Evidence: a15, b23, a13, d12, b12 (human-side fixation K02 is [S]). S1 and S3 already contain most of this. The addition is the overlap check against all prior attempts.
2. **Wide sampling plus code selection for open tasks** [E; K12]. Part: S3 open mode, G8. LLMs match mean originality and lose on variance, so many isolated draws and code picks. Evidence: c09, c10, c24, d15.
3. **Forced reject-or-revise on the first output, triggered by real output** [E; K11]. Part: G2, S5, G5. Novices copy, experts reject; the agent needs a code-triggered critic. Evidence: c22, a10, b22. Consistent with 4b: unstructured self-reflection does not work, so the critic must see check output.
4. **Keep diverge and select as separate steps, with selection in code** [E in direction; K06]. Part: S3, S7 (already present). Adds only an explicit rule: the generator never also selects. Evidence: b12, c14, d07, b07.

### Test first

Not established. Nothing goes into SCHEMA.md until its test passes (see UNKNOWNS.md).

| # | Item | Part | Status | Evidence ids |
|---|---|---|---|---|
| T1 | Separate monitor fired on a code-detected plateau | G1, S6, O8 | [S] | a16, b06, c11, c26, d01-d04; K04, K16 |
| T2 | One-line "avoid the obvious" constraint at S3 open mode, instead of method scripts | S3 | [S] | b08, d05; K07, K15 |
| T3 | Problem-first vs solution-first order; forced cross-space move | S1, S3 | [S] | c03, c04, d16, d19; K09, K14, K20 |
| T4 | Reframe operator O8 on an LLM alone | O8 | [S], contested (null in laypeople, a09) | a09, a10, d08; K05 |
| T5 | Two-stage diverge/converge with stage ablation | S3, S7 | [S] | d07, b07, d06; K17 |
| T6 | Typed idea fragments (What/How/Value) as memory | memory, O7 | [S] | b09, c15, c16, d10, d11; K13 |
| T7 | Option map or other-model candidates at impasses | O7, S3 | [S] | d09, d10; K18 |
| T8 | Order of consulting "model frame" vs "evidence" | G4 | [S] | d14; K19 |
| T9 | Abductive-move coding of traces as a diagnostic | S9 | [S], underpowered | c01, c02; K10 |
| T10 | Pivot-on-plateau rule | G1, S6 | [S] | b05 |
| T11 | Design-codes check (requirement and artefact both ways) | S4 | [S] | a20, a19 |
| T12 | Retrieval of distant precedent without the design-thinking frame | S3, O7 | [S] | a17, b11; K08 |

Reconcile with existing rules. T1 conflicts on its face with G9 (no debate) and G1 (doubt only on a signal): the CRDAL monitor fires every step. Our version must fire on a signal and its cost must be counted (G7).

## 8. Concrete tests on our bench

All arms at equal total tokens (setup cost counted, G7). Raters blind to arm; code metrics preferred.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 monitor | Verifiable design or code task with a numeric validator, 30 steps | plain loop; self-reflection; best-of-N; monitor on plateau signal; monitor every step | Final validator score; tokens; distinct design regions | Monitor beats plain by d>0.5 at equal tokens; if it only wins at equal steps, drop it |
| T2 constraint | 20 open briefs | control; one-line constraint; TRIZ script; C-K script | Distinct ideas per token (embedding clusters); code-distance novelty; list length | One-liner >= method scripts per token |
| T3 problem-first | Programmatic Lawson-style hidden-rule block puzzle plus 10 design briefs with a rubric | solution-first; problem-first; forced alternation | Steps to rule; pass rate on held-out arrangements; share of P<->S moves | Alternation best on hidden-rule items; shows whether the LLM probes or proposes |
| T4 reframe | Items where the first framing fails the check | no reframe; O8 on failed check; reframe always | Pass rate after revisions; frame distinctness | O8 on signal beats always; any gain over none only on hard items |
| T5 two-stage | 30 open briefs | one-shot; stage 1 only; stage 2 only; both | Distinct high-utility items at K=50 | Both about 1.5 times one-shot; ablation shows which stage matters |
| T6 typed memory | Multi-round idea tasks | flat notes; typed What/How/Value with code recombination | Code-distance novelty; valid-idea rate | Higher novelty at same validity (Dish COVER 3.146 to 3.53) |
| T7 option map | Impasse items | own best-of-N; outside map; candidates from another model | Pass rate | About +1 point on weak setups |
| T8 order | Briefs with a seeded wrong frame | frame first; evidence first | Share of concerns reaching final answer | Evidence-first reduces carry-over of a wrong frame |
| Anchor test (add-now 1) | Brief with a flawed example | with and without overlap check and "three structurally different options first" | Copied features vs all earlier attempts | Fewer copies, equal quality |

## 9. What does not transfer, and why

- **Sketching and non-verbal media (aspect 5).** Our agent has no sketch pad. Substitutes (diagrams, code, typed graphs) are untested. Sketch prompting even rated lower for expressing direction in a human study (a18; N=9).
- **Tacit "knowing how" (Ryle, a28).** If design knowledge is practice-bound and not writable as rules, a prompt scaffold may not hold it. No test either way.
- **Wicked problems with no stop rule (a06, a21).** The schema relies on checks (G3, G6). Open tasks need an outside stop rule, such as a budget.
- **Human fixation interventions.** Friction, tolerance for ambiguity, personality moderators (b24, c15) are about humans. For an agent the analogue is task type.
- **Human-facing interface results.** NexusAI, DesignerlyLoop, HAICo gains include usability and workload (b09, b10, c14). Those do not move model output.
- **Business "design thinking".** Cross 2023 separates it; effectiveness evidence is thin (b02). Do not import workshop rituals.
- **Self-rated creativity.** Rosenbaum's divergent result is a self-rating (d06), not output quality.
- **Layperson reframing.** Shin tested people using GPT-4o; the null may not describe an LLM alone, or a stronger model.
- **Debate-like monitors.** Same-model peers cost 2.1-3.4 times the tokens (d03). CRDAL transfers only if the second party differs in role or information.

## 10. Open questions

1. Primary numbers for Lawson 1979 (group sizes, scores) and full Dorst and Cross 2001 tables.
2. Effect sizes and moderators in Sio, Kotovsky, Cagan 2015 (when examples help or hurt).
3. Does an LLM show solution-first behaviour on a hidden-rule block puzzle (d19: no study)?
4. Does CRDAL replicate off battery design, with another model, at equal tokens?
5. Does a reframing operator help an LLM alone?
6. Is a one-line constraint as good as method scripts at equal tokens?
7. Do typed fragments as memory beat flat notes in an agent task?
8. Is there any independent replication or critique of Cross's five aspects (2020s design-research reviews)?
9. Does the diverge-only gain hold in agents, and which stage carries it?
10. How much of "AI raises fixation" is specific to image tools used without guidance?
11. Does Micheli 2019 show outcome evidence for design thinking in firms?

## 11. Sources

[V] opened this session; [M] snippet or citation only.

- [V] Cross (1982) Designerly ways of knowing (abstract page, refs), 2024 reprint ch.1. https://link.springer.com/chapter/10.1007/978-1-4471-7541-4_1 (a01, a03, a28). Original DOI https://doi.org/10.1016/0142-694X(82)90040-0 [M] (c20).
- [M] Lawson (1979) Cognitive strategies in architectural design, Ergonomics 22(1):59-68 (citation only; a03, a04).
- [V] Dorst and Cross (2001) reprint abstract. https://link.springer.com/chapter/10.1007/978-1-4471-7541-4_5 (d16). Original https://doi.org/10.1016/S0142-694X(01)00009-6 [M] (a08, c19).
- [V] Cross (1999/2024) Design cognition: results from protocol studies (abstract). https://link.springer.com/chapter/10.1007/978-1-4471-7541-4_7 (d17).
- [V] Wikipedia: Design thinking https://en.wikipedia.org/wiki/Design_thinking and Nigel Cross https://en.wikipedia.org/wiki/Nigel_Cross (secondary).
- [V] Shin et al. (2025, CHI) No evidence for LLMs being useful in problem reframing. https://arxiv.org/abs/2503.01631
- [V] Wadinambiarachchi et al. (2024, CHI) Effects of generative AI on design fixation. https://arxiv.org/abs/2403.11164
- [V] Chen et al. (2025) Understanding design fixation in generative AI. https://arxiv.org/abs/2502.05870
- [V] Xu, Martelaro, McComb (2026) Supervising Ralph Wiggum. https://arxiv.org/abs/2603.24768
- [V] Miao et al. (2024) Diamond of Thought. https://arxiv.org/abs/2410.06972
- [V] Wadinambiarachchi et al. (2026) Reviving reflection-in-action. https://arxiv.org/abs/2606.26626
- [V] DesignerlyLoop (2025). https://arxiv.org/abs/2511.15331
- [V] Canvil (2024). https://arxiv.org/abs/2401.09051
- [V] Egea et al. (2024) ChatGPT as an inventor. https://arxiv.org/abs/2404.18479
- [V] Rosenbaum et al. (2025) Scaffolding creativity. https://arxiv.org/abs/2510.26490
- [V] Carichon et al. (2026) IDEAFix. https://arxiv.org/abs/2606.00875
- [V] NexusAI (2026). https://arxiv.org/abs/2604.10575
- [V] MUTATE (2026). https://arxiv.org/abs/2605.28465
- [V] Guo, Yin, Sun, Chen (2024) co-evolution in human-GAI conceptual design. https://dl.designresearchsociety.org/drs-conference-papers/drs2024/researchpapers/306
- [V] Zhang et al. (2025) emulate cognitive styles. https://openaccess-api.cms-conferences.org/articles/download/978-1-964867-39-7_12
- [V] A framework for LLM-powered design assistants (2025). https://arxiv.org/html/2502.07698v1
- [V] Zhang and Qian (2025) From copilot to co-thinker. https://www.designsociety.org/publication/48753/from_copilot_to_co-thinker_situating_llms_in_the_designer_s_evolving_thinking_flow
- [V] Ma et al. (2023) Conceptual design generation using LLMs. https://arxiv.org/abs/2306.01779
- [V] Haase and Hanel (2023) Artificial muses. https://arxiv.org/abs/2303.12003
- [V] Jiang et al. (2025) AutoTRIZ. https://arxiv.org/abs/2403.13002
- [V] Wen et al. (2026) HAICo. https://arxiv.org/abs/2512.18388
- [V] Kocaballi et al. (2026) Drag or traction. https://arxiv.org/abs/2603.27550
- [V] Jiang et al. (2021) Data-driven design-by-analogy. https://arxiv.org/abs/2106.01592
- [V] Renze and Guven (2024) Self-reflection in LLM agents. https://arxiv.org/abs/2405.06682
- [V] Bertalanic and Fortuna (2026) The cost of consensus. https://arxiv.org/abs/2605.00914
- [V] Revisiting multi-agent debate as test-time scaling (2025). https://arxiv.org/abs/2505.22960
- [V] Nguyen, Tschiatschek, Singla (2025) CreativeDC. https://arxiv.org/abs/2512.23601
- [V] Chen, Zhao, Cohan (2026) Gap between human and LLM research ideas. https://arxiv.org/abs/2607.01233
- [V] Gao et al. (2026) RE-SEARCH. https://arxiv.org/abs/2611.14487
- [V] Mizrahi et al. (2025) Dish COVER. https://arxiv.org/abs/2504.20643
- [V] Huang et al. (2025) SynAnchors. https://arxiv.org/abs/2505.15392
- [V] How AI ideas affect creativity, diversity and evolution of human ideas (2024). https://arxiv.org/abs/2401.13481
- [V] Mokryn et al. (2026) AI as Anchor. https://arxiv.org/abs/2611.22740
- [V] Rusia et al. (2026) Design Creativity Bench. https://arxiv.org/abs/2610.11539
- [M] Jansson and Smith (1991) Design fixation (via a12). https://arxiv.org/abs/2403.11164
- [M] Sio, Kotovsky, Cagan (2015) Fixation or inspiration? https://doi.org/10.1016/j.destud.2015.04.004 (paywalled; d18, b14)
- [M] Micheli et al. (2019) Doing design thinking. https://onlinelibrary.wiley.com/doi/10.1111/jpim.12466 (403; b15)
- [M] Rittel and Webber (1973). https://doi.org/10.1007/BF01405730 (a21)
- [M] Schon (1983); Simon (1969); Darke (1979); Cross, Naughton, Walker (1981); Cross (2004); Maher and Poon (1996) https://doi.org/10.1111/j.1467-8667.1996.tb00323.x (a22-a26, c18)
- [M] IdeaForge (2026), abstract only, arXiv 2605.13311 (b20).
