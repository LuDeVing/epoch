# Multiplayer space: requirements the project already wrote

Task U2, read-only extraction, 2026-10-17. For the design and build stages of the hackathon track "Multiplayer agentic experiences": two people work on one thing together, each through their own agent.

## 0. Read this first

- **What this is.** The requirements the project already wrote for a shared research space and for people in the loop. They come from 12 docs and notes, plus the code paths those docs point to. Nothing was run. No model calls, no web lookups.
- **Where we stand.** There is no shared space today (TOR L36). People steer through one `control.json` per run and one owner-seeds file. The rest is design on paper.
- **Status words.** *built*: code exists and I read it. *partly*: some of it exists. *proposed*: written in a doc, no code. *derived*: not written anywhere; it follows from the cited source. Drop a derived row if you disagree.
- **Source tags.** A file key plus line numbers, for example `M03 L139`. The key is in section 7. Line numbers were checked with grep.
- **Web facts.** I looked up nothing on the web. The few web-based claims below are copied from the project's notes with the note's own tag: "verified on the page" (by the note's author) or "from memory".
- **Hackathon wording.** What the judges want comes from the workflow brief. I did not check it on the hackathon page.

The five things that matter most:

1. No shared space exists. People use one whole-file `control.json` (last writer wins) and a seeds file.
2. Nothing tells an agent what other people changed. The nearest things are one 600-character owner note with no author, and (proposed) comments handed to critics with the author named.
3. The rules for "no conflicts" are written: rows never overwritten, an edit is a new rev, one writer, votes sum, comments kept, disputes marked. None of them is built.
4. The loop reads people's input at fixed points, not at once. The space has to show "queued" and then "applied".
5. A person cannot see the top 3 next questions before the loop applies the veto (section 5, item 1).

## 1. The shared space in one picture

```
                 +----------------------------------------------+
                 |            SHARED RESEARCH SPACE             |
                 |  problem tree . ideas . results . opinions   |
                 +----------------------------------------------+
                    ^        ^         ^          ^         ^
               Mapper   Inventors   Critics    Builders   People
                                                (+ tests)  (many, any time)
```

- Everyone reads and writes the same space. Agents do the work. People watch, comment and steer. (TOR L19)
- One rule: people steer and add knowledge; **tests decide**. (TOR L197)
- Four things a person can do: add a problem or branch, comment, vote, flag prior art. (M03 L133-140; TOR L191-195)
- The project's own sketch has four panels: problem tree (add a problem), ideas board (comment, vote, flag "known"), test results (see the numbers), log (see who did what). (TOR L177-189)
- Recommended build: a small database (SQLite) behind one writer service, with a thin web page on top. (M03 L197; M00 L87-89)
- The three modes change what "tests decide" means. Modes 1 and 2 have an objective check. Mode 3 has none: a blind panel plays the test, and people count as extra judges at a capped weight. (M03 L7-13; GS L161-195)

## 2. Requirements

49 requirements. R1 to R15 are functional (what people see and do). R16 to R33 are data (what is stored). R34 to R49 are safety (what must never happen). The four headline safety rules are R34 (people steer, tests decide), R35 (nothing deleted), R36 (every record has an owner and a timestamp) and R37 (disputed facts are marked, not overwritten).

### 2.1 Functional: what people see and do

| # | Requirement | Source | Status |
|---|---|---|---|
| R1 | One shared space holds the problem tree, the ideas board, the test results, people's opinions and a log of who did what. Everyone reads and writes the same space. Agents do the work. People watch, comment and steer. | TOR L6-19, L175-189 | proposed (TOR L36: no shared space yet) |
| R2 | Any number of people can be in the space at any time. The loop does not wait for them; only a person's pause or stop halts it. | TOR L16, L188; loop.py L1985-1988 | proposed; pause built |
| R3 | Problem tree view. Parts, sub-parts, questions and helper questions, up to 4 levels. Each node shows its name, what it does now (frame), its origin (map, off-map win, failure question, human), its priority or lowered state, its disputed facts, and the counts of sketches, clusters, built and checked per direction. | PT L26-30, L36-55; M03 L78-84 | data built; view proposed |
| R4 | Each part shows three lines: what it does, its weak spot (with the fact id that shows it, otherwise marked unsupported) and its ask (a question about a problem, never a solution). | M02 L15-25, L42-62 | proposed |
| R5 | Idea clusters view. Each cluster shows its name, part, direction, size, the cards that made it, its rank, whether it was picked for building, its prior-art tag, its "obvious" flag, what it merged from, and its lead sketch (idea, mechanism, prediction, test). | PT L87-91; dashboard.py L75-82; TOR L28 | data built; view is a table today |
| R6 | Arguments view, per idea. The critic's objections (class, severity, "if true" test). The author's one typed reply: concede, rebut with a tagged fact, or propose a measurement. The critic's mark: resolved, revised or standing. At most two exchanges. Nothing is dropped. | TOR L29, L129, L139-154; DL1 L36-39; deepen.py L492-504 | data built; view is a chain in the dashboard |
| R7 | Test results view. Per candidate: the numbers, the rung reached, what they are measured against (baseline, best so far or panel), and a status: win, tie, loss, failed check or not built. Losses and failed checks stay visible, because they are evidence. When the reference moves, old results are re-labelled, not erased. | M03 L12, L17-31 | partly (verify.jsonl built; result records proposed) |
| R8 | A failed check with a reason shows as a child question under its part, with the test that would answer it, the threshold and the failure condition. | M03 L32-44; PT L28-30, L52 | built (as "why did X fail?") |
| R9 | Next-question panel. The top 3 open questions with their score, the reason for each factor, whether this is an exploration round, who decided (default, person, default after veto, or none left) and what was vetoed. A person can veto or choose. The default is to go on with the top one. | PF4 L60; pick.py L1-22, L206-220; TOR L130 | data built; panel proposed |
| R10 | Upward proposals (a new success measure) show as proposals that need a person. The current check keeps deciding until a person approves. | PF4 L72; pick.py L18-19, L103-107; PT L53, L61-63 | data built; approval step not built |
| R11 | Per-part memory view. Facts, tried, priors, cues, open questions and failed framings, each with its source tag (script, measured, web or belief), date, run and round. Archived entries stay readable. | memory.py L1-20, L29-31, L131-138, L288-304; TOR L128 | files built; view proposed |
| R12 | A readable change log for each round: what was added, merged, split, lowered, raised, promoted, disputed or fixed, by whom and why. Plus a full snapshot of the tree after each round. | M03 L86-95 | proposed (nothing in code) |
| R13 | Vote outcomes show beside the voter: hit (the idea won its test), miss (it lost) or open. Hit rates are for people to read. In version one they do not change vote weight. | M03 L145-149, L199 | proposed |
| R14 | Mode 3 view (no objective check). The panel score and spread sit beside people's opinions (score, note, who) and the weight they got. A proposal the panel rates low but people like is marked "split" and kept. Status words are "preferred" and "not preferred", never "won". | M03 L12, L190-193; GS L183-195; panel.py L206-240 | opinions built; "split" mark proposed |
| R15 | Each of the four people actions is wired to the next round, and the space shows the wiring: which round and stage picked the action up, and what it changed. | M00 L101; M03 L135-140 | proposed; the "show it" part is derived |

### 2.2 Data: what is stored

| # | Requirement | Source | Status |
|---|---|---|---|
| R16 | Core entities. A Problem has many Branches. A Branch has many Facts. Branches and Ideas link many to many. An Idea has many Results. Comment, Vote and Flag each point at a target (a branch, fact or idea). | M03 L112-129 | proposed |
| R17 | Every row has: id, author (a named person, or `agent:<role>`), created_at, round and rev. | M03 L120, L131 | proposed |
| R18 | Branch: id, parent, name, origin (map, off or human), priority, status. Tree nodes also get rev, created_round, aliases, results and facts_status. The tree file gets version, round and mode. | M03 L122, L78-84 | proposed |
| R19 | Fact: id, branch, text, source, status. A fact without a source is rejected. Source kinds: diagnostics, scorer, document, human, agent, result, with a ref (file, command, seeds, URL or person), and n_seeds and z for measured facts. | M03 L123; M01 L77, L81-91 | proposed (status words differ, section 5 item 4) |
| R20 | Idea: id, branch, text, status (open, built, tested, dropped or known). | M03 L124 | proposed |
| R21 | A result record hangs under the question the idea answered: name, candidate id, round, origin (tree, off or human), metrics (learn_z, learn_gap, long_z, cost_ratio), status and ref. | M03 L19-27 | proposed |
| R22 | Comment: id, target, text, kind (evidence, question or objection). Vote: id, idea, person, value (+1 or -1), outcome (hit, miss or open). Flag: id, idea, person, claim ("known"), link, scout verdict. | M03 L126-128 | proposed |
| R23 | A link between parts: from, to, kind (shares_fact, interacts, spawned_from or win_from), why, source. | M02 L161-170 | proposed (win branches exist) |
| R24 | Priority is stored with both its factors (unused capacity and evidence), so people can see why a part ranks where it does. | M02 L104-129 | proposed |
| R25 | A reply-round record per objection: reply kind (concede, rebut or measure), fact and its source tag (script, measured, web or belief), test (metric, direction, number, rung), change, verdict (resolved, revised or standing), reason, exchange number. | deepen.py L492-504, L634-637; loop.py L3625-3628 | built |
| R26 | A memory entry: id, date, run and round, source, text and a "used" counter, in six sections plus ARCHIVE. | memory.py L11-18, L131-138 | built; no author field |
| R27 | On disk, per run: `problem_tree.json` (current), a full snapshot per round, `tree_changes.jsonl` (one line per change: round, op, node, by, why) and `CHANGES_round_NN.md`. Ops: add, merge, split, lower, raise, promote, fact_disputed, fact_fixed. | M03 L86-95 | proposed |
| R28 | Rows are never overwritten. An edit is a new rev. Agents write as `agent:<role>`. | M03 L131 | proposed |
| R29 | Store the space in a small database (SQLite) behind one writer service, with a thin web page on top. A document cannot enforce the data model. A full web app is too much for version one. | M03 L197; M00 L87-89, L101; TOR L237 | proposed (owner decision open) |
| R30 | Identity is a named login, with no anonymity, so hit rates mean something. | M03 L198 | proposed (owner decision open) |
| R31 | Times need a zone. The project's own timestamp is local time with no zone. With several people and agents, use UTC or an offset, so events sort the same for everyone. | M03 L120; schemas.py L27-28 | derived |
| R32 | Ids are assigned by the writer. The loop cleans a human branch id to a-z, 0-9 and underscore (16 characters at most) and silently skips a duplicate or a clash with a planned id. The person must be told. | loop.py L1990-2005; PT L38 | derived |
| R33 | The loop's only input from people is `control.json` (read at stage ends, at the question pick and when the panel scores) plus the owner-seeds file (read at start). The writer renders one `control.json`, whole, in one atomic step. A half-written or malformed file would otherwise be ignored in favour of the last good one, and a pause or stop could be lost. | loop.py L1932-1988, L1948-1954, L4445-4451; CL L41 | derived from built behaviour |

### 2.3 Safety: what must never happen

| # | Requirement | Source | Status |
|---|---|---|---|
| R34 | **People steer, tests decide.** A popular idea that loses its test is dropped. A voted idea that fails is dropped and its votes are marked "miss" beside the voter's name. In Mode 3 the blind panel plays the test and people are extra judges. | TOR L197; M03 L13, L145-148; M02 L127 | rule written; vote code proposed |
| R35 | **Nothing is deleted.** A quiet branch is lowered (priority x 0.5, floor 0.1, still one context every 3 rounds), never deleted. Losses and failed checks are kept. A re-plan keeps what the run and people put on the map. Memory entries move to ARCHIVE; a capped prompt view may leave entries out, the file never loses them. Objections are never dropped. | TOR L114, L129; M03 L30-31, L75-76; M02 L178; loop.py L3687-3697; memory.py L144-147, L288-304; DL1 L47 | partly (re-plan carry, archive and objections built; quiet lowering proposed, and M02 and M03 differ on it: section 5 item 13) |
| R36 | **Every record has an owner and a timestamp.** Today: tree nodes have neither; memory entries have a date (no time) and no author; the control log has a time and no person; an opinion has an optional "who". | M03 L120, L131, L198; memory.py L278-280; loop.py L1959; panel.py L217 | proposed |
| R37 | **A disputed fact is marked, not overwritten.** The fact keeps its text. The dispute stores who disputed and why. Every prompt shows the mark. Both versions stay, with dates and run ids, until it is re-measured. | M01 L79, L120-122; M03 L138, L142-143; PE2 L63; tree.py L269-276; PT L50 | partly (agents' doubts are marked; people's disputes and re-measuring not built, PT L103) |
| R38 | A disputed fact is re-measured (on new seeds) before any agent may rely on it. Two people disputing one fact are settled by one re-measurement, and both see the number. With no objective check, the judge panel reviews it instead. | M03 L142-143, L153-154; M01 L122, L158, L173 | proposed |
| R39 | People's influence is bounded. A vote shifts an idea's priority by clamp(0.1 x net votes, -0.3, +0.3), one vote per person per idea. In Mode 3, people are extra judges at 0.25 of the panel (code: default 0.25, never above 0.5, scaled by min(1, people/3)). Weak-spot votes count once per person, cap at 10 votes, and lift a part's evidence to 0.8 at most; only a critic or a judge reaches 1.0. All these values are guesses. | M03 L139, L173, L201; M02 L127, L207-208, L242; M00 L92-93; GS L189-191; panel.py L12-13, L230 | opinions built; votes proposed |
| R40 | One voice per person. Today's opinion code counts opinions, not people, so one person with three opinions gets the full weight. Keep one live opinion per person per candidate; a new one is a new rev. | M03 L139; M02 L127; panel.py L206-231 | derived |
| R41 | The system never rewrites its own test. Upward proposals are proposals only. A change to the success measure needs a person, and the default is hold. | PF4 L72, L81; pick.py L18-21 | flags built (`requires_human`); approval not built |
| R42 | A person may veto or swap the pick before the round. The default is to go on with the top one. A choice must be one of the top 3 and never rewrites the test. | PF4 L60, L72; pick.py L20-21, L206-220; TOR L130 | built in `control.json`; no preview (section 5 item 1) |
| R43 | A reply never gates a build. A persuasive reply cannot skip a test, and a failed rebuttal cannot block a build; measurement decides. The critic updates only on a quoted fact or a measurement, never on confidence. A fact tagged belief cannot settle an objection. Apply the same rules to a person's reply. | DL1 L46-47; deepen.py L504, L589-599 | built for agents; for people derived |
| R44 | Conflicts between people need no referee. Votes sum, so opposite votes cancel. Comments are never merged: the justifier sees both sides and answers both. Nobody deletes another person's comment; only an owner can hide one. | M03 L151-155 | proposed |
| R45 | Two people adding the same problem do not collide. Duplicates merge when they share a parent and their name and frame match at 0.85 or more. The older id wins and the other id is kept as an alias. The merge is logged. | M03 L64-65; PF4 L74 | proposed |
| R46 | What people add is evidence, not rules. Memory is shown to agents as evidence ("dispute it if the facts say otherwise"). Web text never enters memory unmarked. A memory entry must cite an artefact that exists, and only the curator writes, so a person's note enters memory only through that rule unless the rule changes. | memory.py L33-34, L52-53, L222-245; PE2 L55, L59, L64 | built for agents; open for people |
| R47 | A prior-art flag sends the idea to the scout before building. If the scout confirms, the status is "known" and the idea is not built. The flag stays on record with the scout's verdict either way. | M03 L140, L186-188; TOR L32, L195 | proposed (scout built) |
| R48 | **A question a person adds must be measurable and traceable.** To enter the pick, a question needs a test (metric and rung), a threshold and a failure condition. With any one missing it is left out of the pick, though it can still sit on the map as a branch. The loop keeps every key of an `add_nodes` item, so a person can supply these fields. No vague success words: a reframe must change a number the test reads. Every pick traces up to a node of the externally given goal; one that does not needs a person's OK. | PF4 L66, L70, L71; pick.py L5-7, L79-83; loop.py L1991-2010; PT L52 | built for failure questions (`enterable`); for questions people add: derived |
| R49 | **Caps and alarms still apply when people steer.** A budget cap per question and per round (kill at the cap). A novelty floor and a minimum gain. An alarm if the cheapest option wins in over half the rounds. A hold-out, so the chooser cannot overfit the test. | PF4 L68-69, L73; pick.py L7 | partly (the focus cap is built; the rest is proposed) |

## 3. Human actions and what each does to the next round

### 3.1 The actions

"Built" means the loop reads it today. "Proposed" means the effect is written in a doc but there is no code. "Must do" is the effect the docs and the code require. Every input is read at a fixed point, not at once (3.2).

| # | Action and channel today | Status | What it must do to the next round | Source |
|---|---|---|---|---|
| H1 | **Add a problem or branch.** `control.json` key `add_nodes`: a list of node specs (id, name, parent, frame, assumptions, boundary, directions). | built (file); screen proposed | The branch goes on the map once, marked origin "human", with the person's name on it (R17). It gets idea contexts at the next ideation, like any part: `per_node` per direction, which is 1 in later rounds. The docs want 2 per human branch (a proposed knob). A re-plan keeps it. It cannot sit deeper than level 4. | M03 L137, L171; TOR L192; loop.py L1990-2015, L3687-3697; tree.py L679-730 |
| H2 | **Comment** on an idea, branch or fact. No channel today. | proposed | Critics get the comments on their target as evidence, with the author named. The justifier does too, once it is built (TOR L31: planned). A comment that disputes a fact sets it to "disputed". A comment on a quiet branch raises it. Comments are never merged; both sides get an answer. A comment alone cannot resolve a critic's objection; that takes a quoted fact or a measurement (R43). | M03 L76, L138, L153; TOR L193; M02 L178 |
| H3 | **Vote** on an idea. No channel today. | proposed | The idea's priority shifts by clamp(0.1 x net votes, -0.3, +0.3). One vote per person per idea. Opposite votes cancel. The vote can move an idea toward the builders, but the test still decides: after the test the vote is marked hit or miss. | M03 L139, L145-149; TOR L194 |
| H4 | **Flag prior art.** No channel today. | proposed (scout built) | The idea goes to the prior-art scout before any build. Confirmed: status "known", not built, flag kept. Not confirmed: the idea goes on, and the flag and the verdict stay visible. | M03 L140, L186-188; TOR L32, L195 |
| H5 | **Dispute a fact.** No channel for people. Agents' doubt cards do it today. | partly | The fact is marked "disputed", with who and why, in every prompt until it is re-measured. It is re-measured before agents may rely on it. With no objective check, the judge panel reviews it instead. Re-measuring is not built. At most 3 disputed facts show in a part's prompt. | M01 L120-122, L173; M03 L138, L142-143, L153-154; PT L50, L103; tree.py L269-276 |
| H6 | **Veto a next question.** `control.json` key `veto`: a list of question ids. | built | The vetoed id leaves the top 3 and the next one is chosen (recorded as "default after veto"). If all three are vetoed, no question gets focus that round. The veto holds while the id stays in the list. | pick.py L206-220; loop.py L833-867, L1103; PF4 L60, L72 |
| H7 | **Choose the next question.** `control.json` key `choose`: one id. | built | If the id is in the top 3 and not vetoed, it is chosen (recorded as "person"). Otherwise the default top one wins. The chosen question's node gets 2 extra inward contexts (`--focus-contexts`; TOR L130 says its part) for at most 2 rounds (`--max-rounds-focus`). The idea agents see the question with its test and threshold. The test is never rewritten. | pick.py L20-21, L206-220; loop.py L869-880, L1188-1192; TOR L130; GS L214 |
| H8 | **Skip a part.** `control.json` key `skip_nodes`: part ids. | built | The part and everything under it get no idea contexts, and its clusters are not built, from the next time contexts are dealt or clusters are picked (3.2). Remove the id to bring it back. Nothing is deleted. | loop.py L950-960, L1980, L3283; M03 L159, L175 |
| H9 | **Leave out an idea cluster.** `control.json` key `exclude_clusters`: cluster names. | built | The cluster is not picked for building. | loop.py L1981, L3283; M03 L159 |
| H10 | **Give an opinion** (Mode 3 only). `control.json` key `opinions`: a list of cluster or candidate, score 1-10, note, who. | built | Mixed into the blind panel score at weight 0.25 x min(1, n/3), never above 0.5. The proposal's panel score, its rank and the reference may move. Up to 10 notes (300 characters each) are kept and shown. | GS L189-191; panel.py L12-13, L206-240; loop.py L3024-3032 |
| H11 | **Seed a mechanism.** The file `memory/owner_seeds.json`: a list of part and text. It is not a `control.json` key. | built (round 1 only) | One inward "owner" context per seed on the named part, in round 1 only. Text up to 1500 characters. The test-mode cap never drops it. The space should allow seeds in any round (not built). | loop.py L1139-1145, L4445-4451; M03 L161-162 |
| H12 | **Leave a note for every agent.** `control.json` key `note`. | built | Up to 600 characters appear as "NOTE FROM THE OWNER" in the history text that later agents read. It is one string with no author, and a new note replaces the old one. The space must keep many notes, each with author and time. | loop.py L1979, L2253-2254; M03 L159 |
| H13 | **Approve or reject a new success measure** (an upward proposal). No channel today. | proposed | The default is hold: the current check keeps deciding. An approval is recorded with person and time. No code changes the measure itself, and no doc says how a new measure would be installed. | PF4 L72, L81; pick.py L18-19, L103-107 |
| H14 | **Vote that a weak spot matters** (Mode 3). No channel today. | proposed | Raises the part's evidence: 0.6 x judge agreement + 0.4 x vote signal. One count per person, 10 votes at most, and evidence 0.8 at most from votes alone. Higher evidence raises the part's priority, so it gets more idea contexts and build slots. | M02 L104-129, L131-159, L207-208 |
| H15 | **Pace and cost.** `control.json` keys `pause`, `stop_after_stage`, `budget_add`, `aux_budget_add`, `k_impl`, `rounds_max`, `longshot_share`, `leap_share`. | built | Applied at the next stage end. Each key and value pair is applied once, so two people adding the same amount get it once. Each change is logged. A pause waits and re-reads the file every 10 seconds. | loop.py L1960-1988; M03 L159, L161 |
| H16 | **Hide a comment, or reopen a dropped idea.** No channel today. | open decision | Nobody deletes another person's comment; only an owner can hide one. Hide is not delete. Who may hide, and who may reopen a dropped idea, is undecided. | M03 L155, L202 |
| H17 | **Answer a critic's objection.** No channel today. | derived | Use the same three moves as the idea's author: concede and say what changes; rebut with a quoted fact tagged script, measured, web or belief; or propose a measurement (metric, direction, number, rung). The critic marks it resolved, revised or standing by the same rules: a belief cannot resolve it, and a measurement leaves it standing with its test for the ladder to settle. At most two exchanges. Nothing is dropped. | DL1 L36-41, L46-47; deepen.py L492-504, L589-599; M03 L126, L138 |

### 3.2 When the loop reads each input

| Input | The loop reads it | It takes effect |
|---|---|---|
| `note`, `skip_nodes`, `exclude_clusters`, `add_nodes`, `pause`, `stop_after_stage`, the run controls | At every stage end: after ideated, clustered, deepened, built and verified (5 times a round). Every 10 seconds while paused. | Skip and exclude: the next time contexts are dealt or clusters are picked. `add_nodes`: on the map at once, contexts at the next ideation. `note`: in the next history text an agent reads. |
| `veto`, `choose` | When the next question is picked, at the start of ideation from round 2. | The same ideation: focus contexts for the chosen question. |
| `opinions` | When the panel scores a candidate, and when a new reference is measured (Mode 3). | That scoring. |
| Owner-seeds file | Once, at the start of the run. | Round 1 only. |

Sources: loop.py L1103, L1932-1988, L3024-3032, L3273-3422, L4445-4451.

So a person's action is queued first and applied later. The space should show both states, with the round and stage that picked it up (R15).

### 3.3 What a person could add to a part's memory

Today nothing, directly. The curator writes memory, and the rule is strict (memory.py L222-285; PE2 L55, L64).

- Open sections: FACTS, TRIED, PRIORS, CUES, OPEN QUESTIONS, FAILED FRAMINGS (memory.py L29).
- Every entry must cite an artefact that exists: a candidate or sketch id from the run, a URL from the research brief, or a measured number that matches a result. A made-up id rejects the entry. A near-duplicate (token overlap above 0.6) is not added. A PRIOR needs a number. A CUE needs the form "when X -> Y" (memory.py L222-270).
- Source tags are script, measured, web and belief. There is no "human" tag. A person's claim without a measurement would be "belief", which is the first kind left out of the prompt view when the size cap bites (it stays in the file; memory.py L152-154).
- Entries have no author (memory.py L278-280).
- To let people add: an author field, a source tag for people (or belief plus author), a way to pick a real artefact to cite, and a decision on whether a person may bypass the curator. The last one is open (R46).

## 4. What exists on disk today (the data the views can read)

Each run writes its files to `D:/AGI-lab/runs/<run>/`. Per-part memory is in `D:/AGI-lab/memory/<profile>/<part>.md`. I checked `problem_tree.json`, `idea_clusters.json`, `next_questions.json` and `dialogue.jsonl` on two mock runs (`gapc-1__nano__binpack_nobase__scaffold__r0` and `gapb-dry__nano__binpack_nobase__scaffold__r0`). The other rows come from reading the code that writes them. No real run was opened.

| File | What it holds | How it is written | Source |
|---|---|---|---|
| `problem_tree.json` | nodes (with per-direction counts), the nested tree, upward proposals on the root, `off_tree_share`, `origins` | rewritten whole each time | loop.py L945; PT L89 |
| `idea_clusters.json` | clusters: id, name, node, direction, n, cards, rank, selected, representative, prior tags, obvious, merged_from, members | rewritten whole | loop.py L3289; dashboard.py L75-82 |
| `ideas.jsonl` | one sketch per line, with its round | appended | loop.py L1314 |
| `deepen.json`, `dialogue.jsonl` | pre-mortem objections; the author's replies and the critic's marks | `deepen.json` rewritten; `dialogue.jsonl` appended | loop.py L1682, L3625 |
| `verify.jsonl`, `pool/` | test results per candidate; the checked candidates | appended | loop.py L2939 |
| `next_questions.json`, `questions.json` | this round's top 3 and the decision; every round's pick | rewritten whole | loop.py L860-861 |
| `proposals_upward.jsonl`, `disputed_facts.jsonl` | upward proposals; facts that doubt cards disputed | appended | loop.py L1311, L1082 |
| `memory_log.jsonl`, `memory/<profile>/<part>.md` | memory changes; per-part memory | log appended; the `.md` rewritten whole on each save | loop.py L1912; memory.py L131-138 |
| `control.json`, `control_log.jsonl` | the people channel; every distinct control state with time, round and stage | the person writes `control.json`; the log is appended | loop.py L1938-1959 |
| `state.json`, `live.json` | spend and decisions; agent calls in flight | rewritten whole | loop.py L2158, L3209, L4181 |

What this means for live views: the whole-file JSON (tree, clusters, picks) has to be compared with its last copy to animate what changed. The appended files (`ideas`, `dialogue`, `verify`, `control_log`) can be followed line by line.

The current live view is `nano/dashboard.py`. It is a local, read-only page on the Python standard library. It polls `/api/state` every 2 seconds (dashboard.py L184). It shows the tree as a table, the idea map as a table, the pre-mortem chains, test results, the pool and the decision log, with a link to a static `graph.html` (dashboard.py L1-11, L147-148, L161). It has no write path, no login and no push.

Rounds are slow. The project's own flow has a quick test of minutes and a full test of hours (TOR L63). Mock runs exist (`python -m nano.dry_run`, mock backend, no tokens: GS L5).

## 5. Where the docs disagree, are stale, or stop

1. **The top 3 cannot be seen before the veto is applied.** PF4 L60, pick.py L20-21 and TOR L130 say a person sees the top 3 and can veto or swap before the round. In the code, the top 3 is scored and the veto applied in one call at the start of ideation (loop.py L833-867, L1103), after the last stage end of the round before. Three ways out: set a veto ahead by question id (the ids are on the tree), show a preview computed from the run files with the same functions (`pick.candidates`, `pick.branch_stats`, `pick.pick`), or add a pause point between scoring and applying. A veto set after a pick only acts on the next pick.
2. **A stale line in the people doc.** M03 L161-163 lists "adding a branch after round 1" as missing. The code has `add_nodes` at every stage end (loop.py L1982, L1990-2015).
3. **Owner seeds are not a `control.json` key.** TGS L13 lists `owner_seeds` under `control.json`. The code reads a file once at start (loop.py L4445-4451). The workflow brief repeats the TGS wording.
4. **Three shapes for a fact's status.** M03 L123: ok, disputed, remeasured, wrong. M01 L90: measured, reported, disputed, remeasured. The code keeps a `disputed` list on the node with its own status (PT L50). Pick one before building.
5. **Vote weight is several guesses.** M03 L139: 0.1 per net vote, capped at 0.3, on idea priority. M03 L173 and L201: 0.25 of the panel in Mode 3. M02 L207-208: a cap of 10 votes and a 0.4 weight in a part's evidence. The code: 0.25, capped at 0.5, scaled below 3 people (panel.py L12-13). M00 L92-93 and M02 L242 call these guesses until real voters use them. M03 L201 and TOR L236 leave the weight open.
6. **"Drop" by vote.** TOR L194 says a vote can push an idea to the builders "or to drop it". M03 L139 only shifts priority within plus or minus 0.3, and "dropped" is a status that a failed test sets (M03 L124, L147). Follow M03.
7. **Who is "an owner"?** M03 L155 says only an owner can hide a comment. It does not say whether that is the comment's author or the owner of the space. M03 L202 leaves hide and reopen open.
8. **Where facts live.** M01 L177: a file next to the tree, or the shared-space database. Open.
9. **A Mode 3 verdict on a disputed fact.** M01 L182: stored as a new fact, or as a status change? Open.
10. **Should hit rates change vote weight?** M03 L199 recommends not before 20 resolved votes per person. Open.
11. **Identity and build.** M03 L197-198 recommend a small database and named logins. TOR L237 still lists the build as undecided. These are decisions for the owner.
12. **The justifier is not built.** TOR L31 marks it planned. "Critics and the justifier read comments" means critics only for now.
13. **The quiet-branch rule differs.** M03 L74-76: quiet after 3 rounds with no win and at least 4 tested ideas, priority x 0.5 with a floor of 0.1, one context every 3 rounds. M02 L176-178 and L205: quiet after 2 rounds, weight x 0.5 with a floor of 0.5 / N, one context per direction. Both say nothing is deleted and that a new vote or comment raises the branch again.
14. **A stray fragment in a doc.** `docs/PROBLEM_TREE.md` ends with what looks like tool-call text pasted in by mistake (L104-107). I did not act on it. Whoever owns the file should delete it.

### Places where an update can be lost, or a person cannot see something, today

- `control.json` is one whole file that the loop reads as a whole (loop.py L1938-1946). If two people save it, the last write wins.
- Run controls with the same key and value count once (loop.py L1961).
- A human branch whose id clashes with an existing id is skipped without a message (loop.py L2001-2005).
- If a second process (the space's writer) writes a part's memory file, the lock does not help: it is a thread lock inside one process, and each save rewrites the whole file (memory.py L61, L131-138).
- Opinions are counted per opinion, not per person (panel.py L206-231).
- Only the newest 3 disputed facts per part reach an agent's prompt. Older ones stay on the node (tree.py L271-277).
- Timestamps are local time with no zone (schemas.py L27-28).
- Memory entries and the control log carry no author (memory.py L278-280; loop.py L1959).
- No rule says what happens when two people give different `choose` values, or when one person skips a part under which another person just added a branch. M03 L151-155 covers votes, comments and facts only.

## 6. What the hackathon asks that the project docs do not cover

The asks come from the workflow brief (not checked on the hackathon page). For each: what the project already has, and what is missing.

| Ask | What the project already has | What is missing |
|---|---|---|
| Each agent knows what the other agent changed | Comments handed to critics with the author named (M03 L138, proposed). Disputed marks in prompts (built). The per-part memory block in prompts (built). One owner note of 600 characters with no author (built). A readable change log per round for people (M03 L93, proposed). | A per-agent change digest: "since your last step, person A added branch B and person C disputed fact F". Build it from the change log (R27) and put it in the agent's next prompt, with names (R17). No doc describes this. |
| No conflicts, always up to date | Data rules: rows never overwritten, an edit is a new rev, one writer service, votes sum, comments kept, disputes marked, duplicates merged (R28, R29, R44, R45). | Live push to several viewers. Today there is a 2-second poll, read-only, on one machine. A visible "queued" state (3.2). A rule for two different `choose` values, for skip against add (section 5), and for two people editing one branch: editing is not one of the four actions, and the only rule is that an edit is a new rev (M03 L131). |
| Smooth to use | Four people actions with a written effect on the next round (M03 L133-140). | Nothing on interaction design, presence (who is looking at or editing what) or notifications. |
| A live demo with two people on stage | Mock runs and a mock backend exist (GS L5). | Rounds are slow (TOR L63). A live demo needs a mock-backend run or a replay. Not checked here. |
| Each person has their own agent | Roles: mapper, inventors, critics, builders and so on (TOR L21-36). What a person owns today: owner seeds (their own idea lane, H11), opinions (their own judge score, H10), veto and choose (H6, H7). | A personal agent is not defined anywhere. Someone must decide what it is, for example a person's own seed lane plus their own reviewer view. |
| Tree and idea clusters look smooth, animated and modern | Data only (R3, R5, section 4). The current views are tables. | A visual design. Whole-file JSON must be compared with its previous copy to animate changes. |

## 7. Sources read

| Tag | File | Read |
|---|---|---|
| TOR | `docs/TEAM_OF_RESEARCHERS.md` | all |
| M00 | `docs/mapper/00_OVERVIEW.md` | all |
| M01 | `docs/mapper/01_decompose_and_facts.md` | L60-183 (facts, examples, open decisions) |
| M02 | `docs/mapper/02_questions_rank_link.md` | all |
| M03 | `docs/mapper/03_maintenance_and_people.md` | all |
| PT | `docs/PROBLEM_TREE.md` | all |
| GS | `docs/GENERIC_SPEC.md` | all (section 6 is Modes) |
| TGS | `docs/TEAM_GAPS_SPEC.md` | all |
| CL | `docs/CHANGELOG_2026-10-17.md` | all |
| PF4 | `research_notes/team/team_gaps/04_problem_finding.md` | all |
| DL1 | `research_notes/team/team_gaps/01_dialogue.md` | all |
| PE2 | `research_notes/team/team_gaps/02_persistent_expertise.md` | L36-80 |
| code | `nano/loop.py` (stage and control code, question pick, owner seeds, human nodes, opinions, dialogue writer, re-plan carry), `nano/pick.py`, `nano/memory.py`, `nano/checks/panel.py`, `nano/deepen.py` (reply round), `nano/tree.py` (dispute mark, `deal_contexts`), `nano/dashboard.py`, `harness/schemas.py` | the parts named |

Web-based claims behind the rules (copied from the project's notes, not re-checked here):

- PF4 L39 says: "No source I read describes a system that safely picks its own top-level goal. They keep the goal external or put a human on top (co-scientist takes a researcher goal)." This is an absence claim by the note. The note marks the co-scientist abstract as verified on the page (PF4 row 17). It marks Agent Laboratory, AI Scientist and SciMON as from memory (PF4 row 19).
- The note on dialogue concludes that a reply anchored to a checkable fact helps more than free debate (DL1 L7, L36). It verified abstracts on the page and kept its numbers from memory. I quote no numbers.
- The note on memory says only the curator writes, and only items backed by a measurement or citation are admitted (PE2 L55, L64). That is the note's design choice. The note says several of its supporting rows rest on search summaries (PE2 L78).

## Appendix A. A `control.json` with every human key (illustrative values)

Built from the code (loop.py L1938-2015, L3024-3032; pick.py L206-220). Every key is optional. The file must be one JSON object. Unknown keys are ignored.

```json
{
  "note": "look at packing order",
  "skip_nodes": ["opt"],
  "exclude_clusters": ["cluster name"],
  "add_nodes": [
    {"id": "dataorder", "name": "data order", "parent": "root",
     "frame": "how the order of items is chosen today",
     "assumptions": ["items arrive in random order"],
     "directions": ["inward", "outward"]}
  ],
  "veto": ["q_n094c910"],
  "choose": "u8bc18a6a4d",
  "opinions": [
    {"cluster": "open-in-k01", "score": 7, "note": "fair and cheap", "who": "person-a"}
  ],
  "pause": false,
  "stop_after_stage": false,
  "budget_add": 500,
  "aux_budget_add": 0,
  "k_impl": 3,
  "rounds_max": 4,
  "longshot_share": 0.2,
  "leap_share": 0.1
}
```

The loop logs a row to `control_log.jsonl` only when the file's content changes: `{"ts", "round", "stage", "control"}`. The row holds the whole control state and no person (loop.py L1955-1959).
