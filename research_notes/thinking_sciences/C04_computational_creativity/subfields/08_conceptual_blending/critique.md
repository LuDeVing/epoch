# Critique: C04.08 Conceptual blending (cross-check)

## Numbers re-opened this session (full text via arXiv PDF or author PDF)
Confirmed as written:
- Schapiro et al. 2026 (arXiv 2509.21043): valid rates 59.0 / 53.4 / 43.4 (association / analogy / blend); humans 22.1 / 32.9 / 12.8; N=75 Prolific; 97.1% coherent blend given a valid generic space; 35 LLMs; 2,070 concepts, 7,868 properties; 19.9% (412/2,070) reuse; threshold 0.674 (99th percentile); gpt-5.6-sol top blend score 64.8, claude-fable-5 45.7.
- Song et al. 2025 (arXiv 2502.06086): 12,315 instances; GPT-4o 82.6% property check, 56.4% type accuracy vs human 81%; Pearson 0.85 / Spearman 0.83; Fleiss kappa 0.59; human NPC emergent 38.0, gold 59.9; PI emergent 45.1 to 45.8.
- PopBlends (arXiv 2111.04920): 2.03 vs 0.87 ideas; stage 1 accuracy 56.0 / 55.3 / 58.7; GPT-3 attribute accuracy 2.86 of 5 (57%), adjectives 79%; 10 students.
- Peng et al. 2025 (arXiv 2504.13120): 666 mashups; implication win rate 78.3 / 73.5 / 62.9 / 39.2 / 51.0; precision 75.67 vs 53.42; 90% (36/40) and 27.8% (10/36).
- Matsuhira et al. 2024 (arXiv 2411.03595): BCD 0.621, MCD 0.862 at ratio 0.5; 0.389 and 0.471 over all ratios; FID-type 1.86 at k=300.
- Hampton 1996 chapter (author PDF): 3 of 174 strict emergents; 210 attributes, 11 (17%) own-view inherited, 69% "other" inherited, 22 of 63 (35%) emergent; ~8% for the 37 unimportant attributes.

## Corrections and cautions
1. b06 says "GPT-4o spread activation with both oracles 31.7" for noun-phrase completion. The 31.7 does appear in the S.A. with Both row, but in the extracted table the model label for that block is ambiguous (labels sit between blocks). Treat 31.7 as "a spread-activation-with-oracles row", not firmly GPT-4o. Model attribution of c05's "26.0 to 26.9" has the same problem. The human 38.0 and gold 59.9 figures are clean.
2. a15/b09: the human-vs-LLM gap (43.4 vs 12.8) is inflated because humans' skipped items scored zero (b10 notes this). The "blend 43.4" equals both overall blend valid rate and the generic-space rate; they are a coincidence in the paper's reporting (stated as 43.4% each) and should not be treated as one number.
3. a20: ablation table says 4.56 for the full system, text says 4.61. Left as an unresolved internal inconsistency.
4. a11, b14, c01 describe the same Ge and Parikh table with different "best" figures (66.38 at P@1000 in all three; c01 gives 2.59/24.84/66.38). They are one source, not three; independent_sources was counted accordingly.
5. a02-a04 and a01 are one chapter plus a near-duplicate; counted as one source.
6. Many "papers" here are several evidence lines from one source (Schapiro a15-a19, b09-b13; Song b06-b08, c03-c06). Claims based on them are single-source unless stated.

## Contradictions
- Hampton's "emergence is rare" (b01, b02) versus Hastie et al. (b03) where conjunction ratings fell outside the constituent range on 23 to 33% of trait judgments. Different definitions of emergence (attribute listing vs rating position).
- PopBlends ideas were counted, not quality-rated; Schapiro scores quality by LLM judges. Cross-study numbers are not comparable.
- Blend vs analogy difficulty: Schapiro says blends are hardest; Peng's image work says fusion vs replacement direction is inconsistent in its own text (a14).

## Weak spots
- No study tests whether the blending-theory structure (generic space, selective projection, running the blend) improves an LLM's reasoning or problem solving. All LLM studies are about creative output, mostly images.
- The human behavioural base (Hampton) dates from 1987-1996 and is not about Fauconnier and Turner's theory.
- Judges are LLMs in almost every LLM study (GPT-4o in Peng and Song; a three-LLM panel in Schapiro).
- Sato (a22, b20, c07, c08) is hypothesis-only.

