# Tools and questions: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| E09.06-U1 | Does a code-computed backward slice beat free exploration at equal tokens? | Slice step at S5 when a failing run exists | O5, S5 | K15 contested; CausalRepair, BluesFL, SWE-Doctor gains are not equal-token; d21 says strong agents have little headroom | Plain vs plain+slice vs plain+whole trace; bugs with failing test; held-out pass, tokens per fix; 3 seeds | Slice arm beats plain by 4+ points at equal tokens, CI excludes 0, and whole-trace arm does not | High |
| E09.06-U2 | Does question type matter: why-not vs why-did vs hypothesis list? | A fixed question template at S5 | O5, S5 | K17 single-source; no ablation exists (d22, b11, d11) | Four arms: why-did, why-not, 3-hypothesis list, free; same items; root-cause hit rate | One type beats the list by 4+ points on root-cause hit, or why-not wins on missing-output bugs | High |
| E09.06-U3 | Is a slice better used late (at an impasse) than early? | Slice or runtime tool as an S6 operator, not at S3 | S6, O5 | Single-source (debug-gym d08): debug(5) best for all models; older prompts | Slice at S3 vs at S6 after 2 failed revisions vs none; pass and tokens | S6 arm passes within 1 point of S3 arm at 20%+ fewer tokens, or beats it | High |
| E09.06-U4 | Does a bounded "ask runtime" tool beat raw debugger commands? | `ask_runtime(question)` capped call tool | S5, S6 | Single-source Debug2Fix (d23): +13 to +22% vs raw flat; preprint | Question tool vs raw commands vs none; multi-file bugs; pass, call count | Tool arm beats raw arm by 8+ points and none by 4+ | High |
| E09.06-U5 | Does a witness check on self-made repros help? | Code check: repro fails with the reported error | G3, S4 | K16 established but effect small (2-3 of 100); d01, d24 | Check vs no check on items where agent writes a repro; pass, share of misled runs | Check arm better by 2+ points with under 3% token cost | Med |
| E09.06-U6 | Is ChatDBG's follow-up gain just resampling? | A fixed "second look" turn | S5 | Single-source b11: 57, 67, 85%; follow-up gave no feedback; GPT-4-era | Follow-up turn vs second independent sample at equal tokens | Follow-up beats resample by 3+ points | Med |
| E09.06-U7 | Does per-candidate "why this could cause it" re-ranking help? | Explain-then-rerank step on suspects | S4, S7 | Single-source RGFL d22: Hit@1 71.4 to 85%; pipeline, not agent | Explain+rerank vs score-only rerank; Hit@1 and pass | Hit@1 up 5+ points at equal tokens | Med |
| E09.06-U8 | Does contrast (failing vs nearest passing run) help repair? | Contrast pair in S5 context | S5 | Single-source d12: 37.00 vs 30.67 vs random 34.00; ChatGPT-3.5 era | Contrast vs failing-only vs random pair; pass | Contrast beats failing-only by 4+ points and random by 2+ | Med |
| E09.06-U9 | Are tool-computed slices more robust to meaning-preserving rewrites? | Slice step as a robustness guard | G, S7 | Single-source d05 (-7.7% vs -38%); d03 (78% flips, no tools); one benchmark | Original plus 3 mutated copies; outcome agreement and pass, slice vs none | Slice arm agreement 15+ points higher than none | Med |
| E09.06-U10 | At what chain length should the agent switch to a computed slice? | A length rule at S0 | O5, S0 | Not tested; 20/600/100 are plot values on a value-prediction task (d15) | Slice vs free by chain-length bin (under 20, 20-100, over 100 steps) | Slice wins in a bin by 5+ points; set the threshold at the first winning bin | Med |
| E09.06-U11 | Can a cheap confidence signal gate extra backward search? | Gate on agreement or token probability | S6, calibration | Single-source K13: Spearman 0.52-0.57 needs five runs; call cap 20 hurt (d09, d10) | Gate vs fixed 10-call cap vs fixed 5-call cap; pass, tokens | Gate beats both caps in pass per token by 10%+ | Low |
| E09.06-U12 | Does a required causal-path statement (suspect to failing output) lower wrong patches? | Required field in S5 | S5 | Single-source, human only (d18: 61% of time after seeing the fault) | Field vs no field; wrong-patch rate on held-out checks | Wrong-patch rate down 3+ points at under 5% token cost | Low |
| E09.06-U13 | Can a model-made slice (agent style) stand in when no tracer exists? | Fallback slice agent with verify and refine | O5 | Single-source SliceMate a12 (own benchmark); exact match 7.33% for plain GPT-4o (a11) | Agent slice vs tool slice vs none on items with and without a tracer; slice F1 and pass | Agent slice within 5 F1 points of tool slice and beats none by 3+ points | Low |

## Open questions we cannot test on our bench yet
- Whyline human results, replicated independently: needs human participants; not available.
- Original Weiser 1982 statistics: needs access to the ACM PDF; second-hand sources disagree on 2 vs 3 programs.
- Equal-token comparison on SWE-bench-scale repositories: needs a repository bench with tracer support for Python projects; our bench is puzzle-sized.
- How often a reproduction must be built before diagnosis: needs issue-style items without tests.
- Contamination of Defects4J, HumanEval and SWE-bench in the cited gains: needs fresh post-cutoff items.
- "Do Coding Agents Still Need a Debugger?" (2026): needs a retrievable PDF; may change U1.
- Whether strong models gain at all (d21): needs a stronger-model arm than our nano loop; check once U1 has results.

## Order to run
1. **E09.06-U1 (slice vs free vs whole trace).** It decides whether the whole subfield is worth anything for us, and its trace arm also settles the trace-contradiction at the same time.
2. **E09.06-U3 (late vs early slice).** Cheap to add to U1 as one more arm, and it decides where O5 sits in the state graph.
3. **E09.06-U2 (question type).** No study has ever tested it, so one clean result is new knowledge; run on the same items as U1.
