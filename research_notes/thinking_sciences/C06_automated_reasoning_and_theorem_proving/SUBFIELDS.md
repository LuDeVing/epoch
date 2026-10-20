# Automated reasoning and theorem proving: subfields

Automated reasoning builds programs that derive conclusions by rule. It divides by logic and method: resolution and saturation provers for first-order logic, SAT and SMT solving, interactive proof assistants (Lean, Coq, Isabelle), neural proof search, and conjecture and lemma generation. It matters for us because proof search is a clean generate, check and reuse loop: steps are verified by a kernel, and proven lemmas are stored. Marks: [V] = page opened this session; [M] = from memory or seen only in a search result.

## Subfields

| Subfield | What it studies | Key people or works | Useful (H/M/L) | How |
|---|---|---|---|---|
| Resolution and saturation | First-order resolution with unification; Otter, E, Vampire, SPASS | Robinson; Wikipedia article [V] | Med | control: clause selection loop |
| SAT solving, DPLL | Propositional satisfiability | Wikipedia article [V] | Med | S4 TEST |
| CDCL | On a conflict, learn a clause from the implication graph, backjump, restart | Marques-Silva, Sakallah; Bayardo, Schrag [V] | High | lessons as "no-goods" (S5, S9) |
| Interactive theorem proving | Proof assistants where a human or machine supplies steps; kernel checks | Isabelle/HOL, Lean, Coq [V as names] | Med | S8 VERIFY |
| Neural and LLM proof search | Model suggests tactics, search chooses | GPT-f, AlphaProof [M] | Med | S3 plus S4 loop |
| Premise selection | Choosing which known facts to use | Irving et al. [M] | High | retrieval from subgoal library |
| Lemma discovery, conjecturing | Inventing and proving helpful intermediate results | MathlibLemma, arXiv 2602.02561 [V]; Conjecturing-Proving Loop [V] | High | memory: subgoal library, O2 |
| Proof planning and repair | Plans over proofs; fixing broken proofs | Bundy; Ringer [M] | Med | S5 REVISE |
| Autoformalisation | Text to formal statement | Wu et al. 2022 [M] | Low | S2 |
| Counterexample finding | Models that refute a claim | Mace4 (named in Wikipedia) [V]; Nitpick [M] | High | S7 discriminating test |

## Dig into next

1. **Lemma discovery and the proof library.** What makes a conjectured lemma worth keeping (used twice, shortens later proofs)? How is it retrieved without flooding the context? Evidence: the two LLM lemma papers below; our reuse counts.
2. **CDCL-style no-goods.** Can a failed attempt be cut down to a short "this combination fails" and stored for the same problem, as CDCL does with learned clauses that persist through restarts? Evidence: size and reuse rate of no-goods in a small puzzle domain.
3. **Counterexample search as S7 test.** Does running a counterexample finder separate two fitting rules? Evidence: counterexample rate on wrong candidates in our ARC runs.

## Combined with LLMs

Opened, abstract level only, no model names on the pages:
- MathlibLemma (arXiv 2602.02561): an LLM pipeline that mines "folklore" lemmas missing from Lean's Mathlib, formalises and proves them. Outputs: 1,506 Lean-checked proofs that pass a proof-bypass screen, a benchmark of 4,028 type-checked statements, and a small curated subset merged into Mathlib. No success rate given [V].
- Conjecturing-Proving Loop (NALOMA 2026): generates conjectures and proofs in Lean 4, feeding earlier verified theorems and proofs back as context. Claims a higher rate of finding hard-to-prove theorems than generating statement and proof together, and that reusing verified output improves later proof success. No numbers, models or benchmarks on the abstract page [V].
- Wikipedia's article mentions LLMs only in passing [V]. I found no AlphaProof or premise-selection source this session (searches ran out).

## Sources

1. https://arxiv.org/abs/2602.02561 [V] MathlibLemma
2. https://aclanthology.org/2026.naloma-1.5/ [V] Conjecturing-Proving Loop
3. https://en.wikipedia.org/wiki/Automated_theorem_proving [V] overview (first 100,000 characters)
4. https://en.wikipedia.org/wiki/Conflict-driven_clause_learning [V] CDCL
5. https://ic-services.epfl.ch/posters/appdemosposters_get/{cf6a61a6-cd1d-4417-a7fb-28103523cf46}/AI_for_Math_EPFL_Poster.pdf [M] EPFL poster
6. Robinson 1965; Irving et al. 2016; Polu and Sutskever 2020 [M] (no URL)
