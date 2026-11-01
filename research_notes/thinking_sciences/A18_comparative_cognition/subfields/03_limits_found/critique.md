# A18.03 Limits found: critique (cross-check)

## Numbers re-opened this session (PMC HTML and arXiv PDF text)
Confirmed: Taylor 2009 103.3 +/- 20.3 trials, 91.2% pulls, side-switching 22.1% vs 0% (U=9, p=0.0318), all three crows failed transfer 3. Neilands 2016 pre-test 128/240 and D4R binomial p=0.062. Jelbert 2014 water 76.3%, high level 86.8%, narrow-first 56% (p=0.27), U-tube 48.9% (p=0.79). Jelbert 2019 35/48 (72.9%) and 11/12 first tests. Kea 2024 24/48 fan on, chi2=1.775 p=0.187, 480 trials 96 sessions. Martin-Ordas r=0.13 p=0.57, raking z=1.98. Farrar 2020 116 experiments from 63 papers, median 7 animals, median 3 passers, 15 zero-pass and 25 all-pass. Rane 2025 table (ranked 0.97, random 0.92, reverse 0.78, n-term 0.40). Lewis and Mitchell Table 2 values 0.753, 0.488, 0.350, 0.452 with 1,876 human and 6,840 per-model samples. Mecattaf: 59 children, 3 runs per task.

## Corrections
1. a17 says 52 children and child median 0.63 from an earlier line, unverified. Mecattaf paper text says 59 children (replicating Voudouris 2022). Use 59; a17 stays unverified.
2. a07 says 11 birds chose heavy first on 125 of 140 trials. The paper text says the other ten birds were trained and preferred heavy; 125/140 was not found in the page text, so treat that figure as unverified and use "ten birds, p<0.001". Also the two innovators: D4R (12 heavy, 22 light, p=0.062) and D3B (light 18/24 contacts, p=0.012). So the weight-inattention case has one significant bird, not two.
3. a08 gives sinking 88.0% and solid 89.0%. The paper text says "almost 90%"; the exact values were not found in text (probably in a table). Report as about 90%.
4. a10 lists the corvid meta-analysis with no authors. It is Hennefield et al. 2018, the same work as b11 (opened:false). Count as ONE source, not two. Claim K05 already counts a10 and b11 only once in spirit; its independent_sources=3 is a8/a9, a10+b11, b12.
5. Lewis and Mitchell row labels are offset in the text extract; the order Humans, GPT-3, GPT-3.5, GPT-4 matches b17. GPT-3.5 below GPT-3 is odd but as printed.
6. Duplicates: Wu 2024 is b16, c24 (and c07 earlier rows are not duplicates); Ullman is b21 and c26; Mecattaf is a18, c04, c05. Counted once each in independent_sources.

## Contradictions between sources
- Taylor 2009 read crows as analogical reasoners; Taylor 2020 (same author) reads the same data as proximate-cause only. The author changed his reading; the data did not change.
- Crows fail weight in stone dropping (Neilands) but infer weight in breeze (Jelbert 2019); kea fail the breeze task. Not a clean story.
- Jelbert 2014 width fail was reversed by Logan 2014 after apparatus changes (same group).
- Kiciman 2023 shows strong LLM causal scores (post-cutoff 98.5%) against Zecevic parrots and Corr2Cause near random. Different tasks, so contradiction is unresolved.
- Illusion of thinking (collapse) vs Lawsen (artefact). Lawsen's rebuttal is preliminary and AI-co-authored.

## Weak spots
- Founding evidence is N=3 birds; the 8 naive crows on the table were from the same lab.
- Several primate sources (b05 to b10, b12, b13, b14, b15, b19, b25) are abstract-only. Claims K03 and K06 rely partly on them; K03 still has opened sources (a06, b02, b04, c03).
- Many LLM studies use 2022-2024 models (GPT-3, GPT-4). No 2025-2026 frontier reasoning model is tested on a trap-tube style twin test, except Samiei 2026 (read from figures) and Schulze Buschoff 2026.
- Counterfactual drops may reflect harder counterfactual worlds, not missing generality (Wu 2024 say so).
- No source here tests a scaffold (not model) against its own counterfactual twin at equal tokens.

## Seen only in snippets or abstracts
b05, b06, b07, b08 (opened false here, though a12 opened the same Martin-Ordas paper), b09, b10, b11, b12, b13, b14, b15, b19, b25, c26, a13, a14, a15, a17.

