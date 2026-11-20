# Modal and epistemic logic: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| D03.05-U1 | Does a "record the user's belief, do not endorse it" step close the first-person false-belief gap on current models? | A belief-recording step before answering | G, memory | K13; a24, d02; single-source, GPT-4 class, no reasoning models | Plain vs generic CoT vs record-belief; 100 false-belief and 100 true-belief first-person items; accuracy per class | False-belief +10 points or more over plain and over CoT, true-belief loss under 2 points | High |
| D03.05-U2 | Does a mental-state reminder (restate "what X knows" before predicting action) still help reasoning models? | A two-call reminder step | G, O | K26, K27; d01, d02; single-source, non-reasoning models for the +30 | Plain vs generic CoT vs reminder; 200 SimpleToM-style items; behaviour prediction and judgment accuracy | Prediction +10 points over plain and over CoT on both a reasoning and a non-reasoning model | High |
| D03.05-U3 | Does reasoning or CoT hurt on true-belief and no-asymmetry items in current models? | A rule: no default CoT on belief items; always add control items | G11, G | K14, K28; a25, d04, d17; contested | Direct vs CoT vs reasoning mode; 100 true-belief and 100 false-belief items; accuracy per class | Direct beats CoT by 5+ points on true-belief items with no loss on false-belief | High |
| D03.05-U4 | Does a dated per-agent belief table beat free reasoning at Hi-ToM orders 3-4 and FANToM at equal tokens? | Belief table in memory with dated entries | S3, memory | K17, K31; c13, d13, d03, d18; single-source, 2023 models for the big gains | Plain vs CoT vs code-held belief table (LLM fills, code updates); Hi-ToM orders 0-4, FANToM ALL; accuracy per order | +10 points at orders 3-4 at equal tokens, no loss at orders 0-1 | Med |
| D03.05-U5 | Does an explicit depth-k nesting list help nested belief items? | Nesting operator | O | K16, K29; b14, d06, d12; format-dependent (d12) | Plain vs nesting list; depth 1-4 balanced true/false statements; accuracy by depth | +8 points at depth 3-4 and no loss at depth 1 | Med |
| D03.05-U6 | Does stating frame conditions plus a countermodel check fix knowledge or belief inference? | Frame-condition and countermodel step | G, O | K30; d08, d09; single 2026 preprint | Direct vs restated frames plus countermodel vs reasoning mode; balanced paired problems; accuracy vs 50% baseline | Reaches 75% or more and beats direct by 20+ points | Med |
| D03.05-U7 | Do current models still show McGee-style and triad inconsistency, and does a consistency check fix it? | One-context consistency check | G | K10; b03-b05; single-source, 2024 models; no current data | Plain vs consistency step; 50 triads and McGee-style items; count of inconsistent triples | Inconsistent triples cut by a third or more | Low |
| D03.05-U8 | Does offloading nested-belief updates to code (world table, public-announcement update) beat free text on muddy-children puzzles? | Formal-tool operator for epistemic updates | O | K05, K06, K24; a13, c22; Logic-LM old models; no current muddy-children test | Free text vs code world table vs solver; muddy children k=2..5; exact accuracy and round of first correct answer | Table wins by 15+ points at k of 4 or more | Med |
| D03.05-U9 | Does a perturbation check (altered false-belief items) catch shortcut answers? | Perturbation check before trusting a belief answer | G3 | K19; b12, b13; contested, 2023 models | Plain vs check step; original and altered (transparent bag, informed protagonist) items; accuracy on altered | Altered-item accuracy +15 points, original unchanged | Low |
| D03.05-U10 | Does a dated belief log (not overwritten) improve recall of the belief before an update? | Dated belief entries in memory | S3, memory | K31; d18; single 2026 preprint | Overwrite vs dated log; 100 update stories with trajectory questions; accuracy | +10 points on trajectory questions | Med |
| D03.05-U11 | Is a prompted per-step DEL checker as good as the trained DEL verifier at equal tokens? | Prompted step verifier for nested belief | O | K29; d06, d07; needs trained verifier and N up to 1024 | Plain vs majority vote vs prompted DEL checker; Hi-ToM orders 3-4; accuracy | Beats majority vote at equal tokens by 5+ points | Low |
| D03.05-U12 | Does balanced scoring change model rankings on ToM items? Is any gain just answer bias? | A balanced-scoring rule in all epistemic evals (G hygiene) | G | K21, K32; b16, b17, d10, d16; no re-ranking found | Rank arms on raw accuracy vs balanced accuracy on our item sets | Report both whenever the ranking changes (rule, no threshold) | Low |

## Open questions we cannot test on our bench yet

- Current reasoning-model scores on KaBLE. The arXiv text is v1 only; the Nature Machine Intelligence version could not be fetched. Unblock: obtain the KaBLE data and rerun it, or get the later version.
- Gettier and knowledge-luck numbers and replication (Machery et al., Seyedsayamdost, Turri, Nagel). Sources blocked (403). Unblock: PDF access. Only matters if the agent must model lay use of "know".
- Epistemic planning with LLMs under information asymmetry. Peng et al. 2026 (d19) numbers were not read; no DEL planning paper found.
- MindGames on current models. No rerun found. Unblock: rerun the released puzzle generator.
- Whether the reasoning-mode jump on stipulated modal semantics (4.4 to 88.1) holds beyond one model. Unblock: second-model replication.
- Why order collapse depends on format (Hi-ToM QA under 60 vs Street true/false 73-95). Needs a controlled comparison on one model.
- Cost of a trained verifier. No sample-efficient version known; our bench has no labelled belief-trace data.

## Order to run

1. **D03.05-U3** (CoT on true-belief controls): cheapest, needs only existing models and a small item set, and it decides whether any belief step may use CoT at all.
2. **D03.05-U1** (record-the-belief step): the widest gap (first-person false belief, 54.4 average) and the cheapest intervention; closest to a Add-if win.
3. **D03.05-U2** (mental-state reminder): largest measured gain (+30) in a published test, plus a direct reasoning-model check.
