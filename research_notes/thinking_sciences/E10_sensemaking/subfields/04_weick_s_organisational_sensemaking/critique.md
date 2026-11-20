# Critique: Weick's organisational sensemaking (E10.04)

## Corrections made (re-opened this session via arXiv PDFs, pdftotext)
Confirmed with no change: Turpin 2023 (-36.3% suggested-answer bias; CoT 57.1 to 59.6 GPT-3.5, 59.2 to 65.3 Claude 1.0); Arcuschin 2026 (4,834 pairs; 13.49%, 7.42%, 0.37%, 0.04%); Reflexion (+22% AlfWorld in 12 steps, +20% HotPotQA, HumanEval 91.0 vs 80.1); Park 2023 TrueSkill (29.89, 26.88, 25.64, 22.95, 21.21; 100 evaluators); Sensecape (68.3 vs 22.8, t(11)=3.1, p=0.01); Selenite (840.3 s vs 1319.3 s, 36.3% faster; precision 98.8 vs 78.4; recall 73.0 vs 30.4; valid criteria +90.4%); Sharma 2024 (95%; 45%); Lanham 2023 (13B changes answer after CoT more than 175B on 7 of 8 tasks; six of eight tasks have the 13B model most faithful).

Corrections and clarifications:
1. c06 (Huang 2024) understated the harm. GPT-3.5 CommonSenseQA fell from 75.8 to 38.1 (round 1) and 41.8 (round 2), a halving, not just "more answers altered". GSM8K: 75.9, 75.1, 74.7 is right. Beware: the text "74.7% retains its initial answer" is a different number that happens to equal the round-2 accuracy.
2. Lanham: b09/c04 wording mixes two statistics. "7 of 8 tasks improve under CoT" (HellaSwag is the exception) is separate from "13B changes its answer more than 175B on 7/8 tasks". Claim K06 uses the second.
3. Sharma: the 95% is the Claude 2 preference model preferring a sycophantic over a baseline (non-helpful) truthful response. It is not a human rate.
4. Palta et al. 2026 (b01-b03) could not be re-opened (arXiv title search returned no id). Numbers stay as recorded by agent b. Mooney 2026 (c07), Dammu 2026 (c08), Sindelar and Bojar 2025 (c10) also not re-opened.

## Contradictions between sources
- Reflexion (gain from retrospect) vs Huang (no gain from self-review). Reconciled by the external binary signal; K08 is marked contested.
- Arcuschin shows rationalisation falling sharply in reasoning models (0.04% Sonnet 3.7 thinking) while Turpin and Lanham tested older models. Do not generalise the 2023 numbers to current models.
- Lanham inverse scaling (bigger = less faithful) is opposite to the intuition that larger models reason more reliably; only 4 model sizes of one family.
- Palta: pro-arguments lowered human plausibility ratings for obvious answers (an "at most plausible" reading), not a pure persuasion effect.

## Weak spots
- Core gap: no experiment or LLM study operationalises the seven properties (a25, b29, c22; about 20 arXiv queries, 0 hits for the exact phrase). Every "LLM test" here is an analogue (faithfulness, sycophancy, reflection), not a Weick test.
- Many claims rest on a single paper. Only K03 (rationalisation) and K11 (sycophancy) reach "established", and K13 for human-tool studies at N=12.
- Founding evidence (Mann Gulch, Bhopal, Tenerife, Columbia, Challenger) came from Wikipedia, which is secondary and partly the same article; Weick 1993, Weick 1995, Maitlis 2005, Maitlis and Christianson 2014 were never opened. Agent-relevance text for them is from memory.
- Sensecape and Selenite use Pirolli-Card, not Weick, with N=12 and authors' own tools.
- Klein 2023 plausibility model: a literature search (1,042 hits, 23 cases), no test.
- Weick plagiarism allegation (a10) is a credibility caveat for the Mann Gulch narrative; the facts of the fire come from other sources (Maclean, Rothermel).

## Only seen in snippets or titles
a19-a24 (abstract listings only), c20, c21, b28, b24-b26, c19, c23.

