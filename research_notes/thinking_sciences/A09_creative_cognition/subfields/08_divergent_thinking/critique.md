# Critique and cross-check: A09.08 Divergent thinking

## Sources re-opened this session (full text) and result
- Stevenson et al. 2022 (arXiv 2206.08932): beta .17/.14/.10/-.55, r -.56/-.61, F(1,85)=5.53, r=.04 all CONFIRMED.
- Koivisto and Grassini 2023 (Sci Rep): B=0.049 (t274=4.949), 0.027 (t268=3.037), r=.55 [.46,.62], .52 CONFIRMED.
- Hubert et al. 2024 (Sci Rep): F(1,600)=622.10 eta2=.51, DAT 84.56 vs 76.95 t(300)=13.65, AUT elaboration 15.45 vs 3.38, 9.11% overlap, fluency 6.94 vs 7.01 CONFIRMED.
- Haase, Hanel, Pokutta 2025 (arXiv 2504.12320): 77.34 vs 84.56 d=2.41, vs 82.54 d=2.04, aware 60.16 vs unaware 52.56 B=11.89, AUT 65.66-77.85, F(13,356.64)=9.34 CONFIRMED.
- Haase and Hanel 2023 (arXiv 2303.12003): B=-0.21 p=.218, B=-0.18 p=.241, 32.8 humans, 9.4 vs GPT-4 CONFIRMED.
- Jiang et al. 2025 Artificial Hivemind (arXiv 2510.22954): 79%, min-p 81% above 0.7 and 61.2% above 0.8, 71-82% across models, 0.82/0.81, 31,250 annotations CONFIRMED.
- Si et al. 2024 (arXiv 2409.04109): 4.84/5.64/5.81, 119 vs 109 reviews, 71.4% and 63.5%, 200 of 4000 non-duplicate CONFIRMED.
- NoveltyBench (arXiv 2504.05228): 79% classifier accuracy, 20 models, "larger models often less diverse" seen; per-model distinct-k numbers (under 3, utility under 4) not re-verified.

## Corrections and clarifications
1. b11 lists "elaboration 38.69 vs 5.45 words" next to the AUT. That figure is from the Consequences task (t(621)=-36.04). AUT elaboration is 15.45 vs 3.38 (a14, c02 are right).
2. a08/b10 "9.4 humans beat GPT-4": GPT-4 was scored by the AI rater only (humans would have known it was AI). Per prompt: 2 (pants), 29 (ball), 0 (tire), 3 (fork), 13 (tooth). The 32.8 figure is against the best of the other five chatbots.
3. b19 attaches "top-p 0.9 temperature 1.0" to the 79% figure and "temperature 2" to min-p; the paper text only states min-p gives 81% of pairs above 0.7 and 61.2% above 0.8. The min-p temperature detail is unchecked. The later arXiv version covers 42 models (within-prompt similarity 0.821 vs 0.781 across paraphrases).
4. c08: the GPT-4 vs GPT-4o comparison mixes different studies, prompts, raters and dates. d=2.41 is not a clean model-version effect.
5. Si et al.: the 5.64 vs 4.84 difference is on the novelty metric only; human ideas came from experts who may not have submitted their best idea.
6. a15/b13 mix Hedges g sign conventions (positive for LLM > human; negative for LLM vs top 50%). Do not average.
7. a04 and a13 have empty numbers fields; b23 and b24 came from search snippets only.

## Contradictions between sources
- "Best humans win" (Koivisto; Haase 2023: 9.4% to 32.8 humans above chatbots) vs "AI far above humans" (Hubert eta2=.51, g 2.61). Likely reasons: fluency control differs (prospective matching vs post hoc trimming), scorer and task differ, model and date differ.
- Individual originality vs population diversity: LLM equal or higher on individual items (0.711 vs 0.696) but far lower on variability (d 1.8). Both are true; they measure different things.
- Temperature: Peeperkorn finds a small novelty gain; Nath finds no AUT jump effect; Bellemare-Pepin finds DAT rises with temperature (0.5-1.5). Task and metric differ.
- GPT-4 DAT 84.56 (2023) vs GPT-4o 77.34 (2025) while the broader 2025 sweep says newer models score high on average; version drift is not understood.

## Weak spots
- Most LLM-vs-human studies use semantic-distance scoring, which rewards odd words and penalises elaboration; word count correlates -.25 with SD but .41 with human ratings (Beaty and Johnson).
- Human samples are small, student or Prolific, with minimal instructions compared to tuned LLM prompts. Training-data contamination of AUT/DAT is unaddressed (Stevenson suspected it).
- Weak links: DT-intelligence only r about .25, threshold hypothesis not replicated, DT-to-real-creativity prediction weak.
- No study here tests a multi-step thinking scaffold on DT at equal tokens; closest are multi-agent debate (a different construct), verbalized sampling and NoveltyBench regeneration.

