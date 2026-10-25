# Model-based diagnosis: subfields

Model-based diagnosis finds which part of a system is faulty by comparing what a model says should happen with what is observed. Reiter's 1987 theory defines a conflict as a set of components that cannot all be normal given the observations, and a diagnosis as a minimal hitting set of the conflicts. The field divides into consistency-based diagnosis, abductive diagnosis, hitting-set search algorithms, measurement (probe) selection, diagnosability, and applications to software, spreadsheets and knowledge bases. For us it gives a precise way to do S5 (locate the fault by code) and S7 (pick the next test that best separates suspects). Marks: [V] = page opened this session and read; [M] = from memory or seen only in a search result. Honest limit: the readable sources here are thin, and two PDFs could not be read by the fetch tool.

## Subfields

| Subfield | What it studies | Key people or works | Useful (H/M/L) | How |
|---|---|---|---|---|
| Consistency-based diagnosis | Diagnoses as minimal hitting sets of conflicts | Reiter 1987 [M]; definition confirmed by tool summary of a PDF I could not read | High | S5: locate failing step by code |
| Abductive diagnosis | Best explanation by simulating a model and comparing with observations; "Ab" predicate for abnormal behaviour | Wikipedia article [V] | Med | O8 reframe, hypotheses |
| Conflict generation, GDE | Find sets that cannot all be normal; multiple-fault diagnosis | de Kleer and Williams 1987 [M] | High | S4 to S5 handoff |
| Hitting-set tree search | Breadth-first tree; DAG fix for non-minimal conflicts | Reiter; Greiner et al. [M] | Med | control: search over suspects |
| Efficient diagnosis algorithms | New hitting-set algorithms (RBFR-HS), ontology debugging | Jannach et al., IJCAI 2023 (section outline only readable) [V] | Low | background only |
| Probing and measurement selection | Choose the next measurement that best splits diagnoses | de Kleer and Williams [M] | High | S7 discriminating test |
| Diagnosability | Whether behaviour always yields one diagnosis; guides sensor placement | Wikipedia article [V] | Med | test design |
| Spectrum-based fault localisation | Rank code by pass/fail coverage | Abreu et al. [M] | High | S5 on program attempts |
| Readings in model-based diagnosis | Standard reference | Hamscher, Console, de Kleer 1992 [V as citation] | Med | reading list |
| Software, spreadsheet, KB debugging | Applying diagnosis to artefacts | Jannach et al. [M] | Med | S5 REVISE |

## Deep research

One folder per subfield in `subfields/`. Read `DEEP.md` first; section 7 is what the agent should take, section 8 the tests. `UNKNOWNS.md` lists what we don't know and must test before adding. The field synthesis is [`SYNTHESIS.md`](SYNTHESIS.md).

| Subfield | Deep document | Status |
|---|---|---|
| Consistency-based diagnosis | [`subfields/01_consistency_based_diagnosis_and_conflicts/DEEP.md`](subfields/01_consistency_based_diagnosis_and_conflicts/DEEP.md) | done, batch 3 (2026-10-26) |
| Abductive diagnosis | | not started |
| Conflict generation, GDE | covered in [`subfields/01_consistency_based_diagnosis_and_conflicts/DEEP.md`](subfields/01_consistency_based_diagnosis_and_conflicts/DEEP.md) | done, batch 3 (2026-10-26) |
| Hitting-set tree search | | not started |
| Efficient diagnosis algorithms | | not started |
| Probing and measurement selection | [`subfields/06_probing_and_measurement_selection/DEEP.md`](subfields/06_probing_and_measurement_selection/DEEP.md) | done, batch 3 (2026-10-26) |
| Diagnosability | | not started |
| Spectrum-based fault localisation | | not started |
| Readings in model-based diagnosis | | not started |
| Software, spreadsheet, KB debugging | | not started |

## Dig into next

1. **Probing and measurement selection.** Given surviving rules or suspect steps, how do we pick the input that best separates them? Can code compute the entropy over candidates? Evidence: a worked ARC case; how often the chosen probe removes at least one candidate; the Hamscher, Console, de Kleer readings (not yet obtained).
2. **Conflict sets for attempts.** If each step of an attempt has a check, can code find the minimal set of steps that explains a failure? Evidence: step-level checks on our programs; agreement with the step an LLM would blame (models blame poorly, G2).
3. **Spectrum-based localisation.** With several passing and failing attempts, does coverage ranking beat model blame? Evidence: a code task set with seeded faults.

## Combined with LLMs

Nothing found. The two search-quota attempts to run LLM-specific queries ("LLM model-based diagnosis", "spectrum-based fault localization LLM") failed because the session search budget was used up, so this is a gap in my search, not proof that no work exists. The opened pages (Wikipedia on diagnosis and model-based reasoning, Jannach et al. section outline) mention no LLMs. Next step for whoever has search access: run those queries and read any LLM fault-localisation or hitting-set papers.

## Sources

1. https://en.wikipedia.org/wiki/Diagnosis_(artificial_intelligence) [V] model-based diagnosis, abduction, diagnosability
2. https://en.wikipedia.org/wiki/Model-based_reasoning [V] general (no Reiter content)
3. https://www.ijcai.org/proceedings/2023/0789.pdf [V] only section headings readable
4. https://arxiv.org/pdf/cs.AI/0003051 [V] fetched but PDF unreadable; not used for claims
5. https://cs.ru.nl/P.Lucas/teaching/KeR/mbr2.pdf [M] lecture notes
6. https://papers.phmsociety.org/index.php/ijphm/article/view/2363 [M] hitting-set algorithms
7. Reiter 1987, A theory of diagnosis from first principles; de Kleer and Williams 1987 [M] (no URL)
