# Hierarchical task networks: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| C05.08-U1 | Does a given method list beat model-improvised splits? | A small curated method list per problem class, fed to O3 | O3, memory | K03, K21; single-source (SkillsBench, tokens not equal) | (a) curated list, (b) improvised, (c) plain; 40 natural reasoning items; accuracy | (a) beats (b) by 5+ points on hard items and does not lose on easy ones | High |
| C05.08-U2 | Do verified, stored decompositions help over a stream? | Method store with admission test | memory, O3 | K12, K24; ASI, SkillWeaver, ReAcTree; web tasks only | 100-item stream per class; no store vs unverified vs verified store; accuracy on second half, tokens per item | Verified beats no store by 3+ points or saves 20%+ tokens, and unverified is not better | High |
| C05.08-U3 | Does a feasibility check and exit cut wrong answers on ill-posed items? | Named feasibility list and no-valid-decomposition exit | O3, G6 | K11, K26; detection 8.9%, false exits near 0; planning tasks only | 30 solvable + 15 ill-posed items; with vs without exit; detection and false-exit rate | Detection up 20+ points and false exits under 5% | High |
| C05.08-U4 | Is a code postcondition per sub-problem better than an LLM critic? | Code check as the only decomposition verifier | G2, G5, O3 | K25; single-source (critic 1.8x tokens, no gain) | 40 items with 8 injected wrong methods; code check vs critic vs none; wrong answers passed, tokens | Code check blocks 60%+ of wrong methods at under 0.3x of the critic's cost | High |
| C05.08-U5 | Is decomposing on demand better than always-first at frontier level? | Keep A4 as a hard rule (O3 only from S6) | G1, O3 | K06, K27; older models only; weak for small models | 40 multi-step items; on-demand vs always-first vs plain; accuracy, tokens | On-demand matches always-first accuracy within 2 points at 20%+ fewer tokens | High |
| C05.08-U6 | Does a small active method set (1-3) with a fallback beat a larger set? | Cap at 3 methods per item and require a fallback step | O3 | K23; single-source (SkillsBench, ReAcTree) | 1 / 3 / 6 methods, with and without fallback; 40 items | 1-3 beats 6 by 3+ points; fallback adds 5+ | Med |
| C05.08-U7 | Are model-written methods before solving harmful for our agent? | Rule: no self-written pack before the attempt | O3, memory | K22; single-source (-8 to -12) | Self-written pack vs none vs curated; 40 items | Self-written is below none by 3+ points | Med |
| C05.08-U8 | Does O3 still help the strongest model we use? | A per-model gate (20-item pilot) in S0 | S0, O3, G7 | K27; GPT-4o to Haiku spread; nothing on Claude 4 / GPT-5 class | 20 items per model, plain vs O3 | Enable O3 only where pilot gain is 5+ points | Med |
| C05.08-U9 | Task tree with constraint separation vs long thinking | Constraint-separation split for itinerary-type items | O3, G11 | K14, K28; single-source (HTP, 2024 reasoning model) | 40 constraint-heavy items; tree on standard model vs flat CoT vs reasoning model | Tree beats flat CoT by 10+ points and is within 5 of the reasoning model at lower cost | Med |
| C05.08-U10 | How much of the gain is code extraction and not splitting? | Code-based answer extraction at S4 as its own element | G2, S4 | K08; single-source (+17 / +14), Plan-and-Solve sketch null | Extraction alone vs full decomposition vs plain; 40 arithmetic items | Extraction alone gives 70%+ of the decomposition gain | Med |
| C05.08-U11 | Does a code-held step list beat a model-held one on long procedures? | Step list kept in code for recursive tasks | O3 | K19; contested (Hanoi collapse vs output-length artefact) | Hanoi-like and list recursion, N = 4 to 12; accuracy vs N | Code-held wins by 10+ points at N above 8 | Low |
| C05.08-U12 | Does method order matter, and can ordering rules be filtered by execution? | Execution-filtered ordering rules in the store | O3, memory | K17, K23; single-source (Meneguzzi); no study varies order in a fixed set | Fixed 3-method set in 3 orders; generated ordering rules tested on training items | Order changes accuracy by 3+ points, or filtered rules beat random order | Low |
| C05.08-U13 | Does library-first, model-fills-gaps beat model-only? | Gap filling with checked effects | O3, memory | K10; single-source, one lab, demo scale | Library plus gap fill vs model only; 40 items with some methods missing | Gap fill beats model-only by 5+ points with fewer rejected splits | Low |
| C05.08-U14 | Is a free repair step (task insertion) better than strict methods? | One free repair step inside O3 | O3 | K20; single-source, theory only | Strict vs 1 free step; 40 items | Free step lifts accuracy 3+ points with no extra wrong answers | Low |

## Open questions we cannot test on our bench yet

- Break-even error rate of per-decomposition checks: needs measured error rates per class from U4 first.
- Library staleness and conflict over hundreds of items (Hogg 2008 interaction effect): needs a long task stream and a store with usage logs.
- Whether leaf errors dominate in math, code and research questions: needs failure logs labelled plan level vs leaf level (partly free from U1 and U5 runs).
- Lekavy and Navrat critique of HTN expressivity: needs the paper text; low value for the scaffold.
- Whether the Hanoi collapse is an output-length artefact: needs the exact table from the comment; U11 may settle it.
- Frontier-level ADaPT-style gain on Claude 4 / GPT-5 class models: no published test; U5 and U8 are the test.
- Effect of an exit on ambiguous but solvable items: needs a labelled set of ambiguous items we do not have yet.

## Order to run

1. **U1 (given library vs improvised)**: decides whether O3 should carry a method library at all; the rest build on it.
2. **U4 (code check vs LLM critic on injected wrong methods)**: cheap, and sets the verifier design for U2, U3 and U13.
3. **U3 (feasibility check and exit)**: models almost never say "no valid split" and false exits were near zero in the one study that counted them, so the likely gain is large and the cost is one step.
