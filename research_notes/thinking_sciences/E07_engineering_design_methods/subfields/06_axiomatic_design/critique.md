# Critique: E07.06 Axiomatic design (cross-check)

## Corrections made (sources re-opened this session)
1. Frey and Hirschi 2002 (ICAD PDF): confirmed N=12, 2x2 coupled 40 s vs uncoupled 24 s, alpha 0.05, 31 coupled 2x2 tasks, 3.4^n growth. Authors call the 2x2 difference practically small. No change.
2. Homay 2025 (arXiv 2507.09599): confirmed "over 100 software engineers" and "more than 80%" misjudged the faucet. Survey method and sampling are not described; treat as anecdotal.
3. Jiang and Luo 2026 (arXiv 2604.28018): CORRECTION to c17. Helicopter has 14 nodes, not 19; the largest case is HeatEx with 17 nodes. c18 undersold the result: for Claude, domain knowledge hurt on HeatEx (5.4%) and Helicopter (3.6%); Helicopter with k=0 matched the SA reference in 10 of 10 runs, with k=1 in 0 of 10. The "within 1.3%" statement is for Kodak, Brake and HeatEx.
4. Auto-DSM (arXiv 2312.04134): 357/462 = 77.3%, 82.6/54.5/40.0 per source, and ChatGPT direct range 66.7-85.7% all confirmed.
5. AssemCAD (arXiv 2607.05123): table figures confirmed. Confirmed the 62 axioms are engineering rules, not Suh axioms. Name clash only.
6. Yoong et al. 2020 (arXiv 2007.03651): 44 concrete FRs and no false positives confirmed. The naive Bayes 93.75% figure (b18) was not re-checked.
7. Giordano et al. 2025 numbers (a08-a10, c04-c05) were not re-opened this session; they were read in the earlier phase. c05 notes the F1 table was garbled, so the concept-to-number mapping in a10 is only partly certain. a10 and c05 are the same source, so they are not independent.

## Contradictions
- a28/b10/b26 report 6 arXiv hits with one LLM link, while the c-file finds many DSM plus LLM papers. Not a true conflict: DSM work is adjacent, not independence-axiom work.
- c22 (Joshi) claims large AD gains; no other source agrees and only the abstract was seen.
- Frey and Hirschi contradict the strong reading of Suh Theorem 9 at n=2 but support a real cost of coupling at n>=3.

## Weak spots
- Almost all human evidence is ONE experiment (N=12, one lab, slider task), never replicated.
- No LLM test of independence itself. All LLM work is DSM, extraction, or a name clash.
- Many rows are citation counts or abstract-only. b09 (N=96) came from a snippet.
- Homay's papers are advocacy and self-cited.
- The Jiang papers share authors; the Giordano and Consoloni papers share authors.

## Seen only in snippets or abstracts
a21-a27, b05, b06, b07, b08, b09, b24, c07, c08, c09, c21, c22, c24, c25.

## GAPS
1. Does a matrix-first scaffold (list FRs, map to DPs, check triangularity by program) beat free design for an LLM on multi-requirement tasks at equal tokens? No study exists.
2. Does the 3.4^n coupled-search blowup replicate with LLM agents on numeric coupled tuning tasks, and does solving the linear map by program remove it?
3. Can an LLM classify a design as uncoupled, decoupled or coupled from text (humans failed the faucet test at over 80%)? What accuracy against a program-computed matrix?
4. What do the full texts of Goehler, Howard and Frey 2016 and Hirschi and Frey 2002 report (effect sizes, robustness conditions)?
5. Is the Joshi 2026 claim (coupling down 34.2%, iterations down 41%) supported in full text, and how was coupling measured?
6. Do solution-neutral FR rewrites measurably improve LLM design or planning quality (Homay's central claim)?
7. Why does injected knowledge hurt Claude on larger DSMs (Jiang and Luo)? Is it general to scaffolds that add guidance?
8. Is there any independent replication of Frey and Hirschi in other labs?
9. Does the information axiom (minimise information content) have any outcome test, human or LLM?

## Gap search results
Search tools were heavily throttled (arXiv, Semantic Scholar, OpenAlex gave HTTP 429; WebSearch budget ran out after one call). Work used Crossref, Springer abstract pages and full text of two arXiv papers. Evidence is in evidence_d.jsonl (d01-d18).

CORRECTION TO THE CORRECTION: the critique item 3 above was wrong about Helicopter. Table 1 of Jiang and Luo gives Helicopter N=19, E=109 (density 0.32 checks); HeatEx is 17 nodes. The original c17 was right. See d06.

1. Matrix-first scaffold vs free design for an LLM: STAYED OPEN. No study found (d16, weak because of throttling).
2. 3.4^n blowup with LLM agents: STAYED OPEN. No study found. The human result now has one partial replication (d04).
3. LLM classification of coupling from text: STAYED OPEN. No study found (d16).
4. Full texts of Goehler 2016 and Hirschi and Frey 2002: PARTLY CLOSED. Key correction: Goehler, Frey and Howard 2016 is a Monte Carlo simulation of 250 architectures, not a human experiment (d01). It finds the axiom holds only for nominal-is-best requirements and fails for max/min-is-best (p = 1.4e-36). Journal abstract of Hirschi and Frey confirms the ICAD story (d03). Both full texts remain paywalled or blocked, so effect sizes beyond the abstracts are unseen (d02).
5. Joshi 2026 claim: STAYED OPEN, with a new red flag. The abstract credits the numbers to a self-cited separate work (Joshi 2026a) and defines no coupling measure; full text blocked (d10).
6. Solution-neutral FR rewrites for LLMs: STAYED OPEN. Homay 2507.09599 full text has no LLM content (d09). Nearest evidence is O'Hara 2025 solution-jumping detection, 6 antipatterns, 100% detection, no quality comparison (d11), and Elicitron (d12), which is about need discovery.
7. Why knowledge hurts Claude: PARTLY CLOSED. Authors' explanation is semantic misalignment between functional priors and a structural objective; it is a hypothesis. It is model-dependent: GPT and Qwen gain early from knowledge and k=0 catches up later (d05, d07, d08). Not shown to be general to scaffolds.
8. Independent replication of Frey and Hirschi: PARTLY CLOSED. Grogan and de Weck 2016 (10 groups of 3, 42 tasks) replicate geometric growth of time with size for coupled tasks, but same university and a team variant (d04). Citing list of 77 works not retrieved (d18).
9. Information axiom outcome test: STAYED OPEN. Only multi-criteria applications and metrics proposals found (d14, d17). One simulation outcome test exists for the independence axiom (Mollajan 2022, abstract only; d13).
