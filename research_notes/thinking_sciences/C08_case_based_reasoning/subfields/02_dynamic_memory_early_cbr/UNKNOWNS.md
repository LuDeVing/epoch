# Dynamic memory, early CBR: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| C08.02-U1 | Does lesson memory beat best-of-N without memory on reasoning items? | Lesson store read at S3/S5 | memory, G7 | K07 contested; K27 single-source (web only); Memento and ReasoningBank disagree (a23, d01) | Arms: best-of-N no memory; best-of-N plus lessons; 1 attempt plus lessons. Stream of 100+ items, recurring classes. Accuracy | Memory arm beats best-of-N by 3+ points with CI excluding 0 on recurring classes | High |
| C08.02-U2 | Is a self-judge good enough as write gate, or is a verified signal needed? | Gate rule per memory form | memory, G2 | K28 single-source (simulated flips only); K13 established for add-all harm (c12) | Arms: verified-only; self-judge; add-all. Same stream. Accuracy at item 50 and 100; memory size | Judge within 3 points of verified at equal tokens; else verified only | High |
| C08.02-U3 | How often are lessons promoted from 2 episodes wrong? Best confirm count? | Promotion threshold N and a demote step | memory | K02, K30 single-source; no rate anywhere; CYRUS value 6 is unfitted (a03, d12) | Promote at 2, 4, 6 confirmations. Test each lesson on held-out items. Wrong-lesson rate; accuracy | A threshold halves the wrong-lesson rate with under 1 point accuracy loss | High |
| C08.02-U4 | Does cue elaboration (infer missing situation features) raise hit rate? | Elaboration step before retrieval | memory, S0 | K04 established as design only; K31: no agent test, only HyDE for documents (d14) | Arms: raw query key; LLM-inferred feature key; both. Thin-cue items with labelled right lesson. Top-3 hit rate; accuracy | Hit rate up 5+ points and accuracy not lower | Med |
| C08.02-U5 | Is a feature or keyword key better than a task embedding or trace key on diverse tasks? | Key type for case index | memory | K09, K29 single-source, recurring tasks only (c07, d06) | Arms: raw embedding; LLM keywords; reasoning-trace embedding. Mixed-class stream. Hit rate; accuracy | Best key beats embedding by 2+ points accuracy | Med |
| C08.02-U6 | Lessons only, raw cases only, or both? | Two-layer memory | memory | K10 established but task dependent (ExpeL ALFWorld 50 vs 55, HotpotQA 36 vs 31) | Three arms per class type, equal tokens. Accuracy | Both beats best single arm by 2+ points on most class types | Med |
| C08.02-U7 | Do failure-derived lessons help or hurt? | Failure lessons with a "what went wrong" field | memory, S9 | K12 established but design dependent (AWM falls 44.4 to 42.2; ReasoningBank rises 46.5 to 49.7) | Success-only vs success plus distilled failures vs raw failures. Accuracy | Distilled failures add 2+ points and raw failures do not | Med |
| C08.02-U8 | Does matched content matter, or is part of the gain generic guidance? | Decision on matching cost | memory | K29: random cases beat none (74.59 vs 71.93, d06) | Arms: matched lessons; random lessons; none; same count. Accuracy | Matched beats random by 2+ points, else drop matching | Med |
| C08.02-U9 | Does memory help weak backbones, and in which form? | Rule: memory form by model strength | memory, G | K15 established for failure; counter-case Gemma-3-12B 17.1 to 24.1 (d04) | Small and strong model; raw vs distilled form. Accuracy | Distilled helps the weak model by 3+ points while raw does not | Med |
| C08.02-U10 | Does a library of verified helper programs speed solving? | Subgoal library (already planned) | memory, O | K20 single-source (Voyager); DC Game of 24 10 to 99 (c15, c18) | Arms: no library; library by description; library by situation features. Items where helpers recur. Accuracy; tokens | Library gains 5+ points on recurring helper items, no loss elsewhere | Med |
| C08.02-U11 | Is reading the whole history better than memory when it fits? | Switch rule: read all vs retrieve | memory, G7 | K21 established for chat recall; unknown for reusable know-how (c19, c20) | Arms: full history; top-k lessons. Streams short enough to fit. Accuracy; tokens | Memory wins at equal tokens; otherwise read all below a length cutoff | Med |
| C08.02-U12 | Does utility pruning keep accuracy while shrinking memory? | Use-count plus mean-utility prune | memory | K14 single-source (Xiong): about 4x smaller, 2-4 points lower (b15) | Arms: no prune; prune (retrieved 3+ times and low utility). After 200 items. Accuracy; size | Size down 3x with accuracy loss under 2 points | Low |
| C08.02-U13 | Does note linking (A-Mem style) beat a flat lesson list? | Linked notes | memory | K22 contested; third-party scores low (44.54 vs base 52.18, d15) | Own replication vs flat lessons. Accuracy; time | Beats flat store by 3+ points at equal tokens | Low |

## Open questions we cannot test on our bench yet
- Primary human data (Bower, Black and Turner 1979; Reiser et al. 1985; Williams and Hollan 1981; Schank 1982). Unblock: library or paywall access. Low value for the agent.
- Independent replication of Agent Workflow Memory. Unblock: a third party; we have no web-task testbed.
- Early CBR accuracy figures. None exist. Nothing to unblock.
- Wrong-lesson rate for lessons written by other models. Unblock: a labelled lesson set from U3.
- Capability threshold for memory by model size. Unblock: three or more backbone sizes on the same stream.
- Transfer of web-agent results to pure reasoning at frontier level. Unblock: U1.
- Cue elaboration inside an episode memory for agents. Unblock: U4 and a labelled "right lesson" set.

## Order to run
1. U1 (memory vs best-of-N at equal tokens): decides whether any case memory is worth its tokens; every other test builds on it.
2. U2 (write gate): the largest effect in the literature (12-25 points) and cheap to run; it sets the rule for what enters memory.
3. U3 (promotion threshold and wrong-lesson rate): the one core early-CBR rule never measured; it shapes the lesson trust rule already in SCHEMA section 5.
