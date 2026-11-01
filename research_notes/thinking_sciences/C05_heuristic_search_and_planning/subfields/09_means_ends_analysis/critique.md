# Critique: Means-ends analysis (C05.09)

## Checks done this session (sources re-opened, text extracted with pdftotext)
Confirmed exactly: Tree of Thoughts Game of 24 (7.3/4.0/9.0/45/74); PlanBench v4 (GPT-4 206/600 = 34.3%, InstructGPT-3 41/600; Mystery deceptive 26/600 = 4.3%; randomised 12/600); o1 paper (587/600, 340/600, Mystery 317/600 = 52.8%, randomised 224/600 = 37.3%, Fast Downward 0.265 s); Chain of Thoughtlessness (3.83, 59.3, 51.3, 6.89); Lawsen (10 tokens per move, 12-13 disks at 64k, under 5,000 tokens for N=15); MAKER cost table (gpt-4.1-mini .0022, k=3, $3.5K; haiku-4.5 .1839, $71.2K); RAP (1.00/0.86/0.26, 1.00/0.88/0.42, 64%); Apple paper (N=5 31 moves, River Crossing N=3 11 moves, move 100 at N=10); Li and Kingsford 2026 (arXiv 2610.24928) Table totals 77.8/85.0/94.5, nonlinear 33.3/55.3/87.4, Gemini 82.0, CoT pass@3 86.8 and 67.2, ablation 90.5/91.0/76.0/75.1.

