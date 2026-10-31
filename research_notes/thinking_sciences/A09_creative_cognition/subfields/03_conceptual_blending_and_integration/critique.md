# A09.03 Conceptual blending and integration: cross-check critique

Checker pass, 2026-10-31. Texts re-opened from D:/research_scratch/A09.03/ (pdftotext).

## Numbers re-opened and confirmed
1. KOMBINE (arXiv 2509.21043): 43.4% valid blends, 97.1% coherent given a valid generic space, 19.9% (412/2,070) repeats, 37.3% vs 2.6% (14.3x), 94.7% vs 36.3%, same-provider 9.3% vs 4.1% (2.3x), r=0.71/0.70/0.54, 64.8% top, judge agreement 66% / 75% unanimous (n=96). All confirmed.
2. PopBlends: 56.0/55.3/58.7%, best-of-five 90.0/96.6/93.3%, 98.3% scenes, 2.03 (SD .84) vs 0.87 (SD .56). Confirmed.
3. Peng et al. IEI: 75.67/85.00, 53.42/70.33, implication 73.5/51.0/78.3/62.9/39.2, ranks 1.98 vs 2.40, win rate .26 to .35, prompt length 487.95 vs 514.53, 27.8% (10/36). Confirmed.
4. Beyond Pixels: 100 participants, 45 images per method, 4.47 vs 3.62 etc., 64.44/67.11/72.89/76.22%. Confirmed.
5. Hampton 1996 review: 3 of 174 (strict), 23%/33%, 210 attributes, 11 (17%), 55 (69%), 22 of 63 (35%). Confirmed.
6. Coulson and Van Petten 2002: 18 adults, 165 triplets, ratings 1.4/1.9/4.4, linear F(1,17)=6.86 p<.02. Confirmed.
7. Si et al.: 49 per condition, 298 reviews, 4.84 / 5.64 / 5.81. Confirmed.
8. Misty: 14 developers, 103 operations, 34.95% and 33.98%. Confirmed (3.2/5 not re-checked).
9. Sato 2504.21012: fused vs non-fused showed no significant difference. Confirmed; evidence a20 under-reports it (it is a negative result for fusion, see c21).

## Corrections
- **CCPT (Song, Lee, Ahn, Sung, Kim 2025) was misread in b23.** Author is Song et al., not Li et al. The table has, for each LLM, a top row and a "Base" row plus CoT and spreading-activation (S.A.) rows. b23 took the top row (GPT-4o E 40.8, 55.5, 20.4) as the base and reported gains of +5.0, +7.8, +6.5, which mixes a top row with S.A.-with-LLM only. The c19 reading is the one to use: GPT-4o emergent induction E: base 42.4, CoT 43.8, S.A. with LLM 45.8, S.A. with LLM and ConceptNet 57.8 (gold 58.4); noun-phrase completion base 23.1, CoT 25.5, S.A. with both 38.9. So the scaffold gain is about +15 points, chain-of-thought about +1. Caveat: the pdftotext table lays out the "Multi-Oracle" label in a way I could not map with certainty to a row, so the meaning of the model-name row versus the Base row remains uncertain. Both readings agree that S.A. with both is best by 15 to 17 points. Human 38.0 and gold 59.9 on completion are confirmed. b23's "o1 base 32.6" is the model-name row, not a base value.
- **Sato attribution.** b30 says a search summary claimed "no difference between fused and non-fused prompts" for 2505.10948. That result is in 2504.21012 (Waking up an AI). 2505.10948 has no test.
- **KOMBINE dating.** a16 dates it 2026, b18 2025. The arXiv id is 2509 (September 2025); text reads as a revised version with 2026 model names (gpt-5.6-sol, claude-opus-4.6). Cite as arXiv 2509.21043 (v. with 2026 models).
- **KOMBINE "14x".** The 14.3x is at 2 or more shared properties; at 1 or more it is 2.6x. a17 and b19 do not always say this.
- **a16 "agree with humans 75 percent"** applies only to unanimous items; 66% overall (n=60 items, 150 judgments, one human rater).
- **Human blending score.** 12.8% valid rate (c04) and 7.4% composite (b18) are different measures; do not mix.

