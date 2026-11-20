# D02.05 Imprecise credences: critique (cross-check)

## Re-opened and confirmed this session
- Xiong 2024 (arXiv 2306.13063): GSM8K AUROC 54.8% (verbalized) to 92.7% (5 samples + consistency); GPT-4 average AUROC 62.7%; ECE above 0.377 for GPT-3, GPT-3.5, Vicuna. Confirmed (c09, c24).
- Liu 2023 AmbiEnt (arXiv 2304.14399): 1,645 examples; GPT-4 disambiguations correct 32% vs 90%. Confirmed (c15).
- Tian 2023 (arXiv 2305.14975): verbalized confidence often cuts ECE by a relative 50%, "over 50%" with temperature scaling. Confirmed (c10).
- Yona 2024 (arXiv 2405.16908): table cells 0.52, 0.63, 0.70 present. Confirmed in range (c12).
- Jabarian and Lazarus (2206.04605): N=708, 55% prefer risky over dominating ambiguous act. Abstract confirmed (a14); t=11.7 and 118.13/101.03 cents not re-checked.
- Kuzmics et al. (2212.03603), Dembo et al. (2607.09355), Manchingal et al. (2608.23244), Helzner (2607.11920): abstracts and framing confirmed; body numbers (18 of 27, 154 subjects, 73-91% commit, slopes) not re-checked because arXiv/Semantic Scholar returned HTTP 429 during the search lookups.

## Corrections
- Wrong arXiv id guess for AmbiEnt (2305.14610) was mine; correct is 2304.14399. Evidence file urls were not affected.
- Duplicates: a15 = b09 (Kuzmics), b20 = c09 (Xiong), b19 = c11 (Kadavath), b16 = c01 (Hullermeier). Counted as ONE source in claims, not two.
- b20 quotes AUROC 0.522 to 0.605 from the abstract; c09 gives GPT-4 average 62.7% from the body. Different aggregates (abstract range vs average across tasks). Not a conflict, but cite the body figure.
- c10 says "50% or more"; paper says "often ... relative 50%" and "over 50%" after temperature scaling. Read as "often about 50%", not a guarantee.

## Contradictions and tensions
- Human Ellsberg rate: Oechssler and Roomets "slightly more than half" (b10, second-hand) vs Kuzmics 66.7% (n=27) vs Jabarian 55%. Consistent within error but different designs.
- LLMs: b12 (near-ceiling aversion) and b14 (GPT, Llama 100% human-like) vs Helzner (a25): Claude 3.5 nulls, no ambiguity claim. Prompt wording and sampling matter.
- Elga (sharp) vs Levi/Walley (imprecise): philosophical, unresolved; no empirical test settles it.
- c14 (Ye 2024): higher accuracy does not mean lower uncertainty, which cuts against using set size as a quality proxy.

## Weak spots
- Almost all LLM evidence concerns calibration, not imprecise credences as a reasoning step. No paper measures answer accuracy of an agent given a low/high interval flag at equal tokens.
- Credal LLM papers (a19-a24, a27) are 2025-2026 arXiv preprints, mostly white-box or single-benchmark; several tables were not legible in text extraction (a20, a22, a24, a26, a27).
- Founding works (Keynes 1921, Levi 1980, Walley 1991, Ellsberg 1961, Seidenfeld-Wasserman 1993, Camerer-Weber 1992) were NOT opened; content comes from SEP and Elga (a10, a13, a16-a18, b21-b26 all opened:false).
- Fox and Tversky 1995 comparative ignorance is only seen via Wikipedia; this is the main boundary condition for human ambiguity aversion (it shrinks when judged alone) and is unverified.
- Failed replications of Ellsberg effects: only second-hand ("rarer than usually said" in SEP, no numbers).

