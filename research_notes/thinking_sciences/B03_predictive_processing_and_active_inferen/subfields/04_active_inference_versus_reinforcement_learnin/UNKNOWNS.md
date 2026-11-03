# Active inference versus reinforcement learning: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| B03.04-U1 | Does an EIG-ranked probe over a code-kept hypothesis list beat "try something different" at equal tokens? | EIG probe operator | S3 probe | K24, d01-d02; single-source, not token-matched | Plain prompt vs hypothesis list + filter + EIG; hidden-target games, 100 items; success within N probes | Gain >= 10 points, tokens equal, on 2+ models | High |
| B03.04-U2 | How much gain comes from the consistency filter alone? | Filter only (cheaper) | S3 | d02 (85-87 vs 95); single-source | Filter+random probe vs filter+split vs full EIG; same items; success | Filter alone within 5 points of full EIG | High |
| B03.04-U3 | Does an explicit "rule may have changed" hypothesis speed recovery after a hidden change? | Context-switch test after surprise | S9, memory | K03, K28, a05, d11; single-source, built-in in Sajid | Plain memory vs explicit change hypothesis; mid-task rule swap, 50 items; steps to recover | Median recovery >= 30% faster, no accuracy loss without swap | High |
| B03.04-U4 | Does a coverage tracker raise distinct valid outputs in reward-free open mode? | Coverage tracker | S3 open mode | K04, K07, K18; Q-learning 0 vs belief agents 40-44; older RL only | Isolated attempts + tracker vs free self-prompting; open tasks; distinct valid outputs | >= 20% more distinct valid outputs, accuracy not lower | High |
| B03.04-U5 | Does a stop rule (last K answers did not change hypothesis set) avoid noisy-TV waste? | Stop rule | open mode stop | K26, K16, d08; deep RL only | Surprise-seeking probes vs stop rule; tasks with a random-answer source; tokens wasted, accuracy | >= 25% fewer tokens, accuracy within 2 points | Med |
| B03.04-U6 | Is a fixed success criterion safer than an agent-edited one? | Fixed criterion guardrail | G5, G8 | K06, K29, a10, d14, d15; indirect, single-source | Fixed criterion + separate-context judge vs agent-edited; 10 rounds; gold accuracy and drift | Edited arm loses >= 5 points or drifts on >= 20% of items | Med |
| B03.04-U7 | Is probing wasteful on easy items and vague targets? | Gate probes by difficulty and crispness | G12 | K08, K25, a12, d03; single-source | Probe on vs off, easy and vague items; accuracy and tokens | Off arm equal accuracy with >= 15% fewer tokens | Med |
| B03.04-U8 | Token-aware probe cap (info per token threshold)? | Probe cap | G12 budget | K27, d05-d06; simulated, small | No cap vs cap 2 vs threshold 0.01; success per token | Best capped arm beats no cap on success per token by >= 15% | Med |
| B03.04-U9 | What weight of information gain stops hurting accuracy in goal-driven loops? | Weight rule | G12 | K11, K15, b14, b16-b18; contested | Weights 0, 1%, 10%, 50% in goal loop; accuracy | A nonzero weight keeps accuracy and improves coverage | Low |
| B03.04-U10 | Does a code-driven curriculum of untried directions beat free self-prompting (Voyager-style)? | Curriculum operator | S3 open mode | K20, c19, d16; 3 runs each, not token-matched | Code-assigned untried directions vs free self-prompt; equal tokens; distinct valid outputs | >= 20% more distinct valid outputs | Med |
| B03.04-U11 | Recursive planning vs whole-plan choice on multi-step items? | Recursive step choice | S6 | K13, a15; theory only | Whole-plan vs step-by-step re-scoring; multi-step items; accuracy | >= 5 points gain at equal tokens | Low |
| B03.04-U12 | Does a positive goal check at S8 prevent "avoid-errors-only" stalls? | Positive-goal rule | S8 | K05, a08; single-source | Avoid-errors-only objective vs with goal check; accuracy and completion | Without check, completion drops >= 10 points | Low |

## Open questions we cannot test on our bench yet

- Stronger RL baseline for Sajid's FrozenLake (explicit context belief). Needs an independent reimplementation; not a scaffold question.
- Usable rule from Wei's regret bound for exploration budget by difficulty. Needs a way to measure information gain per item.
- Whether small models benefit from code-side statistics (EVOLvE says no). Needs a small-model arm on our bench.
- Dutta 2026 against a plain-prompt baseline. Needs their code or a rebuild.
- Real users instead of simulated answers (PUMA, Dutta). Needs human or high-fidelity simulated users.
- Learning-progress stop rule in LLMs. Needs a defined "model error" for text tasks.

## Order to run

1. U1 and U2 together: the main claim (EIG probe) and its cheap version, on the same items. Largest expected gain, and the filter-only result may be free.
2. U3: the explicit change hypothesis. LLMs perseverate 7-27 trials versus 2.9 for humans, so there is room, and the fix is a few lines.
3. U4: open-mode coverage tracker. Open mode is the reason this subfield matters, and the tracker is cheap code.