## Contradictions between sources
- Interpolation: Matsuhira finds the midpoint is where blends peak (BCD .621), Olearo finds embedding interpolation the worst method. Both agree that one input tends to dominate and that order matters. Both are image models and differ in detection method.
- Distance: Estes and Ward, Wilkenfeld and Ward (not opened) say anomalous or far pairs give more emergence; Chan and Schunn and Kennedy find no direct benefit. KOMBINE uses random unrelated pairs and finds most blends invalid. Left as contested (K09).
- Blending support from brain data (Coulson, Van Petten) versus the replication's reading (Lai) that the same pattern fits other accounts.
- Hampton: emergence rare in plain conjunction versus rich for social stereotypes (Hastie, Kunda): the difference may come from a demand to explain, not from blending.

## Weak spots
- Almost all human data on the theory itself are old (1987 to 2002) and about concept conjunction, not full four-space networks. No experiment manipulates the generic space.
- Every LLM blending study with a number is either judged by LLMs (KOMBINE, CCPT, CreativeMashup, VMetaphor) or small (PopBlends N=10, Misty N=14, Beyond Pixels judges). KOMBINE has 5 items per task per human, one human rater for judge validity.
- KOMBINE, CCPT, Beyond Pixels and PopBlends measure different things (valid generic space, emergent property, visual metaphor, bridge relatedness). None tests "blend improves a downstream reasoning task". The central question for our agent is therefore not measured.
- Evidence a, b, c overlap heavily on KOMBINE, PopBlends, IEI, CCPT: counting them three times would inflate "independent sources". Claims count each paper once.
- No study compares structured blending against a plain "combine A and B" prompt at equal tokens.

## Seen only in snippets or not opened
a11 (Eppe 2018), a28 and b12 (Gibbs), a29 (Coulson and Matlock), a30 (book), b07 as full text, b08, b13, b14 (Chan and Schunn), b16, b17 (Estes and Ward, Wilkenfeld and Ward), c26. Only abstract or summary: a23, a25, b15, b30. Hampton results are from his 1996 review, not the original papers. Si et al. is not a blending test.

## GAPS
1. Does a structured blend step (state generic frame, then blend, then check) beat a plain "combine A and B" prompt at equal tokens on any measured outcome? No study runs this arm.
2. Does the blend operator help on a downstream task (reasoning, design, ARC-like or open-ended problems), or only on idea count and novelty? Find any LLM study with a task outcome, not a rating.
3. How well can code (not a model judge) check a generic frame: non-vacuity, both-input coverage, emergent property absent from both inputs? Is there a published checker or measured agreement with humans?
4. What input distance and pairing rule gives the best valid-blend rate and usefulness? Original Estes and Ward, Wilkenfeld and Ward and Chan and Schunn need to be opened with their numbers.
5. Does model choice or temperature change the abstraction bottleneck (43.4% generic-space success) and does a retry or a different-family second model repair it? KOMBINE only reports temperature 0.9.
6. Original Gibbs (2000), Coulson and Matlock (2001), McCubbins and Turner (2013), and Eppe (2018): do they contain any experiments with numbers that test blending specifically (e.g. offline feature listing, tractability of blending patterns)?
7. Human-expert studies of blending in design or science (Boden-type creative cases): do blends that were later judged valuable show the generic-space step explicitly? Discovery case studies may overlap with another subfield.
8. Replications or failures of Hampton's emergence findings in 2010 to 2026, including LLM versions of Hampton's conjunction tasks (CCPT is one; are there others and what do humans score today?).
9. Is there any LLM test of Fauconnier and Turner's optimality principles (unpacking, topology) as an automatic score, and does it correlate with human value judgments?

## Gap search results

