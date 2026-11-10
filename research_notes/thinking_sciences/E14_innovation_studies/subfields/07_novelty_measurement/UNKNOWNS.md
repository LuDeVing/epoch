# Novelty measurement: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| E14.07-U1 | Does a near frame plus one distant element beat all-near and all-far candidate sets? | Open-mode step: build candidates as known frame plus one far-mechanism element | S3, O7 | K01, K29; single-source; human-only (Hope crowd, Uzzi papers) | 4 arms: all-near, all-far, near+1 far, plain best-of-N; open-mode idea and solution-path items; blind novelty x correctness, correct-and-novel rate | Near+1 far beats best other arm by 5 points or more on correct-and-novel, CI excludes 0 | High |
| E14.07-U2 | Does a retrieval prior-work check (K=5-10) cut false "novel" claims? | Retrieval check before accepting a novel candidate | S4/S8, memory | K16, K17, K24; single-source (Shahid), older models | Arms: no check, K=5, K=10, K=20; prompts with known prior work; false-novel rate and tokens per accepted idea | False-novel rate down 20 points or more, token cost under 1.5x, K=20 no better | High |
| E14.07-U3 | Does novelty rating drop after a verification step, and does the pre-rating predict the post-rating? | Rule: never accept a candidate on its pre-execution novelty; log drop | G3, S8 | K11, K28; single-source (Si 2025), human executors | Items with a runnable check; rate before and after; own vs baseline candidates | Self-generated drop exceeds baseline by 0.5 rating points or more and pre-post r below 0.3 | High |
| E14.07-U4 | Does a different-family judge reduce self-preference on novelty? | Require different-family or mixed-panel judge for open-mode selection | G5, G8 | K14, K27; established for general judging, not measured on novelty | Judge same-family vs different vs mixed panel; open-mode candidates; own-vs-other gap and agreement with blind human labels | Same-family gap above 10 points and cross-family cuts it by half | High |
| E14.07-U5 | Does sequential generation with earlier candidates visible give more distinct candidates than parallel isolated sampling? | Narrow S3's "fresh context" rule in open mode | S3 | K31; NoveltyBench, 3 models; conflicts with current S3 text | Parallel isolated vs sequential visible, same token budget; NoveltyBench-style prompts; distinct-k and blind novelty | distinct-k up 20% or more with no drop in correctness | High |
| E14.07-U6 | Can a per-facet or narrowness rating recover the "not novel" class where models score F1 0.0? | Facet or narrowness judge prompt for novelty screening | S4, O3 | K13, K14, K18; single-source, 2026 preprints | Arms: one-shot novelty, per-facet, narrowness; labelled idea set; F1 on "not novel" | "Not novel" F1 above 0.3 and macro-F1 above 25 | Med |
| E14.07-U7 | Does denial prompting (name the standard method, forbid it) raise correct-and-novel solutions in maths and planning? | Impasse operator variant: forbid the standard method | O4, O8 | K32; code and maths, mixed models | Plain retry vs denial vs MCTS-style branching; items with 3-5 known solutions; correct-and-novel rate | Correct-and-novel up 10 points with correctness down under 5 | Med |
| E14.07-U8 | Do 3 mixed-frame samples plus an integrator beat one agent on novelty at equal tokens? | Revisit G9 for open mode only | S3, G9 | K30; single-source, not equal tokens | 1 agent vs 3 mixed-frame + integrator, equal tokens; blind novelty and distinct-k | Win rate above 60% and distinct-k up, else G9 stays | Med |
| E14.07-U9 | Is there a distance threshold where novelty stops paying? | A cap or floor on distance of analogues | S3, O7 | K06; Lin extremes 61% vs 36%, r=-0.05; human-only | Candidates binned near/middle/far on our task bank; quality per bin | A single bin shows 10-point advantage over the others | Med |
| E14.07-U10 | Does an explicit "make more novel" revision pass beat single-shot, without term padding? | Revise-for-novelty pass | S5, O8 | K20; SciMON, older models, ground truth judged more novel in 85% | Single-shot vs 1 and 2 revision passes; blind novelty plus padding check (new generic terms) | Novelty up 10 points with padding rate under 20% | Low |
| E14.07-U11 | Does any cheap proxy (surprisal, embedding distance to retrieved work) beat chance on blind labels? | Cheap pre-filter in S4 | S3, S4 | K08, K34, K04; weak (r=.170, t=2.6, R2 0.33%) | Proxy vs blind labels on our items, style-matched control | AUC above 0.65 and above the style control | Low |
| E14.07-U12 | Does a fixed strategy list narrow the agent's candidate set? | Rule: vary or withhold the strategy list per sample | G4, S3 | K35; human-only (N=460) | Fixed list vs varied lists vs none; distinct-k and blind novelty | distinct-k down 15% or more under fixed list | Low |

## Open questions we cannot test on our bench yet
- Uzzi's hit result outside WoS (OpenAlex, preprints, patents) with a null model larger than 10 networks: needs a citation database and compute, not our bench.
- Whether the Bornmann 2024 corrigendum or Veugelers and Wang 2019 change validity numbers: both pages returned 403; needs publisher access.
- Human blind novelty labels at scale: our bench has no rater panel yet. Needs 3 raters per item or a labelled external set.
- Novelty for planning and puzzle tasks: no benchmark of solution-path novelty exists for these.
- Whether a cheap proxy matches blind labels: needs the same labelled set.
- Causal evidence for why mixed novelty pays: all paper-level results are correlational.
- Judge self-preference measured on novelty itself (not only on general judging): needs a cross-family judge panel.

## Order to run
1. E14.07-U3 (novelty before and after verification): cheapest, uses existing checkers, and tells us whether pre-execution novelty is worth anything to the agent at all.
2. E14.07-U2 (retrieval check, K sweep): the one intervention with a large effect in the literature (89.66% vs 10-14% on "not novel"); decides whether the memory part gets a prior-work lookup.
3. E14.07-U1 (near frame plus one distant element): the direct test of the Uzzi pattern in open mode; the only item that could change how S3 builds candidates.
