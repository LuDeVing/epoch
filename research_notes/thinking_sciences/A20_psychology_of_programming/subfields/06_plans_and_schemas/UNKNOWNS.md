# Plans and schemas: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| A20.06-U1 | Does a verified subgoal library beat free planning on our strong model? | Subgoal library with success-gated writes | memory (section 5) | K15, K16, K26: older models only; gain shrinks with model strength (b26, d07) | Library off vs verified library; easy and hard tiers; 3 seeds; pass@1 and tokens including build cost | hard-tier pass@1 up by 3 points or more and easy tier not lower by more than 1 point | High |
| A20.06-U2 | Does a wrong stored plan hurt, and does a run-and-compare check remove the harm? | "Check before use" rule for every retrieved plan | G2, G3 | K24 (hints, not plans), d09 mixed AWM result; single-source for plans | 20 tasks with one planted wrong plan each; no check vs run-and-compare; pass rate, tokens | the check recovers at least 70% of the loss and costs under 20% more tokens | High |
| A20.06-U3 | Which retrieval key works: role sentence, code text, or LLM plan label? | The best key as the library index | memory | K25, K17, d06, d08: no head-to-head | One library, one task set; three keys; retrieval hit rate and downstream pass | best key beats code text by 5 points hit rate and does not lower pass | High |
| A20.06-U4 | Do names and role sentences on entries matter on our models? | Name plus role sentence required for each entry | memory | K25: single-source (LILO, DSL tasks, older models) | Anonymous vs named entries; same tasks; solve rate | named entries up by 2 points or more | Med |
| A20.06-U5 | Does a plan in slots (role, init, update, guard) beat a free-prose plan? | Slot format for plans | O3, memory | K12 (SCoT, older models, [E] for a small structure vocabulary), K21 (slots single-source) | Free plan vs slot plan; mid-difficulty coding items; pass@1 | slot plan up 2 points or more, with equal or fewer tokens | Med |
| A20.06-U6 | Does plan-then-code still help a reasoning model that already thinks? | Optional plan stage in S2 or S3 for coding | O3, S3 | K10, K13 [E] on older models; K27, d10, d11 point the other way | Direct; plan then code; best-of-N; N plans; matched tokens; pass@1 and pass@k | plan arm beats best-of-N by 2 points pass@k or more at equal tokens | High |
| A20.06-U7 | Does a retrieved plan hint make the agent miss deviations (expectation error)? | A guardrail: tag predicted values as "expected" and run to confirm | G (new), S4 | K04, K23: single-source; indirect LLM evidence (d01, d02) | Soloway fill-in on canonical vs bent programs; no hint, plan hint, plan hint plus simulate check; default-value answer rate | hint raises default answers by 10 points on bent programs and the check removes at least half of that | Med |
| A20.06-U8 | Is composition (interleaved or merged plans) a real failure source for our agent? | An explicit composition check in O3: list shared variables and run each plan's case alone | O3 | K05, K06, K18: contested; no LLM Rainfall study with structure coding | Same subgoals composed abutted vs interleaved; with and without shared-variable check; composition error rate | interleaved errors exceed abutted by 10 points and the check halves them | Med |
| A20.06-U9 | Should planning be gated on estimated difficulty? | Plan only when S0 marks the item hard | G12, S0 | K11: single-source (Jiang complexity buckets; 6.7B loses) | Plan-always vs plan-if-hard; mixed difficulty; accuracy at equal tokens | plan-if-hard equals plan-always accuracy within 1 point with 15% fewer tokens | Med |
| A20.06-U10 | Does a re-plan trigger during coding beat plan-once? | Re-plan edge from S5 on a failed test or surprise | S5, S6 | K28 (trained 7B only); ADaPT abstract (c27) | Plan-once vs re-plan on failed test; multi-step coding items; pass rate | re-plan up 3 points or more with tokens within 10% | Med |
| A20.06-U11 | Does compose-and-test beat plan translated straight to code? | Compose-and-test step after decomposition | O3 | K14: Parsel ablation 25.5% vs 6%, single-source, Codex era | Plan to code directly vs parts, tests, compose; decomposable tasks; pass rate | gain of 5 points or more | Med |
| A20.06-U12 | Are stored plans sound? Passing tests may not prove the plan was sound (the model fills gaps) | Admit a plan only after it passes at least 2 of 3 runs from plan text alone | memory, G3 | K29: single-source (Rivera, GPT-4, one course) | Run stored plans from text only, once vs 3 times keep 2 of 3; false-positive rate | false-positive rate cut by half at under 3 times the tokens | Low |
| A20.06-U13 | Should a library hold several variants per goal? | Two or more variants per entry, chosen against task constraints | memory | K30: qualitative, 4 narratives | Tasks where the default variant is ruled out; one vs two or more variants; pass rate | variants win by 5 points on constraint-breaking items, no loss elsewhere | Low |
| A20.06-U14 | Does alternating plan-naming and code steps beat one-way plan-then-code? | Alternation as the default loop between S3 and S4 | S, O | K08: single-source (humans, 22 participants, correlational) | One-way vs forced alternation; same items; pass rate | alternation up 3 points or more | Low |
| A20.06-U15 | Does a tool whose call order matches the natural plan reduce errors? | Interface rule: order tool arguments and calls to follow the common plan | O (interface) | K09: single-source (1983, 52% vs 33%) | Natural-order vs reversed tool; error rate | error rate down 5 points or more | Low |
| A20.06-U16 | Does a stored control-flow trace beside the plan label help retrieval? | Hybrid index: plan label plus trace | memory | K20: contested (Pennington, Gilmore and Green, second-hand) | Plan label only vs label plus trace; retrieval hit rate | hit rate up 5 points or more | Low |

## Open questions we cannot test on our bench yet

- Exact human numbers for the 1984 TSE paper, Spohrer 1985 (including the PROUST 75%), Pennington 1987 and Gilmore and Green 1988. Needs the full papers. Until then the human effect size is unknown and cannot be used to size an LLM effect.
- Fisler 2014 and Voyager numbers were not re-checked in this run. Re-check against the PDFs.
- Whether explicit plan teaching helps (de Raadt not opened). A human question; for models it maps to U1 and U5.
- Plan transfer across paradigms (functional, imperative, object oriented). Needs tasks in several paradigms and a paradigm-neutral entry format.
- Wrong-plan harm rate split by verification strength across many task classes. Needs a much larger planted-error set than U2.
- Delocalized plans in large codebases (Letovsky). Needs long-context repository tasks, which our bench does not yet have.
- Typicality as a measured quantity (the 1984 judgement was the authors' own). Needs a code corpus to score how typical a plan is; this would unblock a proper LLM replication of the plan-like vs unplan-like effect.
- Token cost of plan search on 2025-2026 reasoning models at matched tokens. Needs the bench to log cost per state; partly covered by U6.

## Order to run

1. U6 (plan stage vs direct vs best-of-N at matched tokens). It decides whether any plan stage is worth its tokens on our model, and it settles G7 before we build the rest.
2. U1 (verified library on/off by tier). It is the main reason this subfield matters: solved-subgoal memory. Run it with U2 planted wrong plans in the same harness.
3. U3 (retrieval key). Cheap once U1's library exists, and the key choice decides every later library result.
