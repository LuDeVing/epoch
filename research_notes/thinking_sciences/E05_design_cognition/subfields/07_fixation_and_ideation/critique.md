# Critique E05.07 Fixation and ideation (cross-check)

## Checks done (re-opened this session)
- Deng, Brucks and Toubia 2026 (arXiv 2602.20408, PDF read). Confirmed: categories 12.68 vs 12.46; combinations 8.37 vs 8.68 (p=.12); slopes 1.035 vs 1.013 (p=.51); first-idea categories 14.51 vs 8.37; CoT slope 1.013 to 1.363; seeded 1.063 (p=.42); persona+CoT 248 combinations vs human 197 (26%).
- Wadinambiarachchi et al. 2024 (arXiv 2403.11164, PDF read). Confirmed GenAI +.32 (BF 124), image search +.27 (BF 42.48), N=60, image-search fluency -.49 [-.9, -.10].
- Others (Perttula, Neroni, Doshi, Jiang, Si and so on) were NOT re-opened by me; I rely on the agents' opened flags. Only 2 of the 10 target numbers were re-verified. Attempts to reach paywalled or blocked sources (core.ac.uk behind a bot check, Semantic Scholar 429, arXiv API empty) failed.

## Corrections
1. Wadinambiarachchi coefficients (+.32, +.27, fluency -.49) are log-link model coefficients (binomial for fixation, negative binomial for counts), not proportions or raw differences. Evidence lines a16, c01, c02 read like plain effects; treat them as log-scale. CI bounds are [.11,.55] in the text and [.11,.54] in Table 1: trivial.
2. Wadinambiarachchi originality is the share of other participants who did NOT have the same idea cluster. Lower originality means more convergence across people, not lower novelty to experts.
3. Deng persona slope: default 1.013, persona 0.876, persona+CoT 1.086 (main), but 0.930 (p=.19) in the robustness setup. So persona+CoT helps on combinations robustly, not on category slope. Ordinary personas LOWER the within-session slope while raising cross-session diversity: the two mechanisms separate.
4. Deng robustness reports CoT slope 1.095 (not 1.363). Direction holds, size varies.
5. Deng footnote: temperature 1.5 and 2.0 gave garbled text. Supports "temperature is not a diversity lever".

## Contradictions and tension
- Jansson-Smith (copying persists) vs Perttula and Liikkanen (N=16 null on copying) and Purcell 1993 (snippet). Unresolved; boundary seems to be example count, ideas per person, domain familiarity.
- Sio et al.: examples cut categories but raise novelty. Perttula: total categories unchanged, non-redundant categories halved. Outcome definitions differ.
- Deng: LLM within-session fixation equals human. Wadinambiarachchi and Doshi: humans fixate on AI output. Different direction.
- Laban 2025 (one long thread degrades) and Brown 2024 (many samples help) agree on fresh samples, but Brown needs a verifier.

## Weak spots
- Jansson and Smith 1991 and Chrysikou and Weisberg 2005 were never read. a01 to a05, b02, b08 are second-hand. Sio 2015 effect sizes missing. Purcell 1993 is a snippet.
- Deng: simulated LLM participants, one model (GPT-4o), one domain (fitness products), 99 sessions per arm. Nothing on Claude.
- Doshi, Anderson, Padmakumar are humans-with-AI studies: indirect for an agent.
- Zhao 2021 label bias and Lou and Sun anchoring are analogues, not fixation tests.
- Anderson N=36; Howard no control group; Chen N=10.
- Verbalized sampling and NoveltyBench figures come from the authors' own benchmarks.
- No study found that tests fresh-context vs same-context ideation at equal tokens on a reasoning model.

## Seen only in snippets
Purcell et al. 1993; Sio et al. 2015 abstract; Davis sketching partner; Hoggenmueller; Jansson and Smith original; Chrysikou and Weisberg.

## GAPS
1. At equal total tokens, do N fresh contexts with the same prompt beat one long context for idea diversity and best-idea quality on a Claude-class model, with and without a verifier?
2. What are the effect sizes and significant moderators (example number, commonness, timing, domain match) in Sio, Kotovsky and Cagan 2015 (43 studies)?
3. What are the exact Jansson-Smith 1991 and Chrysikou-Weisberg 2005 numbers (N, copy counts, warning condition), and has the flawed-example effect been replicated with in-context examples in LLMs?
4. Does an LLM anchor on its own earlier outputs within a session on reasoning-trace models, and does extended thinking change it (NoveltyBench: more reasoning gave less diversity)?
5. Does persona diversification across fresh contexts hold on Claude and on non-product tasks (proofs, code), where diversity must serve correctness?
6. Does delayed example exposure (after first ideas) reduce fixation in agents, as Perttula's earlier up-front vs delayed result suggests for humans?
7. What share of agent errors in multi-step reasoning are Einstellung-style mental set (Neroni paradigm), and does a restart-with-summary operator reduce them?
8. What saturation threshold (new non-duplicates per sample) should stop spawning fresh contexts, and how does that compare in cost with verifier-based selection?
9. Do incubation or break manipulations have an agent analogue, such as context truncation?


