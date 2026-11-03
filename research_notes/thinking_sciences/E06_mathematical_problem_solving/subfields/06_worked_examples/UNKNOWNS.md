# Worked examples: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| E06.06-U1 | Do stored worked examples still help our current model, or only set format? | Library lookup only for classes/models where it wins | S0 / memory | K24 contested; d01-d03 (Qwen 72B 95.75 vs 95.83; R1 few-shot lowers); older models gain | Zero-shot vs 1 verified same-class example vs format-only stub; same extractor; items split by gold step count; accuracy | Example arm beats both others by 2+ points on 5+ step items with 95% CI above 0 | High |
| E06.06-U2 | Does gating injection on k-sample self-accuracy beat always injecting? | S0 rule: inject only if self-accuracy below 50% | S0 / G7 | K25 single-source (d14: +6.31 low bucket, -2.32 at 100%); small models | Always vs gated (k=4 samples) vs never; 3B-scale and our model; accuracy and tokens | Gate beats always by 1+ point and never by 1+ point, including sampling cost | High |
| E06.06-U3 | Does a retrieval rejection threshold help (show nothing if similarity low)? | Similarity floor in library lookup | memory | K18 single-source (c08: one-shot failed on 1.83-34.96% of zero-shot-solved items; c24) | Retrieve top-1 always vs reject below threshold (top 10%); deduplicated test set; accuracy | Rejection arm beats always-retrieve by 1+ point and is never below zero-shot by more than noise | High |
| E06.06-U4 | Do subgoal labels in stored entries beat unlabelled entries? | Label every library entry with named subgoals | memory / O3 | K15, K26 single-source; formal proofs only (d05: 45.5 vs 40.6); human CS1 slides (b15) | Labelled vs unlabelled same content; code-checked tasks; near and far transfer sets; pass rate | +3 points on near or far transfer, or +2 on both | High |
| E06.06-U5 | Does attempt-first then example beat example-first on novel items? | S0 order rule: attempt first for novel concepts | S0 | K22 contested; no LLM study (d19); g=0.36 human (b21) | Example-first vs attempt-then-example vs none; novel-concept and routine-procedure items; accuracy | Attempt-first beats example-first by 2+ points on a class type; apply only to that type | Med |
| E06.06-U6 | Does fading driven by code-checked success save tokens without losing accuracy? | Fading rule in library display | S0 / memory | K03, K04 contested; human near transfer only (a29); N=62 null (a14) | Always full vs fade after passes vs never; same-type and new-type items; accuracy and tokens | Same-type accuracy within 1 point and 20%+ fewer example tokens; new-type no worse than 2 points | Med |
| E06.06-U7 | Does generate-and-solve in one turn beat pasting a retrieved example? | Analogue step in O7 or S2 | O7 / S2 | K16 contested (Yasunaga +2.8 vs Chen -4.0 for relevant); K17 single-source (Gwak 54.59 vs 50.49) | Self-generate-and-solve vs verified retrieved vs decoupled reuse; GSM8K-like and MATH-like; accuracy | Integrated beats retrieved by 2+ points at equal tokens | Med |
| E06.06-U8 | Does strict admission (masked reproduction plus re-derivation) beat answer-only admission? | Admission rule in S9 / library writer | G5 / memory | K28 contested; d08, d09 no rate measured; K20 70% pass (a22) | Library built three ways (none, answer-check, strict); downstream accuracy; rejection rate | Strict beats answer-check by 1+ point, or rejects 10%+ of entries that later cause errors | Med |
| E06.06-U9 | Does skill-indexed retrieval beat topic and random retrieval for our items? | Skill tags on library entries | memory | K09 single-source (b10: 53.88 vs 50.31); ~+1.3 near ceiling (b11) | Skill vs topic vs random retrieval, equal prompt length; held-out set tagged by skill; accuracy | +2 points over topic retrieval on non-ceiling classes | Med |
| E06.06-U10 | Does complexity plus diversity selection beat random selection for library display? | Display rule: choose long and diverse entries | memory | K12, K30 single-source; old models (b01, d11) | Random vs longest vs diverse vs diverse-long; report gain by item steps | +2 points on 5+ step items with no loss on easy items | Low |
| E06.06-U11 | Are stored repair traces (wrong attempt, error, fix) better than clean-only? | Store repair trace as library entry | memory / S5 | K21, K29 single-source; fine-tuning only (a17, d12) | Clean-only vs clean+repair at equal tokens; items with common error modes; accuracy | +2 points on items where the error mode recurs | Low |
| E06.06-U12 | Does the library sign (help vs hurt) differ by model, and what predicts it? | Per-model switch with automatic check | memory / G7 | K19 contested (d13-d15: Llama up, Qwen and Gemma down) | Library on/off across 3+ models, one reasoning model; accuracy; answer-format failure rate | Keep per model only where gain is 1+ point; log format failures | Med |
| E06.06-U13 | Does an "explain each step" instruction add value on top of examples? | Self-explanation line in S2 | S2 | K05 contested; Barbieri negative moderator (a09); calculus quality-only gain (c16) | With vs without explain instruction on top of examples; equal tokens; accuracy and tokens per correct | Gain 2+ points after paying for the explanation tokens | Low |

## Open questions we cannot test on our bench yet

- First-hand human numbers (Sweller and Cooper 1985, Cooper and Sweller 1987, Kalyuga 2001, Barbieri per-moderator g). Unblock: full-text access or an institutional copy. They would not change the LLM tests above, only the confidence in the human priors.
- Frontier closed reasoning models at equal total tokens. Unblock: a budgeted run on the models we actually deploy; until then U1 is run on our models only.
- Far-transfer measures for fading and subgoal labels. Unblock: a held-out set with a different problem type that shares the same subgoal structure; we do not have one labelled.
- True reasoning-validity of stored examples (right answer, wrong reasoning). Unblock: a step-level verifier or proof checker for maths; code checks only reach the final answer.
- Delay effects (wash-out). Our runs are stateless; a repeated-session design is needed to mimic delay.
- Productive failure for LLMs with a learned memory across items. Unblock: sequential benchmark runs with library state carried across items.

## Order to run

1. U1 (example vs none vs format-only stub): it decides whether any of the library ideas matter for our model, and is cheap.
2. U2 together with U3 (self-accuracy gate and retrieval rejection): both are cheap switches, share one item set, and decide when to show an example.
3. U4 (subgoal labels vs unlabelled): it is the core of the planned subgoal library and has a hard verifier outcome.
