# Relevance-based fate of memories: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| B04.03-U1 | Does an LLM future-use rating at write time predict real later reuse better than recency or access count? | Rating field used to rank lessons | Memory | K20, K26; no direct test; proxies only | Log each lesson (rating, recency, count, surprise, effort) over 300+ tasks; fit simple model; AUC for "used and helped" | Rating adds >=0.05 AUC over best of recency and count | High |
| B04.03-U2 | Does a "needed for class X when Y" field in the lesson raise later use? | Reuse-condition field in lesson format | Memory | K01, K03, K22; human attention effect established; LLM untested | A: field; B: none; same store; new items of same classes; 2 models; reuse accuracy | >=+3 pp, CI above 0, on both models | High |
| B04.03-U3 | Does outcome-based value (later success) beat LLM-rated value for keeping lessons? | Promote and keep by observed help | Memory | K06, K07; reward half positive in humans; single-source | Same stream; value from outcomes vs from rating; end-task accuracy; share of needed lessons kept | Outcome arm >=+2 pp or keeps >=10 pp more needed lessons | High |
| B04.03-U4 | At what store size does pruning pay, and by which rule? | Prune rule plus size threshold | Memory | K14, K25; contested; sign flips by agent and judge | Caps 50, 200, 1000; keep-all, recency, random, utility-gated; held-out stream; accuracy | One rule beats keep-all by >=2 pp at some size on both models, no loss elsewhere | High |
| B04.03-U5 | Is soft demotion with rescue safer than hard deletion? | Archive plus rescue path | Memory | K17, K24; single-source, no head to head | Hard delete vs demote with rescue; lessons that become needed again; loss rate, accuracy, tokens | Soft loses >=50 percent fewer needed lessons at <=10 percent extra tokens | High |
| B04.03-U6 | Is removing a dropped lesson from context better than a "drop" note? | Remove-not-annotate rule | Memory, G10 | K23; established on synthetic key-value streams | Interference set: note vs removal vs boundary reset; accuracy on current rule | Removal beats note by >=5 pp | Med |
| B04.03-U7 | Does idle-time pre-writing of likely-reuse notes beat the same tokens at test time? | Between-task note step | O, memory | K18; single-source; gain grows with predictability; SWE only at low budget | Equal total tokens; predictable vs unpredictable next task; accuracy | >=+3 pp on predictable items, no loss on unpredictable | Med |
| B04.03-U8 | Do write-time features (failed first attempt, effort, tokens) predict reuse? | Cheap tag from run features | Memory | K11, K26; human theta single-source; agent none | Part of U1 logging; AUC per feature | Any feature adds >=0.05 AUC over recency and count | Med |
| B04.03-U9 | Should weak (low-confidence) lessons be kept if class-relevant? | Keep-untrusted-visible rule | Memory | K10; contested; depends on test difficulty | Keep-strong only vs keep-weak-relevant vs keep-all; accuracy | Keep-weak-relevant beats keep-strong by >=1 pp or ties at fewer tokens | Med |
| B04.03-U10 | Does blind multi-factor value beat uniform on our lessons? | Multi-factor score | Memory | K13; single-source; fitted to gold retention, not use | Fit weights on half the stream; test on held-out half; keep 30 percent; answer accuracy | Beats uniform and recency by >=2 pp on held-out tasks | Low |
| B04.03-U11 | Do abstract lessons transfer where specific ones do not? | Abstraction step before storing | Memory, O2 | K19; single-source, synthetic | Specific vs generalised lesson text; cross-class new items | Generalised >=+3 pp on cross-class items, no loss in-class | Med |
| B04.03-U12 | Does forgetting look free only at moderate load? | Load-stress check in the bench | G7 | K16; ZenBrain, one benchmark | Moderate vs stress decay on each pruning rule | A rule that wins at moderate load still ties at stress; else disable | Low |

## Open questions we cannot test on our bench yet
- Human sleep-specific selection: needs human participants and a pre-registered multi-lab design. Treat as a prior only. A proper meta-analysis (K21) would settle the pooled size (own pool r about 0.10, CI 0.01 to 0.18).
- Third-party reproduction of FadeMem, OBLIVION, SF-AMS and RD-Forget on answer accuracy: needs their code and benchmarks. Unblock by running released code on LongMemEval.
- Xiong 2025 Table 2: Figure 5 not viewed; row pairing inferred from memory sizes. Unblock by reading the figure or asking the authors.
- Fresh sweep of 2026 agent papers for write-time tag tests: search quota ran out. Redo when quota returns.
- Idle-time compute under uncertain future queries: needs a stream with controllable predictability.
- SleepGate-style gates on frontier models: needs open weights and KV-cache access.

## Order to run
1. B04.03-U1 (with U8 logging): costs only logging, answers the most decision-relevant gap, and its data feeds U3, U4 and U10.
2. B04.03-U4 (store-size sweep): decides whether any pruning is worth enabling and guards against the high-load downside.
3. B04.03-U5 (soft vs hard): cheap once U4 runs; sets the safe default for any deletion.
