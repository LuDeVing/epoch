# Process models: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| D05.02-U1 | Does stage order or presence matter for our graph? | keep the S3-S8 order as fixed; or drop stages that do nothing | graph order S1-S9 | K02, K22; d01, d02 (order inside chains only); no stage-order test; single-source | Permute/skip S3-S8 vs graph order; 150 checked items (ARC-like + math); accuracy, tokens | graph order beats shuffled by 5+ points, or a skipped stage loses 3+ points; else remove the stage | High |
| D05.02-U2 | Does a define stage (S1/S2) pay for itself on clean and on underspecified items? | keep or cut the define stage; add a premise-check output | S1, S2 | K03, K27, K12; a03, c01, c02, d10, b22; single-source, older models | Define on vs skipped (saved tokens go to a 2nd attempt); 100 clean + 100 missing-premise items; accuracy, flag rate | +2 points on clean or +10 points on flag rate, at equal tokens | High |
| D05.02-U3 | Is a pure model-written review pass worth more than the same tokens spent on k independent samples, for current models? | a rule: no review pass when k samples + check fit the budget | S5, S8, G7 | K04, K06, K23; a19, d03, c22; established for GPT-3.5/4, untested on reasoning models | Review loop (own critique) vs k samples + check vs located-output revise; 150 checked items; accuracy, flips | resampling or located revise wins by 2+ points; then ban pure review | High |
| D05.02-U4 | Does a locate-and-fix review output ("no error" or step index) beat free-text review? | review output format with a no-error option | S5, S8 | K24; d04; single-source, PaLM 2 traces | Free-text review vs locate/no-error output; 100 checked items with correct and wrong first drafts; loss on correct items, net gain on wrong ones | loss on correct items under 2% and net gain +3 or more | High |
| D05.02-U5 | Does a stop rule (k identical trial answers) save tokens without losing accuracy inside our graph? | stop rule at S4/S8 exit | G11, S4, S8 | K26; d07, d08, d09; established for reasoning models, untested in a staged agent | Fixed budget vs stop after k = 2 or 3 identical trial answers vs confidence-gated exit; 200 single-answer items; tokens, accuracy | tokens down 20%+ with accuracy loss under 1 point | High |
| D05.02-U6 | Should review depth be routed by difficulty (revise on easy-medium, resample on hard)? | difficulty router at S0 for review vs sampling | S0, G12 | K29, K23; d14, d03; single-source | Always revise vs always resample vs router; items binned by plain pass rate; accuracy per bin | router beats the best fixed policy by 2+ points overall | Med |
| D05.02-U7 | Is scaffolded review redundant on reasoning models, and does a one-word "Wait" cue do the job on base models? | per-model-class scaffold switch; cue instead of review loop | S8, S0 | K25; d05, d06; single-source, one benchmark | Scaffold review on/off and Wait cue only, on a reasoning and a non-reasoning model; injected-error items + 100 normal items; accuracy, blind-spot rate | cue within 2 points of scaffold on base models, or scaffold adds under 1 point on reasoning models | High |
| D05.02-U8 | Does a self-composed stage plan per task type beat a fixed plan or a self-chosen operator order? | plan-per-class selection at S0 and logged operator order | S0, O1-O8 | K09, K10; b21, c18, a18, c03; single-source, all vs CoT not equal-token sampling | Self-composed plan vs fixed plan vs plain; mixed items incl. world-model items; accuracy, tokens (planning cost counted) | +3 points overall or +8 on one item class, planning cost included | Med |
| D05.02-U9 | Does a Toulmin critical-question gate (7 of 8, then 5 of 8, cap 10 loops) help correctness, not only judged style? | critical-question review for open mode | S8, S7 (open mode) | K11; b24, c19, c20; LLM-judged only | CQoT-style gate vs same tokens in extra samples; open items judged by running or blind human pairs; math items for harm | wins on 60%+ of blind pairs and costs nothing on math | Low |
| D05.02-U10 | Does a stored reflection help only after an external failure signal? | memory rule: write a lesson only after a failed check | memory, S9 | K08; c08, c26; single-source | Retry with stored reflection vs blind resampling; checked items with first-try failures; second-try pass rate | reflection retry beats blind retry by 3+ points | Med |
| D05.02-U11 | Does a forced integrate step fix stalls (many attempts, no selection)? | integrate step before S7 when attempts disagree | S6, S7 | K17; b09-b12; human-only evidence | Forced integrate vs plain select; items where attempts disagree; pass rate | +3 points on disagreeing items | Low |
| D05.02-U12 | Is the 41% base-accuracy gate for correction valid on current models? | S0 rule: skip review when plain accuracy is under about 40% on the class | S0, S8 | K13; b20, c13; single-source, older models | Review on/off by class pass-rate bin (under 20%, 20-40%, 40-70%, over 70%); net gain per bin | clear sign flip between bins | Med |
| D05.02-U13 | Can a stage-adherence judge be trusted? | model judge for stage logging | section 6 logging | K28, K19, K20; d12, d13, a16, c15; no validation exists | 100 human-labelled traces; judge vs humans; kappa | kappa 0.6 or more; else log stage adherence by code only | Low |
| D05.02-U14 | Does postponing hypotheses (Hitchcock) beat early suggestion (Dewey) for an LLM generator? | S3 rule: generate only after S2 lists constraints | S2, S3 | b02, a03; contested conceptually, no LLM test | Early attempts vs attempts after a written constraint list; fixation measured by candidate diversity; accuracy | +2 points accuracy or +20% distinct candidates at equal tokens | Low |

## Open questions we cannot test on our bench yet

- Human data on stage order and premature closure with verified numbers (Klahr and Dunbar, Kuhn): publisher PDFs could not be retrieved. Unblock: obtain the full texts through a library or open copy.
- LLM scores on Watson-Glaser, CCTST, Cornell and Halpern tests by subskill: no paper found. Unblock: run the tests ourselves if item banks are licensed, or find a benchmark paper.
- Whether reasoning models carry Dewey-like stages internally (Jeong et al. 2026 hints at it): needs open-weight models and hidden-state access, which our bench does not have.
- Whether the Hitchcock "suspend judgment" option (neither accept nor reject) helps: our graph forces a submit (G6). Needs items where abstaining is correct.
- Effects on very long agentic tasks: all stage and review studies use single-question items.
- The Jeong et al. 2026 citation id (2609.04753) looks odd for the date; verify it before citing the paper.

## Order to run

1. **U3 (review vs k samples, with located-output arm):** cheapest, and decides whether any review step in S5/S8 earns its tokens.
2. **U1 (stage permutation and skip):** no study answers it; the result can cut stages or confirm the graph.
3. **U5 (stop rule):** established on other models, cheap to build, and a direct token saving.
