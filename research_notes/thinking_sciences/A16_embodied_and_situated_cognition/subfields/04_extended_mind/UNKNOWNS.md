# Extended mind: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| A16.04-U1 | Do curated persistent notes beat the same tokens spent on longer reasoning or a vote, across separate sessions? | Notes store as a standard part of the loop for recurring problem classes | memory, G7 | K29, K30 (d09, d10, d11); contested; Claude 3.5 Sonnet and Gemini 2.5 Flash only; token match not exact | Streams of 30-50 related tasks; (a) notes, (b) equal tokens on longer reasoning or 3-5 sample vote; accuracy per stream; 100+ items per arm | Notes beat (b) by >= 3 points, paired CI above 0, no loss on unrelated streams | High |
| A16.04-U2 | How often does the agent follow a wrong note it wrote itself, and ignore a right one? | Provenance flags and a verify-before-trust step | memory, G2 | K25 (d05); single-source; facts only, not agent notes | Twin Otto: right note, wrong note, no note; known-answer items; follow rate and ignore rate | Wrong-note follow rate > 10% without flags, and flags cut it by >= 30% relative with ignore rate up by <= 3 points | High |
| A16.04-U3 | Does a confidence-based consult gate beat always-consult and never-consult? | Consult gate in S0/S3 | G12, O, memory | K26, K27 (d05, d07, d08); gate idea established, agent version untested | Mixed hard and easy items with a notes store; arms: always, never, confidence gate, check-failed gate; accuracy and tokens | Gate >= best fixed arm in accuracy and >= 20% fewer tokens | High |
| A16.04-U4 | Which note format wins: raw rounds plus fact keys, session summaries, linked notes, verified skills? | One default note format | memory | K21, K32 (d12, d13, c22); vendor claims not independent | Multi-session question set; four formats; recall@k and accuracy | Winner beats flat raw notes by >= 3 points accuracy | High |
| A16.04-U5 | When two notes conflict, does a code rule (newest verified) beat letting the model choose? | Code-side conflict resolver and note versioning | memory, G5 | K28 (d06); single-source; facts, GPT-4 | Seed conflicting notes; arms: model picks, code picks; accuracy | Code rule >= +5 points | Med |
| A16.04-U6 | Does a reflection note beat storing the raw trajectory outside coding? | Reflection step after failure, in classes where it wins | O, memory | K16, K33 (a27, d14, d15); contested; domain split | Failure-retry on coding with tests and QA with and without feedback; arms: reflection, raw trajectory, nothing | Reflection beats raw by >= 3 points only with an outside check; then write reflections only after checks | Med |
| A16.04-U7 | Does note placement (start, middle, end) matter for current models? | Fixed placement rule for the notes block | memory | K15, K34 (b21, d16); no 2026 frontier test | Same note at three positions; accuracy; prompt lengths 2K, 8K, 32K | End or start beats middle by >= 3 points at some length | Low |
| A16.04-U8 | Does reading notes lower the agent's own later reasoning on an unannounced follow-up? | Rule to restate key facts in own words after reading | memory | K07 (b06); human only | Read notes then follow-up needing the same content, vs solve unaided; accuracy | Note readers are >= 5 points lower | Low |
| A16.04-U9 | Does telling the agent a store exists lower content recall and raise key recall (Google effect)? | A rule to write content, not only pointers | memory | K03 (a19, d04); contested, human only | Notice vs no notice; recall of content and keys | Content recall drops >= 5 points with key recall flat or up | Low |
| A16.04-U10 | Does the agent stay calibrated after retrieval, or become overconfident? | Confidence reset after retrieval and a verify step | G | K09, K12 (a17, c28); human only | Ask confidence before and after retrieval; compare to correctness (Brier score) | Brier score worse after retrieval by >= 0.03 | Med |
| A16.04-U11 | Do only verified entries belong in the skill library? | Verified-only library rule | memory, G3 | K18 (c13, c14); single-source; Minecraft code | Repeated procedure tasks; store verified only vs store all; success on reuse | Verified-only beats store-all by >= 5 points | Med |
| A16.04-U12 | Does saving block 1 to notes help the agent on block 2? | Early-save step for long inputs | memory | K05 (a12); human only | Save vs no save vs unreliable save; block-2 accuracy | Save beats no save by >= 3 points and unreliable save does not | Low |
| A16.04-U13 | Does a plain chunked-retrieval default beat a memory product on our tasks? | Plain retrieval as the baseline, no memory product | memory, G7 | K31 (d12); single independent benchmark, GPT-4o-mini | Arms: bare model, BM25, embeddings, one memory product; accuracy and tokens | Plain retrieval within 2 points of the product at lower tokens | Med |

## Open questions we cannot test on our bench yet
- Whether the extended-versus-embedded dispute has any testable consequence for an agent. Nothing in the evidence separates the views. Unblock only if someone states a behavioural prediction that differs.
- Redundancy (does a persona or prompt-only version equal retrieval?). Needs a matched persona-only arm and a metric beyond judge opinion (c02, c04).
- Agency: whether the model, not the app, should decide when to retrieve. Needs a tool-call version of the gate and logs of who triggered each read.
- Skill atrophy (GPS-style): applies only if we ever fine-tune on agent outputs; no fine-tuning arm exists.
- Peer-reviewed replication of Kosmyna and of Sparrow Experiments 2-4: outside our bench; wait for the literature.
- Sources of the Google meta-analysis d range and Voyager ratios: need the source tables.
- 2026 frontier models for lost-in-the-middle and ClashEval: need runs on the current model.

## Order to run
1. U1 (notes vs equal-token reasoning): decides whether the library earns its place at all (G7); highest expected gain.
2. U2 (Twin Otto on our own notes): cheap, and the answer sets how much trust and provenance machinery notes need.
3. U3 (consult gate): cheap once U1 has a store, and it sets when notes are read at all.
