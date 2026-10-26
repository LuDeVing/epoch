# Chess and game expertise: subfields

Chess has been the main laboratory of expertise research since de Groot. The field divides into thought-process studies, memory and pattern theories (chunking, templates), search and look-ahead, skill acquisition, and computer chess and game AI. Opened pages confirm de Groot's staged account and the chunking account of expert memory. They do not mention progressive deepening or search depth, so those claims, and the template theory details, rest on search snippets or memory and need a primary source. Chess has full information and an exact result, so it is a clean test bed, but a narrow one.

## Subfields

| Subfield | What it studies | Key people or works | Useful for our agent | How |
|---|---|---|---|---|
| Thought-process studies | Think-aloud protocols; four phases: orientation, exploration, investigation, proof; much of the move is chosen in the first seconds | de Groot [V via Wikipedia] | High | States S2 to S4, S8 (proof phase = verify) |
| Progressive deepening and search depth | Return to a line and go deeper; skill differences in search depth are small | de Groot [M]; Gobet snippet only [M] | High | S4 and S5 loop; tree limits |
| Chunking | Chunks of 2 to 6 items; experts recall real positions far better, but the gap shrinks on random positions, so knowledge, not raw memory, drives it | Chase and Simon 1973; Gobet, de Voogt, Retschitzki 2004 [V via Wikipedia] | High | Memory (subgoal library) |
| Computational chunk models | EPAM and CHREST simulate learning of chunks | Simon, Gobet [V via Wikipedia] | Med | Memory design |
| Template theory | Frequent chunks gain a fixed core and slots; used as retrieval keys | Gobet and Simon 1996, 1998 (snippet only, [M]) | High | Memory retrieval |
| Pattern-recognition theory of search | Templates guide and shorten search | Gobet 1997 (snippet only, [M]) | High | S0 gate |
| Recognition-primed decisions | Chess players listed among groups using the first workable option; needs experience; fails in unusual situations | Klein [V via Wikipedia RPD page] | High | Mode choice |
| Einstellung effect | A familiar solution blocks a better one | Bilalic et al. 2008 [M] | High | Guardrail (fixation); S3 history |
| Computer chess and game AI | Alpha-beta, Monte Carlo tree search, self-play | Deep Blue, AlphaZero [M] | High | Tree search at S6 |
| Deliberate practice | Practice type and skill | Ericsson [M] | Low | Background only |

## Deep research

One folder per subfield in `subfields/`. Read `DEEP.md` first; section 7 is what the agent should take, section 8 the tests. `UNKNOWNS.md` lists what we don't know and must test before adding. The field synthesis is [`SYNTHESIS.md`](SYNTHESIS.md).

| Subfield | Deep document | Status |
|---|---|---|
| Thought-process studies | [`subfields/01_thought_process_and_progressive_deepening/DEEP.md`](subfields/01_thought_process_and_progressive_deepening/DEEP.md) | done, batch 4 (2026-10-26) |
| Progressive deepening and search depth | covered in [`subfields/01_thought_process_and_progressive_deepening/DEEP.md`](subfields/01_thought_process_and_progressive_deepening/DEEP.md) | done, batch 4 (2026-10-26) |
| Chunking | covered in [`subfields/05_chunks_and_templates/DEEP.md`](subfields/05_chunks_and_templates/DEEP.md) | done, batch 4 (2026-10-26) |
| Computational chunk models | | not started |
| Template theory | [`subfields/05_chunks_and_templates/DEEP.md`](subfields/05_chunks_and_templates/DEEP.md) | done, batch 4 (2026-10-26) |
| Pattern-recognition theory of search | | not started |
| Recognition-primed decisions | | not started |
| Einstellung effect | | not started |
| Computer chess and game AI | | not started |
| Deliberate practice | | not started |

## Dig into next

1. **Staged thought process and deepening.** Questions: Do de Groot's four phases map onto S1 to S8, with "proof" as an extra check on the chosen line before submitting? What is the exact pattern of returning to a line, and how does it compare with our tree limits (3 children, depth 2)? Evidence needed: de Groot's protocols and Gobet's reviews (the PDFs I tried were unreadable).
2. **Chunks and templates as memory.** Questions: What is the unit of a reusable subgoal, a core plus slots? How are partial matches retrieved without false matches? Evidence needed: CHREST papers; similarity retrieval tests on solved problems.
3. **Einstellung.** Question: Does a known pattern block a better answer in LLMs? Does showing lessons only after a first attempt help? Evidence needed: Bilalic et al.; an A/B test.

## Does not transfer

Chess has full information, fixed rules and a clear result. Skill-growth findings (practice hours, age of starting) concern human learning. Memory limits of about two to six chunks are human limits. Findings transfer best to problems that also have an exact check.

## Sources

[V] means opened this session with WebFetch. [M] means memory or search snippet only.

1. [V] Wikipedia, Adriaan de Groot: https://en.wikipedia.org/wiki/Adriaan_de_Groot
2. [V] Wikipedia, Chunking (psychology): https://en.wikipedia.org/wiki/Chunking_(psychology)
3. [V] Wikipedia, Recognition primed decision: https://en.wikipedia.org/wiki/Recognition_primed_decision
4. [M] Brunel repository paper (fetched, unreadable): https://bura.brunel.ac.uk/bitstream/2438/822/4/1791.pdf
5. [M] Gobet, A pattern-recognition theory of search in expert problem solving: https://api.philpapers.org/rec/GOBAPT
6. [M] de Groot (1965), Thought and Choice in Chess.
7. [M] Bilalic, McLeod, Gobet (2008), Why good thoughts block better ones, Cognition.

Opened sources: 3.