## Only seen in snippets or not opened
a25-a28 (Hass, Baas, Nijstad, Runco 2008, Guilford, Silvia, Mednick), b23 (Acar et al. 2020 explicit-instruction g .24-.27), b24 (evaluative skill r=.13), c27. The founding studies (Guilford 1950/1967, Runco 2008) were not opened, a gap for the "founding studies with exact numbers" requirement.

## GAPS
1. Does any scaffolded or multi-step LLM method (not just sampling tricks) raise DAT/AUT originality and population diversity at equal tokens, compared with verbalized sampling and plain best-of-N?
2. What do Guilford's 1950/1967 AUT work and Runco (2008) actually report (numbers, definitions), and what is Runco's exact argument that DT is not synonymous with creativity?
3. How much of the LLM advantage on AUT/DAT survives control for fluency, response length and training-data contamination (new unseen objects)?
4. How stable is LLM DAT/AUT performance across model snapshots and prompts (GPT-4 84.56 vs GPT-4o 77.34), and what are the 2026 frontier numbers?
5. Do semantic-distance scores predict human-rated usefulness and real task outcomes for LLM ideas, or only odd-word novelty?
6. What explains the Hivemind effect, and do banned frequent words, persona diversity or retrieval of seen ideas break it better than temperature?
7. What are the verified Acar et al. 2020 explicit-instruction effect sizes and the evaluative-skill meta-analysis numbers?
8. Is the serial-order effect present in LLM idea chains, and where should a diverge stop rule sit?
9. Does using the agent in a human loop reduce the diversity of the human group's ideas (Anderson 2024 had N=36 only), and is there a replication?

## Gap search results
Evidence in evidence_d.jsonl (d01-d16). arXiv, Semantic Scholar and OpenAlex APIs were rate-limited, so papers were found by the arXiv search page and read as full PDF text. Gaps 2 and 7 hit paywalls.

1. Scaffolded or multi-step methods: PARTLY CLOSED. MUTATE/ReDNA (d01, d02) shows a goal-blind diverge call then a narrowing call raises AUT originality 2.91 to 3.77 and agent path discovery 27/56 to 38/56 on GPT-5.4. Verbalized Sampling (d03) was compared with CoT, sequence and multi-turn at equal N responses and wins on diversity (x1.6-2.1). IDEAFix (d11) finds short "wild, unconventional" cues beat SCAMPER/TRIZ/C-K prompts. Still open: no study compares a diverge-then-select scaffold with best-of-N at equal tokens on DAT/AUT.
2. Guilford 1950/1967 and Runco 2008: OPEN. Crossref confirms the records but PsycNet and Taylor and Francis could not be read (d16, opened:false). No exact founding numbers added.
3. Fluency, length and contamination control: PARTLY. Nothing new on AUT fluency matching. IDEAFix (d11) notes training-data contamination risk on classic tasks; Schaeffer (d05) shows a stricter null shrinks the homogeneity claim. A new-unseen-object test is still missing.
4. Snapshot and 2026 stability: PARTLY CLOSED. Across 54 models, DT diversity scores fall -0.47 z/year while creative writing rises +1.22 and science ideation +1.00 (d08). No 2026 frontier DAT/AUT table found; that part stays open.
5. Semantic distance vs usefulness and outcomes: PARTLY CLOSED. DAT predicts creative writing (validity .51-.71) but no existing test predicts science ideation; capability correlates up to .98 with benchmarks (d07). Originality falls as utility falls on AUT in CreativityNeuro (d09). No human usefulness link at idea level was tested.
6. Hivemind cause and cures: CLOSED enough to act on. Proposed cause is typicality bias in preference data (beta .57-.65, d04). A re-analysis (d05) shows the 0.8 threshold is weak (same-prompt different-idea median cosine 0.70-0.72) but a residual 2-3x effect remains. Persona, anti-modal prompts and sample-then-ban beat temperature and min-p (d06, d14, d15). Banned-word lists and retrieval of seen ideas were not tested head to head.
7. Acar et al. 2020 effect sizes: OPEN (paywalled, d16). b23 stays unverified.
8. Serial order in LLM chains: OPEN. No study found; stop rule remains from human data (K15).
9. Human-loop homogenization: PARTLY CLOSED. Kumar et al. (d10, N=1,100; 460 on AUT) found strategy lists lowered later solo originality (p=.009) and raised similarity (p=.017); idea lists did not. Claim K12 is now contested, not single-source.

Changes to claims.jsonl: K03 downgraded to contested; K12 contested; K02, K04, K07, K09, K11 given extra evidence; new K16-K21.
