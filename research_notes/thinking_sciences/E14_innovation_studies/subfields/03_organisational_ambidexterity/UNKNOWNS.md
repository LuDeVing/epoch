# Organisational ambidexterity: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| E14.03-U1 | Does a balanced explore:exploit token split beat either focus? | A fixed or adaptive explore-share rule in S0 | S0, S3/S4 | K01 contested: Mathias 2014, Clauss 2020, Wenke 2021 against; Kula 2023, He and Wong for. Human only | Explore-only, exploit-only, 50/50, adaptive; mixed check-based and open items; solved rate on held-out check | Best balanced arm beats best focus arm by 3+ points over 10 seeds, CI excludes 0 | Med |
| E14.03-U2 | Does the best explore share move with task novelty? | Per-class explore share stored in S0 lookup, updated in S9 | S0, S9 | K19 single-source (Uotila abstract); K06 single-source (Jansen); human only | Sweep s in {0,.1,.25,.5,.75,1} on familiar vs novel item classes at fixed budget; fit s* | Interior optimum, and s* differs between classes by 0.15 or more | High |
| E14.03-U3 | Does code-chosen operator selection (UCB or Thompson) at S6 beat model-chosen? | Bandit selector for O1-O8 | O, S6, G12 | K12 single-source (MACE, small model); K11 established for in-context explore failure; K21 single-source | Model-picks, round-robin, UCB, Thompson; impasse items; solved rate and lock-in share | UCB or Thompson beats model-picks by 3+ points, or lock-in on one operator falls by 20+ points | High |
| E14.03-U4 | Does adaptive allocation of calls across arms beat a fixed split? | Adaptive allocator across prompts, operators or model sizes | G12, S3 | K21 single-source (d10, d11; open Qwen/Llama only, geometric tasks) | Fixed greedy, random, adaptive; budgets 1k, 5k, 20k; solved rate | Adaptive beats best fixed by 5%+ relative on 2 of 3 budgets | Med |
| E14.03-U5 | Does an explorer agent plus exploiter agent beat one alternating agent? | Optional split for separable-stage tasks only | structure | K17, K18 single-source; K20 established against splits above 500 tokens; Fourne human abstract only | Single alternating vs split with handoff; separable and interactive items; solved rate; handoff tokens | Split beats single by 3+ points on separable items without losing on interactive ones | Low |
| E14.03-U6 | Does a tight rubric on exploit stages plus a loose one on explore stages beat a uniform rubric? | Per-state rubric strictness | G, S3 vs S4 | K07 single-source (Jansen 2006 betas, human only) | Uniform loose, uniform strict, mixed; checked items; solved rate and count of distinct candidates | Mixed beats both uniforms by 2+ points | Low |
| E14.03-U7 | Does token budget act like resource level (balance when small, high-both when large)? | Budget-dependent explore share | S0 | K08 single-source (Cao abstract); d10, d13 partial, call counts not tokens | Balanced vs both-high vs explore-light at 1k, 5k, 20k tokens | Rank order of arms flips between small and large budget, CI excluding 0 | Low |
| E14.03-U8 | Does LLM-propose plus code-select beat LLM-select? | Generate/select split made explicit for open items | S3, S7, G5 | K13 single-source (Harris and Slivkins); G5 already established for selection | LLM selects vs regression or fresh-input agreement selects; solved rate and tokens | Code selection equal or better at fewer tokens | Med |
| E14.03-U9 | Does embedding-similarity novelty rejection (and island count) improve open-mode search? | Novelty rejection threshold in the candidate archive; island count | M (archive) | K14 established for diverse sampling; K23 contested for diversity controls; island count never ablated | No rejection vs 0.95 rejection; 1, 2, 4 islands; count of behaviourally distinct passing candidates; 10+ seeds | Rejection raises distinct passing candidates by 15%+ or best score by 1 SD | Low |
| E14.03-U10 | Does an external novelty or uncertainty rule raise realised novelty where an "explore" instruction does not? | Replace the explore instruction with a rule | S3, G8 | K22 single-source (biochemistry only, frontier models) | Instruction arm vs external novelty rule; open items; distinct outputs on probe inputs | Realised novelty up by 20%+ with no loss in pass rate | High |
| E14.03-U11 | Does a capability gate (no deep refinement for weak models) save tokens? | Model-size gate on depth in S5/S6 | G12 | K21 single-source: weak model gets no depth gain (d10, open models) | Deep vs shallow allocation on small and large model; solved rate per token | Deep chain adds under 1 point on the small model while costing 2x tokens | Med |
| E14.03-U12 | Does a balance or product measure of our own explore/exploit logs predict solved rate across items? | Nothing directly; a logging metric for diagnosis | S9 | K05 single-source (He and Wong); Cao 2009 and Junni say the measure choice changes the answer | Log E and X tokens per item; regress solved on E*X, abs(E-X), E+X | One form explains 5%+ more variance than the others on held-out items | Low |

## Open questions we cannot test on our bench yet

- Pooled r, k and N from Junni 2013, Mathias 2014, Fourne 2019, Wenke 2021 were never read. Unblock: full-text access (publisher pages were blocked) or authors' data tables.
- Whether structural separation raises performance, not just balance (Fourne). Unblock: full text of Fourne 2019.
- Whether human results survive objective, multisource data. Unblock: coefficients from Uotila 2009 and Lubatkin 2006.
- Long-horizon, multi-session sequential ambidexterity (alternating exploit and explore phases over many episodes). Our bench runs single items. Unblock: a multi-session bench with persistent memory.
- Whether MACE-style external UCB generalises to frontier models and non-toy tasks. Unblock: re-run on our own models; the 50.0% to 0.0% figure was not found in the paper text.
- Whether culture-style traits (stretch, trust) have any agent meaning. Unblock: a concrete operational definition; none exists.
- Independent replication of the equal-token single-versus-multi result on non-QA tasks. d14 covers multi-hop QA only.

## Order to run

1. **E14.03-U3 (code-chosen operator selection at S6).** Cheapest, with the strongest analogue evidence (lock-in 50.0% to 0.0% in one small model; K11 established), and it directly changes how S6 picks operators.
2. **E14.03-U10 (external novelty rule versus explore instruction).** Frontier models state exploration but do not realise it (about 92% intent, near-zero correlation); a rule is easy to code and fits G8.
3. **E14.03-U2 (explore share by task novelty).** One sweep also answers U1 and U7 as a by-product, and tells S0 whether an adaptive share is worth building.
