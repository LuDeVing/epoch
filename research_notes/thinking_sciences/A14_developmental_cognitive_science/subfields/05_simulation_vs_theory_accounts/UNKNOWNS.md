# Simulation vs theory accounts: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| A14.05-U1 | Does a separate perspective-filter call beat CoT and self-consistency on our models? | Role-taking filter before questions about another party's belief | O (role-taking), S2 | K06 contested; a16, d05; gain on GPT-3.5, loss on Qwen3 belief | Plain; CoT; CoT x2 vote; filter then answer. BigToM and ToMI false-belief plus true-belief twins, 100 each. Strict pair accuracy | Beats best equal-token arm by 5 or more points on pair accuracy, and no loss on true-belief twins | High |
| A14.05-U2 | Does a code-inserted "what does X know" line before the action question lift behaviour prediction in our setting? | The hand-off line as a standard step | S / O (hand-off) | K11 established; c20 (+33 GPT-4o, +30 Claude); three models only | Plain; generic CoT; code-inserted awareness line. SimpleToM-style behaviour and judgment items, 200 each. Accuracy | Behaviour accuracy up 10 or more points over CoT, and judgment not lower | High |
| A14.05-U3 | Do the reminder and a code-held ledger stack on perturbed items? | Ledger plus reminder as one memory/state pattern | memory, S | K09 (template benchmarks), K11; nobody tested both; no perturbed test | Plain; reminder; ledger; both. Items with transparent container, informed protagonist, extra mover. Accuracy on original and perturbed | Both beats best single arm by 5 or more points on perturbed items | High |
| A14.05-U4 | How reliable is a model-written ledger or filter on free text and multi-agent stories? | A code or second-pass cross-check of ledger entries | memory, G2 | K22 single-source (OmniToM F1 61.63; access 56-75%); K08 UniToMBench collapse | Compare model-written ledger to hand-labelled ledger on 60 multi-agent stories; then answer over each. Entry F1; answer accuracy | Cross-check recovers 5 or more points of answer accuracy, or filter F1 below 0.8 explains the gain loss | High |
| A14.05-U5 | Does an outcome-scored hypothesis list about another party beat token-matched CoT? | Hypothesis operator for interactions with a user or counterpart | O, G2 | K10 established on benchmarks; K23 single-source, no token match; goal sub-score fell in ThoughtTracing | CoT x N at matched tokens; hypothesis list k=3 scored by code. FANToM-style items; multi-turn counterpart games. ALL score; reward | Beats matched-token CoT by 8 or more points, not only plain CoT | High |
| A14.05-U6 | Do 2025-2026 models still over-suspect false belief (high false-belief, low true-belief)? | A true-belief guard step or asymmetric-score gate | G4 | K05 established for o1-preview (100 vs 36); gap 4 open; Gong 2026 has no FB/TB split | Score each model we use on false-belief and true-belief twins separately, 100 each. FB minus TB gap | If gap exceeds 15 points, add a control-pair check to any ToM step; if under 5, drop | Med |
| A14.05-U7 | Does hybrid (rule list plus role-taking) beat either alone? | Both an explicit rule store and a role-taking operator for others | O, memory | K18 contested; a28, b09; no direct test exists (gap 5) | Plain; role-taking only; rule list only; both. Backward inference items (infer intent from actions), 100 | Hybrid beats best single arm by 5 or more points on pair accuracy | Med |
| A14.05-U8 | Does capped thinking beat uncapped on higher-order ToM steps? | Per-step token cap for social inference | G11, O3 | K21 single-source; d01, d02 (o3 .838 to .693; Qwen3-8B capped .706) | Uncapped; cap 1,000; cap 1,500; CoT. Free-form order 2-4 items, 100 | Cap matches or beats uncapped within 2 points at 40 percent fewer tokens | Med |
| A14.05-U9 | Does a second adjustment pass reduce egocentric leak (curse of knowledge)? | Two-pass role-taking with an explicit "facts they lack" list | O | K16 (human-only for anchoring); b08, a04, d06 single model other domain | One-pass role-taking vs two-pass. Items where the character lacks a fact the story states; 100 | Two-pass beats one-pass by 3 or more points at equal tokens | Med |
| A14.05-U10 | Does first-person re-description beat third-person for inferring beliefs? | First-person framing in the role-taking call | O | d06 single-source, other domain; b12 weak mechanistic | Same model, same items: third-person, first-person, first-person plus CoT. BigToM and SimpleToM, 100 | First-person beats third-person by 4 or more points on belief accuracy in two benchmarks | Med |
| A14.05-U11 | Does Foresee and Reflect help in an agent loop? | Foresee step before acting near another party | O | c12 single-source; T4D story form | CoT; FaR; token-matched CoT x2. T4D-style items and a multi-turn helper task. Accuracy | Beats matched-token CoT by 8 or more points | Low |
| A14.05-U12 | Does scoring goal-belief hypotheses by model likelihoods (code-normalised) beat a direct answer? | Likelihood-scoring operator for goal inference | O, G5 | K09 established with symbolic inputs; a17; no text-only test | Direct; likelihood over 4 hypotheses normalised by code. Goal and belief inference from action traces, 100 | Beats direct by 8 or more points on false-belief-type items | Low |
| A14.05-U13 | Does a score on classic belief tasks predict agent behaviour with a partner over turns? | Whether to use static ToM items as a proxy at all | eval | K20 established (Riemer: literal ToM 92-97 vs regret near random) | Correlate item accuracy with turn-level reward in a repeated-game or counterpart task across our arms | Correlation r of 0.5 or more; otherwise drop static items as the gate | Low |

## Open questions we cannot test on our bench yet

- Whether any of this is simulation or theory. No design varies one while holding the other fixed. Would need a clean arm pair on one model; U7 and U10 are only proxies.
- Whether Onishi and Baillargeon 2005 (looking time) replicates at scale. Needs a ManyBabies-style source; not available through our tools.
- Independent replication of SymbolicToM, ThoughtTracing, Hypothetical Minds. Requires running their code; not yet done.
- Mechanistic claims (Zhu steering, Aoki flip rates). Needs open weights and probing tools; steering table rows are still inferred.
- Which perturbations are fair for humans (Strachan N=757 per-item table, in supplement, not opened). Unblocked by opening the supplement.
- Why SimToM fell so far on Qwen3 belief questions in the independent run (prompt, reasoning mode or format). Needs the exact prompts from that paper.
- Interactive loops with real partners over many turns. Needs a harness for multi-turn counterpart tasks.

## Order to run

1. **U2 (awareness hand-off line).** Cheapest, largest published effect (+30 to +33), and only a prompt change.
2. **U1 (perspective-filter call at equal tokens).** The central contested claim; the independent run disagreed with the original, so a clear answer saves a bad default.
3. **U3 (reminder plus ledger on perturbed items).** Nobody has tested the stack and it decides whether the ledger earns its code.
