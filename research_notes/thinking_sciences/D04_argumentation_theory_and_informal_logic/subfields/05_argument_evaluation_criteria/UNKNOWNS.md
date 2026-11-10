# Argument evaluation criteria: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| D04.05-U1 | Does an ARS checklist Verify step improve open-answer quality over a generic check? | S8 ARS checklist with concrete yes/no items for open mode | S8 | K01, K24, K26; b27 gap; nearest d10 (STICK), d01 (CQoT); single-source, proxy metrics | 100 open items with rubric; arms: no verify, generic check+revise, 3-sample SC, ARS+revise; blind cross-family judge; win rate and rubric score | ARS beats generic check by 5+ win-rate points and beats SC at equal calls | High |
| D04.05-U2 | Which ARS move does the work; is a sufficiency-only probe enough? | Sufficiency-only probe in place of the full triad (cheaper) | S8 | K05, K16; c09 (relevance fail under 0.5%); human-only plus one 2026 LLM study; d09 indirect | Same 100 items; triad (3 calls) vs sufficiency-only vs relevance-only at equal tokens; win rate, defects per 1,000 tokens | Sufficiency-only within 2 points of triad at lower cost, or better | High |
| D04.05-U3 | Does a counterfactual-objection probe (CASA) beat "is this enough?" on frontier models and full answers? | Counterfactual objection step inside S8 | S8 / O | K15, K14; b04, b05 (7B models only); single-source | 60 answers with a known removed premise; arms: CASA-style, plain sufficiency question, strongest-objection rebuttal; F1 on hard items | Objection arm beats plain by 5+ F1 on hard items | High |
| D04.05-U4 | Does a global-sufficiency item (name the strongest objection, say if answered) catch defects the local items miss? | Rebuttal item in S8 | S8 | a28, a09 (1 of 304 high); human-only; no LLM test | Answers with and without a planted unrebutted objection; arms: local ARS only vs +global item; detection rate and false alarm rate | Detection up 10+ points with false alarms under 15% | Med |
| D04.05-U5 | Does resample agreement find weak acceptability closed-book on premises? | Resample check for model-asserted premises | S8 / G4 | K33; d13 (factual claims only, inconsistency only); single-source | Answers with seeded false premises; arms: single-pass true/false, 5-sample agreement, retrieval check; AUC | Resample AUC above single pass by 0.05 and no loss on consistent-error items | Med |
| D04.05-U6 | Does CoT before the ARS verdict hurt on frontier models? | Verdict-first rule in S8 (or drop it) | S8 / G11 | K12, K30; a24, a20, d05 (older or open models, other tasks); contested | Human-gold set of sufficiency labels (80 items, hard subset flagged); verdict-first vs rationale-first vs CoT; alpha with gold on hard items | Verdict-first at least equal at fewer tokens | Med |
| D04.05-U7 | Is the judge biased by hedging, length or own-family style? | Judge debiasing: length normalise, cross-family, hedge strip | G5 / S8 | K16, K31; d06, d07, c11; hedge bias untested | Paired rewrites (hedged vs plain, long vs short, fluent vs plain), same-family vs cross-family judge; score gap in SD | Gap above 0.3 SD for any cue means the fix is added | High |
| D04.05-U8 | Does an ARS check reduce acceptance of fallacious or irrelevant text in retrieved context? | Relevance mark-and-drop plus ARS gate for retrieved text | S1 / S8 | K18, K32; c23, d08, b12; single-source each | Passages with 0, 1, 3 irrelevant or fallacious paragraphs; arms: none, relevance filter, ARS check; accuracy and acceptance rate | Accuracy loss cut by 30%+ or acceptance cut by 30%+ | Med |
| D04.05-U9 | Does a single-example or anecdote flag detect weak support in model answers? | Cheap lexical flag feeding S8 | S8 | K07; a07 (essays, CNN .843); human corpora only | Answers resting on one example vs several; flag precision and recall vs sufficiency gold | Precision 70%+ and recall 50%+ | Low |
| D04.05-U10 | Is checking the final justification against the reasoning trace worth it? | Trace-vs-justification consistency check | S8 / G10 | K17; c12 (8 models, 3,182 pairs, single-source) | Items where trace and final answer diverge; arms: ignore, trace-check; accuracy | Catches divergences that raise accuracy 3+ points | Low |
| D04.05-U11 | Do graded, audience-named acceptability ratings beat pass/fail? | Graded verdicts and an audience field | S8 | K34, K22; d14, d16, a25; SEP only; contested | Items with audience-dependent premises; arms: pass/fail vs weak/moderate/strong+audience; agreement with gold and final quality | Graded arm better on win rate by 3+ points or on gold agreement by .05 alpha | Low |
| D04.05-U12 | Would probability-style support estimates beat the checklist for calibrated confidence? | Consistency-based support estimate for final confidence | S8 / memory | K22; a25, a26, d12 (verbal confidence 80 to 100%); no LLM study | Same items; checklist verdict vs resample-based posterior; calibration error and win rate | Calibration error drops 20%+ at equal tokens | Low |
| D04.05-U13 | Do dimension order and listwise judging matter for our judge at equal tokens? | Listwise x3-order judge | S8 | K10; a22, b11 (alpha .203 vs .447); GPT-4o, older corpus | Gold set; one pointwise vs listwise x3 orders vs 3 pointwise samples; alpha on hard items | Listwise x3 above 3 pointwise by .05 alpha | Med |

## Open questions we cannot test on our bench yet

- **Human gold for ARS on model answers.** We have no labelled sufficiency set for open model answers. Unblock: build 80 to 100 answers with two human raters, report alpha overall and on the contested 30% (the .14 regime).
- **Johnson and Blair and Govier books.** Never opened. Unblock: obtain the text or a faithful secondary source and extract limits for conductive arguments and audience-relative acceptability.
- **Frontier-model hard-item judge agreement.** All 2017 corpus results use older or open models. Unblock: rerun the 320-argument corpus with a current model on the hard items.
- **Hedging as a defect or a cue.** Henselmans found hedging marks low grounds. Needs paired-rewrite data (U7) and a human reading to decide.
- **Perspective of the rater.** Quality depends on expert, crowd or novice view (Romberg 2025). Unblock: decide the target audience for our open answers and fix it in the rubric.
- **Annotator-information claim (8 of 103 datasets)** is unverified. Unblock: check the survey text.
- **Self-preference in Henselmans-style results** (judge and subject overlap). Unblock: a cross-family re-judge of a sample.

## Order to run

1. **U1 (ARS vs generic check).** It is the central hole: no study tests it, and the whole subfield's value depends on it.
2. **U7 (judge bias on hedging, length, family).** Every other test uses a judge; this fixes the instrument cheaply before we trust any result.
3. **U2 (sufficiency-only vs triad).** Same items as U1, small extra cost, and a win cuts the Verify cost to a third.
