# Critique: A12.08 Stage model and incubation (cross-check)

Scope: evidence_a (26 lines), evidence_b (30), evidence_c (27). 21 claims written to claims.jsonl (K01 to K21). Schema fit: the schema lists incubation by distraction as "not to add" (4b); nothing here argues against that.

## Sources re-opened this session (11 checks)

| Number | Result |
|---|---|
| Wagner 2004: 13/22 (59.1%) vs 5/22 (22.7%), chi2 = 8.54, P = .014; control chi2 = 7.07, P = .029 | Confirmed (a03, a04, b05) |
| Sio and Ormerod 2009: 117 studies, 3,606 participants, median 25, d = 0.29, CI 0.21 to 0.39, Q = 173.99, df 113, between-study variance .0834; Table 4 subgroups (low load .52, high load .24, rest .46) | Confirmed (b01, b03). Note "visual" is the right label for the middle problem type |
| Lacaux 2021: N1 20/24 = 83.33%, wake 15/49 = 30.61%, N2 2/14 = 14.29%, Fisher P < .001 | Confirmed (b06) |
| Lowe 2025: N2 24/28, N1 14/22, wake 10/18; BF N2>wake 8.19, N2>N1 24.71; 48/68 (70.6%) with nap | Confirmed. **Correction:** the no-nap baseline is 49.5% = 49/99 (p = .007), not "48.5% (48/99)" as in b07. a09 is right. Also the paper states it finds no evidence for N1 (BF N1>wake 1.19) |
| Nieuwenstein 2015: N = 399, accuracies 50.8/61.7/55.4/65.1; trim-and-fill g = 0.018 [-0.10, 0.14], p = .77 | Confirmed (b17). Added caveat: the paper's own footnote says trim-and-fill does poorly when bias is selective reporting, so 0.018 is a correction, not a final truth |
| Schoenauer 2018 magic tricks: incubation F(1,64) = 0.008, p = .930; sleep F = 0.047, p = .829; 1.40 extra tricks | Confirmed (a07, b08). a07 lacks the df for the tricks test (64, not the 73 of the classical-problem test). Name is spelled both "Schonauer" and "Schoenauer" in the files; the PMC text uses the second |
| Baird 2012: N = 145, exposure x incubation F(1,141) = 4.98, p < .01, partial eta2 = .10 | Confirmed (b15) |
| Sanders 2019: 31.7% vs 20.5%, t(56) = 3.22, p = .002, dz = 0.47, CI [0.14, 0.79] | Confirmed (b09) |
| d'Aliberti and Horta Ribeiro 2026: 6.31% pooled, 2.57% vs 16.44% (N = 723,200), detector 1.79% | Confirmed (b25, c11). **Correction:** the 7.6% shift rate is Qwen2.5-1.5B; 6.31% is the pooled figure. The 2.57 vs 16.44 contrast is in that analysis, not across every model |
| Same paper: +8.41pp | **Correction:** Table 5 shows +8.41pp (0.3221 to 0.4062, N = 320,000 paired samples) as the overall second-pass result on math. b26 and c12 describe it as "entropy-gated top 20%". The entropy gate is a separate stratified analysis. The second pass is a full extra generation, so it is not an equal-token result. Crosswords +0.45pp, Rush Hour +0.01pp confirmed |
| Mizumoto 2025: 201 riddles, 38 models, humans 52.9% (CI 46.6 to 59.2, n = 126, 120 items), non-reasoning 7.6%, reasoning 17.6%, OR 2.29 (1.99 to 2.64), 9.42% vs 19.25%, verification failures 5 to 39% | Confirmed (c08, c09, b27) |
| Lin and Snell 2025 sleep-time compute: about 5x, up to 13% and 18%, 2.5x cost | Confirmed from abstract and intro (c15). The "o1 limited gains" line was not re-checked |

## Contradictions between sources

1. Sleep stage: Lacaux 2021 says N1 only; Lowe 2025 says N2 only and rejects N1. Different tasks (number reduction vs perceptual colour rule), non-randomised stage groups, small cells (N2 n = 14 in Lacaux, N1 n = 22 in Lowe). Treat stage specificity as unresolved.
2. Sleep and insight: Wagner 2004 and Lowe 2025 positive; Schoenauer 2018 null on three classic problems and magic tricks. Lowe's own "wake" group (55.5%) is not far above its no-nap baseline (49.5%), so the nap result rests on the N2 post hoc subgroup.
3. Filler demand: Sio and Ormerod and Baird favour low-demand fillers; Segal found no demand effect.
4. Aha in LLMs: d'Aliberti says marker-based aha is not real insight and is harmful; Yang 2025 treats such markers as meaningful internal events (c14, not extracted numerically).
5. Sleep-time compute: Lin and Snell show large savings on stateful math built to be predictable; IdleSpec's own baseline of it gave no gain on GAIA and FRAMES.
6. Meta-analytic bias: Sio and Ormerod judged their funnel symmetric (regression beta = .08, p = .41), yet the same kind of test failed to flag bias that Nieuwenstein's trim-and-fill found in the unconscious thought literature. Do not read d = 0.29 as bias-free.

## Weak spots

