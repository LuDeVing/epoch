# Critique, A17.07 Collective intelligence factor c (cross-check)

## Re-opened this session (full text or page)
Woolley 2010 (gwern PDF), Engel 2014 (PLOS ONE), Bates and Gupta 2017 (PDF), Riedl 2021 (PMC), Rowe 2021 (PMC), Graf 2019 (PDF), Ilic and Gignac 2024 (arXiv), Zhou 2026 (ACL PDF), Riedl 2026 (arXiv). Vaccaro 2024 PDF was only partly readable (370 effect sizes confirmed; g values not re-seen).

## Confirmed
- Woolley: 699 people, first factor 43% (Study 1) and 44% (Study 2), second 18% and 20%; avg member IQ with c r=0.15 (p=.04) and max 0.19 (p=.008) in Study 2; RME r=0.26; Sobel z=1.93.
- Bates and Gupta: 39.8% single factor in Study 1, IQ about 80-81% of group-IQ variance.
- Riedl 2021: 22 studies, 1,356 groups, 5,279 people, mean r 0.27 (0.12-0.50), loadings 0.27-0.52, AVE 44%, leave-one-out r 0.40 (0.26-0.53).
- Rowe 2021: r=.26 (CI .10-.40), N=857 groups, Q(8)=59.36, I2=86.5%; AVE 30.23% over 49 loadings.
- Graf 2019: 745 teams, chi2=40.79, CFI .73, TLI .45; parallel analysis suggests three factors.
- Ilic and Gignac: 591 LLMs, mean r 0.73, 65.6% general, omega h .94.
- Zhou 2026: 108 groups, r 0.55 vs 0.28 human, 66.3% / 18.7%, CFI .967, 75% cost vs 9.7% ACI.
- Riedl 2026: OR 0.92 per member, OR 1.50 per temperature, interaction 0.24 p=.014, 27%.

## Corrections made
1. b02 and a10 disagree: Engel 2014 face-to-face RME with c is r=.53 (p=.002), not .52. a10 corrected in claims (K05 uses .53).
2. c27 says Study 1 had 2-3 members and Study 2 had 3-5. Wrong. Study 1 was 40 groups of 3; Study 2 was 152 groups of 2-5 (a01 is right).
3. AVE 44% (Riedl) and 30.23% (Rowe) are different statistics (AVE from the meta-analytic model vs mean squared loadings over 49 loadings). Do not present as a conflict, but do not quote 44% as "variance explained" without saying which.
4. Woolley's headline 43-44% is first eigenvalue share; principal-axis share on the ten-task set is 31% and 35% (a04). The popular "about 43-44%" overstates.
5. Zhou compares r 0.55 to human 0.28 from different task sets and designs; the gap is suggestive, not a controlled contrast.

## Contradictions between sources
- c versus member IQ: Woolley (weak link) vs Bates and Gupta (IQ about 80%); Rowe pooled IQ-c .185, IQ-criterion .067. Open.
- Whether c exists at all in diverse or virtual teams: Graf (r=.001), Barlow and Dennis (none), Credé and Howardson vs Engel 2015, Riedl 2021.
- Female proportion and turn-taking: positive in Woolley and Engel, null in Bates and Gupta.
- Social sensitivity: strong in Engel (.53-.55), small once IQ is controlled (Bates and Gupta beta .19).

## Weak spots
- Many tasks in human studies share the same authors, platform (POGS) and task family; independence of sources is lower than counts suggest.
- Small group counts: only 6 of 19 samples powered for r=.10-.30.
- c is built from the same tasks it correlates with (part-whole inflation).
- LLM studies are mostly single-paper, 2026, unreplicated (Zhou, Riedl 2026, Li et al., Wu et al.). Models are drawn from a few families, so the strong factor may reflect shared base capability.
- ToM mediation is marginal (p=.053).
- The Riedl 2026 temperature effect confounds exploration with group success.

## Only seen in snippets or abstracts
b13 (Credé and Howardson per-sample numbers), b15 (Woolley 2018 review), b16, b27 (Scofield abstract only), b28, c27, c28, c29, a23. Vaccaro g values were not re-verified here.

## Relevance
Background only. No schema change follows from c. The usable lessons are empirical: more agents often hurt (K12), vote beats debate (K14), distributed information is badly pooled (K15).

