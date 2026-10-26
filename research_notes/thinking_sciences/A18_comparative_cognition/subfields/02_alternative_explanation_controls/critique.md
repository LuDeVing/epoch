# A18.02 Alternative-explanation controls: cross-check and critique

## Numbers re-opened this session (source text read)

| Number | Source reopened | Result |
|---|---|---|
| 3 of 6 crows solved tube; mean 103.3 +/- 20.3 trials | Taylor 2009 (PMC2674354) | Confirmed. The +/- is a standard error, not an SD. |
| 10 of 12 first trials correct; Tiga wrong on T2 trial 1 then right 19 times; Tiga and Slevin right on T3 trial 1 then at chance | same | Confirmed. The paper gives no test on the 10 of 12; the 3 birds x 4 transfers are not independent. |
| All 3 tube-failures failed the trap-table | same | Confirmed. |
| p = 0.0156 (a03) | same | CORRECTED in meaning: this is the chance that all 3 crows have their highest latency or side-switching score in transfer 3 (3 x 0.25 binomial). It is not a test of failing the transfer. |
| O'Neill 2021: HCA 8.69 (SD 1.1) vs UCA 10.95 (SD 2.31), t(3) = -2.16, p = .12; reverse order 7.52 vs 9.26, p = .42; pooled HCA 8.10 vs UCA 10.11, V = 7, p = .15 | O'Neill et al. 2021, Animal Behavior and Cognition 8(2) PDF | Confirmed. Pooled test is a Wilcoxon, p = .15. |
| Ullman: P(chocolate) 99% / 82%; transparent bag 95%; corrected second prompt popcorn 58% vs chocolate 36%; double-space artefact 53% vs 39% | Ullman arXiv 2302.08399 | Confirmed. |
| Wu et al.: parseable programs 99% default vs 62%, 71%, 75% for flipped and rotated settings | Wu et al. arXiv 2307.02477 footnote 11 | Confirmed, but it is a parse rate in the drawing task, not accuracy. Do not quote it as an accuracy drop. |
| GSM-NoOp drops | Mirzadeh arXiv 2410.05229 figure | Confirmed with scope: drops run from -17.5 points (o1-preview) through -29.1 (o1-mini), -32.0 (GPT-4o), -40.0 (GPT-4o-mini) to about -60 or worse for small models. "Up to 65%" is the weak-model end; frontier models lose 17 to 40 points. |
| GSM1k: drops up to 8%, Spearman r2 = 0.36 | arXiv abstract of 2405.00332 | Confirmed. Item count not re-read from the body (see contradictions). |

Not re-opened this session: Kano 2017 (publisher blocked), Shapira 2023 (PDF fetch failed), Jelbert 2014, Logan 2014, Miller 2016, Neilands 2016, Bastos 2021, Lampinen, Turpin, Huang, Razeghi, ConceptARC, FANToM, Gandhi. These rest on the finder agents' reading.

## Corrections and contradictions between the evidence files

1. GSM1k size: b25 says a 1,000-question set, c25 says 1,205 problems. The name says 1000, the paper's body (recalled, not re-read) says 1,205. Quote 1,205 until confirmed.
2. O'Neill title: a21 uses "Revisited", b15 uses "Do New Caledonian crows reason about hidden causal agents". The published ABC 2021 title is "...Hidden Causal Agents Revisited". Same study; b15 and a21 are duplicates and count as one source.
3. b14 is dated 2013 but cites the 2012 original; it is a reply with no new data.
4. a10 and b05 are the same study (Taylor 2010 string pulling) entered twice; a11 and c-files likewise duplicate b01/c01 (Taylor 2009). Duplicates inflate raw counts but not independent_sources in claims.jsonl.
5. a25, b19, c08, c09 are one paper (Wu et al.); a26, b24, c23, c24 are one paper (Mirzadeh); a27, b22, c02, c03 are one paper (Ullman); a29, b26, c12, c13 are one paper (McCoy). Several claims thus rest on one primary source despite many ids. Counted as one in independent_sources.
6. b22 says small edits "flip" the answer. After Ullman's correction the second prompt no longer flips (popcorn 58% vs chocolate 36%); the first prompt still gives the wrong answer at 95%. Claim K12 states this.
7. Water vs sand: Taylor 2011 group level 58% vs 56% (not different) vs Jelbert 2014 76.3% water. Different designs (stone-dropping with matched search task vs Aesop tube), so not a direct contradiction, but they are filed as contested (K06).
8. The hidden-agent finding: Taylor 2012 positive (n=8), O'Neill 2021 null (n=14). No third lab. Contested.
9. b30 is a synthesis written by an agent (opened:false); it contains no new sources. Not used as evidence beyond the statistics point.

