# Critique: E16.06 Pattern-recognition theory of search

## Corrections made (re-opened arXiv PDFs this session)
Checked against full text: Ruoss et al. 2024 (table: 9M 2025/88.9, 136M 2259/94.5, 270M 2299/95.4, blitz 2895 vs humans, 2299 vs bots; Leela 2292/88.6, 2418/95.9, 2858/99.6; AlphaZero 56.1/82.0/95.6; Stockfish 2711/99.8; GPT-3.5 1755/66.5); Jenner et al. (92%, 83%, 29.8%, 22.5k puzzles, 1.88); Schultz et al. (2923/2875, +68 internal Elo with 100 sims, 99.6% tree shape, about +300 Elo, 14,689 chess games); McIlroy-Young (46%, over 52%, 5 points); Karvonen (99.8/99.6, 46%/64%, 2.6x, 41% to 92%). All confirmed. No numeric errors found.
Clarifications (not errors): 2299 is the tournament Elo and also the Lichess Elo vs bots; 2895 is vs humans only (a20 and b07 mix these in one line). AlphaZero policy-only is 1777 tournament Elo in Ruoss but 1620 in Monroe and Chalmers (different setups; do not compare). The Lichess 2600+ claim for a Leela policy bot (c04) comes from an external page, not verified. McIlroy-Young "33-41%" for Stockfish was not located by grep in the text (the 46% and 5-point lines were); treat as first-pass value.

## Contradictions
- Dual-task: Bradley et al. (via b05) report load cuts recall by over two thirds and tactics by one third; Charness reports only a 6-8% drop. Unresolved (K06).
- Recognition versus search cannot be separated by the classic tests (K07).
- Jenner finds look-ahead inside a policy net while Ruoss calls it searchless. Both can hold: no explicit search, but internal planning.

## Weak spots
- Gobet 1997 (the named key work) was never read. This subfield rests on Simon and Chase, Gobet and Simon, and indirect AI studies.
- Human data are small: templates experiments N=13 and N=25, 3 to 5 masters; one single-subject study.
- AI studies show strong play without search, but none test the human claim that patterns shorten search. Closest is Schultz (search added to a searchless model).
- Several 2025-2026 LLM studies (c17-c28) were read at abstract or single-read level; ChessQA has no model numbers.
- b17-b25 (de Groot, Charness 1981, Holding, Campitelli and Gobet, Bilalic, Reingold, Linhares and Brum) were not verified.
- Gobet and Simon 1996 numbers were not re-opened (paywalled); they remain from the first pass.

## GAPS
1. What does Gobet (1997) claim and test, with numbers, about templates shortening search (nodes, depth)?
2. Does a recognition-first pass reduce total tokens at equal accuracy in LLM reasoning (any measured study, not only chess)?
3. How much of the human skill gap is search quality versus recall in the best modern data (eye tracking, think-aloud, Campitelli and Gobet 2004, Bilalic 2008)?
4. Do Einstellung findings show that fast pattern matches block better solutions, and how big is that cost for an LLM first pass?
5. What is the measured gain from search over a policy-only first pass in non-game LLM tasks (math, code)?
6. Can slot-based template retrieval be tested in LLMs with measured transfer across problem instances?
7. What is the replication status of the Charness vs Bradley dual-task dispute?
8. How do the 2025-2026 LLM chess studies (LLM Chess, ChessArena, Hwang) compare at equal token budgets?
9. Is the policy-only Lichess 2600+ bot (Jenner appendix) documented in a primary source?
10. When does imitating human experts (Maia) beat engine supervision for a scaffold's quick pass?

## Gap search results (evidence_d.jsonl, d01-d18; claims now K01-K26)

Closed:
- Gap 1 (Gobet 1997): read in full (d01-d03). The paper does not claim templates cut node counts. It says recognition makes deep search cheaper but also removes the need for it, so depth differs little. SEARCH model: mean depth about 2.5 ply (1,000 chunks), 4 (30,000), over 5 (over 100,000); about 75% of episodes end by recognised evaluation. Parameters are author-set. K18 rewritten and set to established.
- Gap 3 (search vs recall in modern data): Campitelli and Gobet 2004 (d04, d05) shows nodes 88 to 370+, mean depth 2.8 to 13.8 ply, rate 3.2 to 12.3 nodes/min across four players on hard positions, so "flat search" is a task-difficulty artefact; N = 4. K01 qualified. Bilalic 2008 and Sheridan and Reingold 2013 (d06, d07) give the attention mechanism. Not found: a large-N modern study separating search quality from recall.
- Gap 4 (human side only): Einstellung cost is about 3 SD of skill (about 600 Elo); 8/17 experts and 8/17 novices chose the familiar suboptimal move; effect vanishes when the familiar move is a blunder (d06, d07; K19, K20).
- Gap 7: Robbins et al. 1996 opened (d08). Charness's 6-8% and Bradley's "over two thirds" are different manipulations (post-presentation delay vs concurrent load), so it is not a failed replication (d09). Strong players lost 48-60% recall and about 37% tactics under load; "over two thirds" not reproduced. K06 rewritten, still contested.
- Gap 9: documented in Jenner et al. Appendix B via archived Lichess page link (d10); not independently measured. K25.
- Gap 10 and the earlier unchecked figure: McIlroy-Young "33-41%" for Stockfish located in the text (d11). Maia beats engine supervision on matching human choices and loses agreement if tree search is added. K13, K26. The scaffold-quick-pass question beyond move matching has no measured answer.

Partly closed:
- Gap 2: SwiftSage cut tokens per action to 757 vs 1,971 (ReAct) with higher score (d18); Buffer of Thoughts at about 12% of multi-query cost (d17). Both are agent or template systems, not a matched recognition-first vs always-search test on single-answer reasoning. K22 single-source.
- Gap 5: Snell 2024 and Tree of Thoughts (d15, d16) give measured search gains over policy-only passes (math levels 3-4 yes, levels 1-2 no; Game of 24 74% vs 4%). No clean code-task study found. K21.
- Gap 6: Buffer of Thoughts (d17) tests retrieval of templates on held-out instances; no slot ablation and no cross-family transfer. K23.
- Gap 8: LLM Chess, ChessArena and Hwang (d12-d14) opened; none compares at equal token budgets (ChessArena caps 4k vs 16k tokens; LLM Chess varies vendor effort levels). Deeper reasoning helps, parallel sampling does not. K24.

Still open:
- LLM Einstellung cost (gap 4, LLM half): no study found. The web search quota ran out and the arXiv, OpenAlex and Semantic Scholar search endpoints were rate-limited, so this is untested, not shown absent.
- Charness 1976 and Bradley 1987 originals not opened (paywalled or unpublished); Gobet and Simon 1996 numbers still second-hand.
- A direct equal-token test of recognition-first vs always-search for LLMs on math or code (needs to be run by us).
