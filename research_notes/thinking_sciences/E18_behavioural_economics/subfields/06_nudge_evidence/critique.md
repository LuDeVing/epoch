# Critique: E18.06 Nudge evidence (cross-check)

## Re-opened this session (full text)
- Mertens 2022 (PMC8740589): confirmed d=0.45 [0.39,0.52], t(340)=14.38, n=2,149,683, I2=99.67%, 26.79% drop (0.42 to 0.31), food 0.72 [0.49,0.95].
- Maier 2022 (PMC9351501): table confirms RoBMA 0.04 [0.00,0.14], BF01=0.95; precise 0.11, BF01=0.31; finance BF01=41.23 and 30.95.
- Szaszi 2022 (PMC9351519): Andrews-Kasy -0.01 (SE 0.02) and WAAP 0.07 confirmed.
- Milkman vaccine (PMC8157982): N=47,306, +2.1 pp (5%), best 4.6 pp, shrunk 2.8 pp (6.7%) confirmed.
- Milkman savings (PMC12477529): 1,925,785 people, +0.05 pp (0.51%), best 0.13 pp (1.32%) confirmed. This upgrades a22 from abstract-only to full text.
- Cherep PNAS (PMC13291645): control 51%; late suggestion humans 25% vs models 42-77% (Gemini 2.5 Flash 13%, o3 Mini 7%); highlight 57% vs Gemini 1.5 Pro 100%. Confirmed.
- DellaVigna and Linos (NBER PDF): 126 RCTs, 23 million, 1.4 pp (s.e. 0.3), 8.1% over 17.2%; academic 8.7 pp (s.e. 2.5), 33.5% over 26.0%; median n 484 vs 10,006; MDE 6.3 vs 0.8; "one sixth". Confirmed.

## Corrections
- b09 gives 33.4% and 8.0%; the paper says 33.5% and 8.1% (a12 is right).
- Egger b is 2.28 (t(339)) in the original Mertens paper and 2.10 (t(332)) in the corrected data used by Maier and the reply. Different datasets, not a conflict. a03/b03 should say so.
- Severe-bias adjusted d: 0.03 in the original paper, 0.08 in the reply. Treat 0.03-0.08 as the range.
- Human baselines for suggestions differ between the preprint (c02: early 0.37, late 0.34) and PNAS (a25: early 35%, late 25%). Prefer PNAS; the model list also grew from 8 to 14.
- a15 practitioner median 1.95 pp was not reconciled with the paper's 3.3 pp practitioner forecast for academic nudges; a15 not re-verified.
- c06 (Halimeh 2026) was not re-opened; the arXiv search did not return it. Odds ratios 8.70 and 37.24 rest on the earlier read only.

## Contradictions between sources
- Mertens (d about 0.43, structure strong) vs Maier and Szaszi (about 0 after correction). Mertens concede bias; true size unresolved (0 to 0.31). Structure: Maier undecided (BF01 1.12); Szaszi and Jachimowicz keep defaults as the exception.
- Heterogeneity: Maier find heterogeneity everywhere except finance; Bryan et al. read it as context dependence rather than failure.
- Reasoning in LLMs: Cherep finds strong reasoning models near human default rates; Halimeh finds high reasoning halves default following but raises social-proof following. Tasks differ.

## Weak spots
- Abstract-only: a21 (gym full text), a23, a28-a31, b20, b31, c22. The sycophancy and bias papers are not nudge tests.
- LLM nudge studies are 2025-2026 preprints or single groups (Cherep appears in three lines: one source). No independent replication of default hypersensitivity. I set K11 to single-source for that reason.
- No study measures a nudge-style change to a scaffold at equal tokens on reasoning accuracy.
- Founding studies (Madrian-Shea, Johnson-Goldstein) not re-opened; a19 is non-randomised; a18 values were read from a figure (N=161).

