# Critique, E10.01 data-frame theory and frame activities

## Checks done (sources re-opened this session as PDF text)
Confirmed at source:
- Huang et al. 2024 (arXiv 2310.01798): oracle GPT-3.5 GSM8K 75.9 to 84.3, GPT-4 95.5 to 97.5; intrinsic GPT-3.5 CommonSenseQA 75.8 to 38.1 to 41.8; GPT-4 GSM8K 95.5 to 91.5 to 89.0.
- Alavi Naeini et al. 2023 (2306.11167): GPT-4 0-shot 6 walls / 239 groups original, 59 / 595 randomized.
- Laban et al. 2025 (2505.06120): 39% average drop, aptitude -15%, unreliability +112%, 30.9 vs 64.4.
- Jhaveri et al. 2026 (2604.02485): 42% to 56%; judge agreement 98.5-99.5% on 200 items.
- Handler et al. 2026 (2605.15000): about 70% to 48% false action on both sets.
- Braitsch et al. 2026 (2607.10275): 68.1% best, R=0.69, 56.8% in round 1, 43.6% differential, 66.6% diagnosis, 7 of 8 recovery. The Table 2 text layout is garbled (the 68.1 sits on the MiniMax row), but the body text says Opus 4.6 got 68.1%.
- Shidara et al. 2026 (2601.11866): 0.751 (CI 0.738-0.763) vs 0.66 (CI 0.55-0.75); 20/100 human-miss items, 36%; 55.0% decisively correct.
- Kornowicz 2024 (2411.08583): 439 recruited, 375 analysed, Brier 0.173 vs model 0.178, Kruskal-Wallis p=0.154.

## Corrections
1. c18 says "With oracle labels: GPT-3.5 GSM8K 75.9 to 95.5". Wrong. 95.5 is GPT-4's standard score. The correct figure is 75.9 to 84.3 (as in a-file b20). Fixed in claim K07.
2. b20/c18 attach the GSM8K intrinsic drop to GPT-3.5 loosely. At source, GPT-3.5 GSM8K barely moved (75.9, 75.1, 74.7). The big GPT-3.5 drop is on CommonSenseQA only. Claim K07 states both.
3. b17 says "10-shot GPT-4 did not beat 0-shot". Source table rows for GPT-4 randomized are mixed (0-shot 59, 1-shot 57, 3-shot 62, 5-shot 68 walls). Treat "no consistent few-shot gain" as the safe reading, not "none".
4. a03 / b01 count 7 or 6 activities. Klein 2007 lists mapping plus six frame activities. Use "six frame activities plus mapping".
5. b01 says experts have ">5 yrs HCI" while a01 says "more than 10 y". Not resolved (Pontis & Blandford PDF not re-opened). Use "experts" without a year figure.

## Contradictions between sources
- Fixation in medicine: Kim 2025 (physicians 66%, models under 50%) against Shidara 2026 (model 0.751 vs physicians 0.66). Different model generations, same benchmark family, so the weakness may be a generation effect. Status contested (K15).
- Evaluative AI: Kornowicz 2024 found no gain; Le et al. 2024a (as reported by Kornowicz) found one. Contested (K17).
- Reflection: Costa Filho (humans, helps on easy cases) and Huang (LLMs, hurts without outside signal) look opposed. They differ in who reflects and whether new input arrives. Not a true contradiction, but a transfer gap.
- Experts: a10 says experts share the reasoning process with novices; a04/b03 show different behaviour (more questioning). Reconcilable: same process, different cue knowledge.

## Weak spots
- The two founding papers (Klein, Moon and Hoffman 2006; Klein, Phillips, Rall and Peluso 2007) were never opened. Every claim about what the theory says comes second hand (Pontis & Blandford, Rankin et al., notes, Prochaska). The 'max 3 frames' and '3-4 anchors' numbers are second hand only.
- Only one independent empirical test of the theory (Pontis & Blandford, 11 people, 4 analysed in depth). Rankin et al. is a fit to interviews, not a test.
- Many LLM studies are about bias, not frames. The link from "confirmation bias in Wason" to "frame questioning" is our inference.
- Most LLM numbers are 2026 preprints not yet peer reviewed. Handler uses prompts on a few models. Yuan 2026 has 72 responses only.
- The Klein plausibility model rests on 23 cases and one reviewer.
- Pontis & Blandford, Karvetski, Costa Filho and Dhami numbers were not re-opened this session. They keep the first-pass flag.

## Only seen in snippets / not opened
a21, a22, a23, a24, b10 (second hand), b15, b16, b24, b25, b26, c04, c15, c16, c17, c25. Chinn & Brewer (1993) seven responses to anomaly is known only from memory and a snippet.

