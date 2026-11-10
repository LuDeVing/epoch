# MDL and Bayes: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| C11.05-U1 | Does argmax of joint chain+answer log-prob beat majority vote? | Joint-score selector (or log-prob-weighted vote) in S7 when log-probs exist | S7, G5 | K24 contested; d03 beats SC 37 of 40; d01, d02 raw scores lose; older/small models mostly | Same k samples; arms: vote, argmax joint, weighted vote; reasoning and word items; accuracy paired by item | Beats vote by 2+ points, 95% interval above 0, on 2 item types | High |
| C11.05-U2 | Does an explicit prior term (hypothesis length in tokens) add to U1? | Prior-penalised selection rule | S7 | No direct study; two-part MDL in agents d11 (single-source) | U1 arms plus argmax(joint - lambda x tokens), lambda tuned on dev split; accuracy | Beats best U1 arm by 2+ points on held-out items | Med |
| C11.05-U3 | Does short-m@k (stop at first m of k chains, vote) match vote at fewer tokens on our bench? | Early-stop rule in reasoning mode | S3, S7, G11 | K25 established (d05, d08, d16); reasoning models only | Arms: vote of k; short-m@k, m=k/2; random chain; reasoning-mode items; accuracy and tokens | Equal accuracy within 1 point with 20% fewer tokens, or +2 at equal tokens | High |
| C11.05-U4 | Does shuffle-averaging of evidence order beat m independent samples? | Order-averaging step | S3 | K28 single-source; log-loss gain only, 7-9B models (d13, c12) | Arms: one pass; 3 shuffles then vote; 3 samples at fixed order; evidence-heavy items; accuracy and order variance | Shuffle arm beats sample arm by 2+ points | Med |
| C11.05-U5 | Does MDL pruning of the rule store beat an LLM summary? | MDL consolidation of lessons | S9 memory | K26: RIMRULE +4.5 (BFCL), +3.6 (ToolHop), MIDGARD; two sources, small models | Arms: no pruning; LLM summary; length plus uncorrected failures (alpha on dev); repeated-class items; held-out accuracy, store size | +2 points over summary and no loss vs no pruning | Med |
| C11.05-U6 | Does prequential gain (later loss with vs without a note) predict note usefulness better than relevance or recency? | Loss-based note scoring | S9 memory | K07, K30; Voita and Titov (probing only); Memory Tax shows memory loses to RAG | Arms: retrieve by relevance, recency, loss drop; items with stored notes; accuracy | Beats relevance by 3+ points | Low |
| C11.05-U7 | Does a hold-out (conditional) score choose better candidate rules than total fit? | Conditional scoring in S4/S7 | S4, S7, G3 | K20 single group (c13); our two-ARC-programs failure | Arms: fit on all; fit k-1, score held-out; stacking weights; rule-induction items; accuracy on unseen case | Cuts fit-but-wrong rate by 20% relative | High |
| C11.05-U8 | Does an explicit posterior table kept in code lift the round-1 plateau of plain chat? | Code-held Bayes table with model-supplied likelihoods | S5, S7 | K17: plateau in 7-9B models, fixed only by fine-tuning (c07); prompts inconsistent (d18) | Arms: plain multi-round; table in code; hypothesis-elimination items; round-5 accuracy | +5 points at round 5 | Med |
| C11.05-U9 | Does a tempered (down-weighted) combination of correlated samples help? | Tempered vote weights | S7, G4 | K05, K27 simulation only; BMA collapse d10 | Arms: plain vote; weights w^eta with eta 0.5 vs 1 chosen on dev; accuracy | +1.5 points, no loss elsewhere | Low |
| C11.05-U10 | Does stating a prior (base rate) help or hurt, and does it depend on the number of observations? | Prior statement in S1 for estimation items | S1 | K22 BoxingGym: no reliable gain; single source | Arms: no prior; base rate; base rate plus 3 observations; estimation items; error | Helps by 3+ points on 2 item types | Low |
| C11.05-U11 | Does unsupervised mutual-information prompt choice pick a better template than our default? | Label-free prompt selector | O, S1 | K21: about 90% of the way to best template (b26), older models | Arms: default; MI-selected from 5 templates; plain items; accuracy | +2 points over default | Low |
| C11.05-U12 | Is the shortest-chain preference still useful alongside a failed-step filter, and for non-reasoning models? | Failed-step filter plus shortest tiebreak | S7, S5 | d16 failed-step fraction beats length; d08 no stable effect for non-reasoning | Arms: shortest; filter by failed-step fraction; both; reasoning vs non-reasoning model | Both beat shortest alone by 2 points, or non-reasoning arm also gains | Med |
| C11.05-U13 | Does the code length of a candidate answer within one model predict correctness better than self-certainty? | Per-answer code-length confidence for gating | S0, S7 | K10 cross-model only (a17); d02 self-certainty trails voting | Per-item AUROC of summed vs normalised log-prob vs agreement rate on exact-answer items | AUROC 0.05 above agreement rate | Low |

## Open questions we cannot test on our bench yet

- NML, luckiness or minimax-regret selection in LLM agents: no study found and the search was rate limited. Unblock: rerun the search with working Semantic Scholar and OpenAlex access; a tiny Bernoulli selection task could compare NML and Bayes-Jeffreys at small n.
- Order violation for frontier reasoning models: only 7-9B models and GPT-4 era models have been measured. Unblock: log-probabilities from the models we use, plus a martingale check on exchangeable Bernoulli draws.
- Independent replication of "post-training shifts the task prior" and its link to many-shot jailbreaking: only the original authors fit it, and non-Bayesian laws fit as well. Unblock: an external or open-weight replication.
- Sequential refinement beating parallel voting at matched tokens (d07) versus our G11: needs larger problem sets than 30 per benchmark.
- Whether log-probabilities are available for the model our agent runs on. Joint-score tests (U1, U2, U13) need them; without them only U3, U5, U7, U8 can run.
- Prior strength versus number of observations in LLMs: only toy transformers (d15) exist.

## Order to run

1. C11.05-U7 (hold-out score vs total fit): cheapest, needs no log-probs, directly targets the fit-but-wrong failure we already measured in G3.
2. C11.05-U3 (short-m@k): the best-supported effect (4 sources), saves tokens, easy to implement.
3. C11.05-U1 (joint log-prob selection vs vote): the main open question for the subfield claim; if it passes, U2 adds the prior term.
