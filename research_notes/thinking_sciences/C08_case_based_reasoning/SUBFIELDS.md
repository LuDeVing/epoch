# Case-based reasoning: subfields

Case-based reasoning (CBR) solves a new problem by finding similar past problems and adapting their solutions. The standard cycle is Retrieve, Reuse, Revise, Retain (Aamodt and Plaza 1994). The field divides by phase (representation, retrieval and similarity, adaptation, retention and maintenance) and by domain (law, medicine, planning, design). It is the closest classical match to our memory: a library of solved subgoals offered by similarity, with a rule for what to keep. Marks: [V] = page opened this session; [M] = from memory or seen only in a search result.

## Subfields

| Subfield | What it studies | Key people or works | Useful (H/M/L) | How |
|---|---|---|---|---|
| The 4R cycle | Retrieve, reuse, revise, retain | Aamodt and Plaza 1994 (named in Wikipedia) [V] | High | memory and control |
| Dynamic memory, early CBR | Memory organised by episodes | Schank; Kolodner (CYRUS); Lebowitz (IPP) [V via Wikipedia] | Med | memory design |
| Deployed CBR | First successful system | Bill Mark, CLAVIER [V via Wikipedia] | Low | background only |
| Case representation | What a case stores: problem, solution, outcome | Kolodner [M] | High | S9 record format |
| Retrieval and similarity | Nearest cases | Weber; Richter [M] | High | memory retrieval |
| Adaptation | Edit a retrieved solution | Leake [M] | High | S5, O7 |
| Case-base maintenance | Prune, dedupe, keep cases useful | Smyth and Keane; Leake and Wilson [M] | High | when to retain |
| Retention policy | Which new cases to store | CASCADE, arXiv 2605.06702 [V] | High | S9 LOOK BACK |
| Retrieval as a bandit | Choose cases by learned value | CASCADE [V] | High | selection |
| Failure-driven CBR | Keep failures with explanations | Schank; Kolodner [M] | Med | lessons with traps |

## Dig into next

1. **Retention and maintenance.** What is the smallest case record that still lets a later problem reuse it? When does a new case duplicate an old one? Does storing only successes lose useful traps? Evidence: CASCADE-style ablation; our reuse counts and harm cases (a retrieved case that misleads).
2. **Retrieval as a learned choice.** CASCADE treats retrieval as a contextual bandit. Can we do the same on our class record? Evidence: hit rate of top-k cases on held-out same-class and different-class problems.
3. **Adaptation as a typed edit with a check.** Evidence: pass rate of adapted solutions against a fresh attempt at equal tokens.

## Combined with LLMs

- CBR + Re4 for functional test-script generation (arXiv 2503.20576, KDD 2025), full text read in part. Retriever: bge-m3. LLM: an internal model of about 7B parameters, fine-tuned with LoRA. Data: two Huawei Datacom product units (DCN, SP). Metric FF1 (function F1), single run. DCN: naive SFT 49.46, naive CBR 64.01, CBR 64.67, CBR+SFT 67.87, CBR+Re4 70.11. SP: naive SFT 38.71, naive CBR 54.60, CBR 55.83, CBR+SFT 57.98, CBR+Re4 61.92. So retrieval alone gave about 15 points over fine-tuning alone; the Re4 training added 2 to 4 more [V].
- CASCADE (arXiv 2605.06702, preprint): retrieval as a contextual bandit (Neural-LinLogUCB), only memory updates, no weight changes. 16 tasks including ALFWorld, ScienceWorld, MIMIC-III. Models Qwen3 (including 32B) and Gemini-2.0-Flash. Reported: +20.9 percent macro success over zero-shot; Qwen3-32B single-turn 66.68 against 48.33 zero-shot; MIMIC-III 20.75 to 55.76; ALFWorld nearly doubled. The 20.9 figure does not obviously match the 18.4 point gap in the Qwen3-32B example, so the metric definition needs checking in the full paper [V, abstract page only].
- "Direct LLM retrieval matches k-NN only 20 to 28 percent of the time" (Wilkerson and Leake) was seen only in a search summary [M]; not relied on.

## Sources

1. https://arxiv.org/html/2503.20576v2 [V] CBR for test script generation
2. https://www.alphaxiv.org/abs/2605.06702v1 [V] CASCADE
3. https://en.wikipedia.org/wiki/Case-based_reasoning [V] overview
4. https://arxiv.org/pdf/2504.06943v1 [M] CBR and LLM paper
5. https://www-live.dfki.de/fileadmin/user_upload/import/15846_2025_ICCBR_EXAR_BergmannEtAL.pdf [M] EXAR
6. Aamodt and Plaza 1994, Case-based reasoning: foundational issues [M] (no URL)
