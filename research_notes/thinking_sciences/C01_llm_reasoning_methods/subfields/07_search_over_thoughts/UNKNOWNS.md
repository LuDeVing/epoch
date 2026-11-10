# Search over thoughts: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*
## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| C01.07-U1 | Does a value-guided tree beat voting on a reasoning model with a prompted value? | Tree at S6 with value and random-tree control | S6/G2 | K20, d02; single-source, one 20B model | Tree+value vs random tree vs vote; 100 items with code check; solved rate; 3 seeds | Tree beats vote by 3+ points in all 3 seeds and random tree loses | High |
| C01.07-U2 | Can we measure judge accuracy online before branching? | Judge-accuracy gate | G5/S6 | K23, d09, b13; Chen 90% is the only threshold | Score judge on 20-50 labelled partial states; then branch vs sample; solved rate | Gate cuts losses vs always-branch and keeps gains; threshold chosen on held-out set | High |
| C01.07-U3 | Does step-1 disagreement or a failed check make a good branch trigger? | Branch trigger at S6 | S6/G1 | K08, K09, a03; Game of 24 only | Always tree vs never vs trigger; items where plain accuracy is 10-60%; solved rate per token | Trigger within 2 points of best fixed arm at 30%+ fewer tokens | High |
| C01.07-U4 | Does the formalisability gate (code successor/goal in 3 rounds) work on our tasks? | Code-search route | G5/S6 | K26, d13, d14; rule-bound domains only | Gate then BFS vs sampling with code check; Brainteaser/ARC-like items; solved rate | BFS 90%+ where gate passes and gate false-pass under 10% | High |
| C01.07-U5 | Does an idea tree beat sample-rank-dedup on human novelty? | Keep idea tree for open mode | S6 idea tree/G8 | K17, K25, d11, d12; no tree arm exists | 40 prompts; blind 3 raters, length-normalised; novelty and usefulness | Tree +0.5 on 10-point novelty at equal tokens, rater agreement acceptable | Med |
| C01.07-U6 | Does a code-run merge (split, solve, merge, no scoring) capture the GoT gain? | Merge operator | S6/O3 | K12, K27, d15; GPT-3.5, no ablation | Code merge vs GoT scoring vs flat; sort and set intersection at P=32, 64, 128 | Merge within 10% of GoT error at P=128 | Med |
| C01.07-U7 | Does a one-call search trace (AoT) hold beyond arithmetic? | Single-call S6 mode | S6 | K11, a15; single-source | AoT vs multi-call tree on 2 non-arithmetic tasks; solved rate, skipped-branch rate | Within 3 points of tree at under 25% of tokens, branch skipping under 10% | Med |
| C01.07-U8 | Does a reserve list recover falsely pruned branches? | Reserve list for pruned nodes | S6 | critique gap 8; crossword prune missed 3 of 4 solved boards (a05); no test | Hard prune vs prune with reserve; constraint tasks; recovery rate and solved rate | Reserve adds 3+ points solved at under 10% extra tokens | Med |
| C01.07-U9 | Does a difficulty-bin router avoid beam harm on easy items? | Difficulty routing | G12 | K09, b14; trained PRM, MATH only | Router by model-estimated bin vs fixed arm; mixed-difficulty set; solved rate per token | Router saves 5%+ tokens at same accuracy vs best fixed arm | Med |
| C01.07-U10 | Does a plan-diversity step (one plan per operator) raise pass@k? | Operator plans before action | S6/O1-O8 | K14, c19; single-source, code only | Plan-first vs repeated sampling; code items; pass@k at equal tokens | pass@k up 5+ points and unique-plan count up | Med |
| C01.07-U11 | Is a unique-answer count a good stop rule for widening? | Stop-widening rule | G1 | K28, d12, d17; inference only | Fixed b vs stop when new unique answers per sample fall under threshold; solved rate per token | Equal accuracy at 20%+ fewer tokens | Low |
| C01.07-U12 | Do trees help with a strong generator and cheap evaluator at equal dollars? | Split roles | S6/G7 | c12 (GPT-4 era); no reasoning-model test | Strong+cheap vs strong+strong vs vote; dollar-matched; solved rate | Split within 2 points at 40%+ lower cost | Low |
| C01.07-U13 | Does feeding real failed attempts approximate search-trace training? | Failed-attempt context | M/G2 | K13; training evidence only | Retry with failed attempts and their outputs vs fresh retry; solved rate | +3 points over fresh retry | Low |
## Open questions we cannot test on our bench yet
- o-series and Claude-thinking tree-versus-voting evidence: no public arm exists; needs our own runs with a thinking-mode model.
- Per-task judge threshold beyond Chen's 90%: needs a set of labelled partial states per task.
- Depth-cap interaction with breadth (Blocksworld decay): needs long-horizon items.
- Human novelty raters: needs blind raters and a rating session.
- Why Yao and Wang disagree by 20 points at b=1: needs their prompts and seeds.
## Order to run
1. C01.07-U2 (judge-accuracy gate): cheap, and every other tree test depends on knowing whether the judge is good.
2. C01.07-U1 (tree with value vs random tree vs vote): directly tests whether S6 branching beats the sample-and-select default.
3. C01.07-U4 (formalisability gate plus code BFS): biggest known gain (100% on Game of 24) and cheap to try.