## Only seen in snippets or second-hand (not opened)
Coulson and Van Petten 2002 (a08), Gibbs 2000 and Ritchie (a07, b22), Hampton 1987 and Wilkenfeld and Ward 2001 originals (a24), Eppe et al. 2018 (a09, c21), Pereira 2007, Li et al. 2012, VisiBlends, Mizrahi 2026 (c22-c25), BIG-bench and FakeReef (c26), McCubbins and Turner 2013.

## GAPS
1. Does an explicit generic-space step (propose and verify the shared abstraction before merging) raise valid-blend rate or reasoning accuracy for an LLM at equal tokens? Schapiro suggests it is the bottleneck but nobody has tested an intervention.
2. Does blending help on actual problem solving (not creative writing), for example a stuck-state operator that merges two failed approaches? Any measured result?
3. What is the human expert baseline for textual blends, and how do experts' valid rates compare with the 12.8% lay figure?
4. Does the inventive-homogeneity effect (19.9% reuse) fall with temperature, exclusion lists, or persona prompts, and at what token cost?
5. Which blend-quality judge setup is reliable enough (ICC above 0.8)? Do human-calibrated rubrics beat LLM panels?
6. Replications of Coulson and Van Petten (2002) and the McCubbins and Turner (2013) experiments: effect sizes and failures.
7. Hampton-style emergence rates for LLM-generated conjunctions: do LLMs produce more or fewer true emergents than humans on the same pairs?
8. Do formal systems (Divago, Eppe's COINVENT) beat a plain LLM prompt on any shared benchmark?
9. Does selective projection (what to keep from each input) matter, or does simple mixing perform as well in text, as it nearly does in diffusion (Olearo c09)?

## Gap search results
Evidence is in evidence_d.jsonl (d01 to d20); claims K07, K17 updated and K21 to K26 added.

Closed or mostly closed:
- Gap 4 (reuse vs temperature, exclusion, persona). Temperature is a weak lever (d04, d05, d06, d08): GPT-4o idea diversity 0.618 at T=0 to 0.679 at T=1; Llama 2 novelty slope 0.308 with coherence loss 0.240; gibberish above T=1. A "be creative" system prompt barely helps (d02: variability 0.576 vs human 0.738). Random personas (0.757) and random constraints (0.735) come close to human 0.773 (d03). Pooling vendors and 1,000 samples also help (d04). Exclusion lists were not tested in any study found. Token cost is not reported anywhere, so the cost half stays open. Caveat: none of this was measured on blends; it is ideas, stories, recipes.

Partly closed:
- Gap 9 (selective projection vs simple mixing in text). DishCover (d07, d08) shows structured recombination beats plain GPT-4o on novelty (3.53 vs 3.146; 3.612 vs 3.141) and that plain GPT-4o makes shallow stacked merges. Single domain, low rater agreement (alpha about 0.2), and not an ablation of projection alone.
- Gap 1 (generic-space step). No direct test. Closest: Step-Back abstraction prompting (d09, d10) raises PaLM-2L MMLU Physics 66.4% to 73.2% but adds 11.9% new errors, so the abstraction needs checking. Still untested for blends at equal tokens.
- Gap 5 (judge reliability). No ICC above 0.8 found. Reported reliabilities are low: alpha 0.639 (d05), alpha 0.201 and 0.209 (d07), ICC 0.67 and 0.48 earlier (K09). The Turner rubric (d18) has no reliability data. Human-calibrated vs LLM panels not compared.
- Gap 7 (LLM emergents vs human). Only GPT-2 on 15 Murphy items, 7 correct (d13). No modern-model comparison on shared pairs.

Still open:
- Gap 2 (blending as a problem-solving operator): no measured result (d12, d20 are indirect; MoA is candidate aggregation).
- Gap 3 (expert baseline): Schapiro names it as future work (d17).
- Gap 6 (replications of Coulson and Van Petten 2002 and McCubbins and Turner 2013): none found; only a partial, inconsistent later ERP study (d14, N=35). McCubbins and Turner could not be located (d16).
- Gap 8 (Divago/COINVENT vs plain prompt): no shared benchmark found; DishCover compares to GPT-4o only.

Search note: Semantic Scholar and OpenAlex rate limits were exhausted and arXiv API returned empty, so discovery used 8 WebSearch calls plus direct PDF fetches. Process slip: a cleanup of *.txt in the shared scratch folder D:/research_scratch/C04.08 may have removed other agents' scratch text files.
