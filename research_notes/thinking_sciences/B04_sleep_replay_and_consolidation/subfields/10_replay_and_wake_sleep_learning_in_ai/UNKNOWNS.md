# Replay and wake-sleep learning in AI: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| B04.10-U1 | Does a subgoal library built by a wake-sleep cycle beat a plain arm at equal tokens? | Wake-sleep library cycle | memory, O3, S6, S9 | K01, K08, K13, K22; single-source, contested, older models only | Plain vs plain + extra samples vs library; ARC and BrainTeaser train/held-out split; held-out pass rate, 3+ seeds | Library beats extra-samples arm by 3+ points and more than 1 SD on a problem class | High |
| B04.10-U2 | Does verify-before-keeping (re-solve on a held-out problem) raise library quality? | Verification gate on entries | memory, G3 | K09, K23 (ASI +4.2, 15.6% pass); single-source, code only | Verified vs unverified library; same items; pass rate and tokens | Verified beats unverified by 3+ points, and the gate costs under 20% of tokens | High |
| B04.10-U3 | What per-class reuse rate pays for the build tokens? | Reuse-rate gate in S0 | S0, memory | K22, K30; contested, no token-saved-per-reuse figure anywhere | Log wake and sleep tokens, reuses, tokens saved per reuse across cycles | A reuse rate threshold exists that predicts gain with r above 0.5 across classes | High |
| B04.10-U4 | Entry format: name plus one-line rule, worked example, or code? | Chosen entry format | memory | K07, K23, d17; single-source, split by task | 4 format arms plus none; same library content; pass rate | One format beats the others by 3+ points in 2 of 3 classes | High |
| B04.10-U5 | How many entries to inject per step? | Injection cap | memory | K25 (ReasoningBank, Memento); established direction, not tested on reasoning scaffold | 0, 1, 2, 4, 8 entries; pass rate | Peak found; adopt peak. If 4+ beats 1 by 2+ points, raise the cap | Med |
| B04.10-U6 | Does a no-weights "dreaming" step (verified practice variants of library entries) help? | Practice step in sleep | memory, O | K28 (SkillWeaver); single-source, no equal-token control, LLM judge | Library only vs library + verified variants vs same tokens in extra real attempts | Variants arm beats extra-attempts arm by 2+ points with a code check | Med |
| B04.10-U7 | Delta updates vs full library rewrite | Itemised-update rule | memory | K29 (ACE); single-source, DeepSeek-V3.1 only | Same cycles with delta vs rewrite; library size and pass rate | Rewrite loses 3+ points or shrinks the library by half | Med |
| B04.10-U8 | Short-to-long ordering when building the library | Curriculum order | memory | K11 (ReGAL d18); single-source, code domains, one lab | Short-to-long vs random vs long-to-short build order | Short-to-long beats random by 3+ points | Med |
| B04.10-U9 | Do one-line failure lessons beat no failures, raw traces, and hindsight relabelling? | Failure lesson format at S9 | S9, memory | K24, K17; single-source, web tasks | 4 arms; pass rate on later items | Lessons beat no-failure by 2+ points and raw traces do not | Med |
| B04.10-U10 | Where does a flat library break, and does group-first routing fix it? | Size cap plus grouped routing | memory | K26 (d14, d15); single-source, synthetic, one author | 10, 20, 40, 80 entries with near-duplicates; flat vs routed | Flat loses 10+ points past a size; routing recovers half | Med |
| B04.10-U11 | Do sleep-time notes beat more test-time thinking for predictable questions? | Pre-question notes step | memory, S1 | K16 (b17, d07); single-source, GSM and AIME splits, one reversal in SWE | Notes vs extra thinking at equal tokens, binned by question predictability | Notes win in the top predictability bin by 3+ points | Low |
| B04.10-U12 | Does the library gain hold for the strongest model, or does it only help weaker ones? | Model-strength gate | S0, memory | K10, d05 (gains shrink with strength); single-source | T1 repeated on strongest and a weaker model | Gain on the strong model is at least half the gain on the weak one | High |
| B04.10-U13 | Is the gain from the library or from the format prompt (empty-library arm)? | Keep or drop library | memory | K15, d05 (about half of Claude's AIME gain from prompt); single-source | Empty-library arm with same instructions vs filled library | Filled beats empty by 3+ points | High |
| B04.10-U14 | Does hindsight relabelling (failed attempt stored as solution to its own result) help without weights? | Relabelled entries | memory | K17 (SOAR, needs weights); single-source | Store with and without relabelling; pass rate on later items | Gain 2+ points at equal tokens | Low |
| B04.10-U15 | Does prioritising which entries are re-verified or retrieved (by failure or surprise) help? | Prioritised rehearsal | memory | K20 (RL only); single-source, different domain | Uniform vs prioritised re-verification | Prioritised yields 2+ points or fewer tokens at equal score | Low |

## Open questions we cannot test on our bench yet
- **Outside replication on open reasoning.** No unrelated lab has tested DreamCoder-style loops on open-ended reasoning. Unblock: our own bench is the first replication; use 3+ seeds and report SD.
- **A verifier for non-code reasoning steps.** None found. Unblock: build one from re-solving or a held-out instance check, then measure its accuracy against ground truth.
- **Break-even in tokens.** No paper reports tokens saved per reuse. Unblock: instrument the harness first (U3).
- **Training-based dreaming** (SOAR, SSR, generative replay). Needs weights. Unblock: only if a fine-tunable model is added to the project.
- **Why structure and a verifier matter.** K22 is a cross-paper pattern. Unblock: a controlled study that varies reuse structure with the model fixed.
- **Frontier-model LILO, ReGAL, AWM against matched no-library arms.** Not published. Unblock: run on our bench with the strongest model (U12, U13).
- **Entry-format comparisons at read time on reasoning tasks.** Only code and web evidence. Unblock: U4.

## Order to run
1. **U13 (empty-library arm) with U1.** Cheapest and decides whether any library is worth keeping: if the empty arm matches, the rest is moot.
2. **U3 (reuse and token logging) inside every run.** It costs almost nothing and gives the break-even and the gating rule for all other tests.
3. **U2 (verify before keeping), then U4 (entry format).** The largest measured single-source effect (+4.2) and the most direct design choice for the library; run on the same split as U1.
