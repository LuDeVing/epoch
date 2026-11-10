# Cognitive task analysis: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| E04.06-U1 | Does a CDM-style sweep (cues, alternatives, novice pitfalls) on the agent's own failed cases make lessons that beat plain lessons? | A "look back" sweep that writes cue/strategy/pitfall lessons | memory, S9 | K13, K24; no published test (single-source, human-only) | Arms: CDM lessons, same-length plain-structure lessons, none. Items: held-out hard items the plain model failed. Metric: pass rate | CDM minus none >= +3 pp and CDM minus plain >= +2 pp, over 2 seeds | High |
| E04.06-U2 | Is the gain from content or only from having a well-formed lesson? | Keep CDM content only if it beats a non-expert same-format control | memory | K24, K20; Zhao 2026 filler matches real (contested) | Add arms: same-format non-expert content; length-matched irrelevant; role label only. Metric: pass rate | CDM beats both controls by >= 2 pp; otherwise drop CDM and keep the cheaper format | High |
| E04.06-U3 | Do probes recover decision knowledge the agent leaves out of an unprompted summary? | 3 fixed probes in the post-case summary | memory, S9 | K01; a08, b05, b06 (single lab, human-only) | Free summary vs summary with 3 probes, same token cap, 30 solved cases. Metric: decision-step coverage of a gold list from the full trace | Coverage up >= 10 points with no loss of other steps | High |
| E04.06-U4 | Does a notice-strategy-intention step before answering help, and only for strong models? | An optional pre-answer step in S2/S3 for strong models | S2/S3, O | K04, K06; Bridge only (single-source, older models) | Three-field step vs same-length neutral planning step vs none; open-judgement items; strong and weak model. Metric: blind pairwise preference plus score | Strong model +5 pp or +10 points preference vs none and vs neutral step; weak model not worse | Med |
| E04.06-U5 | Do self-written lessons hurt a weak model, and external ones help? | A rule: use external or verified lessons only; gate by model strength | memory, G7 | K20, K03; contested (SkillsBench -8 to -11 pp vs ReasoningBank +4.6 to +8.3) | Self-written, stronger-model-written, curated, none; strong and weak model. Metric: pass rate plus citation check | Self-written below none by >= 2 pp on any model: ban it for that model | High |
| E04.06-U6 | Do random but well-formed lessons hurt (so retrieval must match)? | A relevance gate on lesson retrieval | memory | K05; Bridge random 0.26 vs 0.51 (single-source) | Matched vs random vs none lessons. Metric: pass rate | Random below none by >= 2 pp: require match score before injecting | Med |
| E04.06-U7 | Do failure-derived lessons beat success-derived at equal count? | Prefer failures when mining | memory | K21; d01 (+3.2 pp, AWM -2.2 pp; single-source) | Equal-count failure-only, success-only, mixed, none; two model sizes | Failure-only or mixed beats success-only by >= 2 pp on both models | Med |
| E04.06-U8 | Are claimed cues real? Do they change behaviour when removed? | Cue-removal check before a lesson is stored | G10, memory | K11; d10-d12 (E for faithfulness, untested for lesson cues) | For each lesson cue, remove it from the case and rerun. Metric: fraction of cues that change the answer; held-out gain of verified-only vs all lessons | Verified-only lessons match or beat all lessons at fewer tokens | High |
| E04.06-U9 | How many cases per task type saturate a lesson set, and how many lessons help? | A cap on lessons (2 to 3) and a stop rule for mining | memory | K12; b09 (human interviews 7-10), d05 (2-3 skills +19.0, 4+ +10.1; single-source) | Mine from 1 to 12 cases; vary lessons used 1, 2-3, 4-6. Metric: held-out gain, new clusters per case | Gain at 4-6 lessons below gain at 2-3: set the cap; new clusters per case under 0.2 from case 8: set stop rule | Med |
| E04.06-U10 | Does commit-first ranking before seeing expert reasons beat reading reasons? | A commit-then-compare step when learning from gold traces | memory | K10; a16 (author-run, human-only, d=.63) | Commit-first vs read-only, same tokens; second held-out case. Metric: match to gold cue ranking | Commit-first >= +5 points | Low |
| E04.06-U11 | Can an LLM build cue-action protocols from CDM transcripts as well as human analysts? | LLM analyst for lesson building | memory | K17, K22; codebook application only (d08, d09) | LLM vs 2 humans on 20 transcripts. Metric: blind pairwise preference and overlap, ceiling = human-human | Blind preference >= 45% against humans | Med |
| E04.06-U12 | Does heavy CDM beat cheap extraction only on branching tasks? | Route extraction depth by task type | S0, memory | K19; b14, c24 (no head-to-head) | Cheap vs deep on one branching and one linear task class. Metric: held-out gain per token | Deep wins by >= 3 pp on branching and not on linear | Low |
| E04.06-U13 | Does retrieving cue-action cases beat comparing options on time-pressured items? | Recognition-first retrieval | S3, memory | K18; a02, a03 (author-coded) | Cue-pattern retrieval vs option comparison, fixed budget. Metric: pass rate at low token cap | Retrieval >= +3 pp at the lowest cap | Low |
| E04.06-U14 | Where does the model-strength gate flip for current models? | A strength-based switch for lesson use | G, memory | K03; contested (Bridge vs SkillsBench small model) | Same lesson set on 3 model sizes, procedural-with-check items and open items | Gain sign differs by size on one item type: add gate for that type | Med |

## Open questions we cannot test on our bench yet

- Independent replication of Bridge outside the original group: needs the Bridge data and teacher raters, or a domain with a verifier.
- Corrected surgical effect sizes: needs new large trials or the raw data from the 12 studies; not something our bench can produce.
- CDM reliability coefficients from Klein 1989 and Hoffman 1998: need the full papers (paywalled).
- Forward citations of Bridge and any 2025-2026 LLM-CTA work: needs the Semantic Scholar and OpenAlex APIs once the rate limit lifts.
- Human expert panels for scoring cue lists: our bench has verifiers, not experts; blind LLM-plus-human pairwise review is a stand-in.
- Whether stated cues are the true causes in models: needs counterfactual cue removal per case (see U8); no ready dataset.

## Order to run

1. **U2 (with U1)**: the three-arm content-versus-structure test with irrelevant and role-label controls. It decides whether any CTA content is worth building, and no one has run it.
2. **U5**: self-written versus external lessons by model strength. It is cheap, and the literature conflicts, so a wrong default costs the most.
3. **U8**: cue-removal verification. It is cheap, grounded in strong faithfulness evidence, and may cut tokens by dropping lessons that do nothing.
