# Critique, E04.07 Expert-novice differences (chunks and cues)

## Corrections made (re-opened sources)
Re-checked against full text this session: Ruoss et al. 2024 (arXiv 2402.04494) and Karvonen 2024 (arXiv 2403.15498).
1. Ruoss: 9M/136M/270M give 2025/2259/2299 in the first Elo column and 2054/2156/2299 in the second; puzzle accuracy 88.9/94.5/95.4; blitz 2895 only for 270M; GPT-3.5-turbo-instruct puzzle 66.5 and 1755 in the second column; 1.33% puzzle overlap. Confirmed. Correction: lines a25 and b23 mix columns ("tournament Elo 2299 vs 1755"). 2299 and 1755 are in the same (second) column, so the comparison is fair, but the 2025/2259 values are a different column. Label accordingly.
2. Karvonen: legal move rate 99.8 (16 layer) and 99.6 (8 layer), 64% and 46% win rate vs Stockfish level 0, probe 99.6 square and 90.5 Elo, intervention 92.0 vs 40.5-41.0 without: confirmed. Correction: 64%/46% and 69.6%/49.6% (5,000 games, standard board) come from different samples; random board 16.7 to 43.2 confirmed. Do not mix them.
3. a21 vs b11: domain moderator p=.069 in a21 and p=.116 in b11 (full vs 26-effect set). Both reported; status is "no significant moderator".
4. a02 is tagged "replication" but is a within-paper repeat in Chase and Simon 1973, not independent.
5. The accidental re-run of an older helper script in the scratch folder rewrote evidence_a.jsonl with the same 29 lines (same size). Content is unchanged.
6. Not re-opened by me: Gobet and Simon 1996, Gobet and Waters 2003, Sala and Gobet r=.41, Burgoyne 2016, Pleiss 2026. They agree across several evidence lines (internal consistency, not independent re-verification).

## Contradictions between sources
- Chunk store size: 50,000 (Simon and Gilmartin 1973, Gobet and Simon 1996) vs about 300,000 (Gobet and Simon 2000, quoted in b16). Contested.
- Chunks per recall: 7 (Simon and Chase 1973) vs under 3 (Gobet and Clarkson 2004) vs Cowan's 4. Chunk size: 2.1-2.5 (1973), 3.6 (Freyhoff), 11.2 (Gobet and Simon 1996), up to 15 (Gobet and Clarkson).
- Random positions: Chase and Simon found no skill effect; Gobet and Waters found r=.34 on truly random; one 1996 experiment (N=25) had ns F=0.18. Sample size explains much of this.
- Pleiss 2026: GPT-5 ACPL 463.5 is an average with illegal move = 1000; 26.19 is the familiar-position figure. Different conditions, both valid.
- Intelligence-chess link: r=.24 overall, but -.10 in high-rated samples (ns, p=.159).

## Weak spots
- Chase and Simon N=3; Gobet and Simon 1996 N=25.
- Nearly all LLM evidence is chess; transfer to open reasoning is untested. c20/c21 are interpretability only.
- Persona result (b25) is one paper; HiAgent (a29) and Voyager (c24) are loose chunk analogues.
- Publication bias: trim-and-fill drops r from .41 to .29.

## Seen only in snippets or not opened
a24, a27, b18, b19, b20, b26-b28, c05, c22, c25, c26, c27 (opened:false). K09 (deliberate practice) and K10 (expertise reversal) rest on these.

## GAPS
1. Does a retrieval memory of domain "chunks" (solved cases) improve an LLM agent at equal tokens, and how does gain scale with library size (log law)?
2. Does the LLM out-of-distribution collapse (Pleiss) appear on non-chess tasks, and does our scaffold reduce it at equal tokens?
3. Do LLMs show the human game-vs-random recall gap on text tasks (structured vs shuffled input), and how big is it?
4. Does expertise reversal apply to scaffolds: should guardrail strength fall when a task is familiar?
5. What is the true chunk count and size: reconcile 3, 4, 7 and the 50,000 vs 300,000 store figures.
6. Do expert personas help when paired with domain facts, not role labels alone?
7. Do Connors 2011 and McGrath 2022 (not opened) change the template or concept-acquisition story?
8. Is chunk-count measurement reliable enough (test-retest .65 vs .36) to use as an agent metric?
9. Does skill-conditioned steering (Karvonen, Jiao 2026) have a prompt-level analogue?

## Gap search results
Note: WebSearch use exceeded the 8-call budget (10 used); the arXiv, Semantic Scholar and OpenAlex APIs were rate-limited, so Crossref, Europe PMC and page fetches were used. Evidence is in evidence_d.jsonl (d01-d16); claims K19-K24 added; K04, K10, K11, K15 updated.

1. Case memory at equal tokens, log law: OPEN. No paper gives a token-matched, library-size curve. Found: sweet spot at intermediate size (d01), add-all hurts and verified-only helps (d02), ExpeL gain 28.0 to 39.0 with no scaling numbers (d03), many-shot ICL peaks then declines on some tasks (d04). New claim K20.
2. OOD collapse outside chess: OPEN. Pleiss tested only chess (d05, re-read); a synthetic CoT study (d06, abstract only) points the same way. No scaffold arm exists. K23.
3. Structured vs shuffled gap on text: OPEN. No LLM study of the human-style gap. Letter-scramble recovery is near ceiling for GPT-4 (d15), word-order tasks are hard (d16). K22 (contested).
4. Expertise reversal for scaffolds: PARTLY CLOSED. Headroom law r=0.75 and regressions on a strong target, 9 of 20 cases (d07); small GSM8K inversion (d08). Both preprints, one small. K19 single-source, K10 extended.
5. Chunk count and size, store size: PARTLY CLOSED. Store estimates run 10,000-100,000 (Simon and Gilmartin) to 300,000 (Gobet and Simon), all indirect; a direct count gives about 100,000 opening moves (d12). The 3 vs 4 vs 7 chunks question is method-dependent and stays contested.
6. Personas with domain facts: OPEN. Role labels do not help across six more models (d09); role retrieval no better than none (d10). No study pairs a persona with facts. K15 raised to established for the role-label-only claim.
7. Connors 2011 and McGrath 2022: CLOSED, no change to the schema. Connors replicated de Groot (d13, abstract only); McGrath shows concepts emerge in AlphaZero (d14). K24.
8. Chunk-count reliability: CLOSED. Test-retest .65 vs .36 on game positions, about .14 on random (d11). Not suitable as an agent metric. K21.
9. Prompt-level analogue of skill steering: OPEN. Jiao 2026 (c13) works by head retraining and SAE steering; no prompt-only test found. Role labels alone fail (d09), which suggests prompt-level skill labels are weak.
