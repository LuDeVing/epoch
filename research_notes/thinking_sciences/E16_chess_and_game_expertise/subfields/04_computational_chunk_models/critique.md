# Critique: E16.04 Computational chunk models (cross-check)

## Re-checked numbers (10 most important)
Re-opened this session (arXiv abstract pages, Crossref, Europe PMC):
1. Ruoss et al. Lichess blitz Elo 2895 vs humans, 270M, no search: CONFIRMED (abstract).
2. Karvonen skill vector raises win rate "up to 2.6 times": CONFIRMED (abstract). Detail figures (69.6% vs 16.7%) not re-opened.
3. HiAgent: "twofold increase in success rate", 3.8 fewer steps: CONFIRMED (abstract). 21% to 42% consistent.
4. Schultz et al.: grandmaster-level chess with search, human-like budget: CONFIRMED qualitatively; Elo 2923 and +68 not re-opened.
5. Sala & Gobet meta-analysis exists, moderate significant correlation, effect in nearly every study: CONFIRMED. The value r=.41, k=28, N=903 could NOT be re-verified (formula stripped in abstract). Treat as unverified.
6. Gobet & Simon 1998/2000, Gobet & Waters 2003, Chase & Simon 1973 figures: NOT re-opened (PDFs not fetched; Semantic Scholar rate-limited). They stand on the original agents' reading (opened:true).

## Corrections and flags
- b24 and c22 are the same HiAgent paper. The real authors are Hu et al. (2024); "Zhang et al." in b24 is wrong. Count as one source.
- b20, c11, c12 are the same Karvonen paper; a10/a11/b04/b26/b27 are one Gobet & Simon (2000) paper; a06/a07/a08/a09 one 1996 series; a16/b08/c04 overlap. Independent-source counts in claims.jsonl use this.
- Karvonen inconsistency: c11 gives 64% win rate for the 16-layer model, c12 gives 69.6% for the standard board. Likely different evaluation settings (not resolved). Do not quote one without the other.
- b22 McGrath et al. is dated 2021 (preprint) but is PNAS 2022; c09 author name garbled ("Jon-and"); c20 "ICLR 2026" venue unchecked.
- a01 says master recall 16 of 25 pieces; a04 says ~93% for masters; these are different studies (Chase and Simon sample vs summary of de Groot). Not a contradiction but easy to mix up.
- Chunk-size estimates conflict: 1973 master largest chunk about 7 pieces (a05), 3.8 first-chunk in middle game (a01), vs 16.8 in 1998. Cause: display method (hand placement limits) and more players.

## Contradictions between sources
- Random positions: Chase & Simon 1973 found none; all later work (a10, a14, a15, b03, b10, b12) finds a small positive effect, about one piece per 400 Elo (b03). Resolved in favour of small effect; the 1973 null was one master, tiny N.
- Number of chunks: Chase & Simon claimed constant; a01 itself and a10 show it rises or humps; b11 (Gong 2015) finds no correlation with rating at brief views. Contested.
- Chunk store size: 2,500 (Holding) vs 50,000 vs 300,000 (c26). No direct measurement.
- Semantic effects (b06): chunking needs an added link to semantic memory; pure chunk models fail alone.

## Weak spots
- Founding data are N=3 (a01/a02). Most CHREST validation is by Gobet's own group; few independent replications (Gong, Ericsson & Moxley 2015 is the main one).
- Small samples in training studies (N=2: a16, b08, c04).
- CHREST fit used parameters inherited from EPAM; model underestimates Master recall (b26).
- LLM evidence is indirect: board-state probes, searchless play, and memory-management agents. None tests chunk theory on an LLM (b25, K22).
- HiAgent's gain is vs full-history baseline, not vs other summarisation schemes; the link to chunking is by citation of Miller, not by test.
- Many c-entries (c08, c09, c16, c17, c18, c23, c24, c25) have no numbers (abstract only).

## Seen only in snippets or second-hand
a23, a24, a25, a26, b18, b19 (opened:false); b09 (Saariluoma & Laine, Ericsson & Harris read via Gobet & Jackson); c07 exact accuracy; Linhares & Freitas 2010 critique content never read.

