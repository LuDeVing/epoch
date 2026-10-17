# Interrogating the run itself

*2026-10-12. The HTSA method applied to its own nano loop: every part questioned aspect by aspect, open questions followed one level down, improvements collected. Answers are from the code as it is today, not from hopes. Each improvement ends with a cost estimate (small = under an hour, medium = a few hours, large = a day).*

---

## Part 1. The problem map

**Q: Are the seven parts the right split?** They follow the structure of the script (modules). That is natural for building, but it biases ideas toward local edits. An idea that spans two parts (for example, co-designing how layers are stacked with how information is mixed, or changing the data order together with the learning schedule) has no home, must be filed under one part, and competes there against purely local ideas.
**Q: What does an agent do with a cross-part idea?** It sketches it under its assigned part; the builder is then told "everything outside this part stays identical", so the cross-part half is cut off or silently violates the rule.
→ **Improvement 1a.** Add a "whole recipe" inward node whose boundary is "any two parts", with its own share of build slots. *Small.*

**Q: Do the assumptions ever change?** They are written once by the planner. The interrogation stage asks every idea "what does it silently assume?" and those answers are stored, but never flow back into the map.
→ **Improvement 1b.** After each generation of interrogation, append newly discovered assumptions to the part's list, so the next outward sketches can drop them. This closes a real loop: questioning an idea reveals assumptions, assumptions seed the next ideas. *Small.*

**Q: Who draws the map?** The cheap model. The map decides what the search can see at all, which is the most leveraged single call in the run, and it is the one call given to the weaker model.
→ **Improvement 1c.** Draw the map with the strong model. One call. *Trivial.*

**Open, followed:** *Should parts be weighted by headroom?* The round-robin gives every part equal slots. The research briefs know how many open directions each part has, and the experiments ledger will know where past wins came from. → **Improvement 1d.** Weight slots by the count of open directions in the brief, with a floor of one per part. *Small, later.*

## Part 2. Web research

**Q: How is "already known" decided?** By word overlap between a cluster name and brief entries. It catches exact names and misses paraphrases: "share the KV cache" matched, "sliding window attention in early layers" did not match the brief's "alternating short/long sliding-window attention".
→ **Improvement 2a.** One cheap-model call per part: "here are the clusters, here is the brief, which clusters are the same technique as which entries?" Lexical matching stays as the fallback. *Small.*

**Q: Does the run learn across runs?** Interrogation produces sourced facts, verification produces results, the overnight verdict writes an experiments ledger. None of it is read by the next run. The brief cache is the only memory, and it holds only what the research agent found.
→ **Improvement 2b.** At run start, read the experiments ledger and inject previous verdicts into the briefs as known or failed entries ("tried in run X: verified / failed by this much"). After a run, merge sourced facts from the interrogation into the brief cache. *Medium.*

**Q: Does the web make agents converge?** Everyone who searches finds the same speedrun list. The "at least half your own" rule limits it but nothing measures it.
→ **Improvement 2c.** Count SOURCE = own versus URL per card and per part and show it on the dashboard. If web-sourced ideas dominate the selected set, that is visible. *Trivial.*

## Part 3. Idea sketches

**Q: What are the private defaults used for?** They are stored and never used. The design says they exist to measure whether the process gets beyond the obvious, but nothing measures it.
→ **Improvement 3a.** Tag clusters that match a private default as "obvious" (same matcher as prior art) and show the count. Optionally give obvious clusters a small selection penalty. This is the first time the run would have a number for "beyond the first thing that came to mind". *Small.*

**Q: Does the sketch agent see the right amount?** It sees the whole script every time. Fine for inward ideas. For outward ideas, the whole script pulls attention back into the current design; the stripped-script card helps but only one agent per part gets it.
→ No change now; measure first with 3a and 2c.

**Q: Where do upward proposals go?** To a file nobody reads.
→ **Improvement 3b.** Print them in the final answer for the human. *Trivial.*

## Part 4. Grouping

**Q: Is the same idea ever built twice?** Yes, possibly. Grouping is done per part and direction. "Parallel attention and feed-forward blocks" can appear under the depth part and under the feed-forward part and will be two clusters, both eligible for slots.
→ **Improvement 4a.** After per-part grouping, one cheap-model call over all cluster names to merge cross-part duplicates. *Small.*

