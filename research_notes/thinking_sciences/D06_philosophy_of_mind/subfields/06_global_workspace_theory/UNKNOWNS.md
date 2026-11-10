# Global workspace theory: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| D06.06-U1 | Does passing one code-chosen item forward beat pasting several candidates? | Hard single-item commit between S4/S7 and later states | S7, G5 | K20, K19, K17, K16; single-source; no soft-mix arm anywhere | T1: 6 attempts; A keep 1, B keep 3, C all 6 pasted; 100+ checkable items, 3 seeds; accuracy | A at least equal to B (within 2 points) and above C by 2 or more points, CI excluding 0 | High |
| D06.06-U2 | Does a fixed-size carried state, rewritten each step, beat an uncapped log? | A capped state block (about 300 tokens) rewritten by the model, kept by code | memory, S9 | K18, K17, K07; MemAgent is RL-trained retrieval QA; Du is abstract only; single-source | T2: items over 10 steps; A cap 300, B full log, C cap 1,000; accuracy and failure step | A or C at least equal to B at steps above 10 and tokens down 30% or more | High |
| D06.06-U3 | Does a goal-plus-interim-conclusions block beat raw history? | Explicit running summary state | S-state, memory | K13 (concept [E], benefit untested); a28, a10, c22 | T3: as T2; A summary block, B raw prior attempts and outputs; accuracy and error propagation | A at least +2 points, or equal at 30% fewer tokens | High |
| D06.06-U4 | Is there an interior optimum for number of carried items k? | A tuned default k per mode | memory | K08, K21; Goyal peak 5 of 2-10 (small net, one task); Dossa flat 32-512; Phua threshold; no LLM replication | T4: 100 fixed items; k = 1, 3, 5, 8, 12; accuracy vs k | A k whose accuracy beats k=1 and k=12 by 2 or more points each; else keep k fixed and small | Med |
| D06.06-U5 | Can we open the full pipeline only after errors (vigilance) and save tokens? | S0 gate driven by a vigilance counter V (down 0.1 V on pass, up 0.5(1-V) on fail) | S0, G1 | a01 (toy); our G1 data (92% plain vs 75% forced doubt); single-source | T5: mixed easy and hard items; A gated, B full pipeline always; accuracy and tokens | Same accuracy (within 1 point) at 30% or more fewer tokens, no loss on hard items | High |
| D06.06-U6 | Does a hard threshold commit (candidate must pass a check before entering state) beat soft weighting? | Check-gated entry to the state block | S4, S7, G3 | K02 (bimodal access, human [E]); transfer is analogy only; ignition itself contested (K04) | T1 with arm D: soft score-weighted merge of top 3 vs hard gate; accuracy | Hard gate at least equal and 2 or more points above soft merge | Med |
| D06.06-U7 | Do stale items hurt, and does decay help? | Leaky state: items expire unless re-cited within 3 steps | memory | c12 (design idea, no data); LbMAS: marking stale messages instead of deleting lowered MMLU 85.17 to 84.38; single-source | T6: multi-turn items; A persist, B decay in 3 steps; accuracy and stale-item errors | B above A by 2 or more points | Low |
| D06.06-U8 | Does recite-then-solve with a short state beat full context on long inputs? | Recitation step before solving on long items | S1, memory | K17: Du 13.9% drop with length; recitation up to +4% RULER; abstract only | T7: inputs over 20k tokens; A recite plus short state, B full context | A at least +2 points at equal tokens | Med |
| D06.06-U9 | Do S9 lesson lines (reflection) help at equal tokens? | Keep lesson lines in memory | S9, memory | K12: Park TrueSkill 29.89 vs 26.88 (believability only, single-source); J-space reflection result is fine-tuning | T8: repeated classes; with vs without lessons; accuracy on repeated classes | +2 points or more on seen classes, no loss on others | Med |
| D06.06-U10 | Does diversity-driven temperature in S3 raise coverage at equal tokens? | Temperature rises when candidate diversity H is low | S3 | K15: Theater of Mind proposal, no experiments; parameters unspecified | A fixed temperature vs B Tgen = Tbase + a*exp(-b*H); 100 open or multi-answer items; distinct-correct-candidates count | B finds 10% or more more distinct correct candidates, no accuracy loss | Low |
| D06.06-U11 | Does a one-item-per-step broadcast order (queue of one) beat letting the model see all open subgoals at once? | Single active subgoal broadcast in S6 | S6, operators | K01 concept; no direct test; ToT b=1 45% vs b=5 74% argues for keeping more | S6 impasse items; A one active subgoal, B all open subgoals listed; accuracy | A at least +2 points | Low |
| D06.06-U12 | Is the Butlin indicator checklist predictive of anything measurable? | Nothing in behaviour; keeps as documentation | none | K11; opinion not measurement | Score three scaffold variants on GWT-1 to GWT-4; compare with their T1 to T3 accuracy ranks | Rank correlation of 0.7 or more across 6 or more variants; else drop from design reviews | Low |

## Open questions we cannot test on our bench yet
- Does the Anthropic J-space result (cap of at most 25 items, broadcast-head ablation) replicate on another vendor's model, or with multi-token concepts? Needs open-weight models with interpretability tooling or independent access.
- Does a long, soft context ever beat a hard bottleneck on tasks where the discarded item turns out to matter? Needs a task where the key fact is hidden in a rejected candidate. Our bench has no such item set yet.
- Is the human failure of PFC ignition (Cogitate) relevant to how strongly we cite GWT? Cannot be tested on LLM tasks; only a citation-policy question.
- Full text of the 2026 meta-analysis (117 studies): moderators and the unseen VAN SMD were not read; needs library access.
- Tait et al. (2026) evaluating GWT markers in LLMs returned 403 and was not read; needs an alternate copy.
- RL-trained memory (MemAgent, context curator) shows gains that a prompt-only scaffold may not reach. Needs a trained-model arm, which is out of scope for a scaffold-only agent.
- Whether a workspace helps more for weak models than strong ones (BIGMAS says larger gains on weaker models, with no token match). Needs a model-size sweep at equal tokens.

## Order to run
1. D06.06-U1 (T1: hard single-item commit vs keep-3 vs paste-all). Cheapest, uses attempts we already generate, and answers the central gap (K16).
2. D06.06-U2 (T2: capped rewritten state vs full log). Tests the one new structure (a fixed-size state block) and measures token savings.
3. D06.06-U5 (T5: vigilance gate). Pure token-saving test on logs we already have; if it holds it also supports G1 and G12.
