# Anomalies and paradigm change: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*
## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| D01.05-U1 | Which code-measured trigger best fires S6 without an oracle | The winning trigger as the S6 rule | S6 | K20, d02, d16; single-source, traces only | Arms: plain, residual ratio, 3 flat refits, prediction-miss rate, self-rated; DiscoverPhysics hidden-source and NewtonBench shifted laws; pass rate and tokens to pass | One code trigger beats plain by 5+ points pass rate and beats self-rated | High |
| D01.05-U2 | Is hold-then-replicate better than reframe-at-first-clash for an agent | Replicate-before-reframe default in S6 | S6/O8 | K01 (human, established), K19 (single-source), b01, d06 | Arms: reframe at first clash, method check then reframe after 1 replication, never reframe; dossiers with real anomalies plus noise artefacts and real controls; missed plus false reframes | Replicate-first has lower total error and pass rate no more than 2 points below best | High |
| D01.05-U3 | Does a forced "name one structurally new entity" step raise frame change | Step in O8 after poor residuals | O8 | K09, d01, d02; single-source; HypoArena (d17) warns of prompt swings | Arms: think-longer, forced entity step, refit only; latent-structure worlds plus worlds where frame is right | +5 points pass on hidden-source worlds and false-reframe rate rise under 10 points | High |
| D01.05-U4 | Cost at equal tokens of a K=4 hypothesis population with discriminating experiments and pre-commit | Population (K=4) in S4-S6 | S4-S6/O8 | K08, K22, a19, d04, d05; single-source, episode-matched | Arms: single hypothesis, K=4, K=4 without pre-commit; held-out anomaly worlds; explanation score and pass@1 | K=4 beats single by 8+ points at equal tokens | High |
| D01.05-U5 | Does a derivability check cut wasted reframes | Check before escalating a surprise | S6/memory | K15, a22, b18; single-source | Arms: reframe on any surprise vs only if not derivable from logs; logged runs with injected surprises; wasted reframes and pass rate | Wasted reframes down 25%+ and pass not lower | Med |
| D01.05-U6 | Does requiring a named alternative frame before dropping the old help | "Name alternative first" in O8 | O8 | K16, a05, a07, a09, b10; contested | Arms: drop-first vs alternative-first; frame-overturn set; frame-change rate and false reframes | Alternative-first beats drop-first by 5+ points pass | Low |
| D01.05-U7 | Does showing the 8-type response menu raise true theory change | Response menu in the ledger | S6/O8 | K04, a06, d13; single-source, frequencies unknown | Arms: no menu vs menu with costs; injected anomalies with known truth; true theory-change rate and false-change rate | True rate up 10+ points, false rate up under 5 | Low |
| D01.05-U8 | Does forcing an exploration burst on stalled residual undo strong-model lock-in | Burst rule in S6 | S6 | K14, K21, a24, d03; single-source | Arms: plain, think longer, forced exploration burst after stall; NewtonBench hard settings | Pass up 5+ points for strong models, no loss for weak | Med |
| D01.05-U9 | Does a "list anything conflicting with the template" step stop silent normalisation | Conflict-scan step in S1 | S1/G | K06, d15, a04; single-source, no original | Arms: plain vs conflict-scan; familiar templates with unstated contradictory item; silent-normalisation rate | Rate down 30% relative with no loss on clean items | Med |
| D01.05-U10 | Do side-effect or accident discoveries need their own entry route | Side-effect log in O8 | O8 | K24, d09, d10; secondary only | Arms: anomaly-only vs anomaly plus side-effect log; tasks with a useful side effect; discovery rate | +10 points discovery on side-effect tasks, none lost elsewhere | Low |
| D01.05-U11 | Does a credibility-first rating cut the 2-point believability gap in LLMs | Credibility-first step | G | K03, a10, a07; human-only | Arms: plain vs credibility-first prompt; identical result under opposite primed frames; rating gap | Gap shrinks 50%+ with no loss of accuracy | Med |
| D01.05-U12 | Does a set-breaking cue help after N same-method failures | Cue in S6 | G | K17, c20, c12; contested, no figures | Arms: plain vs cue after 3 same-method failures; Einstellung-style items; steps and pass rate | Pass up 5+ points | Low |
| D01.05-U13 | Does a counter-example prompt help on our own item types, not only 2-4-6 | Counter-example test in S4 | G | K12, b20, c16; established on rule tasks | Arms: plain vs counter-example prompt; ARC-like rule items and 2-4-6 items | +5 points on our items | High |

## Open questions we cannot test on our bench yet
- True paradigm-level anomaly (a held frame overturned): no published set, and we have none. Unblock: build a small frame-overturn set where the obvious frame is wrong.
- Chinn and Brewer 1998 numbers (N, frequencies, factors): full text blocked. Unblock: library access.
- Primary-source check of the oxygen case: needs historians' texts, not agent work.
- Replication of Bruner and Postman: original unread; find the 1949 paper.
- Equal-token EvoSCM cost by part: needs code or our own rebuild (U4).
- Whether residual triggers carry to ARC or brainteaser items, which have a checker but no continuous residual.
- LLM judge bias in DiscoverPhysics scoring: needs a human-checked subset.

## Order to run
1. U1 (trigger ablation): cheap, uses existing worlds, and decides how S6 fires for everything else.
2. U2 (hold versus reframe): decides the default policy at S6/O8; human evidence is established, agent evidence is absent.
3. U13 (counter-example prompt on our items): cheapest, and the only candidate with an established effect to confirm on our bench.
