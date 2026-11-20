# Deployed CBR: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| C08.03-U1 | Does verified case memory beat no memory and random items on our reasoning items? | A verified-case store, 1 to 4 items, shown after the first attempt | memory, S3 | K08, K10, K18; agent benchmarks only (c18, b20, d09) | Arms: none; random 2; top-2 similar verified; 3 seeds; recurrent-class items; solve rate | Similar beats both none and random by 5+ points, 95 percent CI above 0 | High |
| C08.03-U2 | Raw cases or distilled lessons: which wins per task type? | Per-class rule: raw or lesson | memory | K09, K17 contested (d01, d06, d08, a31, c14); not token-matched | Raw vs one-line lessons vs none; matched tokens incl. curator; per item type | One form wins by 3+ points on a type in 2 of 3 seeds, else keep lessons | High |
| C08.03-U3 | Gated write-back size on our stream | Retain only on verified pass | memory, G2 | K16 direction established (d04); Re4 magnitude unknown (c11) | Frozen vs add-all vs gated; 300+ item stream; accuracy and store size | Gated beats frozen by 2+ points and add-all by 5+ | High |
| C08.03-U4 | Failed cases as distilled lessons or contrast pairs | Failure lessons in memory | memory, S7 | K04 contested (a05, d02, d13); raw failures hurt | Successes only vs plus raw failures vs plus distilled failures; repeat-error rate | Distilled failures cut repeat errors 20 percent relative with no accuracy loss | Med |
| C08.03-U5 | Retrieve by failing output instead of problem text | Error-keyed lookup at repair | S7, memory | Single industry source (c17) | Problem-keyed vs error-keyed; code repair items; pass@1 after one repair | Error-keyed +5 points cross-domain | Med |
| C08.03-U6 | Context filter before retrieval | Context tags on cases | memory, S0 | K05 single-source, human-only (a06); no LLM test (d18) | Similarity vs similarity plus same-context filter; items where context flips the answer | +5 points on flipped-context items, no loss elsewhere | Med |
| C08.03-U7 | Refine a retrieved case against execution output before reuse | Code-checked Revise on a case | O7, S5 | K13 single-source (c14, d11) | Reuse as is vs refine with execution; checkable items | Refine +3 points at equal tokens | Med |
| C08.03-U8 | Use memory only at impasse or above a similarity threshold | Similarity gate and impasse trigger | G1, G12, S6 | K18 mechanism (d05, d09); no threshold in any source | Always on vs gated by similarity score vs impasse only; mixed novel and recurrent items | Gate removes harm on novel items and keeps 90 percent of gain on recurrent | High |
| C08.03-U9 | Executable cases beat text lessons on code-like items | Store programs, not prose, for code classes | memory | Single source (c14, b26) | Program cases vs text lessons; ARC program items | Programs +3 points | Med |
| C08.03-U10 | Is the K = 1 to 4 optimum general on our items? | Fixed K default | memory | K07 established on agent tasks (b11, d03) | K 0, 1, 2, 4, 8 | Peak within 1 to 4 and flat after | Low |
| C08.03-U11 | Does the Memento gain survive a disjoint case bank? | Confidence in K06 | memory | K19 single-source, unreplicated; contamination suspected | Case bank from disjoint training tasks only; same planner | Gain stays 3+ points | Low |
| C08.03-U12 | Does persistent memory cut exploration in open mode? | Memory off in open mode | G12, S3 | K14 four seeds; NOMAD worse (c15) | Open-mode NoveltyBench with and without memory; 8+ seeds; diversity score | Memory lowers diversity: keep it off in open mode | Med |

## Open questions we cannot test on our bench yet
- A controlled before/after study of a 1990s deployed CBR system with N and baseline. Needs the paywalled primary papers (Mark 1989; Hennessy and Hinkle 1992) or industry archives.
- The size of the Retain effect in Re4. Needs the figure image or the authors' table.
- Real recurrence rate of our items. Needs a task-embedding analysis of the bench before deciding if memory can help (r 0.563 to 0.717 is within agent datasets).
- Human-in-the-loop revise (CLAVIER style). Our agent has no human at runtime; a ground-truth checker would stand in.
- Token-matched comparisons from the literature. None exist; only our own runs can close them.

## Order to run
1. U1 (memory vs random vs none): tells us if memory is worth anything on our items; cheap, and every other test reuses its arms.
2. U3 (gated write-back vs add-all vs frozen): best established direction with an unknown size; decides whether any Retain step ships.
3. U8 (similarity gate): sets when memory may fire and guards against the harm seen in c18 and c15; reuses U1 data.
