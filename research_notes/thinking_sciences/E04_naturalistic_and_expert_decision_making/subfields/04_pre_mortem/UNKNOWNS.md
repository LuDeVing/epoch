# Pre-mortem: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| E04.04-U1 | Does a "has failed" frame beat a "may fail" frame for LLM accuracy | Failure-frame wording in the doubt step | G1 / O-check | K01; Mitchell abstract (certainty); contested; InvThink forward control says no (d10) | Same items, same length: "has failed" vs "may fail" vs neutral step; 3 seeds; accuracy and valid causes | "Has failed" beats "may fail" by 2+ points accuracy or 20%+ more valid causes, CI above 0 | Med |
| E04.04-U2 | Is the gain from reasons-against content, not the frame | Plain "list reasons my answer is wrong" step instead of a premortem | G1 | K06; Koriat 1980 (human, numbers unseen); single-source | 2x2: frame x (reasons-against vs neutral list); reasoning items; accuracy and Brier | Content main effect of 2+ points with no frame effect; then adopt the plain version | Med |
| E04.04-U3 | Can a cheap signal gate the step (3-sample disagreement, low P(True)) | Premortem fires only on disagreement or low P(True) | G1 / S-signal | K20; Adaptive-Consistency (d06), P(True) (d07); no premortem-specific test | Never-on, always-on, gated; mixed-difficulty items; accuracy per token and fire rate | Gated within 1 point of always-on and at least 30% fewer tokens, and above never-on | High |
| E04.04-U4 | Does turning named causes into external checks avoid the self-critique drop | Premortem causes become tests or tool calls | O-check | K19 established for critique (CRITIC +6 to +10 F1); not tested for premortem | Internal-only vs external-check premortem vs none; items with runnable tests; accuracy and right-to-wrong flips | External arm beats none by 2+ points and flips no more than 1% right to wrong | High |
| E04.04-U5 | Do stored failure lessons beat or add to imagined failures | Error-pattern memory feeding the check | memory | K13, K18, K21; PreFlect prior worth 7.88 of 12.12; single-source, no head-to-head | Premortem only, lessons only, both, none; multi-episode agent tasks; success over 5 episodes | Lessons or both beat premortem-only by 3+ points over 3 seeds | High |
| E04.04-U6 | Does a pre-action "what could go wrong" plus backup help tool agents | Pre-action failure query before costly tool calls | O-check | K12; Wang 2024 23.5 vs 22.7 vs 19.8; bundled, no ablation | Pre-action query vs post-failure reflection vs none; tool tasks; success and plan revisions | Beats post-failure reflection by 2+ points at equal tokens | Med |
| E04.04-U7 | Does listing causes inflate stated failure probability (Hill's subadditivity) in LLMs | A calibration guard: confidence set from checks, not cause count | G-calibration | K08, K23; human-only (N=32; 78% subadditive) | With vs without failure list; Brier and mean stated failure vs observed error | Stated failure overshoots observed by 0.05+ or Brier worsens by 0.01+ with the list; then add the guard | Med |
| E04.04-U8 | What does a premortem cost in over-hedging on benign items | A false-alarm budget on the step | G1 | K11, K23; InvThink FRR 0.361 (trained, safety only) | Premortem on vs off; items that should be answered; hedge or refuse rate and accuracy | Hedge rate rises 3+ points; then add a hedging cap | Low |
| E04.04-U9 | Does plan complexity or unfamiliarity moderate the effect | Complexity as a gate signal | S-signal | K03; Peabody Exp 2 vs Exp 3 (N=72, 82), human-only, single-source | Premortem effect by difficulty tercile on the T1 items | Gain in top tercile 3+ points higher than bottom tercile | Med |
| E04.04-U10 | Does pooling 3 failure lists beat 1 at equal tokens | Pooled failure lists with recurrence filter | G1 / O-check | K24; self-consistency +17.9 pools answers only | 1 list vs 3 pooled (budget matched, so shorter lists); valid causes and accuracy | Pooled arm beats single by 2+ points at equal tokens | Low |
| E04.04-U11 | Is the BTF-2 pre/post-mortem association causal | A pre/post-mortem rationale dimension in forecasting | O-check | K14; correlational, 3x cost, bundled; contested | Add or remove the dimension in the forecaster prompt; resolved forecasting items; Brier at equal cost | Brier improves by 0.005+ at equal cost | Low |
| E04.04-U12 | Do modern reasoning models still show the self-critique accuracy drop | Keep or relax the "no ungated self-critique" rule | G1 | K09; Huang results are GPT-3.5 and GPT-4, older models only | Re-run Huang-style intrinsic critique on our current model; GSM8K-style and commonsense items | Change from baseline within +/-1 point; then the rule can be relaxed for that model | Med |
| E04.04-U13 | Do the Veinott findings (confidence drop) correspond to better plans | Evidence that human premortem helps plan quality | none (human check) | K02; N=178, means unseen, outcome is confidence only; human-only | Not a bench test. Obtain Veinott 2010 full text and read means and SDs | Paper shows a plan-quality or error outcome, not only confidence | Low |

## Open questions we cannot test on our bench yet

- **Mitchell 1989 full text.** We do not know where the 30 percent comes from or which condition. Unblock: obtain the paper (library access).
- **Veinott 2010, Gallop 2016 numbers.** Means, SDs, effect sizes unseen. Unblock: full texts.
- **Real plan outcomes.** No study links a premortem to real project success. Our bench cannot test this; it needs a field trial with outcome data.
- **Social safety effect.** Irrelevant to one agent, but it is Klein's main stated aim. Would matter only if we add multiple agents or humans.
- **Group vs individual premortem.** One poster, no numbers. Needs human study.
- **Causal test inside BTF-2.** Needs their pipeline and frozen corpus.
- **Wang 2024 ablation.** The anticipatory step alone is not isolated. Unblock: re-implement and ablate.
- **Trained versions (InvThink SFT+RL, CoMem, AUGUR).** We change the scaffold only, so weight training is out of scope.

## Order to run

1. **E04.04-U3 (signal gate).** Tests G1 directly and is cheap. If gating works, every other premortem variant can be tested only where it fires.
2. **E04.04-U4 (external check).** The best-supported direction; decides whether the premortem step is safe at all (Huang vs CRITIC).
3. **E04.04-U5 (stored lessons vs imagined failures).** Largest measured gain in the evidence (PreFlect prior, +7.88 of +12.12), and it decides whether the premortem step is needed once memory exists.
