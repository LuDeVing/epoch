# Working-memory limits and chunking: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| A08.08-U1 | Do named subgoal summaries of finished subgoals beat raw history? | Summarise a subgoal into one named line when it closes | memory, O3 | K19 contested; HiAgent 21 to 42, unreplicated, no clean ablation (c21, d15) | Raw vs named summaries vs masking (window 10); 15+ step tasks; exact-answer accuracy, tokens | Summaries beat raw by 5+ points at equal tokens on 2 task families | High |
| A08.08-U2 | Is plain masking of old observations as good as summaries on our scaffold? | Mask-first rule; summarise only if masking fails | memory | K26 single-source; SWE-bench, cost -41 to -57% (d06) | Masking vs summary vs raw, equal tokens; accuracy and turns | Masking within 2 points of summary at 40%+ fewer tokens | High |
| A08.08-U3 | Does a code-held state ledger beat model-held state across turns? | Program re-sends a structured ledger each step | G (program holds state), S1 | K17, K29 single-source: restating recovers only 15-20% (a22, d10); ledger untested | Accumulating chat vs model restate vs code ledger; sharded multi-turn items; accuracy and run-to-run spread | Ledger recovers 50%+ of the one-shot gap, or cuts spread by a third | High |
| A08.08-U4 | Is deleting superseded facts better than telling the model to ignore them? | Delete rule for stale state | memory | K16 single-source; "ignore" helps little (c15); deletion works in d06 | Delete vs ignore-instruction vs masked, equal remaining tokens; update-heavy items (3 to 400 updates); latest-value accuracy | Delete beats ignore by 10+ points | High |
| A08.08-U5 | Where in the prompt should the current subgoal sit? | Subgoal-last (or start+end) layout rule | S1, S3 prompt | K15 pattern established but older models (d01); start+end untested | Start vs middle vs end vs start+end at 25% and 90% fill; accuracy | A placement beats middle by 5+ points at 25% fill, or end beats start at 90%; else no rule | Med |
| A08.08-U6 | What is our backbone's working-set size (items tracked)? | Per-class cap on items per step in the class record | S0, G | K11, K12 single-source, older models; GPT-3.5 d' 1 at n=3 but Llama 70B holds 10-back (a17, c06, c07) | n-back and state-update sweep, n=1..10, bare vs scaffold; accuracy by n; check task understanding first | Clear drop point under 80% accuracy found (then cap one step below) | High |
| A08.08-U7 | Does reciting the needed facts first recover accuracy under padding? | A restate step before reasoning | S1, S3 | K28 single-source; GPT-4o +4% RULER, Llama-8B +31.2% GSM8K (d03) | Padding 1x, 3x, 5x; plain vs recite-then-solve; accuracy with recite tokens counted | Net gain of 3+ points at 3x padding | Med |
| A08.08-U8 | Is an item cap counted in large structures (2, 4, 8) real? | Cap of N named structures per step | G | K31 single-source, abstract only (d14); human only | Cap 2/4/8 structures per step; same tokens; accuracy | Accuracy drops 5+ points between caps, showing a knee | Med |
| A08.08-U9 | Does binding entity with attribute in one unit help current models? | Bound-format state | S2 | K21 single-source; +35.4 on text-davinci-002 (b17); older model; K22 contested | Separated vs bound state; tracking items; accuracy | Gain of 5+ points on our backbone | Med |
| A08.08-U10 | Do stable named chunks placed first help the other items? | Stable chunks at start of prompt | S layout | K30 single-source, human, abstract only (d13) | Chunks first vs last; accuracy on remaining items | First beats last by 3+ points | Low |
| A08.08-U11 | Does a pattern or workflow library beat raw history at equal tokens? | Subgoal library (SCHEMA section 5) with 3 stored workflows | memory | K32 single-source; WebArena 23.5 to 35.5, no equal-token control (d11) | 3 workflows vs same tokens of raw history vs none; repeated problem classes | Library beats raw history by 5+ points and uses fewer steps | Med |
| A08.08-U12 | Where does summary compression lose needed detail? | Compression-ratio limit and failure-tuned summary rules | O, memory | K27 single-source, K09 contested; 56.0 to 43.5 untuned, 56.5 tuned (d07); 2-word vs 3-word chunks human-only (a11) | Ratios 1x/2x/4x/8x; with and without rules built from failure cases; accuracy, lost-fact log | Tuned rules keep 90% of raw accuracy at 2x or more compression | Med |
| A08.08-U13 | Is a bounded rewritten state good without RL? | One consolidated state rewritten each step | memory | K33 single-source; MEM1 needs RL; training-free ReSum only +4.5% (d08, d09) | Rewritten bounded state vs full context; 16+ steps; accuracy and peak tokens | Within 3 points of full context at half the tokens | Low |
| A08.08-U14 | Do the 2023-2024 degradation numbers hold on our current backbone? | Confirms the "minimal context per step" rule is worth its cost | G (context per step) | K14 established but mostly older models (a20, a21) | 1x vs 3x padding, same useful content, our backbone | Drop of 5+ points at 3x padding (else the rule is cosmetic) | Med |

## Open questions we cannot test on our bench yet

- Baddeley and Hitch (1974) dual-task numbers: not obtained. Unblock by opening the chapter or a secondary source with the digit-load table. Low value for the agent.
- Thalmann et al. (2019) effect sizes and Gobet and Clarkson (2004) methods: only abstracts read. Unblock with the full texts.
- Whether the Wang and Sun parameter-count rule (t=3.03, N=30, 26.1% of variance) holds inside one model family. Needs a multi-size sweep we do not run.
- Whether a 3-5 item limit exists in frontier models. Needs a clean item-count task with confirmed task understanding (Hu and Lewis); no public number found.
- HiAgent replication: needs the authors' code and the AgentBoard tasks. First resolve the Table 1 caveat (23.94 and 35.02 are the Jericho row).
- Attention-based explanations (dispersion, retrieval heads): need interpretability access to our backbone.
- Slots versus resources in humans: unresolved and not needed for the agent.

## Order to run

1. **U6 (working-set size of our backbone):** cheap, and it sets the cap and the difficulty range for every other test.
2. **U3 and U4 (code ledger; delete vs ignore):** one shared update-heavy, multi-turn item set. Highest expected gain, because multi-turn loss (-39%) and stale-state interference are the largest measured effects.
3. **U1 and U2 (named summaries vs masking vs raw):** settles the contested HiAgent claim and gives the memory rule; run on the same long-horizon items.
