# Conceptual change and revolutions: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| D07.05-U1 | Best consecutive-failure count N for the impasse trigger | Fixed default N in S6 | S6, G1 | K29, K19: single-source; Smith uses 5, Reflexion 3; never swept; one preprint | N=1, 2, 3, 5 vs best-of-N one-shot; ARC items with a check plus multi-step puzzles; solved rate, 2 seeds | One N beats best-of-N by 3 or more points and beats N=1 by 2 or more points on 100+ items | High |
| D07.05-U2 | Does a reframe operator beat blind sampling at all | Keep O8 as an operator; otherwise mark it "not to add" in 4b | O8 | K19: Smith 2026 full loop 0.8027 vs best-of-15 0.8463; Kuhn agent not ablated | O8 arm vs best-of-N draws; items that reach S6; solved rate | O8 beats best-of-N by 3 or more points with a 95% CI above zero | High |
| D07.05-U3 | Does "Wait" re-read match a heavy reframe | "Wait" re-read as the default cheap step before O8 | O8, S5 | K27: single-source (Tsui 2025, s1); non-reasoning models mainly | Wait vs heavy reframe vs none; both reasoning and non-reasoning backbones; solved rate and correct-to-wrong rate | Wait gets within 1 point of heavy reframe at under half the tokens | High |
| D07.05-U4 | Does a reframe select guard cap the flip loss | Mandatory select step after every reframe | O8 guard, G5 | K26: three sources (Snell 38%, FlipFlop 10.4%, Self-Contrast 52 -> 11); not tested on our operator | Reframe with and without a select that can keep the first answer; items with correct first answer; correct-to-wrong rate | Loss under 5% with the guard and at least 2x lower than without | High |
| D07.05-U5 | Does the refutation form (name old frame, why it fails, new frame) beat plain retry for LLMs | Refutation-form prompt in O8 | O8 | K09, K28: human-only (g=0.41, trim-and-fill 0.28); Reflexion explain-failure +8% HotPotQA | Plain retry vs explain-failure vs refutation form, same failed-test signal; items that reach S6; solved rate | Refutation beats explain-failure by 2 or more points and plain retry by 4 or more | Med |
| D07.05-U6 | Is a model-judged anomaly useless as a trigger on current models | Confirm G1 numerically; allow doubt triggers only for reasoning models | G1 | K03, K27: contested for reasoning models; Huang older models only | Model doubt vs failed-test count vs consecutive non-improving; mixed items; solved rate and false-trigger rate | Model doubt gains 2 or more points over no trigger on a reasoning backbone, else keep G1 as is | Med |
| D07.05-U7 | Do parallel frames beat one frame retried | K-frames operator with code selection | S3, S4 | K15: established on ARC (17 -> 30) and ACRE (28 -> 59); equal-token control missing in part | K distinct frames each checked on examples vs one frame retried K times; ARC; solved rate | Frames arm beats retry by 3 or more points at equal tokens | Med |
| D07.05-U8 | Does a retired-frame note stop the old claim returning | Retired-frame note and leak check in working state | memory, S6 | K10, K33: human-only (persistence d=0.75 to 1.06); no LLM test found | Multi-turn items with an inserted correction; no note vs retired note; rate old claim reappears | Leak rate falls by 30% or more relative with no loss in accuracy | Med |
| D07.05-U9 | Can Bayesian surprise detect impasse cheaper than a failed check | Surprise signal for tasks with no check | S6 | K17, K32: single-source (AutoDiscovery); costs 2 x k samples plus the experiment | Surprise vs one failed check vs self-consistency disagreement on single-answer items; precision and recall of failure; tokens per signal | Surprise gives equal recall as the best cheap signal at no more than 2x tokens, on items with no check | Low |
| D07.05-U10 | Does an explanatory-coherence tally pick the right frame | Tally of explained minus contradicted items before S7 selection | S5, S7 | K13, K33: contested; ECHO modelled humans; no LLM test found | Two plausible frames with an evidence log; free choice vs tally; selection accuracy | Tally beats free choice by 5 or more points on 60+ items | Low |
| D07.05-U11 | Does restating the task under the new frame fix counterfactual drops | Restate-then-solve step in S1 | S1, O8 | K31, K06: open; Wu shows comprehension check passes while task fails | Direct vs restate-then-solve on counterfactual arithmetic and spatial items; accuracy on counterfactual form | Gain of 5 or more points on counterfactual form with no loss on default | Low |
| D07.05-U12 | Does difficulty routing (cheap draws first, reframe only on unsolved) win | Route reframe by item difficulty | G12, S0 | K30: contested (Snell vs Smith) | Uniform reframe vs routed; mixed difficulty set; solved rate at equal total tokens | Routed beats uniform by 3 or more points | Med |
| D07.05-U13 | Does an outlier check handle one wrong exemplar | Outlier check in S2 | S2, G3 | K16: single-source (Qiu); drops at 12.5, 25, 50% corruption | Inject one wrong example; no check vs outlier-check step; solved rate | Recovers half or more of the drop | Low |

## Open questions we cannot test on our bench yet

- Exact human counts of ignore, reinterpret and change (Chinn and Brewer 1993; Dunbar 1997). Needs the full papers; both publisher pages were blocked. Unblocks a human-informed N for U1.
- Whether the Kuhn agent adds anything inside Smith's loop. Needs the authors' code with an on/off arm or our own re-implementation.
- Whether reasoning models with tools judge their own anomalies reliably on open-ended tasks. Needs an open-ended bench with a ground-truth error signal.
- Whether children's conceptual change and scientists' change share a mechanism (K24). Not testable on an LLM bench.
- Whether LLM context windows show continued influence of a retracted claim. We need a probe set with corrections inserted at set distances (partly U8).
- Bruner and Postman (1949) numbers. Unverified from memory; need the paper.
- Cost of long scaffolds: whether Smith's loss came from context cost (2.5x cache re-reads) or loop design. Needs token accounting per operator in our harness (G12).

## Order to run

1. **U4 flip guard.** Cheapest, and it checks a loss (10-38% of correct answers) that any reframe operator would add.
2. **U2 reframe vs best-of-N.** The decision test: if O8 does not beat blind draws, drop the rest of the O8 trigger work.
3. **U1 trigger count N.** Runs on the same items as U2, so it adds little cost and fills the main gap (no study varies N).
