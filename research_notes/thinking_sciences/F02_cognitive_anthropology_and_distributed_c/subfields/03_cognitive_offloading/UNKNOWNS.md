# Cognitive offloading: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| F02.03-U1 | Does a program-held state store (counters, lists, totals) beat state kept in the transcript on long runs? | Rule: all counts and running state live in code | memory, G | K01, K05 established on single-step arithmetic; no multi-turn test | A transcript state; B code store applied by program; 5-20 turn items, 3 seeds; exact accuracy | B beats A by 5+ points, or equal accuracy with 20%+ fewer tokens | High |
| F02.03-U2 | Forced program-defined offload at set steps vs model-chosen offload | Program decides when the tool is used | G | K07 (human direction, size unread), d10 (chosen won for 2 of 3 models); contested | A forced by rule; B model chooses; C hybrid; same items; accuracy | A or C beats B by 3+ points on 2 of 3 item sets | High |
| F02.03-U3 | Does restricting code to state and counts avoid tool-induced myopia and keep the accuracy gain? | Tool role limited to state and counts; derivation written first | G | K18, K25 single-source, hard competition math only; prompt-only fix lost 1.9 of 2.4 points | A no code; B free code; C code for state only, derivation first; final accuracy plus step quality | C keeps 70%+ of B's accuracy gain and step score within 2 points of A | High |
| F02.03-U4 | Clear content from context after writing it to the store: with vs without a forced re-read | Clear-after-write with re-read step | memory | K28 vendor figure (+29%, +39%, 84% fewer tokens, no N); human evidence mixed (Grinschgl vs Storm and Stone) | A keep all; B clear, no re-read; C clear, forced re-read; long runs; later-step accuracy and tokens | C within 1 point of A at 30%+ fewer tokens, and B worse than C | High |
| F02.03-U5 | Prompt-only tool-call caps: where does accuracy flatten? | Per-mode tool-call cap | O | K19, K26: trained fixes only (68.3% fewer calls; about one-fifth the calls on GSM8K) | Caps 0, 1, 2, 4, unlimited on tool-optional items; accuracy and tokens | A cap holds accuracy within 1 point and saves 25%+ tokens | Med |
| F02.03-U6 | Per-step routing: executable steps to code, semantic steps to the model | Route by sub-step type | O | K06 single-source, older models; K04 formulation-bound limit | A all code; B all text; C per-step routing; mixed items; accuracy | C beats the better of A and B by 3+ points | Med |
| F02.03-U7 | Can the agent notice a wrong value in its own store, and do program-checked writes stop it? | Checked writes, cited reads, recheck | memory | K27 established harm (98.2% injection, 76.8% attack success); detection unmeasured | Plant a wrong value; A unchecked; B program-checked writes and cited reads; rate the value reaches the answer | B cuts the rate by half or more at under 5% extra tokens | Med |
| F02.03-U8 | Show the agent its own measured tool-vs-self error table | In-context error table, or program routing from it | O | K09 contested; human d about .26-.35; fake feedback null | A no table; B table in context; C program routes by table; routing accuracy | C beats A by 3+ points; add B only if it beats A by 2+ | Med |
| F02.03-U9 | Execute algorithms in code, not text (Hanoi and similar) | Algorithm steps run by code | G | K21, K30 contested; Lua generator result unquantified | Hanoi n=6 to 15, 10 runs per n; A algorithm in text; B code runs it; success counts | B succeeds at n of 12+ where A collapses | Med |
| F02.03-U10 | Told-to-code vs free choice in the mid range | Instruct code use above a size threshold | O | K23 single-source; GPT-4o missed code mid-range (d11) | Mid-complexity counting and multiplication; instructed vs free; code-use rate and accuracy | Instructed beats free by 3+ points | Med |
| F02.03-U11 | Does a code interpreter help current frontier models on plain counting and state tasks, or only on large numbers? | Size-gated code use | G, O | K24: o4-mini +19.3, GPT-4.1 +2.4, GPT-4.1-mini -1.3 (hard math, not counting) | Counting at sizes 10 to 1000; same model with and without code; exact accuracy | A size threshold appears above which code wins by 5+ points and below which it does not | High |
| F02.03-U12 | Store removed or added late vs built from step 1 | Always build store from step 1; never drop silently | memory, G | K16 human only (Florean 2026; "Let it go" 2026) | Store from start, added mid-run, removed mid-run; recovery accuracy | Removal cost exceeds late-add gain by 3+ points | Low |
| F02.03-U13 | Does scoring reasoning quality (not only the final answer) change which arm wins? | Step-level check for offloading arms on the bench | G | K18 single-source; needs a step grader | Fixed step rubric applied across U1-U11 | A ranking flips in at least one test | Low |

## Open questions we cannot test on our bench yet

- Burnett and Richmond 2026 effect sizes, k and forced-minus-chosen gap: paper paywalled. Unblock with the full text or the authors. Until then do not quote a size.
- Salomon (1997) and Salomon, Perkins and Globerson (1991), "effect of a tool": never opened (SAGE 403, ERIC no record). Unblock by library access. An "effect of" test would need a scaffold-removal run.
- Instructed vs invented offloading strategy with a p value for LLMs: no study found. U10 gives a partial answer.
- Per-bin Tool-Induced Myopia dose-response values: figure only. Unblock by authors' data or a re-plot.
- Thinking vs non-thinking models on offloading behaviour (thinking models call code on about 50% more problems): needs a bench with a thinking-mode switch.
- Frontier 2026 models on Illusion of Thinking puzzles with code execution: Lawsen's claim has no counts.
- Human memory consequences (Google effects, photo-taking, smartphone presence): not agent-testable.
- Weight-level methods (OccamLLM, DPO for TIM, OTC-PO, SMART, MEM1, MemAct): need training access, out of scope for a frozen API agent.

## Order to run

1. U11 then U1: size-gated code use, and code-held state vs transcript state. Cheap, high gain, and they size the effect for everything else.
2. U3: restrict code to state and counts and score step quality. It decides whether code is safe to use at all, given tool-induced myopia.
3. U4: clear-after-write with and without a forced re-read. Large token savings if it holds, and the only evidence is a vendor figure with no N.
