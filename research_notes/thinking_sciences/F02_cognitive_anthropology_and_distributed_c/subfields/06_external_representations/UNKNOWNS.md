# External representations: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| F02.06-U1 | Does a code-checked written state beat a free-form drawn state and plain CoT on our model? | Per-step state ledger recomputed by code, mismatches fed back | G2/G3, S2 | K03, K04, K17; a11, a12, d06; single-source, older models, no token control | Plain CoT vs terse CoT vs free-form grid vs checked grid; 60 grid/route/tiling items; final and per-step state accuracy | Checked grid beats best of plain and terse CoT by at least 5 points, paired p<.05, check tokens counted | High |
| F02.06-U2 | Does a code-built object list beat a raw row-text grid on ARC for our model, and at which detail level? | Object-list builder at O6 for grid items | O6 | K05; b16, c09, c10; GPT-4 only, 50 easy tasks | Raw grid vs objects vs objects+edges; ARC portfolio, all items; solved items, paired | Objects beat raw by at least 5 points and edges do not beat objects | High |
| F02.06-U3 | How wide is the format spread on our current model? | A pilot-chosen fixed format; a noise-floor rule for later tests | S2/O6, G7 | K06, K22; b20, d11, d12; 2023-2024 models only, contested | 4+ meaning-preserving formats (plain, Markdown, JSON, HTML, YAML), 30 items per class; range of pass rate | Spread at least 5 points: add per-class format pilot. Under 3: drop format work | High |
| F02.06-U4 | Do natural-frequency or nested-set restatements help LLMs on Bayes items? | Program converts probabilities to counts before the model reads them | O6 | K10, K11; a10, b09, d01-d03; human-only, LLM citation chain false | Probability vs frequency vs nested-set vs terse CoT; 30 Bayes items, several models; exact-answer accuracy | Restatement beats probability by at least 5 points and beats terse CoT | Med |
| F02.06-U5 | Does a rule enforced by a validator beat the same rule stated in prose? | Validator-enforced rules for puzzle-type items | G2/G3 | K01; a02-a05; human-only, N=18 | Hanoi/river-crossing variants; prose rules vs validator rejection; violations and solve rate | Violations fall at least 50% and solve rate rises at least 5 points | Med |
| F02.06-U6 | Can a few-item pilot pick the form per task class at net-positive tokens? | Pilot step that fixes text grid, objects, table or image per class | S0, S2/O6 | K07, K08, K18; c04, d08, d04; router needs 14,200 labels | Best fixed form vs pilot of 8 items choosing; 30 held-out items; accuracy with pilot tokens included | Pilot-chosen form at least matches best fixed form, net of tokens | Med |
| F02.06-U7 | When does a rendered image beat the text grid? | Render-and-read step only for classes with awkward text coordinates | O6 | K18; d04, d05; GPT-4o only, 2024, single-source | Same items as text grid vs code-rendered image on a multimodal model; accuracy | Image beats text by at least 10 points on a class; else keep text | Low |
| F02.06-U8 | Does placing needed facts adjacent in the written problem raise accuracy (Larkin and Simon locality)? | Program groups or reorders facts by the step that uses them | O6 | K16; d13; indirect analogue only | Same content, adjacent vs scattered vs random order; 40 multi-step items; accuracy | Adjacent beats scattered by at least 5 points | Med |
| F02.06-U9 | Does stating the hidden constraint help on insight-type items against a strong baseline? | Constraint-reveal restatement at S2 after a failure | S2/O6, O4 | K13, K21; b01, b27, d14; contested, human picture result only | Plain CoT vs terse CoT vs constraint stated; BRAINTEASER-like items | Gain at least 5 points over best baseline, with baseline under 80% | Low |
| F02.06-U10 | Does answering as a program or generator beat an explicit full list? | Prefer program output for long enumerations | S2 | K14; c22; single-source, one task | Hanoi N=6 to 12; program vs list | Program beats list by 10 points at N of 8 or more | Low |
| F02.06-U11 | Does structured-output-first cost accuracy on our model? | Hard rule: reasoning free-form, only final answer structured | G2/O6 | K20; d11; single-source, non-reasoning models | Free text vs JSON-mode vs reason-first schema; GSM8K-type items | JSON-mode loses at least 3 points (rule then becomes [E]) | Med |
| F02.06-U12 | Does a rewrite or restatement gain survive a CoT baseline? | Problem-rewrite step at S2 | S2 | K19; d15; single-source, baseline had no CoT | Direct vs CoT vs terse CoT vs rewrite+CoT; mixed difficulty | Rewrite beats CoT by at least 3 points at equal tokens | Med |

## Open questions we cannot test on our bench yet
- Larkin and Simon 1987 and Chuderski 2021 originals are unread (publisher 403). Unblock by finding open copies. They would give exact claims on computational equivalence and the large null insight test.
- 2025-2026 frontier reasoning models: no format paper covers them. Unblock by running U3 on our own model before trusting any 2023-2024 number.
- Physical enforcement and handling of real objects: models have no hands; only the validator analogue is testable (U5).
- A direct LLM test of Zhang and Norman's dimension-binding result (location beats colour and size): needs an isomorph generator with several encodings; not built.
- Image-based forms need a multimodal model and a code-render tool in the harness.
- Zero-shot drafting vs few-shot hand-written drafts (Chain of Draft): needs hand-written draft exemplars per task class.

## Order to run
1. U3 (format spread on our model): cheapest, and it sets the noise floor every other test must beat.
2. U1 (checked written state vs free-form vs plain/terse CoT at equal tokens): biggest expected gain, and no equal-token comparison exists in the literature.
3. U2 (object list vs raw grid on the ARC portfolio): reuses an existing portfolio and has the strongest tool-built-form evidence.