## GAPS
1. Does a game-vs-scrambled recall test on an LLM (long-context case recall: structured vs shuffled facts) show a small residual skill effect as chunk theory predicts, and how does it scale with model size?
2. At equal tokens, does a chunk-with-slots (template) note format beat flat note lists for multi-fact retrieval and reuse in our agent?
3. Does summarise-on-subgoal-close (HiAgent style) replicate in our scaffold, and does it beat other summarisers at equal context budget?
4. What is the right working-set cap for an LLM scaffold (3-4 chunk units per the human and CHREST fits) and does exceeding it hurt?
5. Do the Sala & Gobet numbers (r=.41, k=28) and Gobet & Simon 2000 curve constants hold on re-reading the full papers?
6. Is LLM memory location-specific (order/format sensitive) the way human chunks are (mirror/quadrant tests), and does order randomisation hurt retrieval?
7. How many reusable patterns does a library need before search depth gains flatten (CHREST SEARCH curve: ~2.5 plies at 1,000, over 5 at 100,000 chunks)?
8. Can a chunking model such as CogAct or CHREST matched to an embedding retriever on classification (85% opening task) at equal tokens?
9. What explains the Karvonen 64% vs 69.6% discrepancy and does the random-board collapse (16.7%) transfer to non-chess LLM tasks?
10. Are there independent (non-Gobet-group) replications of template theory beyond Gong et al. 2015 and Saariluoma & Laine?

## Gap search results (2026-11-03, evidence_d.jsonl d01-d18)
Search limits: the WebSearch budget was already used up, OpenAlex, arXiv search and Semantic Scholar were rate-limited. Work used Europe PMC, arXiv abstract/PDF pages, local copies of earlier papers.

1. Structured vs shuffled recall on an LLM: STAYED OPEN. No direct study found. Nearest analogues: Karvonen random-start chess (scale adds 20 points on standard boards, 1 point on random starts; d03), CHESS-WORLD-MODEL random-play split (d16).
2. Template (slots) vs flat notes at equal tokens: STAYED OPEN. No study found.
3. Summarise-on-subgoal-close: PARTLY CLOSED. Independent Context-Folding (d09) beats a summarise-when-full agent at equal 32K context, but the prompt-only margin is small (0.420 vs 0.386 on BrowseComp-Plus N=150; 0.492 vs 0.488 on SWE-Bench N=500). HiAgent's own control (d08) shows decomposition alone gives +30 of its +50 points. MEM1 (d10) is RL-trained. Not yet replicated in our scaffold.
4. Working-set cap: STAYED OPEN. Only indirect support: input length hurts (0.92 to 0.68, d07), n-back limit (d17). No chunk-unit cap test.
5. Sala & Gobet numbers: CLOSED. r=.41 [.29,.51], k=28 samples from 24 studies, N=903 verified; adjusted r=.29 for publication bias (d01). Gobet & Simon 2000 constants verified against Table 1 (d02); note the text says c rises x15 for Masters but the table gives about x13.
6. Order/format sensitivity: MOSTLY CLOSED (yes). Premise order (d06), position in context (d05), board rotation (d04). Mirror is tolerated, so the human mirror/quadrant analogy is only partial.
7. Library size vs depth: PARTLY ANSWERED by the model only (d13). No LLM data.
8. CHREST/CogAct vs embedding retriever: STAYED OPEN.
9. Karvonen 64% vs 69.6%: CLOSED for the discrepancy (different Stockfish limits, d03). Transfer of the random-board collapse to non-chess tasks stays open; the 'random board' is a random-move start, not scrambled pieces.
10. Independent template replications: PARTLY CLOSED, and the answer is mixed. Lane & Chang 2018 (N=79, d11) favour a conceptual-knowledge account; Saariluoma & Laine 2001 (N=2, d12) support curve shape but offer a rival mechanism. Chassy 2023 (d14) has Gobet as co-author.

Corrections made to claims.jsonl: K14, K07 raised to established; K16 and K20 reworded; K19 raised to established with three sources; K22 reworded; K23-K27 added. Caveats: d06, d07 numbers read through page summaries; d09 table cells matched using printed deltas; d11 abstract only.