Gap searcher pass, 2026-10-31. Evidence in evidence_d.jsonl (d01 to d19). Tool limits: WebSearch quota was exhausted, arXiv and Semantic Scholar APIs were rate limited and often failed, Elsevier, Wiley and De Gruyter pages returned 403. PDFs were read from D:/research_scratch/A09.03/ (CCPT, Kennedy, Fujiyoshi, Wang and Luan, Peeperkorn, Chan Dow Schunn, Zahn et al.).

### Correction to the earlier correction (CCPT, d01)
The checker note above says the scaffold gain is about +15 points (42.4 to 57.8). The paper text contradicts that. It says GPT-4o with spreading activation plus ConceptNet is 12.3 points above gold on R_H,M,P and 1.6 below gold on R_N,P; only the fourth GPT-4o row fits (41.5 vs gold 29.2; 85.8 vs 87.4). So rows are Base 40.8, CoT 42.4, S.A. LLM 43.8, S.A. ConceptNet 45.8, S.A. both 45.2, then the gray Multi-Oracle row 57.8 (best of 5 samples, an upper bound). Scaffold gain is about +5, chain-of-thought about +1.6, best-of-5 about +17. K05 and K17 were edited. The first reading in b23 (+5.0) was closer than the "correction".

### Gap by gap
1. Structured blend vs plain combine at equal tokens: STILL OPEN. Nearest is Fujiyoshi 2026 (d08): 74/80 vs 49/80 in one case, AI judge, author rubric, tokens unmatched; 7 of 8 batch successes with no baseline. Weak. New claim K25.
2. Downstream task outcome: PARTLY ANSWERED, not for blending. Analogy and recombination have gold-answer or completion outcomes (Thought Propagation +12% / +15%; Discovery by Dreaming GSM8K +14.5 pp, but as training, and in-context use reversed the gain). No blend operator tested on a task. K27.
3. Code check of a generic frame: STILL OPEN. Nearest is a typed-structure functor-preservation gate (d09: 13,951 to 163 to 9; reject below 0.30; about 17:1). No measured human agreement; authors say so. K26.
4. Input distance and pairing: MOSTLY CLOSED for distance. Chan, Dow and Schunn (d03, opened): nearer sources did better (-0.33 log-odds per unit of max distance, CI -0.06 to -0.60; far equals no citation). Kennedy (d02, opened): atypical seeds gave no creativity gain (N=195). Estes and Ward and Wilkenfeld and Ward remain second-hand (d05, d06) and Chan and Schunn 2015 abstract only (d04). Pairing rule for valid-blend rate in LLMs is still unmeasured. K09 updated.
5. Model, temperature, retry, second model: PARTLY ANSWERED for temperature. One model, weak effect (d07: novelty beta .308, coherence beta .240). Nobody tested retry or a second model on the generic-space step; KOMBINE abstract only hints that cross-provider models reuse fewer properties (d16). CCPT best-of-5 (+17 points) is indirect support for retries with a check (d01). K24.
6. Gibbs, Coulson and Matlock, McCubbins and Turner, Eppe: STILL OPEN (paywalled, not opened; d17). K29.
7. Expert cases with an explicit generic-space step: STILL OPEN. No such study found; left to the discovery case studies subfield.
8. Hampton replications and LLM conjunction tasks: PARTLY ANSWERED. No direct replication found. LLM-era work: CCPT (d01; humans 49.2 and 38.0), GPT-3 compounds (d13), embedding study (d14). Quantum-cognition modelling of Hampton data is theory fitting only. K28.
9. Optimality principles as an automatic score: STILL OPEN. Only a proposal poster without results (d18). K29.

### What changed in claims.jsonl
K05 text and status (now single-source, CCPT numbers fixed), K09 (adds originals and numbers), K10 (adds d04), K16 (adds CCPT best-of-5), K17 (base number fixed). New: K24 to K29.

### Remaining risks
Several sources are abstract-only (d04, d05, d06, d10, d12, d14; opened:false). The unreachable papers may hold the numbers asked for in gaps 4 and 6.