## GAPS
1. Does an LLM-group general factor survive when members are not drawn from the same few model families, and after controlling for mean member capability?
2. At equal tokens, does one scaffolded agent beat N parallel agents on tasks where single-agent accuracy is above 45%, and where is the crossover?
3. Does any social-sensitivity-like step (explicit perspective-taking) raise multi-agent scores beyond base model strength, with adequate power (more than 50 runs per arm)?
4. What is the actual first-factor share of c with the Woolley principal-axis method on the Riedl pooled data versus the 43-44% headline?
5. Is Bates and Gupta's IQ explanation or Woolley's c explanation right once measurement reliability and task difficulty ceilings are handled? (A pre-registered large replication is missing.)
6. Why does c vanish in Graf's pooled data and Barlow and Dennis: task-type mix, computer mediation, or scoring rules?
7. Does the hidden-profile information-pooling failure (30.1% vs 80.7%) shrink with a structured shared-facts step, and at what token cost?
8. Is the speaking-turn equality effect causal (intervention) in humans or LLM groups?
9. Does the cross-task correlation of a single scaffolded agent (not a group) across task types match LLM population r 0.73, i.e. is there a "scaffold factor"?

## Gap search results
Search tools were nearly unavailable (WebSearch budget used up after one call; arXiv, Semantic Scholar and OpenAlex APIs returned 429). Evidence comes from direct fetches. 18 lines in evidence_d.jsonl (d01-d18). Claims K22-K28 added; K02, K04, K07, K08, K11, K13, K16, K17, K19 extended.

1. LLM factor across model families, controlling mean capability: STAYED OPEN. Zhou's 108 groups come from only 8 LLMs (5 providers, 3 Qwen); mean member g has 37% importance in a random forest (partial control), process over 50% (circular). No study with disjoint model sets (d03, d04). Wu et al. (c16) shows same-capability models differ by up to 11 teamwork points, which is the only control seen.
2. Single scaffolded agent vs N agents at equal tokens: MOSTLY CLOSED. Kim et al. matched 4,800 tokens; MAS loses above about 45% single-agent accuracy (beta -0.236, p=.004) and wins only on decomposable low-baseline tasks (+80.8% Finance). Tran and Kiela: single agent best at 500-5k thinking tokens, beaten at 100 and roughly tied at 10k (d01, d02). The 45% boundary is a fit across six benchmarks, not a sweep.
3. Perspective-taking with adequate power: CLOSED, NEGATIVE. Riedl 2026 used 200 groups per arm and found no overall success difference for ToM; emergence share fell to 18% from 37% (d15). Li 2023 belief-state results are three trials per condition (d16).
4. Woolley principal-axis share on Riedl's pooled data: NOT ANSWERABLE from main text. Riedl used a meta-analytic one-factor model (AVE 44%) and reports no eigenvalue share. Loadings .27-.52 imply at most 27% mean squared loading, so 44% looks inconsistent; mean r .27 implies about 27% (d09, d10, inference; SI and 2022 correction unread). The earlier correction 4 (Woolley PAF 31% and 35%) stands.
5. Bates and Gupta vs Woolley with reliability and ceilings: STAYED OPEN. Latent SEM on 80 groups gave IQ path 1.0 with zero residual (d12), but Raven ceiling, overlap of tasks with IQ content, and no preregistration remain. 58% power in Study 1 (d13).
6. Why c vanishes in Graf and Barlow and Dennis: PARTLY CLOSED. Graf uses five collapsed task types and a mixed-medium pool with one moderator; it is a 4-page abstract (d07, d08). Barlow and Dennis was paywalled (403) and not opened. Scoring rules untested.
7. Hidden-profile pooling with a structured step: CLOSED. Two rounds of fact sharing plus doubt, then one decide pass: GPT-4.1 .037 to .800, Gemini-2.5-Flash .173 to .727, Flash-Lite .043 to .743 (18 tasks, 5 runs, 4 agents). Token cost not reported (d05, d06).
8. Turn-taking causal: STAYED OPEN, leaning null. Equal-talk instruction F(2,34)=1.14 p=.33 (40 groups, ceiling); video vs audio dyads raised turn inequality but CI was not significantly different (99 dyads, p=.22). No LLM-group test found (d11, d14).
9. Scaffold factor for a single agent: STAYED OPEN. No such study found; Ilic and Gignac is across models (d17).

Corrections to earlier critique: Riedl 2026 temperature was not varied in the main 600 runs (only in the preliminary 7,150-run grid), so the "temperature confound" weak spot applies only to the preliminary grid. K17 reworded: the ToM prompt did not raise overall success.
