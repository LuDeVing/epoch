# A09.02 Dual-process view of creativity: cross-check critique

## Corrections made (sources re-opened this session)
Re-opened and confirmed against full text: CreativeDC (about 13 distinct, 12 high-utility vs about 8, Vendi, p<.001); Chen and Ding (GPT-4 DAT 89.1, above 96.1% of humans; GPT-3.5 80.8); Bellemare-Pepin (GPT-4 mean DAT 85.6 at the highest temperature, above 72% of humans); Padmakumar (+6.9%, +6.3%, +9.6%, +4.9%, -18%, +3.7%); Nieuwenstein (196 vs 203, 55.61 vs 55.17, Bayes factor 7.83, pooled g 0.15 CI .03-.26); Sio and Ormerod (117 effect sizes, 3,606 participants, Q 173.99, weighted 0.29, unweighted 0.36); Benedek (Gf-creativity r .45 to .34, 43%, updating .53/.29); Lee and Therriault (b .56 and .82, divergent-convergent -.52 ns); Nijstad chapter (20 studies, N=2118, flexibility-originality r .34).

Corrections:
1. Flexibility-originality r: evidence b02 (via Sowden review) says 0.36; the original Nijstad table says .34 (k=10, N=1439). Use .34. The review quotes it wrongly or from another table.
2. b23 said "asking for novelty and Denial Prompting"; confirmed, but the source calls them "asking for novelty" (with chain of thought) and "denial prompting" run on post-trained OLMo models, 750 examples each. The novelty gain is small and the paper says total novelty effect is "much smaller" than from scale/post-training.
3. a26, b24 and c15 are the same paper (CreativeDC); counted as one source. Same for a01/b01/c01 (Sowden review) and a28/a29 families.
4. a16 and a21/a24 numbers are abstract-only; treated as single-source.

## Contradictions between sources
- Temperature and GPT-4: Chen and Ding found no gain from temperature for GPT-4 (greedy already 89.1); Bellemare-Pepin found a significant rise with temperature but top score 85.6, lower than Chen and Ding's greedy score. Different prompts and DAT variants; not comparable. Peeperkorn finds only weak links to novelty. Status: contested.
- Lee and Therriault (divergent and convergent unrelated, share associative fluency) vs Benedek (executive functions, not shifting, drive divergence): different latent structures.
- Incubation is a small robust gain (g .29) while the sibling unconscious-thought effect failed to replicate (N=399, BF 7.8 for null): a split within the "slow unconscious" idea. Sio and Ormerod also show heavy heterogeneity (Q 173.99, df 113).
- Barr: more time helps remote analogies (+12 points) but analytic-vs-intuitive cues do not (69.9 vs 69.0): capacity, not style, matters.

## Weak spots
- No study directly tests "mode switch by code" against "mode switch by model" at equal tokens. All LLM evidence is indirect: two-stage prompts (CreativeDC, LLM Discussion, ReDNA) beat baselines but baselines differ and token parity is not controlled.
- LLM Discussion uses gpt-3.5 and an LLM judge of the same family; ReDNA is a 10-scenario preprint; Universe of Thoughts and TinyTim are small and by the authors' own metrics.
- Neural studies (Ellamil, EEG, bioRxiv) are small (N 28 to 41), not about LLMs; Ellamil and the 2016 reflection study numbers were not read (abstract pages).
- The Sowden review itself says Type 1/Type 2 does not map to generation/evaluation, which weakens the "dual-process" label as a design basis; the usable part is the alternation, not the labels.
- No failed replication of the dual pathway model itself was found; the fluency-flexibility link (r .72) is partly definitional.

## Only seen in snippets (opened:false)
b27 Nusbaum and Silvia, b28 Said-Metwaly, b29 Gerwig (MDPI 403), c23 Helie and Sun (secondary), c24 Scientific Reports Dec 2025 GenAI vs human, c25 brain alignment vs chain of thought, c26 cross-study originality ratings, c27 Beaty 2014. Not used for any established claim.