## Weak spots

- Animal evidence is mostly one lab (Taylor, Gray, Jelbert, Logan, Miller and co-authors) and tiny samples (3 to 14 birds). Independent confirmation exists mainly for trap tasks (Martin-Ordas, Seed) and kea string-pulling (Bastos).
- No claim here has a measured effect of a control on an LLM agent scaffold. All LLM studies measure models, not scaffolds; whether a scaffold shrinks the default-versus-counterfactual gap is untested.
- Most LLM models are 2023-era (GPT-3, GPT-3.5, GPT-4, PaLM-2, Claude 1). Almost nothing in the evidence covers 2025-2026 reasoning models on these controls, except the o1 rows in GSM-Symbolic.
- Kosinski (75% for GPT-4) versus Ullman and Shapira (failures) is unresolved for current models.
- Two items are abstract-level only: FANToM per-model numbers and Miller 2020.
- Seen only in snippets or second-hand: a08 and a09 (Visalberghi, Povinelli, Seed) come second-hand from Martin-Ordas 2008; a22 commentaries (Boogert, Dymond) come from O'Neill's introduction.
- "Established" for K05, K10 style claims means two or more independent sources agree on a direction, not that the size of the effect is stable.

## GAPS

1. Does a scaffold (reflection, multi-sample, code-selected verification) shrink the default-versus-counterfactual gap of Wu et al. at equal tokens, or does it only raise both? No source measures this.
2. Do 2025-2026 reasoning models still fail the Ullman and Shapira logic-preserving ToM perturbations and the permuted-alphabet analogies, and by how much?
3. How many held-out variants per problem class are needed for a G3 check to separate real rule use from fitting (power analysis; animal studies used 3 to 14 subjects)? Is there LLM literature giving false-accept rates for single-variant versus multi-variant held-out checks?
4. Is the GSM-NoOp irrelevant-clause drop reduced by an input-hygiene step (restate the task, strip unused quantities) in a measured study, and at what token cost?
5. Which control type gives the largest drop in false passes on ARC-style tasks: surface re-coding (colour or symbol permutation), mutated inputs, or symmetry checks? ConceptARC gives variation tests but no control-by-control comparison.
6. Does the animal-side lesson "a failed control may be task load" (Logan 2014 rescue version) have an LLM analogue, i.e. do model failures on counterfactual or perturbed items disappear when distractors or length are cut?
7. What is the replicated, independent-lab evidence for the string-pulling feedback-loop account versus insight in birds beyond the Taylor and Bastos groups (e.g. ravens, rooks, parrots)?
8. Is contamination (GSM1k-style gap) detectable cheaply for our own benchmark sets, and does the Razeghi frequency effect appear in current frontier models?
9. Do chain-of-thought unfaithfulness results (Turpin, bias insertion) hold for current reasoning models with long hidden reasoning, and so should G10 checks use bias-insertion tests?
10. The Kano 2017 inanimate-control result was not re-opened; does the submentalizing exchange (Heyes vs Kano and others) end with a design that resolved it, and what was the control that did?

## Gap search results

Evidence is in `evidence_d.jsonl` (d01 to d25; 24 opened, d02 not). New claims K28 to K38; K08, K10, K11, K13, K14, K15, K17, K24, K25 updated. Search quota ran out partway; remaining lookups used arXiv listing pages and Europe PMC. Most findings are from open or older models; no source tested our own scaffold.

