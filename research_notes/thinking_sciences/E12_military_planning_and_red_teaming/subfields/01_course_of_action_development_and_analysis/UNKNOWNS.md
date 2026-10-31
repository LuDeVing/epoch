# Course-of-action development and analysis: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*
## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| E12.01-U1 | Do 3 distinct plans, compared, beat 1 plan plus check, or best-of-N? | "Several distinct options" in S3 with code selection | S3, S7, G12 | K30, K27, K36; contested; no direct test | Arms: 1 plan + external check; 3 distinct plans + tested pick; best-of-N. 150 validated planning items, split easy/hard. Metric: validated success | 3-plan arm beats both by 3+ points on hard items with CI above 0, and loses by under 1 point on easy | High |
| E12.01-U2 | Does a distinctness filter raise final success? | Distinctness check (doctrine "distinguishable") before test | S3, G | K02, K31; PlanSearch single-source, needs verifier | Same items, with vs without idea-distance filter; metric success@k and diversity | +2 points success@k at equal tokens, no drop above 1 point at k=1 | High |
| E12.01-U3 | Does testing against best-of-k adversary replies change picks and raise win rate? | Adversary-reply test before select | S4, O select | K07, K08; single-source synthetic, 2026 preprints | Static LLM rank vs k=1 vs k=4/8 replies; two-player items with held-out opponent; metric win rate | k=4 or 8 beats static by 5+ points | High |
| E12.01-U4 | Does a cheap rubric opponent match sampled replies? | Rubric-picked reply (saves tokens) | S4 | K10; single-source synthetic | Rubric reply vs best-of-8 reply, same items | Within 2 points of best-of-8 at under half the tokens | Med |
| E12.01-U5 | Does a prompted (untrained) opponent model beat static ranking? | Opponent-model step (most likely / most dangerous) | S4 | K24, K34; trained module only, humans-only gap data | Static vs LLM-simulated reply vs rule reply; held-out stronger opponent; metric win rate | Prompted opponent beats static by 3+ points | Med |
| E12.01-U6 | Does a premortem beat a plain "list risks" prompt? | Premortem step | O critique | K28; contested, human thesis only, indirect LLM | Premortem vs risk list vs none, same extra tokens; plans with hidden failure modes; metric success | Premortem +3 points over risk list | Med |
| E12.01-U7 | Does randomising order/framing in selection cut bias? | Order/framing randomisation in S7 | G | K33; single-source, non-military | Selection step, original vs shuffled; metric flip rate, success | Flip rate above 10% and shuffle-vote lifts success 2+ points | Med |
| E12.01-U8 | Does low temperature plus reflect-first at the choose step help? | Cooler choosing step | G | K20; single-source, 10 runs, wargame only | Choose step at t=1.0 vs 0.3 vs reflect prompt; metric success and variance | Variance down and success not down | Low |
| E12.01-U9 | Is cross-sample inconsistency a usable confidence signal? | Disagreement flag in S0/S9 | S0, S9 | K22; single-source | Inconsistency score vs correctness, 200 items; metric AUROC | AUROC 0.65 or higher and adds to existing signals | Med |
| E12.01-U10 | Can a current model adjudicate COA vs reply as well as a simulator? | LLM adjudication where no simulator exists | S4 | K32; older models only (GPT-4, 59.9%) | 100 pairs, current model vs simulator; metric agreement | Agreement 90% or higher (else keep the ban) | Low |
| E12.01-U11 | Does a fallback plan pool raise completion? | Keep second valid plan | memory | K12; non-LLM, noise only | Pool vs single plan, steps fail randomly; metric completion | +5 points completion for under 20% more tokens | Low |
| E12.01-U12 | Does single decider plus critic cut keeping a failing plan vs peer vote? | Structure rule for keep/drop | G9 | K26; single-source, investment task | Two structures on switch-or-stay items; metric rate of keeping a failing plan | Critic structure lowers rate by 20+ points | Low |
| E12.01-U13 | Does a difficulty router (revise easy, diversify hard) beat a uniform budget? | Router rule | G12 | K30; single-source, math tasks | Router vs uniform on mixed-difficulty items; metric success | +3 points at equal tokens | Med |
## Open questions we cannot test on our bench yet
- Does the five-test doctrinal screen predict outcomes? Needs FM 5-0, JP 5-0, ARI reports (Pounds and Fallesen, Thunholm) and an outcome-scored dataset.
- Real size of the Klein 1995 and Johnson and Raab 2003 effects. Needs the original papers.
- Whether take-the-first applies to an LLM. Needs items where the first option can be scored against later ones.
- Whether escalation and harmonious-dialog biases carry to non-geopolitical plan selection. Needs a non-military selection bench with a scorer.
- Independent replication and token cost of COA-GPT. Needs a StarCraft II setup or a second simulator.
- Whether COA-Bench and IFPV results hold against best-of-k baselines at equal tokens. Needs their code or data.
## Order to run
1. U1 (3 distinct vs 1 plus check vs best-of-N): it is the core decision for S3 and no source tests it.
2. U3 (adversary replies vs static ranking): two 2026 preprints suggest large gains, and it reuses a two-player item set.
3. U2 (distinctness filter): cheap, runs on the U1 items, and shows whether diversity is the active ingredient.