- The unconscious thought literature (decision tasks) is mixed into incubation evidence by Gilhooly. Its collapse (K10) does not directly refute incubation on insight problems.
- Gilhooly 2016 is the second-hand source for Segal, Smith, Dijksterhuis and his own tests; he is an advocate (a18, b10, b12, b13, b14 share this one source). Claims K11 and K12 therefore count as single-source in practice.
- Almost all human studies have small cells (about 15 to 28 per group) and one task each.
- Retest gain after a break is confounded with a second try (Schoenauer b21; Henok a17 has no no-gap control).
- No LLM study tests incubation. All LLM entries are adjacent (aha markers, verification, offline compute, puzzle accuracy). Four of them (c01 to c04) compare accuracy only, with contamination possible.
- Several LLM results come from small open models (Qwen2.5-1.5B, Llama 8B) and may not carry to frontier models; GPT-4o and DeepSeek-R1 were checked on math only.

## Only seen in snippets or second-hand (opened:false)

a08 Holda 2020 (abstract only; Europe PMC record), a10 Konkoly 2026, a11 and a12 and b10 and b19 (via Gilhooly), a13 and b12 Segal (via Gilhooly), a14 and b13 Smith, a15 Baird abstract (b15 is the opened version), a18 Gilhooly tests, a19 Steindorf and Dijksterhuis, a20 Hassin, a21 and b29 and c19 Helie and Sun (c19 from press), a25 Macchi 2026, b16 Cai 2009 numbers (a06 is the opened version), b20, b28, c25 Raz 2024, c26 Gizzi 2022, c27 Dream-COP listing.

## GAPS (most decision-relevant first)

1. Does any LLM or agent study test a break, context reset or re-attempt after impasse at equal tokens on insight items, and does it beat one continuous pass? (K13 found none; our own search was limited by rate limits.)
2. In the d'Aliberti second-pass result (+8.41pp on math), what is the gain when tokens are matched to one longer first pass, and does it hold for frontier reasoning models, not just 1.5B to 8B models?
3. Do Yang 2025 aha-moment results survive a definition based on output change rather than linguistic markers? What are their effect sizes?
4. Is sleep-time compute helpful when the future question is not predictable (IdleSpec baseline showed none on GAIA and FRAMES)? What is the predictability threshold?
5. Does the repeat-exposure dependence in Baird 2012 (gain only on previously seen problems) replicate on insight problems rather than Unusual Uses, and with a no-gap control?
6. Is Lacaux N1 or Lowe N2 right, or is neither? Is there a randomised or larger sleep-stage test (not needed by the agent, but decides whether the sleep literature is reliable at all)?
7. What are Segal 2004's sample sizes and the full effect sizes for break vs no break and demand? Only the Gilhooly description was seen.
8. What do the Steindorf 2021 and later unconscious-thought replications find on insight (not decision) tasks, and what did Weisberg 2015 and Bowden 2005 report as null incubation results?
9. Does the Sanders 2019 cue-during-sleep effect (dz = 0.47) replicate outside one lab, and what is the agent analogue (resurfacing cues for unsolved items from a log)?
10. Do reasoning models verify better when verification is moved to code or an independent sample (G3, G4), measured on NazoNazo-like riddles at equal tokens?

## Gap search results

Evidence in evidence_d.jsonl (d01 to d16; 12 opened, 4 summary-only). Claims K05, K07, K09, K11, K13 to K17 updated; K22 to K26 added.

| Gap | Result |
|---|---|
| 1 Break or reset at equal tokens on insight items | Partly closed. No insight-item test exists. Nearest: Bulut 2026 (d01): continuing beat restart 9 of 9 at matched tokens; 1 of 178 cells prefix-limited (MATH, two small models). Reset gives no sign of benefit. |
| 2 Token-matched d'Aliberti second pass; frontier models | Open. No equal-token baseline in the paper; intervention only on Qwen 1.5B/7B and Llama 8B (Llama 3.1-8B -4.19pp on a MATH subset). The +8.41pp (main) and +7.74pp (appendix) figures come from different tables. |
| 3 Yang 2025 effect sizes under an output-change definition | Closed as "not tested". Marker-based; reports collapse rates, no accuracy effect size. |
| 4 Sleep-time compute and predictability | Mostly closed. Gain widens with predictability across five quantiles (no threshold); IdleSpec baseline gave 31.0 vs 30.9, 29.4 vs 33.2, 50.1 vs 50.5 average accuracy (vanilla vs sleep-time). |
| 5 Baird repeat-exposure replication | Partly closed. Du 2025 (N=85, no control): repeated > novel on UUT fluency, not on CRA. Teng and Lien 2022 (N=90): no mind-wandering benefit. Still no insight-problem test with a no-gap control. |
| 6 Lacaux N1 vs Lowe N2 | Open. No larger or randomised test found. |
| 7 Segal 2004 sample sizes | Open. Only the verbal result (break helps; length and demand do not) via Gilhooly. |
| 8 Unconscious thought and null incubation on insight | Partly closed. Steindorf 2021 (N=822) is a decision task, mixed. No insight-task replication found. Weisberg and Bowden null results not found. |
| 9 Sanders cue effect replication | Partly closed. Beijamini 2021 null for cueing (56/58/57%) on a different task; a 2021 follow-up reportedly supports cueing with a moderator (unopened, 403). |
| 10 Verification moved to code or independent sample | Open. No equal-token study found. Riddle Riddle 2026 (d14) shows LLMs over-apply inventive reasoning (84.9% vs 50.7%). |

Search budget used: 8 WebSearch calls. Weak points: several Semantic Scholar and arXiv API calls were rate limited or returned empty.