## GAPS (most decision-relevant first)
1. At equal tokens, does a trigger-based reframe (fires on an anomaly or strain count) beat plain chain of thought and an always-reframe loop on tasks with a misleading first frame? No study tests this on an LLM.
2. What are the exact trigger rules in Klein 2007 and Klein 2023 (what counts as an anomaly, how many are tolerated, how the 3-frame limit arises)? Need the founding chapter or the 2023 full text.
3. Does the question-the-first-answer gain (humans, easy cases only) hold for LLMs when the check uses an outside tool versus only the model itself, and does it vanish on hard items?
4. Is LLM frame fixation still present in current reasoning models on an independent fixation benchmark (the Kim vs Shidara contradiction)?
5. Does a forced disconfirming-test step (Think-in-Opposites style) carry from rule-discovery tasks to open diagnostic and debugging tasks, and at what token cost?
6. Do the Chinn & Brewer seven responses to anomaly (ignore, reject, exclude, abeyance, reinterpret, peripheral change, theory change) give a better operator set than preserve versus reframe? Read the original.
7. How does the agent decide to stop elaborating and commit (the stopping rule)? Klein's "plausibility feels sufficient" has no measured threshold. Look at the metareasoning subfield.
8. Can a frame be tracked as an explicit editable object (anchors, expected data, open anomalies) in context, and does this beat free-text reasoning at equal tokens (Jain 2025 proposes it; Zheng 2025 models it; nobody measured)?
9. Do reframes that differ in assumptions (the deep-story point from Prochaska 2024) give more diverse and more correct answers than reframes that only reword?
10. Do the experts' extra steps (source-quality checks, discarding data, longer elaboration) improve outcomes, or just correlate with expertise? Pontis & Blandford show behaviour, not accuracy.

## Gap search results (evidence_d.jsonl d01-d20; claims K25-K32 added, K02/K06/K07/K10/K15/K23 updated)
Limits of this pass: the web-search quota ran out early, so the work used direct page fetches and the arXiv API. The disk had 13 MB free, so no PDFs were kept. Sources that returned 403 or were never found: Klein et al. 2007 chapter, the FOCUS report, Chinn and Brewer 1993.

1. Trigger-based reframe vs plain CoT vs always-reframe at equal tokens: STILL OPEN. No study. Indirect cost evidence for always-reframe: wrong answers have 418% more thought switches (d19) and one model changed 98.7% of answers when told to revise (d14). Indirect support for gated action: ECLoop gate (d10).
2. Exact trigger rules: PARTLY CLOSED, in the negative. Klein 2023 re-read (d01) has no numeric anomaly tolerance, strain threshold or frame limit. The 2007 chapter was not obtainable (d02). The "3 frames" figure stays second hand.
3. Question-the-first-answer for LLMs, outside tool vs model only: MOSTLY CLOSED. Tools beat no-tool critique (d13, d12, d15). 2026 models gain from no-tool revision on verifiable tasks, and the gain tracks checkability (rho 0.65), not baseline accuracy (rho 0.05) (d14). No direct easy-vs-hard split exists; "vanishes on hard items" is not shown for LLMs.
4. Fixation in current reasoning models: PARTLY CLOSED. Same benchmark, same group: best model 50% (Dec 2024) to 75.1% (2026), physicians 66% (d03, d04). Looks like a generation effect. Not independent, 100 items, 20-item hard subset with wide intervals. No independent fixation benchmark found.
5. Forced disconfirming step on open tasks: PARTLY CLOSED. Rule discovery gains are solid in humans (d07, d08) and LLMs (d05, d06). On open troubleshooting one agent lost about 5 points without its counterfactual critique (d09), but cost was not reported and the study bundles many parts. Token cost of the step alone is unmeasured.
6. Chinn and Brewer seven responses as operators: STILL OPEN. Original unread. Secondary text gives the seven classes and the credibility and ambiguity factors (d16). No LLM use.
7. Stopping rule: PARTLY CLOSED. Klein gives no threshold (d01). One measured commit gate exists (d10: +4.8 to +11.8 points, up to 12.1% fewer tokens). Self-agreement is not a safe stop signal (d17). Link to the adaptive-stopping subfield.
8. Explicit editable frame object vs free text at equal tokens: PARTLY CLOSED for structure, OPEN for the frame object. Controller-held belief state beat ReAct, and prompting ReAct with the same procedure did not (d11). Structured state beat prose state by 10 of 100 (d10). Nobody tested anchors, expected data and open anomalies in context at equal tokens.
9. Assumption-changing reframes vs rewording: STILL OPEN. Only a scoring method exists (d20, prediction dissimilarity).
10. Do experts' extra steps improve accuracy: STILL OPEN. Nothing new found. Related: agents drop noticed conflicts, and prompting for conflicts can lower accuracy (d18).

Other corrections: Shidara's abstract says the top 5 models got 55-70% right with high confidence, but the body supports only 55.0% (Claude 4.1 Opus, 20 items). The a-file and b-file expert-years disagreement (5 vs 10) is still unresolved.
