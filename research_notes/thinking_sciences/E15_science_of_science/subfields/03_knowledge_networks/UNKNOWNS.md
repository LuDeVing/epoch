# Knowledge networks: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*
## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| E15.03-U1 | Does a flat-default, graph-for-temporal/multi-hop router beat flat-only memory? | Query-type router in memory lookup | memory | K14, K18 (established for RAG QA; vendor and neutral studies; not in a scaffold) | Arms: flat; graph; router. Items: our session-memory QA, 3 types. Metric: accuracy by type, tokens incl. build | Router >= flat on lookup and +5 points on temporal/multi-hop, tokens within 10% | High |
| E15.03-U2 | Do distance-2 (shared-neighbour) analogues help reasoning more than nearest-embedding ones? | Two-hop analogue retrieval | memory; S3 | K03 (science only; human-only) | Arms: nearest-k; two-hop-k; half and half. Items: ARC/analogy items with a solved earlier sibling. Metric: solve rate | Mixed arm >= nearest +3 points over 3 seeds | High |
| E15.03-U3 | Does an explore/exploit retrieval mix (85/15) beat greedy retrieval? | Reserved explore slot in retrieval | S3 | K08 (human-only, no direct test) | Arms: greedy; 85/15; 70/30. Items: open-mode and ARC. Metric: solve rate, unique approaches (code-clustered) | Unique approaches +20% with solve rate not lower | High |
| E15.03-U4 | Does a code duplicate filter plus graph-neighbour seeding lift unique-idea share above about 5%? | Seeding and dedupe in open mode | S3 | K10 (single-source, older models) | Arms: bare resample; seeded; seeded plus filter (cosine 0.8). Items: NoveltyBench prompts, 100 samples each. Metric: unique share, NoveltyBench score | Unique share +5 points absolute, quality check pass rate not lower | High |
| E15.03-U5 | Does grounding (retrieved prior results) lift self-ranking of ideas above chance? | Retrieval-grounded ranking step, code-checked | G5/G8 | K11, K21 (53.3% raw; 38.8 to 53.0 with retrieval; fine-tune out of scope) | Arms: raw model ranker; ranker with retrieved prior results; random. Items: pairs with known executed outcomes. Metric: pairwise accuracy | Accuracy >= 58% on 200+ pairs | Med |
| E15.03-U6 | Does a compare-and-rewrite novelty loop raise distinctness without lowering correctness? | Max 2 rounds, code similarity gate | S3 open mode | K12 (single-source, human-rated, older models) | Arms: one-shot; 1 round; 2 rounds. Items: open-mode tasks with executable check. Metric: distinctness (code), check pass rate | Distinctness +30% and pass rate within 2 points | Med |
| E15.03-U7 | Does hub bias exist in agent memory, and does degree-penalised retrieval fix it? | Degree penalty in ranking | memory | K04 (single-source; LLM graphs are sparse, d09) | Arms: plain rank; degree-penalised. Items: 200 stored notes, mixed queries. Metric: share from top 10% degree nodes, solve rate | Hub share >40% in plain arm AND penalised arm gains >=2 points | Low |
| E15.03-U8 | Do temporal edges (valid-from, valid-to) help "current value" questions? | Time-stamped fact edges | memory | K16, d11, d12 (vendor, no flat baseline in Zep) | Arms: flat; flat plus time edges; full context. Items: changing-fact QA. Metric: accuracy, tokens | +10 points on temporal, loss <=3 points on detail | Med |
| E15.03-U9 | Do source and tool edges help a single agent? | "Produced by / checked by" links in notes | memory | K06 (human-only analogy) | Arms: notes without; notes with source and tool tags. Items: reuse of past results. Metric: reuse accuracy, wrong-source reuse rate | Wrong reuse falls >=25% relative | Low |
| E15.03-U10 | Does an avoid-the-crowd penalty (distance from own prior outputs) raise novelty without losing correctness? | Distance-from-own-history term in selection | S3/S7 | K07 (human-only; established in science) | Arms: no penalty; penalty; random. Items: NoveltyBench plus checkable tasks. Metric: novelty, correctness | Novelty +15%, correctness within 2 points | Med |
| E15.03-U11 | Do embedding dot-product rankings of unseen candidates beat keyword retrieval for analogues? | Embedding ranking of analogue pool | memory | K05 ("8 times" figure unverified) | Arms: keyword; embedding; random. Items: held-back analogues. Metric: recall@5 | Recall@5 +10 points | Low |
| E15.03-U12 | Is graph memory worth the build tokens at our memory size? | Gate: build graph only above a size threshold | G7 | K19 (established for 11k passages) | Arms: flat vs graph at equal total tokens incl. build, at 100, 1k, 10k notes. Metric: accuracy per token | Graph wins at some size; record the break-even | Med |

## Open questions we cannot test on our bench yet
- Independent replication of the ideation-execution gap outside NLP: we have no executed-idea corpus. Unblock by building executable-idea tasks with auto-checks.
- Cheap check separating useful from merely novel ideas: needs outcome-labelled ideas (Wen's pairs could seed it).
- Tshitoyan "8 times" figure and non-materials embedding ranking: need the Nature full text and a non-materials corpus.
- Graph vs compression in Zep: needs a flat-vector baseline at the same token count.
- Does the 85/15 ratio hold in LLM search? Needs the U3 sweep first.
- People-aware graphs: no multi-agent setting in our design, so only the source-edge analogue is testable.

## Order to run
1. U1 (router): cheapest, the best-supported effect, decides whether any graph is built at all.
2. U4 (dedupe and seeding on NoveltyBench): we already have the bench and a known weak spot (3.18 to 9.63 shows headroom).
3. U2 (distance-2 analogues): the main unanswered gap and the one thing the science supports that no LLM study tests.
