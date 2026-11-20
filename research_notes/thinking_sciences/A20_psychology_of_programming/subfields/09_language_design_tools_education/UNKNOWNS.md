# Language design, tools, education: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| A20.09-U1 | Does applying the model's proposed error fix and rerunning beat trusting its explanation? | Rule: never act on an explanation of an error; always apply and rerun | G2 / S5 | K05; a14, c01, d02; single-source, 2022 model | A: explain and accept. B: apply fix, rerun, feed back one round. 60 failing-code items, runtime and compile errors; metric: fixed after one round | B beats A by 8 points or more, 95% CI above 0, on at least 2 models | High |
| A20.09-U2 | Does a compile or type-check gate in the repair loop cut errors and lift pass rate at prompt level? | Compile gate in S4 for typed-language items | G3 / S4 | K16; d01, d02; single-source, open 2B-34B models, needs decoder access | A: plain generation. B: generate, compile, one located repair round. 100 TypeScript items; metrics: compile-error rate, pass@1 | Compile errors down 30% relative or more and pass@1 not lower | High |
| A20.09-U3 | Does reformulation after a fail help on verbose items but not conceptual ones? | Reformulate only for verbose or unclear statements; route conceptual failures to decompose or specialise | O8 / S5, O1, O3 | K06; a15, c10, a16; established for 2022 models | A: same-prompt retry. B: plain-language restatement then retry. 80 first-failed items tagged verbose vs conceptual; metric: solve rate per tag | B beats A by 10 points on verbose; no loss on conceptual | Med |
| A20.09-U4 | Which tool-interface parts help at equal tokens (lint guardrail, summarised search, 100-line window)? | Keep only parts that win; set tool defaults | S4 / S5 tools, G7 | K11, K18; c22, d10; single-source, GPT-4 Turbo, not equal tokens | Full vs minus-lint vs minus-summary-search vs minus-window, same token cap; 100 repo bug-fix items; metric: resolve rate | A part is kept if removing it costs 3 points or more | Med |
| A20.09-U5 | Does explain-first (concept summary before code) beat delegate-first on unfamiliar APIs? | Explain-first step in S1 for unfamiliar-library items | S1 / G | K02; c15, d05, d06, c17; contested, human-only, post hoc clusters | A: write code directly. B: concept summary, then code, then check. 60 items on an obscure library; metric: held-out variant pass rate | B beats A by 5 points or more | Med |
| A20.09-U6 | Does restating the task before generation (not echoing it) lower copy-the-prompt failures? | Mandatory restate in S1 (may already be covered) | S1 | K07; b03, c09; human-only | A: task text straight to generator. B: restate then generate. 80 items; metric: pass rate, copy overlap | B beats A by 3 points or more at equal tokens | Low |
| A20.09-U7 | Does a small fixed role vocabulary in the scratchpad help? | Tag scratchpad entries with 4 to 6 roles | memory | K09; a01, a03, a04, d12; contested, human-only, mostly null | A: free notes. B: tagged notes. 60 multi-step items; metrics: accuracy, tokens | B beats A by 3 points or more, or ties with 10% fewer tokens | Low |
| A20.09-U8 | Does a separate security-check pass lower insecure output? | Independent check pass for code with security surface | G / S8 | K10; c14; single-source, Codex-era, human participants | A: plain. B: plain plus independent check. 40 items with crypto, SQL, signing; metric: insecure-output rate | B lowers rate by 30% relative or more | Low |
| A20.09-U9 | Does scaffold gain depend on item difficulty (gap-widening analogue)? | Standard strata report; route budget by difficulty | G7 / G12, S9 | K03; b04, b05, c17, d09; established for humans only | Re-analyse existing bench runs split by difficulty tercile; metric: gain per tercile | Gain differs across terciles by 5 points or more with CI excluding 0 | High |
| A20.09-U10 | Does gain differ for familiar vs novel problem classes (METR analogue)? | Report and budget by familiarity | G12 | K04; b08, b10; contested, human-only | Split bench items by whether the class has memory records (familiar) or not; metric: gain per stratum | Gain sign or size differs by 5 points or more | Med |
| A20.09-U11 | Do type or syntax choices of the target language change frontier-model accuracy? | Prefer a language or add type hints per item class | S2 | K17; d03, d04; single-source, 2022 models | Same tasks in 3 languages (typed, untyped, typed with annotations stripped); metric: pass@1 | Any language or annotation effect of 3 points or more, replicated on 2 models | Low |
| A20.09-U12 | Do instruction-only "do not output the answer" rules leak with 2025-26 models? | External filter on forbidden output in hint modes | G5 | K12; c19, c20, a26; established for older models | A: instruction only. B: instruction plus filter. 50 hint-mode items; metric: leak rate | A leaks above 5% and B under 1% | Low |

## Open questions we cannot test on our bench yet
- Human learning claims (skill loss, retention, illusion of competence): need human learners. Our bench has none. Unblock: a human study, or proxy by testing transfer on held-out variants (U5).
- Exact effect sizes for Stefik and Siebert 2013, Hanenberg 2010, Uesbeck 2016: papers were paywalled. Unblock: full-text access.
- Weinberg and Shneiderman numbers: books not available. Unblock: library copy.
- 2025-26 replication of Kazemitabaar (N=69) and Shen and Tamkin (N=52): none found. Search APIs were rate limited, so absence is not proof. Unblock: re-run the search later.
- METR follow-up: none on the blog listing. Unblock: check arXiv directly.
- Roles of variables outside the Finnish group: none opened. Unblock: citation search.
- Equal-token SWE-agent ablations: the original did not equalise tokens. U4 covers it.
- Type-constrained decoding needs decoder access: not possible through an API. Only the gate version (U2) is testable.

## Order to run
1. U1 (apply and rerun vs trust explanation): cheapest, uses existing failing-code items, sits directly on G2.
2. U9 (strata re-analysis of existing runs): no new tokens needed, and it changes how every other result is read.
3. U2 (compile gate at prompt level): cheap to build, and the strongest measured number in this subfield (compile errors down 75.3% and 52.1% with constrained decoding).