**Q: How is a cluster's representative chosen?** By the longest prediction plus test text. That rewards verbosity, which the design explicitly says must not count.
→ **Improvement 4b.** Choose the representative with the cheapest test, then the most cards, never length. *Trivial.*

## Part 5. Selection

**Q: Can an idea born in the interrogation actually win a build slot?** Rarely. The ranking is strict priority order and the first key is "number of different ways in that produced it". An offshoot cluster has one card, "deepen", so it loses to any two-card cluster regardless of novelty. The dry run confirmed it: all selected clusters were original ones. The whole interrogation stage can add facts but its new ideas are mostly starved.
→ **Improvement 5a.** Replace the strict ordering by a weighted score: spread across cards, novelty tag, departure, cheap test, with weights as settings. Also treat an offshoot's parent chain as one way in, so an idea that two different interrogations produced counts as two. *Small, high impact.*

**Q: Does selection prefer new over known?** New gets a bonus only at the second key. The first strong-model run produced five known techniques. If the goal is to find new things, the run should guarantee some.
→ **Improvement 5b.** A quota: at least half the build slots go to clusters tagged new, when enough exist. *Trivial.*

**Q: What is the ratio of thinking to testing?** With defaults, about 115 strong-model calls produce 12 builds per run. Verification is free and takes about three minutes per candidate on the card. The cheapest real test of an idea is to build it.
→ **Improvement 5c.** Default build slots 10 to 12 in round one and 4 in round two, and one interrogation generation by default. More ideas get real checks for the same money. *Trivial.*

## Part 6. Interrogation

**Q: Does the interrogating agent see the code?** No. It gets the idea text, the part's description, and the rules. It is asked how the idea interacts with every other part, what it costs in memory and time, and what it must initialise, without ever seeing the script. Its answers about the code are guesses.
→ **Improvement 6a.** Include the script, or at least the part's own code region and the training loop, in the root interrogation prompt. *Trivial, high impact.*

**Q: Does it see the research brief?** No. It will re-search what the brief already holds, or contradict it.
→ **Improvement 6b.** Include the part's brief entries in the root prompt. *Trivial.*

**Q: Which open question is followed?** The one the agent lists first. The design distrusts self-judgment, and here it decides where the recursion goes.
→ **Improvement 6c.** Ask the agent to mark each open question "would change how this is built: yes / no", and follow only those. Open questions that would not change the build are curiosity, not work. *Small.*

**Q: Are the facts true?** Nothing checks. Numbers without a source are as welcome as numbers with one.
→ **Improvement 6d.** Require a URL on any fact containing a number; drop unsourced numeric facts the way briefs drop unsourced entries. *Small.*

**Q: Does the second generation pay?** It interrogates untested variants of untested ideas. Its value is unknown until one run measures how many second-generation ideas reach the pool.
→ Measure in the first run: the dashboard should show, per generation, sketches born, clusters selected, candidates checked. *Trivial.*

## Part 7. Building

**Q: Is the boundary rule enforced?** No. "Everything outside this part stays identical" is a sentence in the prompt. Nothing checks the returned script against it.
→ **Improvement 7a.** Diff each candidate against the baseline and locate changed functions and classes. If anything outside the part's boundary changed, fail at a new rung 0 with the list of violations as feedback, for free. This also catches silent rule violations like changed evaluation code. *Medium, high value.*

**Q: Full file or patch?** The builder rewrites all 400 lines each time, about 12k tokens of output, and any slip anywhere breaks the build. A patch would be cheaper and localised but harder to apply reliably.
→ Keep the full file; 7a catches the slips.

## Part 8. The ladder of checks

**Q: What does the one-minute test measure?** That the loss falls by at least 0.05 from the first five steps to the last five. Almost anything that runs passes. The pool is then ranked by that drop, which rewards things like a higher learning rate in the first minute, not better learning overall.
→ **Improvement 8a.** Compare at matched steps: the candidate's loss at step N versus the baseline's loss at the same step N with the same seed, with the baseline curve recorded once in the profile. Rank the pool by that difference. *Small.*
→ **Improvement 8b.** Add a five-minute rung before the overnight run, same matched-step comparison. Five minutes of card time per candidate is cheap next to an hour and a half of overnight training. *Small.*