## GAPS (most decision-relevant first)
1. At equal tokens, does a code-set diverge-then-converge pipeline beat a single prompt or best-of-N on open-ended and on closed (verifiable) tasks? No paper controls token parity.
2. Does the diverge stage help or hurt on closed-answer reasoning (math, ARC)? All positive evidence is open-ended creative output.
3. Is structural diversification (separate calls, banned concepts, category forcing) better than temperature at equal tokens, for current frontier models (2026)? Evidence is mostly gpt-3.5 or small OLMo.
4. Can an LLM critic evaluate originality without the elaboration and length bias (OCSAI r .28 vs humans on mixed data), and does same-family judging inflate gains?
5. What switching schedule is best: one diverge then one converge, or interleaved cycles with a critic (reflection study suggests interleaving), measured on LLMs?
6. Does showing earlier candidates during diverge cause fixation in LLMs as in humans (Jansson and Smith)? Not tested on models.
7. Does the flexibility (breadth) vs persistence (depth) split transfer to LLM search: which route gives more valid originality (Nath et al. found flexible LLMs score higher, abstract only)?
8. Does a context-reset or "incubation" analogue produce the small incubation gain seen in humans (g .29)?
9. Does the Artificial Hivemind homogeneity persist under multi-stage scaffolds, and does cross-model diversification help?
10. Are the reasoning-trained models worse at divergence (brain alignment preprint, Lu et al. self-correction result)? Needs full reads.

## Gap search results

Sources opened this pass: Verbalized Sampling (HTML, main text and appendix tables), Artificial Hivemind (full PDF), Zhang et al. 2025 (full PDF), Ma and Grandi 2024 (full PDF), CreativeDC (HTML), Wadinambiarachchi 2024, design-fixation preprint 2502.05870, abstracts of NoveltyBench, Tree of Thoughts, CreativityPrism, and an automated-creativity-evaluation paper. The arXiv, Semantic Scholar and OpenAlex APIs returned 429 and the WebSearch budget ran out, so gaps 5, 7, 8 got no new source. Evidence is in evidence_d.jsonl (d01-d17).

1. Equal tokens, diverge-then-converge vs single prompt or best-of-N: STAYED OPEN. CreativeDC (d07) again has no token count and no ablation. Verbalized Sampling (d01) matches the number of responses (not tokens) and wins over a sequence baseline (poem 2.39 vs 2.07, joke 3.01 vs 2.93 human diversity), which is the closest evidence.
2. Does diverge help closed tasks: PARTLY OPEN. Tree of Thoughts (d11) 4% to 74% on Game of 24, but with an evaluator and many calls. Diverse generation improved math training data 30.6 to 36.1 (d02). No test of a creative diverge-then-converge prompt on ARC or math.
3. Structure vs temperature for 2024-25 frontier models: MOSTLY CLOSED. GPT-4 temperature is non-monotonic, critique-edit step best (d06); min-p at T 2.0 leaves 61.2% of pairs above 0.8 (d03); VS 1.6-2.1x on GPT-4.1, Gemini-2.5, Claude-4 (d01). Token parity still missing.
4. LLM critic bias: PARTLY CLOSED. GPT-4 and GPT-4o have no novelty-fit trade-off (r .13, .16 vs humans -.39) and GPT-4o selects worse than humans (d05); judge-human agreement falls on near-equal and contested items (d04); a retrieval judge reached 83-85% vs ChatEval 73-77% (d13). Same-family inflation and length bias were not measured: still open.
5. Switching schedule: OPEN. Only indirect support (a second critique-edit pass helped, d06).
6. Fixation by shown candidates in LLMs: OPEN, with a counter-signal. Humans fixate on AI images (d08, d09); NoveltyBench abstract says in-context regeneration raises diversity (d10). No direct model test.
7. Flexibility vs persistence in LLM search: OPEN (not reached).
8. Incubation analogue: OPEN (no source found).
9. Hivemind under scaffolds: PARTLY CLOSED. Plain sampling and plain cross-model mixing do not help (inter-model similarity 0.71-0.82, d03); VS lifts diversity (d01); effect of multi-stage scaffolds on cross-model similarity untested.
10. Reasoning models worse at divergence: PARTLY OPEN. o3 and R1 are as collapsed as others under direct prompting (poem diversity 13.2, 12.4) and respond to VS (d02). No paired comparison with non-reasoning bases; the brain-alignment preprint was not identified (d16, unusable).

Claims changed: K17 and K16 now contested; K09 raised to 3 sources; K04, K06, K07 gained evidence; new K20-K25 added.