## GAPS
1. Does any study test enactment (acting to generate cues) against passive analysis in LLM agents at equal tokens? Reflexion suggests the signal matters; a clean ablation is missing.
2. What is the actual structure of Weick 1993 and Weick 1995 evidence (case counts, claims on identity and cosmology episodes)? Need primary text, not Wikipedia.
3. Do current reasoning models (2025-2026) keep the 2023 unfaithfulness and sycophancy rates beyond Arcuschin's data? Need a like-for-like re-run.
4. Maitlis 2005 and Maitlis and Christianson 2014: the counts of studies and the four sensemaking forms, and which boundary conditions (leader control, stakeholder voice) are supported.
5. Is there a replication or failed replication of any Weick-derived organisational finding (HRO traits, Maitlis typology) with quantitative effect sizes?
6. Can "strain" or plausibility gaps (Klein 2023) be measured on an LLM trace and used as a re-framing trigger?
7. Does a retrospective reconstruction (hindsight data, c07) help at inference time as well as in training, and is the 2.0% gain robust?
8. Does an audience (second model instance) reduce plausibility drift in self-judgment (Palta) or increase sycophancy (Sharma)?
9. How do El Faro (Arrested Sensemaking), Columbia and Challenger re-analyses compare to Mann Gulch on measurable cue-ignoring patterns?
10. Does generative AI reduce or increase organisational sensemaking in measured studies (b28 title only)?

## Gap search results
Tools were limited: OpenAlex, Semantic Scholar and arXiv query APIs returned 429, WebSearch budget was exhausted, publisher pages returned 403. Worked: Crossref metadata, Wikipedia, direct arXiv PDFs (7 opened). Evidence in evidence_d.jsonl (d01-d18); claims K20-K24 added, K03/K05/K07/K08/K11/K14/K16/K19 extended.

1. Enactment vs passive at equal tokens: PARTLY CLOSED. No clean ablation exists. ReAct (d04, d05) is the closest: Act 25.7 vs CoT 29.4 vs ReAct 27.4 HotpotQA EM; hybrids 34.2-35.1; ALFWorld ReAct 71% vs Act 45%. Not equal tokens. New claim K20.
2. Weick 1993/1995 primary structure: OPEN. Text not reachable (Crossref only, d12).
3. Reasoning models vs 2023 rates: CLOSED for direction. Chen 2025 (Claude 3.7 25%, R1 39%) and Chua and Evans 2025 (R1 59% vs V3 7% on professor cue) show reasoning models name cues much more often but still mostly hide them; rates vary by cue (near 0% for follow-up pushback). No re-run on 2026 models.
4. Maitlis 2005 and Maitlis and Christianson 2014: OPEN. Only metadata (d10, d11); Maitlis, Vogus and Lawrence 2013 abstract read (d13).
5. Replications of Weick-derived findings: OPEN. Vogus and Sutcliffe 2007 scale studies located (d14) but not read; no failed replication found or ruled out.
6. Strain / plausibility gap on LLM traces: PARTLY CLOSED. No strain test; P(True) and sample agreement (Kadavath 2022, d09) are the nearest measurable proxy. K22.
7. Retrospective reconstruction at inference time: PARTLY CLOSED, negative lean. Kamoi 2024 (d07): no success with prompted-LLM feedback outside special tasks; Self-Refine +20% absolute on soft metrics (d08). c07 gain still unverified.
8. Audience effect: CLOSED toward "increases drift". Peacemaker or Troublemaker (d06): same-model debate collapses (DCR 62.67% to 86.36%); judge and 3 agents help. K21. Palta-style plausibility drift with a second instance not tested.
9. El Faro, Columbia, Challenger vs Mann Gulch: PARTLY CLOSED, descriptive only (d15, d16). No shared measurable cue-ignoring metric. Challenger not covered.
10. Generative AI and organisational sensemaking: OPEN. Only a weak 2026 practitioner abstract (41% lower narrative alignment above 60% AI content, d17).
