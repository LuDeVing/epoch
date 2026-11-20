# Categorisation and attention: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| A19.04-U1 | Does a paraphrase-spread control change which scaffold gains we believe? | A rule: every scaffold test reports worst, best, mean over at least 5 wordings | G7 | K22; Sclar median 7.5, up to 76; Cao 45.48 (older open models) | Plain vs scaffold on 3 existing bench sets, 5 paraphrases each; metric: gain minus paraphrase spread | Any previously reported gain falls inside the spread on at least 1 of 3 sets | High |
| A19.04-U2 | Does "belongs to" vs "is similar to" wording shift our agent's rule-vs-resemblance choices? | Per-task-class wording choice in S2 representation | S2, O6 | K01; human d=0.86, N=7,396; not tested on LLMs | 40 fresh rule-vs-resemblance items x 5 paraphrases; arms belongs-to, similar-to, neutral; metric: rule-choice share | Gap of 10 points or more between belongs-to and similar-to, and it holds in 4 of 5 paraphrases | High |
| A19.04-U3 | Does re-framing the task move answers more than a scaffold step? | A framing-control arm in every G7 test | G7 | K14; one study (Sun and Wang d=-2.095); wording noise K22 | Same items as U1; arms neutral, change-framed, scaffold; metric: accuracy | Framing gain at least half the scaffold gain on any set | High |
| A19.04-U4 | Does a context-first vs focal-first instruction change accuracy on distractor-heavy or change-detection tasks? | A one-line S1 instruction ("scan all context before the main item"), or a drop of the idea | S1, O6 | K23, K06; GSM-IC +3 to +5 for "ignore" on a 2023 model; context-first untested; humans single-source | 60 distractor problems + 40 planted-change items; arms focal-first, context-first, neutral; metric: accuracy, detection rate by change type | Either direction gains 5 points or more over neutral on distractor set, outside paraphrase spread | Med |
| A19.04-U5 | Do persona or prompt-language prompts change our model's answers at temperature 0 and 1? | Confirmation to keep persona and language prompts out (4b entry) | G4, 4b | K13 established for 8 other models; K25 Lu et al. unverified | 40 fixed items; English vs Chinese; with and without persona; temperatures 0 and 1; per-model d | d below 0.1 on all items: add to 4b. d of 0.3 or more on our model: open a follow-up test | Med |
| A19.04-U6 | Does naming the relation in a retrieval cue help analogue retrieval? | Cue-writing step in O7 that names relation or causal structure | O7, memory | K24, K18; human single-source (Gentner 1993); LLM evidence secondhand | 30 problems, 1 correct precedent among 10 distractors (half surface-matched); arms object cue, relation-naming cue, both; metric: top-1 retrieval and downstream solve rate | Relation-naming or both arm beats object cue by 10 points on top-1 and does not lower solve rate | Med |
| A19.04-U7 | What is our agent's default grouping on fresh triads (relational vs taxonomic), and is the published-triad result memorised? | A default-bias note for S2, or nothing | S2 | K11, K12; Jin 0.85 to 0.87 (10 real items); Hu 8.10 vs 6.04; contested direction | 30 fresh triads + 10 published; 100 runs at temperature 1 and 0; metric: relational share, fresh vs published | Fresh share differs from published by 15 points or more: record as memorisation, no add. Otherwise record the default only | Low |
| A19.04-U8 | Does an instruction that names the relevant cue (object vs surface) steer a vision-input agent? | A cue-naming line when images are in the task | O6 | K20; prompts moved shape bias 49% to 72% (VLM, low-level cues) | If images are used: 50 cue-conflict items; arms named cue, other cue, none; metric: share choosing named cue and accuracy | Share shifts 15 points or more with no accuracy loss | Low |
| A19.04-U9 | Do LLMs show a thematic-to-taxonomic shift when given age-labelled triads? | Nothing for the schema; basic knowledge | none | K19; no study found in 8 searches (weak absence) | 40 triads with age labels (3, 5, 8, adult); metric: taxonomic share by age | Not an add test; run only if cheap and U7 is done | Low |
| A19.04-U10 | Does the bias-free score (hit and correct-rejection) change conclusions on our validity or syllogism sets? | A scoring rule in G10 tests: report yes-rate and sensitivity | G10 | K04 refuted belief bias as accuracy gap (Unsworth and Medin); human data only | Existing syllogism set; arms none (scoring only); metric: yes-rate per condition, sensitivity vs raw accuracy | Yes-rate differs by 10 points or more between conditions, or ranking of conditions changes under sensitivity | Med |
| A19.04-U11 | Is a style score from an LLM judge reliable enough to use? | A rule: human spot check of 50 or more items for any judge-scored style metric | G8 | Sabir: judge 29.00% vs human 17.75% holistic | 50 outputs scored by judge and by two humans; metric: agreement and bias | Judge differs from humans by over 10 points: require the spot check in every judged test | Low |

## Open questions we cannot test on our bench yet

- Lu et al. 2025 numbers: full text and items are paywalled or unreleased. Unblock by requesting items from the authors, or running U5 on our own items.
- Original triad effect sizes (Chiu 1972; Ji and Nisbett 2000): counts were not in any review we read. Unblock by opening the primary papers.
- Evans et al. 2009 and Lacko et al. 2025: not opened in full. Unblock by getting the PDFs.
- Whether holistic or analytic style helps an agent solve problems: nothing measured it. It needs a task set where the answer depends on context vs focal detail, built by us.
- Contamination of triad items: needs unseen items from a new source; none published.
- Eye-level attention: no agent analogue; nothing to run.
- Fully crossed content x language design for VLM captions: needs a vision model and a Japanese image set; we have neither on the bench.

## Order to run

1. **U1 (paraphrase spread).** Cheapest, applies to every other test, and decides whether small gains are real.
2. **U2 (wording lever, belongs-to vs similar-to).** Only large, replicated effect in this subfield (d=0.86); never tested on a model.
3. **U3 (framing control).** Reuses U1 items; shows whether framing beats scaffold steps, which would change how G7 tests are read.
