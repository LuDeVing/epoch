# Boden's creativity types: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| C04.01-U1 | Does a Boden-mode generator (combine / explore / rule-drop) beat a plain search wrapper? | Mode generator in open mode | S3 | K01-K03; single-source (UoT), 52-58% vs ablations, 7-52x tokens | (a) plain best-first, (b) C/E/T operators, (c) one prompt; 20 open + 20 low-constraint tasks; distinct-meaning count per 10k tokens, debiased pairwise win rate | (b) beats (a) by 5+ points win rate or 20%+ yield on both backbones | High |
| C04.01-U2 | Does the UoT mode ranking replicate on another backbone and judge family? | Constraint-level mode routing | S0, S3 | K02, K24; single-source, ranking flipped on GLM-4-9B | Same four arms on 2 backbones, judge from another family, 100 tasks; rank of modes | Same mode wins on both backbones and Kendall tau above 0.6; else no routing | High |
| C04.01-U3 | How many rule drops before correctness collapses, and does a drop beat resampling? | Rule-drop operator with a drop cap | O4 | K21, K22; single-source, GPT-4 pass@1 16.1 to 2.1% over 5 rules | Drop 0-3 rules vs plain resampling; 100 checkable code tasks; pass on original tests, divergent-solution rate | Drop arm gives 1.5x more divergent valid solutions at 2 or fewer drops with pass-rate loss under 50% | High |
| C04.01-U4 | Is an axiom-level drop better than a leaf-rule ban? | Axiom-level operator (list assumptions, drop one with many dependents, re-derive) | O4, O8 | K23; contested, our inference from d16 | Axiom drop vs technique ban vs resample; checkable tasks and ARC-style puzzles; valid-and-different solution rate | Axiom arm beats leaf arm by 10+ points valid-and-different rate | Med |
| C04.01-U5 | Does a transfer check after analogy raise strong transfer? | Check step in O7 | O7 | K04; single-source, strong transfer 32-52% | With vs without check; 30 analogy tasks; strong-transfer rate (judge) plus correctness | Strong transfer up 10+ points with no loss of correctness | Med |
| C04.01-U6 | Does verbalized sampling raise non-duplicate yield per token in open mode? | Verbalized sampling prompt in S3 | S3 | K11; single-source per method, 1.6-2.1x diversity | Direct vs verbalized vs set prompt; 50 open prompts; distinct-meaning count per 10k tokens, q@Tail | 1.3x yield with q@Tail not lower by more than 5% | High |
| C04.01-U7 | Is explore-early, refine-late better than a constant mix? | Scheduled explore/refine | S3, S5 | K13, K28; single-source, never compared | Constant mix vs 40/60 schedule; one checkable task, 20 iterations; best score at fixed tokens | Schedule wins by 5+ points on best score on 3 of 4 task sets | Med |
| C04.01-U8 | Does set-level prompting plus a quality filter keep both diversity and quality? | Set prompt then filter | S3 | K27; single-source, distance 0.24 to 0.80, win rate 0.33 to 0.21 | Independent samples vs set prompt vs set + filter; open prompts; distance and win rate together | Distance up 2x with win-rate drop under 3 points | Med |
| C04.01-U9 | Is a judge-free meaning-entropy signal a good stop rule and diversity metric? | Entropy stop rule | S3, G | K29, K12; single-source, rho 0.56 with humans, small panels | Stop on entropy plateau vs fixed budget; 200-batch runs; tokens saved at same final cluster count | 30%+ tokens saved with under 5% fewer clusters | Med |
| C04.01-U10 | Is our judge stable under conceptual (not register) paraphrase and aligned with humans? | Judge-panel rules, unanimous-only | G8 | K14, K15; contested, register probe d=0.15-0.29, 0.80 vs 0.65 | 100 outputs reordered in concept and in register; 30 human labels per task; rank flip rate, Spearman with humans | Flip rate under 10% and Spearman with humans at least 0.65; else drop the judge | High |
| C04.01-U11 | Do creativity wrappers hurt quality in the novel tail in our setting? | A hard ban on persona / meta-prompt wrappers in open mode | G4, S3 | K25; single-source, -6.9% to -32.5% | Plain vs wrapper arms; 100 prompts; q@Tail | Any wrapper below plain by 5%+ on q@Tail is banned in open mode | Low |
| C04.01-U12 | Does cluster-based dedup, rather than cosine, change which ideas we keep? | Cluster-based dedup | S3 | K10, K08; single-source | Cosine 0.8 vs concept clusters vs none; 4000 seeds on 5 topics; non-duplicate yield, human spot check of 50 pairs | Cluster arm yields 20%+ more kept ideas with under 10% false merges | Low |
| C04.01-U13 | Do explicit R/T/E lists in the prompt beat unlabelled generation? | Wiggins vocabulary in S3 prompt | S3 | K20; single-source, no measurement | R/T/E lists vs plain; 30 tasks; novelty and constraint adherence | Wins by 5+ points on win rate or yield | Low |

## Open questions we cannot test on our bench yet
- Whether the three Boden types are separable mechanisms at all (one factor explains 81.5% of variance, K26). Needs a human or cross-model study with item-level type labels; we have none.
- Whether prompt-level rule change meets Boden's and Wiggins's actual definition of transformation. Needs the primary texts (paywalled, 403/404) or a domain expert.
- Whether human creators show novelty falling as performance rises. Needs a human study; none found.
- Weight-level interventions (random-prefix decoding, steering, min-p, set-reward training). Need sampler or weight access; a scaffold-only bench cannot run them.
- Open-mode tasks with no verifier, where the generate-test loop is unavailable. Needs a trusted automatic novelty check; none exists.
- The Lu et al. 2026 execution audit and TwistBench. Not located; find them or ask the authors.

## Order to run
1. C04.01-U10 (judge stability and human alignment): every other open-mode test depends on a judge we can trust, and it is cheap.
2. C04.01-U3 (rule-drop budget on checkable tasks): it has a real verifier, so the answer is exact and it sets the cap for O4.
3. C04.01-U1 (mode generator versus plain wrapper at equal tokens): the central S3 question; run on two backbones so it also covers U2.
