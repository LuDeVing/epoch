# Critique: A10.03 Chunking and templates

## Corrections made (re-opened this session)
1. Sala and Gobet 2017 (PMC full text): r=.41 CI [.29,.51], k=28, N=903, I2=63; trim-and-fill .29 [.17,.41]; games .42, music .69, programming .36, sports .30, other .24; k=26 gives .39. CONFIRMED. An earlier abstract gives .42; cite .41. The domain moderator test is only p=.069 and sports/other CIs include 0.
2. Pleiss et al. 2026 (arXiv 2601.16823, abstract and HTML): direction confirmed, gain per reasoning token falls with unfamiliarity (about -50% near, -89% random relative to familiar). The 4.75x and 7.79x centipawn ratios are main results, confirmed. CORRECTION: c04's "22.55% per 1,000 tokens" is a relative figure and the paper's per-token units are unclear (0.99 / 0.49 / 0.11 per 1,000). Use the ratios only. The abstract phrase "decreases with distributional proximity" is easy to misread; it means gain is larger for familiar positions.
3. Berlot-Attwell 2024 (arXiv 2410.20274, ar5iv): 1,233 lemmas (about 6%) in final prompts, one lemma reused once, TroVE 15 functions in 3 of 7 splits, 3 reuses in 3,201 questions. CONFIRMED. Added: authors credit self-correction and self-consistency for gains; the no-reuse ablation beat TroVE on 3 of 4 splits (2 significant). b23 understated this.
4. Voyager (arXiv 2305.16291): 3.3x items, 2.3x distance, 15.3x faster CONFIRMED; random curriculum -93%, no self-verification -73% confirmed. CORRECTION: GPT-4 vs GPT-3.5 is 5.7x more unique items. Library-removal numbers sit in a figure, so "plateaus late" is qualitative only.
5. Not re-opened (rate limits, OpenAlex blocked, time): Chase and Simon 1973 numbers, Gobet and Simon 1996/1998, Gong 2015, Gathercole 2019, fingerprint, bridge, fMRI, AWM, BoT, LILO, DreamCoder. These rest on the evidence agents' reading and are not independently confirmed here. Only 4 of the planned 10 sources were re-opened.

## Contradictions
- Chase and Simon 1973 found no skill effect on random boards (N=3); pooled later data show a small effect (about 1 piece per 400 Elo). Small-N noise explains it.
- Chunk size: master largest chunk about 5 (1973) vs 14-17 (computer display, 1998/2004) vs 4.6 (Gong 2015). The measure, not the person, drives the number.
- a05's first-chunk 3.8 is from a secondary citation; the 1998 replication found larger chunks.
- Capacity: Miller 7 vs Cowan 3-5; presentation time also moves it (b21).
- Library learning: Voyager, AWM and BoT report gains; Berlot-Attwell finds near-zero reuse in math. Domains differ and no positive study runs a reuse ablation.

## Weak spots
- Almost all LLM evidence is single-source, paper-reported, with unequal token budgets. None compares library vs no library at equal tokens.
- No LLM study runs the true Chase-Simon recall contrast (c24); the chess paper is a proxy measuring move quality.
- Seen only in abstracts or snippets: b25, b26, b27, b28, c25, c26.
- Template theory rests mostly on one lab (Gobet group); independent replication is thin.

## GAPS
1. At equal total tokens, does a subgoal library beat no library on our agent, and is the gain from reuse (zero-reuse ablation) rather than self-correction?
2. What library granularity (single step, 3-5 step chunk, parametrised template) maximises hit rate and accuracy? Human chunk-size data are method-dependent.
3. Does retrieval survive surface changes (paraphrase, reorder), given human chunks are location and format specific?
4. How should thinking-token budget scale with task familiarity or library hit, given Pleiss's falling gain per token?
5. Is there any LLM study of Chase-Simon recall (meaningful vs shuffled structured input) or span with chunked vs unchunked input, 2023-2026?
6. Do templates with slots (Gobet-Simon) beat fixed chunks for LLM agents? Any test of slot-filled routines vs static ones?
7. Library maintenance: when do stale or wrong chunks hurt (case-base maintenance link)? Any measured harm from large libraries?
8. Do named and documented chunks beat code-only ones across tasks (LILO is three domains only)?
9. Does chunk advantage transfer across domains (S.F. letters stayed 7)? How domain-bound must a library be?
10. Independent replication of Pleiss et al. on other model families and non-chess domains.

## Gap search results (2026-11-01, evidence_d.jsonl d01-d17, claims K20-K28)
Search was hard-limited: WebSearch budget used up, arXiv/Semantic Scholar/OpenAlex rate-limited (429). Sources were found via one arXiv search page that worked early, then opened as full PDF text (pdftotext). Coverage is therefore partial.

1. Equal-token library vs none: PARTLY CLOSED. ReasoningBank (d03, d04): +4.3% tokens for +20.5% relative success; no-memory best-of-5 is 42.2 vs memory single run 49.7 (WebArena-Shopping). Still no zero-reuse ablation anywhere, so reuse vs self-correction stays OPEN. SkillEvolBench (d06) adds that raw-trace replay often beats distilled skills.
2. Granularity: PARTLY CLOSED. No single best size. Mixed granularity beat flat (ALFWorld 51.31 vs 47.14; d08); best skill length varies by model, and Qwen3-8B was hurt by every skill level (d09). Single step vs 3-5 chunk vs template was not swept directly: OPEN.
3. Surface-change robustness: PARTLY CLOSED. Wording-only retrieval fails; structure signal worth 6.5 points (d10). No direct paraphrase/reorder test of chunk retrieval: OPEN.
4. Token budget vs familiarity: CLOSED in direction. v3 of Pleiss: 3,426 / 11,800 / 16,953 tokens; gain per 1,000 tokens 22.55 / 7.23 / 3.81% (d13). This corrects the critique's earlier "-50%/-89%" figures (older version). Rule for the agent not tested.
5. LLM Chase-Simon recall or chunked span: OPEN. Only Gong 2023 n-back (abstract, d15) found; searches for chunking studies were blocked, so absence is not proven.
6. Slots vs fixed chunks: OPEN. SkillMigrator and PolySkill use slot templates (d11) but no controlled slots-vs-none contrast was found.
7. Maintenance and harm: CLOSED for direction. Add-all loses to a small verified memory in 4 of 4 agents (d01); wrong items spread by copying (d02); more retrieved items hurt, 49.7 to 44.4 (d05); big libraries cut ESR 35.6 to 27.8 (d07); validation gate removal 56.5 to 42.5 (d12). Staleness over time is not isolated.
8. Named/documented vs code-only: OPEN. ASI favours verified programs over text (d16); MASA shows length must fit the model. No documented-vs-undocumented test beyond LILO.
9. Domain transfer: OPEN. Libraries transfer across agents (d17) and across sites with structure keys (d10); cross-domain limits not measured.
10. Independent replication of Pleiss: OPEN. Only the authors' own Claude Opus 4.6 and Gemini 3 Flash extension (d14), chess only.

Notes: all new LLM results are paper-reported by the authors, not independently reproduced. d16 and d17 are abstract pages only; the SkillWeaver first author was not verified. The SELM no-skill baseline (30.0 vs 36.43) is ambiguous in the text.