## Gap search results

Evidence is in evidence_d.jsonl (d01 to d22). Claims K02, K03, K05, K08, K13, K15, K21 were revised and K25 to K33 added. The web search quota ran out early, so most sources came from Crossref, Europe PMC, DataCite and arXiv PDFs. Paywalled papers (Jansson-Smith, Sio 2015, full Chrysikou-Weisberg) stayed closed.

| Gap | Status | What was found |
|---|---|---|
| 1. N fresh contexts vs one long context | Partly closed | Independent single-idea fresh contexts are the least diverse arm: GPT-4o 0.452 vs 0.679 for one session listing ideas (d06). On Claude Opus 4.8, three independent samples gave distance 0.24, one response with three ideas gave 0.80, with win rate 0.33 vs 0.21 (d08). With a verifier on MATH, sequential revision narrowly beat parallel and hard items needed a mix (d11). Still open: equal-token test with a Claude model on a non-product task, and the best-quality-with-verifier case for ideas. |
| 2. Sio 2015 effect sizes | Open | Only an abstract-level summary seen (d03). Direction: few, uncommon examples help most; quality rises with copying. No numbers. |
| 3. Jansson-Smith and Chrysikou-Weisberg numbers; LLM flawed-example replication | Partly closed | Chrysikou-Weisberg abstract read: N=89 (3 conditions) and N=60; defixating instructions diminished fixation (d01). This contradicts the earlier "warnings fail" claim, now contested (K02). Jansson-Smith numbers unreachable (d02). No LLM in-context flawed-example replication exists in what was found; IDEAFix (d20) is the nearest and does not show an example. |
| 4. Anchoring on own outputs; extended thinking | Partly closed | Showing earlier answers plus "give a different one" raised diversity to human level (d09), so it is not harmful when asked for difference. Repeated "make it bolder" refinement lowered diversity 0.575 vs 0.679 (d07). Previous titles in the prompt did not stop duplicates (d10). More reasoning effort gave fewer distinct outputs for OpenAI o-series, no change for Gemini (d09). No Claude extended-thinking diversity test found. Claude with reasoning avoids an Einstellung trap benchmark (d17). |
| 5. Persona diversification on Claude and on proofs or code | Partly closed | For open ideation, random personas or constraints restore diversity (0.757 vs 0.679; d07), GPT-4o, no Claude. On correctness tasks personas cost accuracy (MMLU 71.6 to 68.0; CSQA -2.1 to -4.4) and temperature spread does nothing (d18, d19); what helps is strategy-mode coverage (d21). Still open: any Claude test on proofs or code. |
| 6. Delayed example exposure in agents | Open | No agent study. Human evidence is indirect: harm from exposure shows up late and breaks remove it (d05). Perttula and Liikkanen remains the only direct human timing result. |
| 7. Share of agent errors that are Einstellung; restart-with-summary | Partly closed, share still open | Agents repeat the same blocked mechanism on every model; a threshold-triggered divergent-then-select switch lifted Claude Sonnet 4.6 from 53.6% to 73.2% (d14). Summary at 32K vs 64K gave 57.7% vs 41.7% in long search (d12). No paper reports the share of errors due to mental set. |
| 8. Saturation threshold and cost vs verifier | Partly closed | Si et al.: about 200 of 4,000 ideas non-duplicate at cosine 0.8 even with titles shown (d10). Terwiesch: no plateau from 100 to 1,000 (d07). So claim K13 is now contested. Dropping low-confidence terminations before voting gave +2.6 to +4.9 points at no extra samples (d13). No tested cutoff rate. |
| 9. Incubation analogue as context truncation | Partly closed | Human: incubation helps divergent tasks most (d04) and removes exposure harm (d05). Agent: shorter context triggers for summaries raised accuracy (d12), through fewer give-ups rather than less fixation. No test of fixation after a context reset. |

### What this changes for the schema

1. S3 should not mean "N bare fresh contexts, same prompt". Each fresh context should write a list of several ideas (or be told earlier ones) and carry a persona or constraint; then a selector or verifier picks.
2. Warnings are not useless; test an avoid-X line rather than rule it out.
3. Keep personas short and out of correctness-critical runs, unless they name a strategy mode.
4. Add a switch trigger on repeated same-mechanism failure, and a summary-and-continue trigger on context length; both have support on agents.

### Weak spots remaining

- Closed-model evidence is thin: Claude appears in d08, d14, d17 only.
- d06 and d08 use different tasks and different diversity measures; tokens were not matched in either.
- Most diversity numbers are embedding distances, which a judge or human may not share.
- d09 reasoning-effort values were read from a figure.
- Everything about Jansson-Smith and Sio 2015 numbers stays second-hand.
