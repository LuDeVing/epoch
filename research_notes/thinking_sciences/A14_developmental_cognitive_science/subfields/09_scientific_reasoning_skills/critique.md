# A14.09 Scientific reasoning skills: cross-check critique

## Numbers re-opened this session (full text or PDF, scratch under D:/research_scratch/A14.09)

| # | Evidence | Source re-opened | Result |
|---|----------|------------------|--------|
| 1 | a22 / a23: 11 LLMs, 45 turns, success 6% to 78%, mean 42% to 56% | arXiv 2604.02485 abstract and intro | Confirmed. Qwen3-32B baseline 0.41 confirmed in the results table. |
| 2 | c01-c03: 75% / 68% success, rho -0.779 (p=0.003), 27.3% positive tests, 59.2%, rho -0.937 | arXiv 2606.04751 | Confirmed. |
| 3 | c07, c10: DiscoveryWorld easy completion ReAct 0.38 / P+E 0.18 / Hyp 0.28; easy knowledge 0.25 / 0.11 / 0.34 | arXiv 2406.06769 results table | Confirmed. Unit-test average ReAct 0.60 / P+E 0.44 / Hyp 0.64 (table, 3 columns of score, completion, knowledge style); "60%+" in b19 is true only for some agents. |
| 4 | c27 / b24: 32.4%, 34.3%, o1-preview 42.2% | arXiv 2410.05080 abstract | Confirmed. |
| 5 | a24: active 0.69, passive observer 0.45, passive proposer 0.12; humans 9.6 / 6.4 tests | arXiv 2606.06464 | Confirmed. |
| 6 | a04: 39% of later CVS explained, N=170 | PMC7736087 | Confirmed. |
| 7 | a06: Schwichow 72 studies, g=0.61 | PMC7736087 intro | Confirmed as stated there, but it is second-hand. |
| 8 | b06: Kaiser reading vs generation | PMC6315139 | Text located; not fully re-derived. Treated as confirmed on spot check only. |
| 9 | a19: Klahr and Nigam about 77% vs 23% | Semantic Scholar, OpenAlex | NOT confirmed. Publisher hides the abstract. Stays "from memory". |
| 10 | a02/a03 Bramley 2022 figures | not re-opened | Left as the a-agent recorded them (opened:true there). |

## Corrections made
- a06: marked opened:true but its URL is the Peteranderl paper (PMC7736087). It was read as a citation, not the Schwichow paper. Treat as second-hand. Claim K03 counts it with caution.
- b19: "60%+ range per authors" is too broad. Unit-test averages in the table are 0.60, 0.44 (Plan+Execute), 0.64 (see row 3 above).
- a23: the row mixes a Wason table with another table (baseline 0.64 / TiO 0.56 appears for a different task or metric). Use only the Wason numbers, not the 0.56 in that table.
- a08 vs b09: same longitudinal paper with a different last author listed (Moeller vs Sobel et al.). One source, not two.

## Duplicates (counted once)
a05/a04 (Peteranderl); a07/b11 (Moeller 2022); a09/b07/b08 (Schlatter 2020); a08/b09 (theory of mind longitudinal); a22/a23; a24/a25; b17/c20 (ScienceWorld); b18/c07-c10/b19/b20 (DiscoveryWorld); b24/c27 (ScienceAgentBench); a27/b21/c15-c18 (BoxingGym); a15 (Coenen 2019) is a model feeding a01.

## Contradictions and tensions
1. One-at-a-time vs grouped tests: the classic CVS teaching goal (one change) conflicts with Bramley/Coenen, who show grouped tests win under sparsity. S4 "one change per test" is correct only when many causes are plausible or interactions are possible.
2. Discovery vs instruction: Klahr and Nigam (unverified) favour instruction; Kaiser found no benefit of self-generation, and Vollmeyer and Burns (cited) favour exploration for system knowledge.
3. Explicit hypothesis step: helps easy knowledge (DiscoveryWorld) but hurts hard completion; and Jhaveri's opposites prompt helps thinking models but not small non-thinking ones.
4. BoxingGym: reasoning-tuned models (OpenThinker) lost to instruction-tuned Qwen, but FalsifyBench shows reasoning models falsify more. Different tasks, not reconciled.
5. Test choice vs inference: children can choose well but infer badly (Bramley), while preschoolers recognise confounds but do not choose controlled tests (Moeller). The dissociation runs in opposite directions.