| # | Gap | Result | Status |
|---|---|---|---|
| 1 | Scaffold shrinks default-vs-counterfactual gap at equal tokens? | No equal-token study. Webb 2024 (d12): GPT-4 with code matched humans (P=0.496) where plain GPT-4 did not, so the gap was a counting load that a tool removed (K28). Kutakh 2026 (d18): on Haiku 4.5 the gap is only 1.3 to 1.7 points and code scaffolds did not shrink it (K37). Self-consistency raises both default and distractor accuracy at 20x tokens (d07). | Partly closed: direction known, equal-token test still open |
| 2 | Do 2025-26 reasoning models still fail Ullman/Shapira ToM and permuted-alphabet items? | No run found. 2026 ToM papers (d10, d11) used open models up to Llama-3-70B and DBRX; none fully robust; reasoning fine-tuning amplified a wording shortcut. Reasoning-model evidence exists only for ConceptARC (o3, d22) and GSM (R1, o1, d15). | Open |
| 3 | How many held-out variants; false-accept rates? | No false-accept curve exists. Measured gaps between single-variant and all-variant pass: 72.4% vs 6.0% (GSM-IC), 58 to 74% vs 0 to 4.4% (ToM) (K29). Any false-accept number must come from our own tasks. | Open (gap size known, count not) |
| 4 | Does restate-and-strip reduce the NoOp drop? | Not tested anywhere I found. Closest: an "ignore irrelevant information" sentence gave +5.4 micro and +9 macro points on old models at about zero token cost (d07, K30). Audited-distractor work (d19, K32) suggests part of the drop is bad distractors. | Open for restate-and-strip; partly answered for the ignore sentence |
| 5 | Which control cuts ARC false passes most? | No head-to-head. Only measure: rule audit, ~27% of o3's correct text outputs rest on unintended or wrong rules vs ~7% for humans (d22, K34). | Open |
| 6 | LLM analogue of "failed control may be task load"? | Yes, partly. Code removing counting load (d12); distractor dose-response: Grok-3-Beta 43% to 19%, GPT-4.1 26% to 2% from 1 to 15 distractors (d16, K31). Nobody reran the same failed item with distractors cut. | Mostly closed (analogue shown, rescue test not run) |
| 7 | Independent-lab evidence for feedback loop vs insight? | Moscow (6 hooded crows, loose string, d24) and Cambridge (4 jays, mirror string, d25) report slow learning and say they cannot separate the accounts; kea (d23, Taylor group) fail even after feedback experience. No independent lab settles it. | Open; K08 stays contested |
| 8 | Cheap contamination detection; Razeghi effect in frontier models? | Detection: yes, via a fresh matched set, distinguishability audit (21.83% vs 20% chance, 1,205 items), likelihood check (d20), and per-model perturbation gap (d18) (K35). Razeghi needs pretraining counts; no frontier test found (d21). GSM-Symbolic drops are not all significant and number size is a confound (d17, K36). | Half closed; Razeghi-on-frontier open |
| 9 | Do Turpin results hold for long-reasoning models? | Partly. Hint verbalisation is 25% (Claude 3.7) and 39% (R1) (d03), so omission persists. A no-hint swapped-question test gives R1 0.37%, Sonnet 3.7 thinking 0.04% (d04), and a critique says verbalisation is budget-limited (d05). Bias insertion alone is a weak G10 check (K33). | Closed with caveats |
| 10 | Kano 2017 and the Heyes exchange | Krupenye et al. 2017 (d01) opened: inanimate control, 22 of 43 looked, 14 of 22 first looks to target, p=0.28. It answered Heyes' request in the authors' view, with a low-power null. Heyes' reply and the TiCS note were not opened (d02). | Mostly closed; Heyes side not read |

### Corrections to earlier files
- GSM1k size is 1,205 (confirmed in paper body, d20); the "1000" is the name. b25's 1,000 is wrong.
- K25 numbers (22 of 43; 14 of 22; p=0.28; original 22 of 30) confirmed against the PDF text.
- A claim in the Chen/Anthropic paper summary (25% and 39%) is an average over six hint types; individual hint rates were in figures and are not quoted.

### Caveats on this pass
- d03 and d19 were read through a page-summary tool, not full text.
- Several new LLM sources (d10, d11, d18, d19) are 2026 preprints or a blog post; not peer reviewed.
- Lewis & Mitchell table values were garbled in text extraction; only the human mean (0.753) and the GPT range (0.35 to 0.49) are quoted.