## GAPS
1. Does a structural scaffold change (forced format, default plan, effort cap) beat advice-style prompt additions at equal tokens, scored on fresh held-out items with the winner's estimate shrunk?
2. How much of our own measured scaffold gain disappears on a larger fresh sample (is the DellaVigna one-sixth ratio visible)?
3. Can LLM judges or the agent itself predict which scaffold variant wins better than chance (the megastudy forecasting failure)?
4. Does a deliberate reflection step reduce default and suggestion pull in the target model without raising social-proof or authority pull (Halimeh interaction)?
5. Is default hypersensitivity stable across paraphrases of the task and across model versions (Montero-Porras)?
6. Do RLHF-amplified biases (decoy, framing, omission) reach our task families, and does a debiasing step help at equal tokens?
7. How well does a scaffold effect persist across task types and models (the heterogeneity question), and which moderators predict it?
8. Do mid-run guidance injections (Wink-style) raise accuracy or only reduce visible misbehaviour?
9. Is there a true small effect of structure nudges in human field data after bias correction? Needs preregistered large trials.
10. Do scaffold defaults have a side effect analogous to the 3% anchor (Madrian-Shea) on dimensions the model was not asked to choose?

## Gap search results (evidence_d.jsonl, d01-d16)
Search budget ran out partway (WebSearch exhausted; Semantic Scholar, OpenAlex and arXiv APIs returned 429). Work came from direct fetches and PDFs.

- Gap 1 (structure vs advice at equal tokens): partly informed, still OPEN. Meincke et al. (d06, d07): advice-style CoT gives small gains against a no-thinking control, near zero against the model default, marginal for reasoning models; four advice wordings made negligible difference. Nobody tested a structural change against advice at equal tokens.
- Gap 2 (does our gain shrink on a larger sample): OPEN. It needs our own harness. Wink (d02) shows the pattern in a deployed system: recovery 91% in the table, only about 4-5% in the live A/B.
- Gap 3 (can judges or the agent forecast winners): partly informed, OPEN. LLM forecasts of survey-experiment effects correlate r=0.85 but overestimate size and weaken on megastudies (d13, abstract only); human experts do not rank treatments better than non-experts (d14, abstract only).
- Gap 4 (reflection without raising social-proof pull): OPEN. Halimeh re-read (d08, d09): API-level high reasoning cut default following 92% to 86% (OR 0.51) but raised social following 96% to 98% (OR 1.71). Prompt-level reflection untested. This also closes the earlier c06 open item (numbers confirmed in full text).
- Gap 5 (paraphrase and version stability): paraphrase half CLOSED. Montero-Porras (d11, d12): same model flips 0.27 to 0.88 with wording; gpt 5.1 vs 5.4 differ under permission wording. Sclar (d04, d05): format spread up to 76 points, weak cross-model correlation. Version stability beyond that single comparison is not measured.
- Gap 6 (RLHF biases in our task families, debiasing at equal tokens): NOT SEARCHED (rate limits and a PMC captcha, d16). OPEN.
- Gap 7 (heterogeneity and moderators): partly informed. Moderators seen: model size class (d10: default OR 15.94 small vs 4.64 flagship; social OR 17.59 small vs 107.57 flagship, exploratory), wording, format, reasoning setting. OPEN as a predictive model.
- Gap 8 (mid-run guidance: accuracy or only visible misbehaviour): answered for Wink: only visible misbehaviour and process metrics were measured (d01-d03); judge precision 85.7%; 37% of non-recoveries ignored the guidance. Accuracy effect remains OPEN.
- Gap 9 (true small structure effect in human field data): NOT SEARCHED (d16). OPEN.
- Gap 10 (side effect like the 3% anchor): human evidence strengthened (d15: half still at default rate and fund after three years, wealth effect offset on average; abstract only). No scaffold-side measurement. OPEN for our agent.

Status changes in claims.jsonl: K11 and K13 raised to established (three groups on defaults; wording and format sensitivity from two). K20 reworded to say accuracy was not measured. K10 and K12 extended. New: K22, K23 (single-source), K24, K25 (open).
Still weak: d13, d14, d15 are abstract or project pages only; Meincke is an industry report with an unrecorded exact URL.