## Weak spots
- Founding studies (Chen and Klahr 1999, Klahr and Nigam 2004, Klahr and Dunbar 1988, Kuhn 1995, Tschirgi 1980) were never opened. All exact numbers for them are missing. a16 to a21 hold no usable figures.
- No failed replication of CVS-teaching effects was found; the only counter-evidence is Kaiser (n small, reading vs generation) and Freer (low-achieving gap).
- Several LLM studies are 2026 preprints with no replication (FalsifyBench, Jhaveri, Samiei, ACED). Prompt effects come from one lab each.
- Many LLM benchmark lines (c19 to c31) are only loosely tied to controlling variables.
- Evidence a08, b10, b14, b16 rest on citations.

## Seen only in snippets or abstracts
c20, c21, c22, c23, c24, c25, c30, c31 and b02, b04, b05, b10, b12, b14, b16.

## GAPS
1. Does a "vary one thing" rule in S4 improve an LLM agent at equal tokens on tasks with several plausible causes, and does it hurt on sparse-cause tasks where grouped tests win? (Direct decision for S4; needs a switch-box and a ramps item set.)
2. What are the real numbers in Chen and Klahr (1999) and Klahr and Nigam (2004) (sample sizes, percent mastering CVS, transfer rates)? They anchor the whole subfield and were not opened.
3. Do LLMs confound variables in developmental CVS items (ramps, springs, balls) and how does reasoning budget change it? No study found.
4. Does a counterexample or opposites instruction (Jhaveri) replicate on a non-thinking base model, and does it cost more than it gains at equal tokens?
5. Is there any replication or failure of Jhaveri's and Bertolazzi's 2-4-6 results by an independent lab, and do the effects hold on tasks beyond rule discovery?
6. How well do LLMs coordinate theory and evidence (Kuhn): do they keep a disconfirmed hypothesis, or change several variables at once, in multi-week style tasks?
7. What do Kuhn, Garcia-Mila, Zohar and Andersen (1995) and Kuhn's later microgenetic work report in numbers, and what failed to replicate?
8. Does handing the agent the outcome of its own earlier tests (Samiei's observer vs proposer gap) matter for batched test plans in S4?
9. Do any MicroDYN or complex-problem-solving studies test LLMs on vary-one-thing-at-a-time (Molnar and Csapo's setting)?
10. What explains the opposite dissociations between choice and inference across ages (Bramley vs Moeller)?


## Gap search results (evidence_d.jsonl, d01-d20; claims K22-K29 added)

Tools note: WebSearch quota was used up. Worked: PubMed efetch, ERIC API (abstracts), Europe PMC full text, WebFetch on arXiv abs pages and PDFs. Blocked or rate-limited: arXiv API, OpenAlex, most of Semantic Scholar search, publisher PDFs, PMC pages. Paywalled founding papers could be read at abstract level only.

| Gap | Status | What was found |
|-----|--------|----------------|
| 1. Does "vary one thing" help an LLM at equal tokens, and hurt on sparse-cause tasks? | Half closed. Still needs the experiment. | No equal-token study. But the boundary is now shown with numbers: Bramley (N=104) children switch to multi-switch tests on sparse boxes (60.7% older, first test) vs 39.1% on dense; LLMs fail AND (joint-cause) rules with one object per step (GX-Chen 2025, oracle solves all); Samiei shows successful agents move from 1-object to 2-object tests on conjunctive rules. Rule for S4: one change per test only when many causes are plausible; split-half when few. Item sets (switch box with sparse and dense, AND and OR) are still unbuilt. |
| 2. Real numbers in Chen & Klahr 1999 and Klahr & Nigam 2004 | Half closed. | Confirmed from PubMed: Chen & Klahr N=87, ages 7-10; Klahr & Nigam N=112, grades 3-4. Replications: Strand-Cary & Klahr N=72 (same lab), Lorch 2010 (797 to 848 children in 36 to 39 classrooms), Matlen & Klahr N=57. Percent mastering CVS and transfer rates were NOT found; **77% vs 23% remains unverified** (no open copy; CMU link 404; publishers 403). |
| 3. Do LLMs confound variables on developmental items; effect of reasoning budget? | Open. | No study found (ERIC, Europe PMC, PubMed, citation lists). Indirect: in the Blicket game more reasoning effort made conjunctive exploration worse (GX-Chen, o-mini series); in Jhaveri, thinking mode raised rule discovery more than any prompt on small models. |
| 4. Does the opposites prompt work on a non-thinking base model, at equal tokens? | Mostly closed (negative). | Instruct non-thinking models gain 0 to +17 points from the opposites prompt (Qwen3-8B 0.06 to 0.06; 14B 0.23 to 0.29; 32B 0.33 to 0.36; Llama-3.3-70B 0.21 to 0.38), and Dual-Goal lowers some. Tokens per turn are nearly unchanged for non-thinking (about 7 to 15). Thinking models gain more (Qwen3-32B 0.41 to 0.60) at about 40% more tokens per turn. No pretrained base model tested. |
| 5. Independent replication of Jhaveri and FalsifyBench | Closed as "none found". | FalsifyBench (different lab) does not replicate Jhaveri's prompts and argues Jhaveri ignores Klayman and Ha. Both find reasoning models falsify more. Citing lists: Jhaveri 9 papers, FalsifyBench 2; none replicates. Generalisation beyond rule discovery: only Jhaveri's Blicket distillation. |
| 6. Do LLMs keep disconfirmed hypotheses or change several variables at once, multi-session? | Open, partly informed. | Piriyakulkij 2024: LLMs revise hypotheses well but choose experiments no better than random in places (ReAct 4.60/8 vs humans 5.26 vs scaffold 6.55). ACED-Bench lists wrong intervention, lost evidence, no stopping. No multi-session Kuhn-style study. |
| 7. Kuhn et al. 1995 and later numbers; failed replications | Partly closed. | 1995: 17 community-college students and 15 fourth graders, strategies mixed, critique of stage story (ERIC EJ518579). 2009: 91 sixth graders; collaboration only a temporary help. No percentages in any abstract. Dean & Kuhn 2007 is the nearest failure-to-extend of the direct-instruction result. |
| 8. Do earlier test outcomes matter for batched plans? | Closed for the human case; untested for batches and LLMs. | Samiei full text: proposers saw another person's outcomes (0.12 object accuracy) vs own outcomes (0.69). Not the same as writing a batch then seeing results. Keep S4 sequential. |
| 9. LLM studies in MicroDYN or VOTAT settings | Open. | None found in ERIC, Europe PMC, PubMed or citing lists. arXiv search itself was blocked. |
| 10. Why do choice and inference dissociate in opposite directions (Bramley vs Moeller)? | Closed by correcting the premise. | Moeller (N=57, ages 3-6) found some above-chance recognition and some above-chance controlled-test choice, but unrelated to each other; it is not a clean reversal of Bramley. Task differences remain: Bramley asks for the one working switch with a payoff, Moeller asks forced-choice controlled tests in knowledge-lean tasks. |

### Changes made to claims.jsonl
- K05 stays contested and now names the replications (Strand-Cary, Lorch) and the qualifications (Dean & Kuhn, invent-then-tell tie, Kaiser). 77/23 still unverified.
- K02, K07, K11, K12, K13, K19 extended with the new numbers and corrections.
- New: K22 (disjunctive bias, one object per step), K23 (outcome-aware choice), K24 (task segmentation and the one-factor suggestion), K25 (two halves of CVS), K26 (invalid-design examples), K27 (LLMs pick experiments poorly), K28 (Kuhn 1995, abstract-level), K29 (no independent replication of the opposites effect).

### Cautions for the next reader
- Most d-lines for the founding developmental studies are abstract-level (PubMed or ERIC), marked opened:true because the abstract page was read, but no cell-level numbers were seen.
- d15: the thinking-mode table lost its row labels in text extraction. The thinking cells were matched to Table 2 by turn counts; the non-thinking cells are clean.
- d13: per-model Q&A percentages are only in figures, so none are quoted.
- d19 is an absence check (opened:false) done under rate limits.