## Corrections
1. a22/b02: the PlanBench table prints "14/600 (0.23%)" for Instruct-GPT3 on Mystery deceptive. 14/600 is 2.3%, so 0.23% is a typo in the paper. The evidence line copied the typo.
2. Mystery Blocksworld GPT-4 numbers differ by paper version: PlanBench v4 gives 26/600 (4.3%), while c24 (Planning Abilities, later version) gives 1/600. These are different prompts and versions. Never merge them. In the arXiv 2302.06706 copy fetched here, the table is GPT-3 family only (GPT-3 6/600, InstructGPT-3 41/600, BLOOM 4/250), matching a23.
3. a21/b07/c14 list the same MAKER numbers three times; the three are one source. Likewise b08, c06-c08 are one paper (MAP), and a27/b09/c30 are one paper (ToT). I counted independent sources honestly in claims.jsonl (several claims drop to single-source versus the evidence agents' count).
4. c13: "41% to 73%" is optimal solves on 81 configurations, not a failure-conversion rate; the 52% is the weakest-setting conversion. I kept both distinct in K16.
5. a20 vs b06 vs c11 agree; but the Lawsen test was preliminary and non-peer-reviewed; "contested" is the right status.

## Contradictions between sources
- Apple (collapse is a reasoning limit) vs Lawsen (token limit plus impossible River Crossing instances). Partly resolved: output budget explains N>=12; Apple saw collapse near N=9 so early stopping also occurs. MAKER shows execution is possible with voting. No clean verdict.
- Algorithm-given experiment (a19) says execution fails even with the algorithm; Lawsen says a function output succeeds. These test different things (full move list vs generator).
- Hanoi "template-friendly" (c17, holds longest) vs c16 (policy reuse of seen continuations): suggests success on Hanoi can be memory, not search.
- GPT-5.4 gains nothing from MEDAKA; Claude and Gemini gain 10-50 points. Model-dependence unexplained.

## Weak spots
- The core of the subfield (Newell and Simon 1959/1961/1972, Ernst and Newell 1969, Sweller 1983/1988, Owen and Sweller 1985, Vollmeyer 1996, Kotovsky 1985, Atwood and Polson 1976) is NOT opened: 20 of the 98 evidence lines are unopened and have no numbers. The "founding studies with exact numbers" requirement is unmet.
- Only one direct test of means-ends analysis as an LLM prompt (Li and Kingsford 2026), single group, synthetic water-vessel tasks, thinking mode off. No replication.
- Most "MEA" LLM studies actually test decomposition or search, not difference reduction itself. Evidence for the specific difference-driven operator choice is thin.
- Human goal-free effect: only seen through a review page listing citations. The meta-analyses (b20, b21) come from low-visibility venues and measure teaching models.
- Hanoi results depend on tokenizer and output format; many are preprints.
- b13 (72% bottleneck) is a secondary citation of the human data.

## Seen only in snippets or secondary pages
a01, a02, a03, a06, a09-a17, b20-b30, b32, b33 (no primary text); Wikipedia pages (a04, a05, c22, c23); c31 (ALFRED 20%) only headline.

## GAPS
1. Does the gap-driven step (measure difference, choose operator, recurse on preconditions) help when the base model already has long-form reasoning (GPT-5.4 showed no gain)? Needs an equal-token test on our agent with thinking on and off.
2. What are the actual numbers in Newell and Simon's protocol studies (GPS vs thinking-aloud subjects: percent of match, number of subjects, tasks)? Open Newell and Simon 1972, Ernst and Newell 1969.
3. What are the effect sizes and boundary conditions for goal-free versus goal-specific problems (Sweller and Levine 1982, Owen and Sweller 1985, Ayres 1993, Vollmeyer 1996), and did Vollmeyer find that systematic strategy rather than goal-freedom explains it?
4. Which part of MEDAKA matters beyond state tracking: operator choice by gap size, or recursion? Does it transfer from continuous water-vessel tasks to discrete tasks (Blocksworld, Hanoi, code)?
5. How should O5 handle interacting subgoals (Sussman anomaly)? Is there an LLM study that measures protecting achieved goals or goal ordering, and its gain at equal tokens?
6. Does per-step voting or verification (MAKER, LLM-Modulo) beat simply increasing reasoning budget at equal tokens, for which step types?
7. How much of LLM success on Hanoi and Blocksworld is memorised patterns (c16, c17)? What do obfuscated variants show for scaffolded agents versus plain ones?
8. Are there independent replications of ADaPT-style as-needed decomposition against always-decompose, and what does decomposition cost in tokens?
9. Do human bottleneck-aware subgoal choices (Correa 2023, Donnarumma 2016) improve LLM subgoal choice when used as a selection rule?
10. Is the large human-learning meta-analytic effect of MEA teaching (1.431, 0.920) supported by any high-quality study, or should it be dropped?

## Gap search results

Constraint: the WebSearch quota was exhausted at the start, and OpenAlex, Semantic Scholar and arXiv search returned 429. Publisher sites (Wiley, ScienceDirect) returned 403. I used direct arXiv, PLOS and Crossref fetches. Evidence is in evidence_d.jsonl (d01-d21; d09 and d21 are opened:false). New claims K26-K30; K19, K20, K22, K23 updated.

Closed (as far as this session can close them):
- Gap 6 (voting/verification vs more budget): mostly closed. Singhi 2025 (d11): at equal compute, majority vote beats LLM generative verification until about 8x compute, wins by 3.8% only at about 128x. Exact external verifier is different: o1-preview hard Blocksworld 23.65% to 98.2% at about 2.7x cost (d14). MAKER (d10) has no equal-compute test. Rule: more samples for soft checks, exact checks for rule-checkable steps. Not tested on step types beyond Hanoi moves and math.
- Gap 10: effectively closed by dropping. No full text or quality information was reachable; K23 status set to dropped-unsupported.
- Gap 4: closed as "untested". Only state tracking and recursion were ablated (d01); operator choice by gap size and discrete-domain transfer were never run in the paper.
- Gap 7: partly closed. Renamed/obfuscated variants cut plain GPT-4 from 34.3% to 4.3% and 2% (d15); counterfactual tasks show mixed recall and reasoning (d18). No scaffolded-vs-plain renamed comparison exists in what I read.

Partly answered:
- Gap 1: no equal-token thinking on/off test of MEA exists. Indirect evidence says little gain: GPT-5.4 tied AoT+ with MEDAKA at 78.5, thinking was off in the paper (d03); generic CoT on reasoning models gave +2.9, +3.1 and -3.3 points (d04); thinking vs non-thinking at matched tokens shows no edge at low complexity (d05). Needs our own run.
- Gap 3: mechanism answered in words, numbers still missing. Vollmeyer 1996 abstract (d06): specific goals push difference reduction and less systematic testing; systematic rule-induction instruction helped under both goal types. So strategy is the mediator. Effect sizes for Sweller and Levine 1982, Owen and Sweller 1985, Ayres 1993 not obtained (d09). One classroom study (N=111) found far-transfer gain but higher load (d08).
- Gap 9: Donnarumma 2016 primary confirms 72% one-bottleneck choice (d19). No LLM test of a bottleneck rule found.
- Gap 5: no LLM study of goal ordering or protecting achieved goals was found. PlanBench shows about 39% of GPT-4 Blocksworld plans miss the goal even under relaxed checks (d15), and exact verification fixes much of it (d13, d14). Treat the Sussman handling as an untested design choice.
- Gap 8: ADaPT re-read (d16) has no always-decompose ablation and no token cost; no independent replication found. The only measured cost of a MEA-style scaffold is MEDAKA at 1.8x-3.8x CoT tokens (d02).

Still open:
- Gap 2 (Newell and Simon 1972 and Ernst and Newell 1969 numbers): not reachable. The archive.org full text returned only menus and the RAND report returned 403. K24 stays unverified. Do not quote protocol match rates.

Correction to the cross-checker: the PlanBench "0.23%" typo is not in the critical-investigation version I read (d15 prints 14/600 as 2.3%). It may be in another version; keep versions separate.
