# Whorfian psychophysics: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| A15.06-U1 | Does stating the time/space frame explicitly cut errors on direction-ambiguous items? | One frame line in S1 restatement for direction-dependent classes | S1 | K23, d12, a05, c13; single-source, LLM and human | 60 ambiguous time items + 60 perspective items; A plain, B + frame line; accuracy, 3 samples | B beats A by >= 5 pp with CI above 0, no loss on unambiguous items | High |
| A15.06-U2 | Is our model's accuracy sensitive to prompt language or paraphrase at our working size? | A wording-sensitivity probe: re-ask in a second wording, log disagreement in the class record | S0, G4 | K11, b22, d10, d11; single-source, gap shrinks with scale | 100 exact-answer items, original vs 2 translations vs paraphrase; accuracy gap, agreement | Gap >= 4 pp or disagreement >= 10% on some class, and disagreement predicts error (AUC > 0.6) | High |
| A15.06-U3 | Does a vocabulary-constrained member add real diversity to an ensemble? | One constrained-vocabulary member in S3 for open mode | S3 | K20, d18; single-source preprint, sign varies by model | 40 checked problems; A 3 plain members, B 2 plain + 1 No-Have/E-Prime, length-matched; coverage, final accuracy | Coverage +5 pp and final accuracy not lower, on 2 task sets | Med |
| A15.06-U4 | Does an irrelevant distance cue shift LLM duration estimates more than the reverse? | A note in S1 input hygiene: strip irrelevant magnitude cues across dimensions | S1 | K02 human-established; LLM untested (K15) | Path length vs walk time pairs; cue present vs removed, both directions; slope on irrelevant dimension | Asymmetry slope_TS - slope_ST > 0 with CI above 0 and cue removal improves accuracy >= 3 pp | Med |
| A15.06-U5 | Does an explicit reference-frame step or Spatial-Guided prompt help spatial items at equal tokens? | Frame step for spatial classes | S1/S2 | K14, c13; reported gains 2.9 to 30%, not at equal tokens | 80 FoREST/COMFORT-style items; plain vs frame prompt; accuracy | +5 pp at equal tokens on two item sets | Med |
| A15.06-U6 | Are ambiguous wordings ("move forward") swung by a spatial prime in LLMs, as in humans? | Rule: no spatial metaphors in task statements for direction items; make U1 frame line default | S1 | K07, a05, a06; human only | Meeting-question variants with ego/time-moving primes; answer share Friday vs Monday | Shift >= 15 pp between primes | Med |
| A15.06-U7 | Does the Goli-Singh language effect on time preference replicate on another model? | Nothing in schema; only a rule never to treat language gaps as signal | G4 note | K12, c01-c03, d07-d09; contested, unreplicated | 22-language discounting on our model, plain vs CoT, vocabulary and translation controls | Weak vs strong FTR gap with CIs separated in both standard and CoT arms | Low |
| A15.06-U8 | Does pitch wording (height vs thickness) change LLM acoustic judgement? | None expected; only music-domain prompts | none | K17, d13; untested | 40 tone-pair items; high/low vs thick/thin wording; accuracy, r with human similarity | Accuracy difference >= 5 pp (otherwise record as null) | Low |
| A15.06-U9 | Can a short metaphor prime (distance vs amount) shift a later estimate? | Nothing; confirms "no priming prompts" | none | b03, b05, a04; human, weak, brief | 60 duration items; no prime vs distance prime vs amount prime; estimate shift | Shift >= 0.3 SD and replicated on a second item set | Low |
| A15.06-U10 | Does item or reading order act as a bias on sequence judgements (analogue of reading direction)? | Order-randomisation step for sequence items | S1 hygiene | K05, b15; human cultural; LLM analogue untested | Time-ordering items, events listed forward vs reversed vs shuffled; accuracy | Forward vs reversed gap >= 5 pp (then shuffle becomes default) | Med |
| A15.06-U11 | Is the Chinese-English reversed-order gap a data effect or a language effect? | A class-record flag for order-reversed inputs | S0 | K11, d10, d11; single-source | Same logic items, forward vs reversed, two languages, plus a rare-order English control | Reversed gap persists in English rare-order control (then it is frequency, not language; add the flag) | Low |

## Open questions we cannot test on our bench yet

- Human preregistered large-N replications of Boroditsky 2001: needs human participants. The Ns of the three failed replications (Chen; January and Kako; Tse and Altarriba) are paywalled and unread.
- Casasanto 2016 chapter text: needs access to the Routledge volume. Only the Language abstract was read.
- Winawer-style discrimination speed in VLMs: needs a vision-language model with logit access and colour stimuli. One search summary claims a language-conditioned boundary shift in aligned layers (c09), unopened.
- Mirror-reading baseline in Crossley and Bylund (46.9% vs 53.1%): needs the PDF re-read.
- Data-mix control for language gaps: needs two models matched on size and differing only in language share. Not available to us.
- Effect sizes for Zhang and Rayz deictic asymmetry: the authors report none; needs their data or a rerun.
- Cross-language LLM tests need vocabulary and spelling controls (d16). We have no such controlled word lists.

## Order to run

1. A15.06-U1 (explicit frame line): cheapest, one prompt line, a clear metric, and the only item with both human and LLM support.
2. A15.06-U2 (prompt-language and paraphrase sensitivity): reuses existing bench items and doubles as a G4 check on correlated errors.
3. A15.06-U10 (item order as a bias): reuses the time-ordering items from U1, tests the one human mechanism (reading direction) that replicates cleanly, and costs almost nothing.