## GAPS
1. Does a scaffolded LLM keep its gain on a counterfactual twin of each test at equal tokens, or does the gain vanish like the crows' hole rule? (No source tests a scaffold directly.)
2. Do 2025-2026 reasoning models (not GPT-3/4) still drop on altered-alphabet, counterfactual and GSM-NoOp twins, and by how much?
3. Which error signature (like crow weight inattention) separates a shallow rule from a mechanism in an LLM physics or code task, and can code count it?
4. How much of the LLM drop on perturbed tasks is distractor handling versus lost rule? Need rule-comprehension controls with exact rates.
5. Is the two-hole failure itself replicated by anyone outside Taylor's lab? No independent replication found; seek Gray/Jelbert, Seed or Bird follow-ups with other corvids.
6. Does intervention-first (run a test before answering) narrow the conjunctive-rule gap in strong LLMs at equal tokens (Samiei 2026 vs Lampinen 2023)?
7. What is the real exact accuracy for Mecattaf LLM levels, and does a tool-API interface (not images and action scripts) lift causal-level scores?
8. Do inhibition-type failures (crows needed to stop pulling) have an LLM analogue, such as failing to stop a salient but wrong move, and can a code gate fix it?
9. Is the Hennefield trial-and-error result (learning only from success) visible in LLM retry loops, in per-attempt logs?

## Gap search results (evidence_d.jsonl, d01-d22; claims K21-K28 added)
Tool note: WebSearch quota ran out early and the arXiv, Semantic Scholar and OpenAlex search APIs were rate-limited (429) by parallel agents. Papers were fetched by known arXiv id and Europe PMC; no broad literature sweep for 2025-2026 follow-ups was possible. Absence claims below mean "not found", not "does not exist".

1. Scaffold on a twin at equal tokens: PARTLY CLOSED, still open for the exact test. Li 2024 (GSM-Plus, d07) and Shi 2023 (d08) ran prompting scaffolds on perturbed twins. Gains held in absolute terms but the gap did not close (GPT-3.5: CoT 74.17 -> 62.92; COMP+SC 80.00 -> 69.47; GSM-IC best macro 45%). Both use old models and unequal tokens. Claim K22, provisional.
2. 2025-2026 reasoning models on twins: PARTLY CLOSED. GSM-NoOp: o1-preview -17.5, o1-mini -29.1 (d01). CatAttack: R1 4.50% vs 1.50% random (d04). A 2026 replication with Opus 4.6 and Haiku 4.5 found the drop vanished after audit (d03). Altered-alphabet and counterfactual twins: no 2025-2026 run found (d10 is still GPT-3/4). K21, contested.
3. Error signature countable by code: PARTLY CLOSED. Hint or comment adoption (CodeCrash, d13) and operation applied to an irrelevant quantity (d02) can be counted by running code. No source reports the adoption rate itself. K24, provisional.
4. Distractor vs lost rule: PARTLY CLOSED. Only 12.4% of generated distractors survived audit (d03); 60% of CatAttack variants kept the original meaning (d05). So a large share of drops is ambiguity. No source gives comprehension-control rates per perturbation. Still needs our own comprehension probe.
5. Independent replication of two-hole: NOT CLOSED for the exact test, CLOSED for the pattern. Rooks (d15, d16), Darwin's finches (d17) and hooded crows (d19) show pass-then-fail-transfer. No Gray, Jelbert, Seed or Bird two-hole follow-up found. All are abstract-only (opened:false). K23, K02 raised to established.
6. Test-first at equal tokens: OPEN. Samiei 2026 has no LLM passive arm (d14). K26.
7. Mecattaf exact levels and tool API: OPEN. Per-level numbers are only in figures; the 16 citing papers listed by Semantic Scholar include none that swaps the interface (d21). K27.
8. LLM inhibition analogue and code gate: PARTLY CLOSED. Premature commit and non-recovery (Laban, d11) and the self-correction blind spot with a 'Wait' gate (Tsui, d12: 64.5% blind spot, -89.3% with Wait). Evidence uses injected errors and mostly non-reasoning models. K25, provisional.
9. Learn-only-from-success in LLM retry logs: OPEN. Hennefield numbers verified (d20: OR 5.00 vs 0.67) and gives a method; no LLM application found. K28.

Corrections and notes from this pass
- Mirzadeh table gives GPT-4o 94.9 -> 63.1 (a LessWrong post quotes 63.0); use the paper.
- CodeCrash reasoning-model table rows were garbled in text extraction; only the text claims are used.
- d15 to d19, d22 are abstract-only via Europe PMC; mark them unopened in any later audit. d19 has no author record.
