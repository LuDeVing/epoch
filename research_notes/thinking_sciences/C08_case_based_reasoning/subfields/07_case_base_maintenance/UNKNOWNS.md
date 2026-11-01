# Case-base maintenance: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| C08.07-U1 | Does add-if-verified with deletion beat a plain fixed-size window on non-agentic reasoning items? | Verified-write gate plus capped bank as the default S9 rule | memory, S9 | K01, K02; single-source (Xiong, GPT-4o-mini, 4 agent tasks); d04 partly | Arms: add-all, fixed 20-lesson window, add-if-verified; 300+ item stream, 3 seeds; held-out accuracy and prompt tokens | Verified beats fixed by >= 3 points with interval excluding 0, and add-all is no better than fixed | High |
| C08.07-U2 | How accurate must the retain judge be? Xiong and ReasoningBank disagree | A rule: gate on verifier/code only, or allow a judge above accuracy X | memory, G5 | K03 contested; d18, d19, d10 | Retain judge: verifier, cross-model judge, self-judge, none; plus simulated 100/80/60% accuracy; same stream; accuracy | Self-judge arm is within 1 point of verifier (then allow it), or below fixed (then forbid it) | High |
| C08.07-U3 | Does outcome-based (history) deletion of lessons beat no deletion at a fixed cap? | Per-lesson win/use counters and a delete rule (n>=5 uses, win rate below threshold) | memory | K04, K05; single-source, mixed: helped 2 of 4 agents | Cap 50; arms: none (FIFO), history deletion, periodic, random; 1000-item stream; end accuracy | History beats random and FIFO by >= 2 points on at least 2 task types and loses on none | High |
| C08.07-U4 | Do competence rules (protect pivotal, delete auxiliary/support) transfer to LLM lesson banks with embedding coverage? | Competence-aware eviction with a probe set | memory | K07, K08, K27; 1995 toy domain; coverage only used at query time (d11, d12) | Cap 50; competence-based vs history vs random vs recency; probe set of 100 held-out items; accuracy and share of pivotal kept | Beats history-based deletion by >= 2 points, or matches it with no usage log | Med |
| C08.07-U5 | Delta update vs full rewrite of the notes file | Mandatory delta-with-code-merge for any lesson store | memory, S9 | K14; single-source (ACE, one collapse event) | Same model edits notes over 200 steps; arms: full rewrite, delta + code merge; accuracy and notes length per step | Rewrite shows a drop of >= 5 points or length loss >= 50% at any step in >= 1 of 3 seeds | High |
| C08.07-U6 | Failure lessons vs success-only under a size cap; what share of failures to keep | Store distilled failure lessons in a fixed share | memory | K15; single-source; d04 conflicts for raw failures | Failure share 0/25/50% as distilled lessons; raw failures as extra arm; equal tokens; accuracy | Some failure share beats 0% by >= 2 points and raw failures do not | Med |
| C08.07-U7 | Does in-place revision of a lesson on failure beat append? | Revise-on-failure operator for lessons | memory, S5/S9 | K12; single-source (Memp, +0.7 reward) | Arms: append, success-only, revise in place; same stream; accuracy and steps | Revise beats append by >= 2 points | Med |
| C08.07-U8 | Does neighbour-consistency cleaning help a bank with wrong lessons? | Local filter at retain time for free-form items | memory | K25; Gao +13.8 to +18.8 EM on 7B models; Min shows no effect on classification | Inject 20% wrong lessons; arms: none, neighbour filter, history deletion; reasoning vs classification items; accuracy | Filter recovers >= 50% of the loss on reasoning items | Med |
| C08.07-U9 | Is there swamping at 10x to 100x bank size? Does dedup fix it? | Dedup/size trigger in code | memory | K17, K29; no accuracy data beyond about 3k; speed flat (d13) | Grow bank with verified plus synthetic near-duplicates to 1k/10k/100k; retrieval precision at k and accuracy; dedup on vs off | Accuracy falls >= 3 points between sizes and dedup recovers >= half | Low |
| C08.07-U10 | Do decay, usage or heat eviction beat recency or no forgetting? | Replace FIFO with the winner | memory | K22, K30; no ablation anywhere (MemoryBank, SAGE, MemoryOS) | Cap 50; recency, Ebbinghaus decay, heat, none-with-top-k; accuracy | One beats recency by >= 2 points on two streams | Low |
| C08.07-U11 | Does curation help only through its extra tokens? | Keep the curator step only if it pays | memory, G7 | K10, K11; single-source; AIME 2024 has 30 items | Raw history, retrieval-only, curated notes at the same prompt tokens; 100+ items, 3 seeds | Curated beats both raw arms by >= 3 points with interval excluding 0 | Med |
| C08.07-U12 | Does lesson abstraction by rules equal abstraction by the LLM? | Cheap rule-based lesson template | memory | K18; AWM rule vs LM gap 0.1 on WebArena | Rule template vs LLM-written lessons; equal tokens; accuracy and cost | Within 1 point and cheaper | Low |
| C08.07-U13 | Is a plain top-k over all cases as good as any pruned bank on reasoning sets? | Keep plain retrieval and skip pruning for small banks | memory | K24; Evo-Memory ExpRAG about equal to the best evolving method | Plain top-4 over all verified cases vs pruned bank, same k; AIME/GPQA slice | Pruned gains < 1 point (then do not prune) | Med |
| C08.07-U14 | Fixed cached lesson set vs per-query retrieval at equal tokens | Simpler cached set per problem class | memory | K26; Bertsch gap 51.5 to 4.9 points; human-era, text classification | Cached class-level set vs per-query retrieval; class-structured stream | Cached within 1 point of per-query | Low |

## Open questions we cannot test on our bench yet

- Reproduction of Xiong's design on a stronger backbone and a different agent family: needs agent tasks with long streams (2000+ runs) and ground-truth outcomes; our bench streams are shorter.
- Original numbers of Minton (1990) and Francis and Ram (1993): papers not found online; needs library access. Without them the utility-problem mapping to token cost stays an analogy.
- Leake and Schack exploration-versus-exploitation maintenance (ghost cases): only the title was seen; need the paper to know what to implement.
- Delany and Cunningham case editing and Brighton and Mellish ICF as such on LLM banks: need their algorithms read in full, then an implementation.
- Banks of tens of thousands of cases: our agent does not produce them; needs a synthetic generator that keeps realistic near-duplicate structure.
- Judge accuracy at 2026 frontier scale: all judge-sensitivity data are from small or mid models; needs a bench stream with ground truth and a controllable judge noise.
- Competence at scale: exact "solves" matrices need |bank| x |probe| model calls; needs a cheap estimator, or an embedding proxy validated against the exact matrix on a small bank.
- Distribution drift: Delany and Cunningham-style concept drift in a stream; our bench items are i.i.d. per class, so it cannot show it.

## Order to run

1. C08.07-U1 (verified write vs add-all vs fixed window): the largest effect in the literature (up to 25 points) and the only one that decides whether the S9 retain rule is a gate or an append.
2. C08.07-U2 (judge accuracy): settles the Xiong versus ReasoningBank dispute, and it reuses the same stream and logs as U1 at one extra arm per judge.
3. C08.07-U5 (delta vs rewrite): cheapest test, largest single-event loss (accuracy 66.7 to 57.1 in one step), and it fixes how every later memory test is run.