**Q: Why did a baseline-identical file fail the timing check today?** The profile said 1.23 s per step and the card ran at 2.2 s. The step-time rule compares against a stale profile taken on a different day.
→ **Improvement 8c.** Re-time the baseline for three steps at the start of every run, about thirty seconds, and compare against that. *Trivial.*

## Part 9. Revision

**Q: What gets revised?** Up to two failures per round, operator chosen at random. The failure record says which rung failed, but the choice ignores how close the failure was.
→ **Improvement 9a.** Order the queue by rung reached, highest first, and choose "fix" for rung failures and "specialize" for budget or size failures instead of at random. *Trivial.*

## Part 10. Rounds and budget

**Q: What does round two know about round one?** Nothing. Round-two sketch agents get the same inputs as round one. Which ideas were built, which failed and why, which passed, is in the logs and not in any prompt.
→ **Improvement 10a.** Give round-two sketch and interrogation agents a short record: "built in round one: X (checked), Y (failed at rung 2: too slow), Z (failed to build)". Noticing failure and switching is the core of the thesis and it is missing at the ideation level inside a run. *Small.*

## Part 11. The overnight verdict

**Q: How noisy is three seeds?** The spread estimated from three runs is itself very uncertain. A rule of "beat the mean by two spreads" with three seeds will sometimes pass noise and sometimes block a real gain.
→ **Improvement 11a.** Measure the baseline noise once properly: five seeds of the baseline, about two and a half hours of card time, before the first real verdict. Use that pooled spread for every later verdict, and keep adding baseline seeds across runs. *Small code, GPU time.*

**Q: How long will the overnight take?** Three seeds times about thirty-one minutes times every candidate, plus the baseline. Ten candidates is about sixteen hours.
→ **Improvement 11b.** Staged seeds: one seed for every candidate first, ordered by the five-minute rung. Only candidates within reach of the bar get seeds two and three. Candidates clearly below the bar after one seed stop. *Small.*

## Part 12. Dashboard and roles

- Add per-generation counts (6, measure), the own-versus-web share (2c), the obvious-idea count (3a), and the boundary-check result (7a). *Small.*
- Planner on the strong model (1c). API key required for the search-heavy settings.

---

## Ranked list

| # | Improvement | Why it matters | Cost |
|---|---|---|---|
| 1 | 6a + 6b: interrogation sees the code and the brief | Today it answers code questions blind | trivial |
| 2 | 5a + 5b: weighted selection with a novelty quota | Offshoots and new ideas are currently starved of slots | small |
| 3 | 7a: enforce the part boundary by diff, free rung 0 | The central build rule is unenforced | medium |
| 4 | 8a + 8b + 8c: matched-step comparison, five-minute rung, fresh baseline timing | The current one-minute test ranks by a weak proxy and fails on stale timing | small |
| 5 | 11a + 11b: measure baseline noise with five seeds, staged seeds overnight | The verdict rule is noisier than it looks and the night is too short | small + GPU time |
| 6 | 10a + 1b: round two learns from round one, assumptions flow back from interrogation | The "notice failure, switch" loop is missing inside a run | small |
| 7 | 4a + 2a: cross-part merge of duplicates, model-based prior-art tagging | Same idea built twice; known ideas mislabelled new | small |
| 8 | 3a + 2c: measure "beyond obvious" and own-versus-web share | The run's main claim has no number yet | small |
| 9 | 5c: more build slots, one generation by default | Testing is cheaper than thinking here | trivial |
| 10 | 2b: read the experiments ledger at start, write facts back to the brief cache | Memory across runs | medium |
| 11 | 1a, 1c, 1d, 3b, 4b, 6c, 6d, 9a | Smaller fixes listed above | trivial each |

**Status 2026-10-12:** all items built and dry-run tested except 1d (weighting parts by headroom, deferred). Rung numbering changed with the build: 0 boundary, 1 build, 2 steps, 3 learn at 45 matched steps, 4 long at 240 matched steps, 5 full. The five baseline seeds (11a) are produced by `python -m nano.batch_verify --run <any run> --baseline-seeds 5` and take about 2.5 hours of card time; they have not been run yet.
