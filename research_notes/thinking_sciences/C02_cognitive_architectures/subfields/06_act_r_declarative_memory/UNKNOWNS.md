# ACT-R: declarative memory: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

All tests use one shared replay (about 80 memories, 20 sessions, 100-200 questions, graded reuse, some one-off exceptions and stale facts; claim K29). Arms get the same token budget. Use 400+ items or paired replays (K30) and 3 seeds. "Delta" is a paired difference in answer accuracy unless stated.

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| C02.06-U1 | Does a use-count / base-level term on top of recency + importance + cosine raise retrieval accuracy? | Score = cosine + importance + ln(sum of age^-0.5) over logged uses | memory | K06, K07, K22; Hou 2024 single-source, 10 author tasks (b15) | Arms: cosine; Park; Park + base level; ACT-R B + cosine. Replay with graded reuse. Metric: accuracy, NDCG@5 | Park + base level beats Park by 2 points or more, paired p < .05, and does not lose on never-reused items | High |
| C02.06-U2 | Is a power-law decay better than exponential at ranking in an agent store? | Choose the winning form as the recency term | memory | K02, K24; contested in humans (b02, d10); no LLM test | Same score, three forms (power, exponential, stretched). Metric: held-out NDCG@5 | One form wins by 1 point NDCG or more over the others on 2 stores; otherwise keep the simplest | Med |
| C02.06-U3 | Which clock: wall time, turns, or intervening memory events? | Age measured in events (or turns) | memory | K05, K23; human slowed clock (a12), single-source; five papers, five clocks, no comparison (d15) | Replay with idle gaps between sessions. Three clocks. Metric: NDCG@5 and accuracy | Event or turn clock beats wall time by 1 point or more on sessions with long gaps; no loss elsewhere | High |
| C02.06-U4 | Does ranking by activation without deletion beat deleting low-activation items? | Rule: scores only reorder and cap; never delete | memory | K12 established that aggressive deletion hurts (a25); K26 rank vs delete untested (d07, d09) | Same store: rank-only, delete-below-threshold, neither. Same token cap. Metric: accuracy, store size | Rank-only is at least equal to neither, and delete loses by 2 points or more | High |
| C02.06-U5 | Should a use count only when the memory is cited in the final answer? | Increment on cite, not on retrieve | memory, logging | K27; one abstract, ALFWorld, 5.9% marginal help (d13) | Replay with distractor memories retrieved often. Count-on-retrieval vs count-on-cited. Metric: accuracy in later sessions | Count-on-cited beats count-on-retrieval by 1.5 points or more | Med |
| C02.06-U6 | Can any scoring handle announced exceptions to a habit? | Add a goal or explicit-statement boost to the score | memory | K25; one item (Hou Task 0, d06); both scorers failed | 20 exception items with matching habits. Arms: Park, base level, base level + statement boost. Metric: accuracy on exceptions; accuracy on habit items | Boost fixes 50 percent or more of exceptions with no drop of more than 1 point on habit items | Med |
| C02.06-U7 | Does spacing-aware counting help an agent (bursty uses counted once)? | Gap-gated use count (count a use only after a gap or new session) | memory | K03; established in humans (a04, a08, b08); never tested in an LLM store | Items with equal counts, bursty vs spread. Plain count vs gap-gated. Metric: recall at long lag | Gap-gated beats plain by 2 points on spread items and ties on bursty ones | Low |
| C02.06-U8 | Does a fan penalty on shared cues help retrieval? | Divide cue weight by number of memories sharing the cue | memory | K10; SYNAPSE ablation 25.9 to 16.8 on open-domain (d01); same authors, one benchmark | Queries with cos < 0.3 and crowded cues. Cosine vs cosine + fan. Metric: accuracy; NDCG@5 | Gain of 2 points or more on low-similarity queries, no loss overall | Med |
| C02.06-U9 | Is the SYNAPSE-style time-aware gain real beyond a newest-is-right benchmark? | Time-aware spreading as an optional re-ranker | memory | K10; same-author replication on three backbones (d02); temporal bias (c08) | Benchmark with items where the older fact is right. Leak/time edges on vs off. Metric: F1 split by newer-right vs older-right | Gain on newer-right with a loss of at most 1 point on older-right | Low |
| C02.06-U10 | Does cosine-only already capture most of what base level adds? (parity result for priming, b20) | Skip the base-level term if gap under threshold | memory | K15, K11; cosine 73.4% vs BM25 (c06) | Cosine vs cosine + base level on first-use-heavy streams (under 30 percent repeats) | Base level adds under 1 point on low-repeat streams: record "use only when repeat share is over 70 percent" | Med |
| C02.06-U11 | Does the gain depend on the repeat share of the stream? | A rule to switch the base-level term on by measured repeat share | memory, S0 | K17; music, 72-89% repeats (c13) | Three replays with repeat share 20, 50, 80 percent. Metric: gain of U1 arm per replay | Gain grows with repeat share (slope above 0) and is below 1 point at 20 percent | Med |
| C02.06-U12 | Is practice-dependent decay (Pavlik-Anderson) needed? | Add the extra parameter | memory | K04 contested (b03, b04 against; a09 for) | Fit constant d vs activation-dependent d on the replay log. Metric: held-out NDCG@5 | Adaptive decay beats constant by 1.5 points NDCG on two stores | Low |
| C02.06-U13 | Do results hold at d in {0.3, 0.5, 0.7}? | Default d = 0.5 with a stated range | memory | K16, K28; SYNAPSE 40.0/40.5/38.1 (d03); OBLIVION non-monotone (d07) | d sweep on U1 arm, 3 seeds | Spread across d is below seed noise (about 2 points); otherwise tune d on held-out items | Low |
| C02.06-U14 | Does a token-cost win exist even if accuracy ties? | Use activation to cap memory tokens | memory, G7 | K14; OBLIVION 73% cost cut at 1.6 points (c11); CAMeR 83.2% (c10) | Measure tokens to correct answer: all retrieved vs top-k by activation | Same accuracy within 1 point at 30 percent fewer tokens or more | High |

## Open questions we cannot test on our bench yet

- A published, answer-level benchmark with graded reuse and exceptions. CAMeR scores weights only; LoCoMo and LongMemEval cannot test use history (K13, K29). Unblock: build the replay described above, or extend CAMeR with questions.
- What Honda et al. 2025 measured (abstract only, no numbers; d05). Unblock: full ACM text (403 this session) or a contact route.
- SYNAPSE on another benchmark by other authors (K10). Unblock: public code and a benchmark with older-fact-right items.
- Whether the Rocchi passenger-credit result generalises beyond ALFWorld (abstract only; K27).
- Power vs exponential in humans: Averell & Heathcote 2011 and Murre & Chessa 2011 not opened (K02, K24). Unblock: institutional access.
- Whether practice slows decay in declarative recall of the kind an agent stores (K04). Rivera-Lares had floor effects at 1 week; no replication with longer delays.
- Noise parameter sweep: none found (K28).
- Whether a real ACT-R engine (pyactr) under an LLM beats a re-implemented formula (Sievers & Russwinkel 2025, a24, no evaluation).

## Order to run

1. C02.06-U1 (use-count / base level on Park): the core question; everything else reuses its replay.
2. C02.06-U4 (rank vs delete) and C02.06-U14 (token cost): same replay, cheap, and they decide whether decay may touch the store at all.
3. C02.06-U3 (clock: wall vs turns vs events): same replay, cheap, and the choice changes how every other term is computed.
