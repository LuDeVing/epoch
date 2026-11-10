# A19.08 Individual-level links: cross-check critique

## Corrections and confirmations (sources re-opened this session)
- Jin et al. 2023 (arXiv 2308.14242), confirmed: AHS GPT-3.5 5.35 (SD .11), GPT-4 5.01 (.10), norm 4.87 (.49, N=702); DSS 4.59 vs 4.00 (N=158), GPT-4 3.97 p=.344; SCS-Ind 6.98 and 5.32 vs 4.73 (N=382); SCS-Interd GPT-3.5 5.85, GPT-4 4.95 vs 4.81, p=.07 (so "near norm" is only marginal). TCT 0.87 / 0.85. All with 10 runs per cell. Note: the extracted table labels the GPT-4 AHS row "DSS"; this is a layout glitch, not a data error.
- Kovac et al. 2023 (arXiv 2307.07870), confirmed: largest human d=0.53 (and -0.52); ChatGPT max |d|=5.86. Correction of emphasis: 5.86 is a single value under one context pair (history - joke), not a typical shift. Many pairs are 1-3.
- Park et al. 2024 (arXiv 2411.10109), confirmed: interview 0.83 (raw 65.67% / self-consistency 79.53%), survey+interview 0.86, demographic 0.74, persona 0.71; ablation 0.79. a28 and c18 agree.
- Hu et al. 2026 (arXiv 2601.17096), confirmed: R-C score US 8.10 (1.44) vs Chinese 6.04 (1.54), t=-13.81, d=1.38; landscape objects US 11.53 (4.39); scene objects English vs Chinese t(374.94)=-3.60, d=.36; landscape Chinese vs English d=.49. Warning: 8.10 appears as two unrelated values (US R-C score; Chinese landscape object count in a22; also t=8.10 for smiles). Not an error, but easy to mix up. a22 reports landscape count Chinese model 8.10 and b23 gives 8.10 (SD 1.91); consistent.
- Varnum et al. 2010 numbers (r=.11 composite; mean within-domain r<.06): already opened in a02; not re-opened here. Treated as read once.
- Not re-verified: Sun & Wang p-values and d=.045 (preprint search returned nothing quickly; recorded from two agents b10/c03 who agree), Tao et al. distances, Oyserman meta-analyses (abstract only), Na et al. full tables.

## Contradictions between sources
- Jin et al. (stable holistic lean across temperature and wording) vs Sun & Wang (language effect negligible) vs Hu et al. (reversals). These test different things: Jin tests default style of one model; Sun & Wang and Hu test whether prompt language switches style. Not strictly contradictory.
- a22 says Chinese model drew fewer objects but more scene objects; a23 says English prompts gave more scene objects. Different contrasts (model origin vs prompt language).
- Evidence file a counts "measures": 10+10 in the PNAS abstract vs 5 social + 11 cognitive in an APS poster. Unresolved.
- The task text says "Na et al. 2009"; the paper is 2010 (PNAS), cited as unpublished 2009 manuscript by Varnum.

## Weak spots
- The founding study was never opened in full. Every number about it is second-hand from its own authors' review (self-report of own limits).
- No direct replication of Na et al. found; 60 citing snippets only. Absence of replication is not shown.
- Almost all LLM studies test group-level (country) alignment, not individual-level structure. No study found that measures the correlation between cognition and social-orientation scores across many sampled LLM personas, which is the actual Na et al. test applied to LLMs.
- Jin et al. uses 10 runs, not independent persons; p<.001 is run-noise.
- Claim "demographics explain <10% variance" is from annotation tasks, not cognition.

## Only seen in snippets or abstracts
b03-b06 (citing snippets), a06-a16 (abstract only), b07, c05 (login wall), c21, c24.

## GAPS
1. In humans, what are the exact N and per-pair correlations in Na et al. 2010, and does a separate sample reproduce "negligible" within-group correlations (including 2023 "independent manifests" validation)?
2. If an LLM is given many sampled personas, do its scores on social-orientation scales and on holistic/analytic tasks correlate across personas, or are they as uncorrelated as in humans?
3. Does cultural-style persona prompting change accuracy on real reasoning tasks (not scales) at equal tokens, for current models?
4. Does prompt language change LLM thinking style once items are not withheld (original Lu, Song, Zhang data and items)? Who is right: them or Sun & Wang?
5. Do group-based persona prompts beat no persona on individual-level prediction of a specific user when that user's own data is available (Park-style) at equal context length?
6. How large is the variance of an LLM's cultural-style scores across neutral context changes compared with human test-retest, for 2025-2026 models?
7. Is the weak within-group link a measurement artefact (reference-group bias, low reliability) or a real structure? Reliability numbers of each task per sample are missing.
8. Does RLHF or instruction tuning cause the "Service Persona Camouflage" flattening (base vs tuned model comparison)?
9. Do other recent individual-level studies (e.g. Vignoles 2016 seven-dimension model) show a stronger individual-level link than the one-axis model?

## Gap search results
Sources opened this session: Na et al. 2010 full text (PMC2851996), Khan et al. 2503.08688, Zhang et al. 2609.00565, Taday Morocho et al. 2602.18462, Venkit et al. 2601.07110, Zheng et al. 2311.10054, Hu et al. 2601.17096 (text search), Lu et al. abstract. The arXiv, OpenAlex and Semantic Scholar APIs returned HTTP 429 (shared limits), so searching was by 8 web searches plus direct downloads. Evidence is in evidence_d.jsonl (d01-d18).

- Gap 1 (Na exact N and per-pair r): PARTLY CLOSED. N=235 US adults; mean r .008 (social) and .038 (cognitive); 2 of 45 pairs significant; five-culture two-task check r=.04 pooled and .73 at culture level. Per-pair SI tables not read. The 2023 "independent manifests" validation and any independent replication STAYED OPEN (no hit).
- Gap 2 (LLM persona correlation structure across personas): STAYED OPEN. No study found that correlates social-orientation and holistic scores across many sampled LLM personas. SCOPE (d12) compares response-similarity structure, not these constructs.
- Gap 3 (cultural persona on real reasoning accuracy): STAYED OPEN for cultural personas. Closest: Zheng et al. (d13), generic personas do not improve accuracy; culturally adapted math text costs 0.3-5.9% (snippet only).
- Gap 4 (Lu et al. vs Sun and Wang): STAYED OPEN. Lu et al. full text paywalled and items withheld; only the abstract was read.
- Gap 5 (group persona vs personal data): MOSTLY CLOSED. Demographic persona is no better than no persona (d11: .366 vs .370; .398 vs .391); demographics explain 1.5% of variance (d12); personal interview gives .83 vs .74 (Park). Equal context length still not controlled.
- Gap 6 (LLM variance vs human test-retest, 2025-26 models): PARTLY CLOSED. Khan et al. show format shifts above one human SD; no human test-retest comparison with 2025-26 models.
- Gap 7 (artefact vs structure): PARTLY CLOSED. Authors report test-retest .51 and r=.031 after dropping low-alpha measures; reliability table not read. The reference-group bias argument stands (K04).
- Gap 8 (RLHF cause of flattening): STAYED OPEN. Hu et al. ran no base-vs-tuned comparison. Zhang et al. show fine-tuning flattening, a different intervention.
- Gap 9 (Vignoles seven dimensions): STAYED OPEN. Full text behind a captcha; only sample sizes (2,924 students, 16 nations; 7,279 adults, 55 groups, 33 nations) seen.
