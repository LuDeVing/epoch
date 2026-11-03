# Distributed cognition theory: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| F02.01-U1 | Does a real interpreter beat model-simulated execution on current models | Rule: computable steps go to a real executor, never simulated | O tool/check step; G | K01, K28; single-source, Codex-era; ToRL and CoC are not equal-token | CoT vs real-run code vs code with model-simulated result; GSM8K, large-number variant, code-trace items; accuracy | Real beats simulated by 10+ points and beats CoT by 5+ at equal tokens, on 2 model families | High |
| F02.01-U2 | Does large-number robustness hold for code offload | Route arithmetic-heavy items to code | O tool step | K02; single-source (GSM-HARD cells differ between text and table) | Original vs scaled-number items; CoT vs code; accuracy drop | CoT drops 15+ points more than code | Med |
| F02.01-U3 | Does a rule-based verifier loop beat model self-critique | Verifier-backprompt loop as default where a verifier exists | G external critic; S verify | K11, K04; results cited from other papers, older models | Blocks World and constraint puzzles; self-critique vs verifier backprompt, same calls; plan validity | Verifier arm 20+ points above self-critique and above plain | High |
| F02.01-U4 | Does a cheap re-entry cue (Wait, role flip) restore self-correction on our model | Cue layer before the external check | O verify / re-entry | K25; single-source, injected errors, non-reasoning models | Items with natural errors; none vs cue vs cue plus external check; accuracy | Cue gains 5+ points over none at under 10% extra tokens | Med |
| F02.01-U5 | Does an explicit final verification step help our loop | Mandatory verify state before submit | S verify | K08, K09; one system (ChatDev), LLM-annotated | Loop with and without final verify on mixed tasks; accuracy and premature-stop rate | +5 points, or premature stops halved, with token cost under 10% | Med |
| F02.01-U6 | Single thread vs decomposition by task structure; is 45% usable as a threshold | Router: single on sequential, decompose only on independent subtasks | O decompose; G12 | K10, K23; correlational, threshold fitted on same benchmarks | Single, voting, debate, centralised decomposition on tagged sequential and parallel items; accuracy per type | Decomposition wins by 5+ points on parallel items and ties or loses on sequential; threshold predicts the winner in 80%+ of our task types | High |
| F02.01-U7 | Does a visible scratch field help beyond hidden reasoning | Scratch field for long-chain and trace items only | S working notes | K03; older and fine-tuned models; null on real MBPP | Long arithmetic and trace items; hidden vs visible scratch | +5 points on long-chain items, no loss elsewhere | Low |
| F02.01-U8 | Is probe-to-think (cheap external action) better than pure thought | Epistemic-action operator: test or print before reasoning it out | O act/probe | K17; human Tetris only, no LLM test | Items where a cheap probe exists; think-only vs probe allowed | Probe arm +5 points and probe cost below the reasoning cost it replaces | Med |
| F02.01-U9 | Voting vs one long chain by difficulty | Difficulty-based split of sample count vs chain length | G11, G12 | K07, K27; abstract-level, older models | Fixed tokens; N short plus vote vs one long chain; easy, medium, hard tiers | Voting wins on hard tier by 5+ points with no loss on easy | Med |
| F02.01-U10 | Which memory design pays on long tasks: long context, notes file, retrieval | Notes or retrieval layer only where it beats plain context | memory | K12, K26; authors' benchmark and independent benchmark disagree | Long-conversation recall plus selective-forgetting items; four arms; score retrieval and forgetting apart | Layer beats long context by 5+ points at equal tokens | Med |
| F02.01-U11 | Relation-organised notes vs flat notes | Notes grouped by relation | memory design | K29; human only (d=1.04) | Same notes, flat vs categorised; later recall of related items | +5 points on relational recall | Low |
| F02.01-U12 | Do stored verified routines help on repeated task families | Skill store of tested code | memory | K13; Minecraft, GPT-4, 3 runs | Task families seen repeatedly; with and without routine store; accuracy and tokens on later items | Later items +10 points or 20% fewer tokens, no harm on new families | Low |
| F02.01-U13 | Which MAST failure modes does a fixed non-LLM harness remove | Harness-level termination and verification checks | G; S | K08; no direct test | Log premature stop, missed completion, missing verification; harness off vs on | Failure rate in those modes halves | Med |
| F02.01-U14 | Are our scratch notes faithful about injected hints | Audit rule on traces (G10 stays) | G10 | K14, K24; established on others' models, not on ours | Inject a hint; compare answer shift with mention in notes | Report only; raise weight on executed checks if mention rate is under 50% | Low |

## Open questions we cannot test on our bench yet

- Direct tests of DC or extended-mind predictions (coupling strength, offloading threshold) on LLM agents: no paper found, and the search was rate-limited. Unblock: repeat the literature search, then design a threshold sweep.
- Zhang and Norman 1994 and the Vallee-Tourangeau digits: unopened or unverified. Unblock: obtain the PDFs.
- Independent replications of interactivity effects: none found. Human-only, not needed for the agent, but it limits the weight given to the human literature.
- Whether Kim's 45% threshold holds outside its six benchmarks: needs our own task types and enough items per cell (their CI is about 20 points at n=20).
- Multi-agent tests with truly independent information (different tools or documents per agent), where social scaffolds might help: our bench has no such task type.
- Second half of MemoryAgentBench (not read): may change the memory advice.
- Camerer 2018 per-study outcomes and the collective-intelligence papers (Woolley, Riedl, Ren and Argote) were not opened.

## Order to run

1. U1 (real vs simulated execution): biggest known effect, cheapest to build, and it decides whether code offload gets a hard rule.
2. U3 (rule-based verifier vs self-critique): tests the external-signal principle on our model and sets the default check design.
3. U6 (routing by task structure): decides when decomposition is allowed at all and tests the 45% prior.
