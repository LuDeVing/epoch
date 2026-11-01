# Planning-performance research: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| E17.04-U1 | Does a short plan step beat direct answering on current models for open-ended judgment? | Plan-first step in S1/S2 for multi-step items | S1-S3 | K09, K12 (older models, math/code); K21 against (CoT hurts some tasks) | Direct vs 150-token plan then answer; 100+ judgment and multi-step items; paired accuracy | Gain of 2+ points, CI above 0, no loss on easy items | High |
| E17.04-U2 | How many options before selecting is enough on open tasks? | An option-count rule (N by difficulty) | S3 | K20 (code with checker); K17 unread (single-source) | N=1, 3, 6, 12 with code selection; items with a checker; pass rate and distinct families | Knee found; N>3 beats N=1 by 3+ points | High |
| E17.04-U3 | Do separate calls plus dedupe give more distinct options than one list? | Separate-call generation with similarity dedupe | S3 | K16 (Meincke; GPT-4 era; human comparison) | One call listing N vs N calls; items with panel or checker score; distinct-family count and score | 20%+ more distinct families and score no lower | High |
| E17.04-U4 | Can an aggregated selector replace a checker for business-type options? | Mean of 5+ shuffled judge calls in code as fallback selector | S7, G5 | K23 (crowd match is human comparison; Doshi abstract only, single calls inconsistent) | Single self-pick vs fresh judge vs mean of 5 shuffled vs checker; items with expert key; top-1 agreement | Mean of 5 beats single judge by 5+ points | High |
| E17.04-U5 | Does difficulty-scaled planning budget work outside math? | Budget tiers by difficulty probe | G12, S0 | K22 (math, PaLM 2-S* only); K03 (human firms) | Flat vs tiered at equal total tokens; mixed-difficulty set; accuracy | Tiered beats flat by 3+ points, or ties at 25% fewer tokens | High |
| E17.04-U6 | Does a binding "options compared" field improve answers? | Required field naming options and the reason for the choice | S7 | K19 (human survey only) | With vs without field; decision items; accuracy and unsupported-answer rate | Unsupported answers drop by a third, no accuracy loss | Med |
| E17.04-U7 | Does a hypothesis-and-test step before committing help? | State claim, cheap test and flip rule before acting | O verify, S8, G2 | K05 (humans; same research group; replication running) | Plan-then-act vs hypothesis-and-test; forecasting or diagnosis items; accuracy and Brier | Gain of 2+ points where the test is runnable | Med |
| E17.04-U8 | Is replanning on failure better than a fixed plan, without training? | Replan trigger tied to failed checks | S6 | K13 (contested; trained planner) | Fixed vs replan after failed check; multi-step items; 5+ seeds; success and minimum | Success up 5+ points and minimum no worse | Med |
| E17.04-U9 | Does an outside-view (reference class) step reduce estimate bias? | Base-rate step for estimates | G, memory | K06 (single-source; human students) | Inside view vs reference class first; duration and quantity items; log error and calibration | Error down 10%+ | Med |
| E17.04-U10 | Does verifier back-prompting beat plain resampling at equal N, and where does it fail? | Back-prompt with checker output | S4, G2 | K11 (single-source; older models; fails when proposer lacks a foothold) | Resample vs back-prompt; constraint items; pass rate by base-success bin | Higher pass rate when base success is over 20% | Med |
| E17.04-U11 | Do aggregated LLM strategic rankings correlate with experts? | Use aggregated judging for strategy items | S7 | Doshi abstract only; correlations unread | Rank 60 business-model-like options by experts vs mean of 5 calls; Spearman | rho above 0.5 for the aggregate, 0.15 above a single call | Low |
| E17.04-U12 | Does a stakeholder step help on multi-party tasks? | Stakeholder listing in S1 | S1 | a01 (moderator claim only, no test) | With vs without stakeholder list; multi-party items; accuracy | Gain of 3+ points | Low |

## Open questions we cannot test on our bench yet
- Pooled effect sizes (r, CI, I2) of the business meta-analyses and their publication-bias tests. Missing: full text (Wiley, SSRN, JSTOR blocked). Unblocked by institutional access.
- What the founding comprehensiveness studies found, and whether the effect reverses in unstable environments. Needs the primary papers.
- Whether LLM option generation changes real firm decisions or outcomes. Needs field data we do not have.
- Long-horizon business outcomes for LLMs: Vending-Bench-style runs need 5+ seeds and the minimum reported.
- Strategy tasks with no ground truth: no verifier substitute is validated. A panel-scored item set with an expert key would unblock it.
- The conflicting o1 Mystery Blocksworld figures (52.8% vs 74.3%) need a matched rerun.
- The independent Uruguay replication of hypothesis-testing training finishes Sept 2026.

## Order to run
1. U1 (plan-first vs direct): cheapest, biggest uncertainty, and it decides whether S1/S2 keep a plan step.
2. U4 (selector without a checker): decides how S7 works on every item with no ground truth; G5 and G8 depend on it.
3. U2 with U3 (option count and separate-call generation): tests the subfield's core claim, comprehensiveness, directly on S3.
