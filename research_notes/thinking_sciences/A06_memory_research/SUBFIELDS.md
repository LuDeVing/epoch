# Memory research: subfields

Memory research studies how information is encoded, stored and retrieved. It divides by system (working, episodic, semantic, procedural), by process (encoding, consolidation, retrieval, forgetting) and by organising structure (schemas, networks). For our agent, which has a lesson store and a subgoal library, the retrieval side matters most: what cue finds the right item, what interferes, and how stored schemas bias new work.

## Subfields

| Subfield | What it studies | Key people or works | Useful for our agent | How |
|---|---|---|---|---|
| Encoding specificity and cue-dependent retrieval | Recall is better when retrieval conditions match encoding; a weak cue studied with the target beats a strong cue that was not [V1] | Tulving and Osler (1968); Thomson and Tulving; Godden and Baddeley (1975) | High | memory: key lessons by what will be present at retrieval |
| Critiques of encoding specificity | Match is correlational; cue distinctiveness may drive recall; "outshining": context helps mostly when better cues are missing [V1] | Nairne; Higham; Postman (1975) | Med | use distinctive keys, not only matching ones |
| Interference | Proactive (old blocks new) and retroactive (new blocks old); strongest for related items; proactive buildup is released when category changes [V2] | McGeoch (1932); Underwood (1957); Wickens; Muller and Pilzecker (1900) | High | memory: cap similar entries per class; vary category |
| Cue overload and fan effect | More items per cue lowers retrieval [M; not on the interference page] | Watkins; Anderson | High | library size per cue |
| Schemas | Reconstructive recall (Bartlett's War of the Ghosts); schemas guide attention, fill gaps, create false memories (Brewer and Treyens office study), persist against contrary evidence [V3] | Bartlett (1932); Piaget; Rumelhart (1980); Minsky frames | High | memory structure; also a source of fixation |
| Semantic networks and spreading activation | Memory as a network; activation spreads along links with decay and threshold; semantic priming; used in information retrieval and AI [V4] | Collins and Loftus (1975); Anderson (1983) | Med | S3 grounded retrieval; similarity search |
| Retrieval as consolidation | Retrieval can speed consolidation; schema-consistent info integrates faster [M, search snippet only] | Chinese Advances in Psychological Science 2024 article | Low | background only |
| Retrieval failure view of amnesia | Memory impairments often reversible with right cues [M, snippet only] | Psychological Review 2025 article | Med | supports cue design |
| Working memory | Short-term store and control [M] | Baddeley and Hitch; Cowan | Med | see A08 |
| Retrieval-induced forgetting; memory errors | Recalling some items suppresses related ones; misinformation [M] | Anderson, Bjork and Bjork (1994); Loftus | Med | warning: one lesson may suppress siblings |
| Case-based reasoning | Retrieve, reuse, revise, retain [M] | Kolodner; Schank | High | subgoal library by similarity |

## Dig into next

1. **Encoding specificity and cue design.** Questions: (a) What key should a lesson carry (class, surface words, structure) for the right item to be retrieved? (b) Does a distinctive key beat a matching one, as Nairne would predict? (c) How often does a retrieved lesson mislead? Evidence: retrieval precision and downstream accuracy from our logs; cue manipulations on lesson keys.
2. **Interference.** Questions: (a) At what library size per cue does benefit fall? (b) Does Wickens-style category change reduce buildup (shuffle or vary classes shown)? (c) Do near-duplicate lessons hurt more than unrelated ones? Evidence: library-size ablation at equal tokens.
3. **Schemas and case-based reasoning.** Questions: (a) What schema-like structure (class, preconditions, operator that worked) supports reuse? (b) When should a retrieved case be adapted or rejected? Evidence: Kolodner's cycle compared to our S9 record; Brewer and Treyens-style test of schema-induced false recall in model summaries.

## Does not transfer

Decay over time, sleep and emotional consolidation, state-dependent effects (alcohol, mood), ageing effects, false memory driven by suggestion and brain systems are about biological memory. Our store has no forgetting unless we build it, and the context window is not Baddeley's working memory.

## Sources

[V] = opened this session with WebFetch. [M] = memory or search snippet only.

1. [V] Encoding specificity principle, Wikipedia: https://en.wikipedia.org/wiki/Encoding_specificity_principle
2. [V] Interference theory, Wikipedia: https://en.wikipedia.org/wiki/Interference_theory
3. [V] Schema (psychology), Wikipedia (first 100k characters): https://en.wikipedia.org/wiki/Schema_(psychology)
4. [V] Spreading activation, Wikipedia: https://en.wikipedia.org/wiki/Spreading_activation
5. [M] Oxford Handbook of Human Memory contents: https://memory.psych.upenn.edu/Oxford_Handbook_of_Human_Memory (not opened)
6. [M] Schema-based consolidation article: https://journal.psych.ac.cn/xlkxjz/EN/Y2024/V32/I11/1854 (not opened)
7. [M] Retrieval failure article: https://researchconnect.suny.edu/en/publications/rethinking-memory-impairments-retrieval-failure/ (not opened)
