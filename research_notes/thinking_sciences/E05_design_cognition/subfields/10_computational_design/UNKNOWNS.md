# Computational design: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| E05.10-U1 | Does Be-first, Bs-by-code tagging of scratch state beat plain chain of thought? | F/Be/Bs/S fields in S3/S4 scratch state | S3, S4 | K01 established as coding scheme only; K22 no LLM test (d14) | Plain CoT vs tagged state; 40 checkable design/planning items, 10 seeds; held-out pass rate and tokens to first pass | Gain of 3 points or more on held-out pass rate, CI excludes 0, no loss on ARC control | High |
| E05.10-U2 | Does an itemised expected-vs-derived compare cut revision rounds? | Evaluation step listing unmet Be items before S5 | S4, S5, G2 | K22 unverified; FMEA review claim unmeasured (d13); critique pass is the analogue (d11) | Revise from located failing output vs revise after itemised Be-vs-Bs compare; 40 items with a wrong first attempt; rounds to pass, final pass rate | Rounds to pass down 15% or more, or pass rate up 3 points, at equal tokens | High |
| E05.10-U3 | Is an LLM tagger of F/Be/Bs/S reliable enough to drive control or diagnostics? | Tag gate: tags used only if kappa passes | S, G10 | K06, K23 single-source; 71% on n=31 held out (b22); analogue kappa 0.68 (d09) | 3 humans and 1 LLM tag 200 agent-trace segments; rationale vs none; kappa per label | Kappa 0.7 or more on every label used; behaviour label dropped if below 0.6 | High |
| E05.10-U4 | Does forced decompose-then-recompose help an LLM? | Recompose check inside O3 | O3 | K04 contested (Song d up to 2.55, Luo eta 0.336 vs Wells null); human-only; K22 no LLM test (d15) | No forced pass vs breadth-first decomposition plus recomposition check; 40 multi-part items, split by size; pass rate and tokens | Gain of 3 points or more on large items and loss under 1 point on small items; else add only for large items | Med |
| E05.10-U5 | Does an FBS stage chain (R, F, Be, S) with code selecting at each hop beat free prompting? | Stage chain in S3 for open design items | S3 | K17 single-source; human picks words; t-tests look inflated (d03); gain 0.41 on 5 points | Free prompt vs stage chain; 30 open items with code-checkable rubric, 10 seeds; rubric score and diversity | Rubric score up 0.2 SD or more with equal or better diversity | Med |
| E05.10-U6 | Does the scaffold's gain shrink as base skill rises? | Rule: apply scaffold only if plain pass rate below a set value | G12, S0 | K18 single-source; 5 professionals (d03) | Same items on weak and strong model, plain vs scaffold; gain per model | Gain on weak model at least twice the gain on strong model, over 3 item sets | Med |
| E05.10-U7 | Do F/B/S memory nodes beat free-text memory on reworded past cases? | F/B/S record format in memory | memory | K09 single-source; toy domain; no gain with many records (c04) | Free-text vs F/B/S nodes; 50 hard reworded cases; recall at k=8 | Recall up 0.15 or more on sparse cases, no loss on dense cases | Med |
| E05.10-U8 | Does a critique-and-revise pass raise diversity per token, and does few-shot cut novelty? | Critique pass in the divergent operator; no few-shot examples in divergence | O (divergent), G8 | K10, K11 single-source; older models (GPT-3, GPT-4) | Zero-shot plus cue vs few-shot vs critique pass; 30 idea items, 10 seeds; DPP and hull diversity; share judged novel by running check | Critique arm diversity up 10% or more per token and no feasibility loss | Med |
| E05.10-U9 | Does an LLM design agent show narrow spread across seeds, and does an FBS reformulation step widen it? | Reformulation step as a spread remedy; spread monitor | G, O8 | K14 single-source (variance 0.042 vs 0.102, c18, not re-read); K22 no reformulation test | Plain vs plain plus FBS reformulation; 10 seeds per item; embedding spread and distinct-solution count | Spread up 15% or more with pass rate unchanged | Low |
| E05.10-U10 | Does a skipped Be (F straight to S) predict errors in agent traces? | Skip-Be flag that forces a verify step | S, G3 | K20 single session, descriptive (d06); fast-route theory only (b16); K21 unverified | Tag 300 traces; compare error rate of skip-Be runs vs others; then force verify on flagged runs vs not | Skip-Be error rate at least 1.5x others, and forced verify cuts errors by 20% or more | Med |
| E05.10-U11 | Do trace entropy and first-passage time flag stuck loops better than our impasse detector? | Entropy or first-passage as an extra S6 trigger | S6 | a06, a07 describe the metrics; link to fixation untested; no effect size | Compute on 200 logged runs; compare flag precision and recall vs current detector at equal tokens | Adds recall 10 points or more at equal precision | Low |
| E05.10-U12 | Does counting reciprocal problem-solution triggers (not switches) separate good from bad runs? | Co-evolution count in the run log as a diagnostic | log, S2 | K16 established for practice; K19 single-source, one session (d05) | Log new problem items and solution items; correlate reciprocal count with pass rate on 200 runs | Correlation 0.3 or more after controlling for run length | Low |
| E05.10-U13 | Does allowing requirement revision mid-run beat a fixed spec on tasks with hidden requirements? | Explicit mid-run requirement revision rule in S2 | S2, S5, G2 | K16 established for human practice (a17, a04); no LLM test | Fixed spec vs revisable spec; 30 items with a hidden requirement revealed by output; pass rate on final spec | Gain of 5 points or more with no rise in drift (original requirements dropped) | Med |

## Open questions we cannot test on our bench yet

- **Gero 1990 and Gero and Kannengiesser 2004 numbers.** Pages were blocked. Unblock: get PDFs through a library or author copy. Until then no number from the founding papers is used.
- **Any causal test of the eight processes.** None found. We would have to build it ourselves (U1, U2 are the first such tests).
- **Maher's case-based design and Maher and Poon 1996.** No original numbers or replications seen. Unblock: read the original AI in Design 96 papers.
- **Kannengiesser and Gero 2019 H1 and H2 (professionals more system 1?).** Conference paper not fetched. Unblock: get it from the publisher or NSF repository.
- **Human expertise gradient for agents.** We have only model strength, not novice vs expert. Closest proxy is U6.
- **Whether the Song, Luo and Wells expertise conflict is real.** Needs the same task and the same measure in one sample. Human-only; outside our bench.
- **Multi-coder reliability on design protocols by LLMs.** Needs a human-coded FBS protocol set we do not have. U3 builds a small version on agent traces only.
- **Elhambakhsh's falling test accuracy with more fine-tuning data.** Single source; we do not fine-tune, so it is low value.
- **Bruggeman 2025 and Ege 2025 numbers** were taken from evidence files without a re-read. Re-open before using them in a threshold.

## Order to run

1. **U2 (expected-vs-derived compare before revise).** Cheapest, uses existing check code, and targets G2, our best-supported guardrail.
2. **U1 (Be-first tagged scratch vs plain CoT).** The main gap in the literature (no study at equal tokens) and the gate for every other tag-based idea.
3. **U3 (tagger reliability).** Needs only 200 trace segments. It decides whether tags may drive control or diagnostics (U10, U11, U12) at all.