## GAPS
1. Does adding a low/high "unknown" flag (interval from 5 samples) change final accuracy or abstention quality at equal tokens versus a point confidence? (No paper tests it.)
2. Does sample-spread interval beat verbalized interval on non-arithmetic tasks (open QA, planning)? Xiong shows the gain mostly on GSM8K.
3. How often do LLM-stated intervals fail to contain the point estimate, across models other than GPT-5-mini (a19: about 70%)?
4. What is the dilation rate in LLM updating: does a stated interval widen on irrelevant evidence?
5. Which tie-break rule (abstain, maximin, ask, E-admissibility) works best when the interval straddles a decision threshold?
6. What is the exact size of Fox and Tversky's comparative-ignorance effect (alone vs side-by-side), and does a prompt that shows one claim at a time lower LLM ambiguity aversion?
7. Do Ellsberg-urn results in LLMs (b12, b14, a25) predict anything about answer quality, or are they just behaviour curiosities?
8. Do the primary numbers for Kuzmics (18/27), Dembo (154 subjects, 20 rationalizable), Manchingal (73-91% commit) and Helzner hold in the full text?
9. Is there any failed or null replication of credal-set uncertainty gains in text LLMs outside the authors' own papers?
10. Does a vacuous (full-range) flag ever help an agent, or should the rule be "never output [0,1]" (belief inertia)?

## Gap search results (2026-11-19)
Method: full text opened for Kuzmics, Dembo, Manchingal, Helzner, Yang et al., Xiong, Tian, Tak, Bini and Arlo-Costa and Helzner (the only open source for Fox and Tversky's numbers). New evidence: evidence_d.jsonl (d01-d17). WebSearch budget ran out after one call; arXiv and OpenAlex lookups for new papers returned empty or errors.

- Gap 1 (flag vs point at equal tokens): STAYS OPEN. Closest result is d09: ProbInt interval is about tied with Vanilla verbalized confidence on AUROC. No accuracy or abstention test at equal tokens.
- Gap 2 (sample spread vs verbalized on non-arithmetic): CLOSED. Spread helps mostly on GSM8K; GPT-4 non-arithmetic consistency AUROC 56 to 69 (d12), and with GPT-5 and gemini-2.5-pro sample frequency is worse than verbalized confidence (d09). K08 now contested.
- Gap 3 (point outside interval, other models): PARTLY OPEN. 72.33% containment on AmbigQA (d08), pooled; no per-model split and no other families.
- Gap 4 (dilation in LLM updating): STAYS OPEN (d16, no source found).
- Gap 5 (tie-break rule): STAYS OPEN. Only maximin/maximax alignment with the model's own answers (d11).
- Gap 6 (Fox and Tversky size): CLOSED for humans: N=141, $17.94 vs $18.42 alone, $24.34 vs $14.85 together (d01), with a failed partial replication N=97, 15.33 vs 5.42 alone (d02). LLM one-claim-at-a-time test STAYS OPEN; existing LLM Ellsberg prompts are side by side (d14).
- Gap 7 (Ellsberg in LLMs vs answer quality): STAYS OPEN. Behaviour measured (d14, d15), no link to quality.
- Gap 8 (primary numbers): CLOSED with two corrections. Kuzmics 18/27 is rules inconsistent with all classical ambiguity models, not a preference rate (d04; K02 reworded). Dembo 154 and 20 confirmed (d05). Manchingal 73-91% commit at 89-98% accuracy NOT found; real figures at 80% coverage 99.0 / 71.5 / 43.5 (d06; K11 now contested). Helzner is a temperature-sensitivity paper, not an ambiguity claim (d07).
- Gap 9 (independent replication of credal gains): STAYS OPEN. Only author-reported limits (d06, d17); no outside replication found.
- Gap 10 (vacuous flag): STAYS OPEN. Theory only (belief inertia, K05); no LLM test.

Still not opened: Keynes, Levi, Walley, Ellsberg 1961, Seidenfeld-Wasserman, Camerer-Weber, the Fox-Tversky QJE original (numbers are via Arlo-Costa and Helzner), Chow-Sarin and Dolan-Jones.
