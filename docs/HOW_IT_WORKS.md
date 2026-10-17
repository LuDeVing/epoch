# How a run works

*One complete run of the HTSA thinking process, from start to finish, in plain words.*

## The goal of a run

- We have a small language model and a recipe for training it. The recipe is a single script.
- A run must change that recipe so the model learns better, using exactly the same text and the same amount of training.
- "Better" is decided by an exam: after training, how well does the model predict text it has never seen. Lower surprise is better.
- The unchanged recipe is trained first. Its exam score is the bar every idea has to beat.
- The run itself does not train anything fully. It produces a shortlist of changed recipes that have survived cheap checks. The full training happens afterwards, overnight.
- The owner can state the purpose behind the goal in one or two sentences (for example: ideas that would make the strongest open-source model, with this small recipe as the test bench, so every idea must say why it would hold at large scale). Every agent reads it at the top of the problem statement.
- A run can be restricted to some parts of the recipe, for example the architecture only. The problem statement then names the parts that may change, with their boundaries, and the parts that stay exactly as they are, and the boundary check enforces it on every build.

## Why it is built the way it is

- If you simply ask an AI for ideas, you get the obvious ones, and asking again gives you the same ones in different words.
- A person who is good at this does something else: splits the problem into parts, finds out what others already tried, looks at each part from several angles, writes down a guess that can be proved wrong, tests it cheaply, fixes the near misses, and never trusts their own enthusiasm.
- The run is that behaviour, carried out by many separate AI agents under the control of a plain script. The script decides every step. The agents only fill in the pieces.

## The fixed rules

Written down before any idea exists, and shown to every agent:

1. Same training text.
2. Same amount of training, same exam. The exam is not run by the recipe: the recipe saves its trained weights, and a separate script owned by the run loads them and grades them on the held-out text. Whatever the recipe reports about itself is only compared with that grade.
3. The model may not grow by more than one tenth. Shrinking is always allowed.
4. It must fit in the memory of one laptop graphics card and run at most twice as slowly per step.
5. The script must still be runnable by the checker the same way as before.
6. No new software, no internet, no launching other programs, no peeking at the exam. Every training process runs under a watchdog that enforces this from outside: the candidate runs in a child process (on Windows inside a job object that allows one process), with secrets stripped from its environment; it can only read the training text (the exam text is not in its folder); network, process and low-level system calls are refused; a time cap is applied; the training tokens it reads are counted by the launcher and compared with what it reports; and any attempt is recorded and fails the candidate.
7. Only the exam score counts. It must beat the original's pooled average by at least 0.005 with an anytime-valid statistic (an e-value of at least 100, the one-percent level) over at least three runs, and survive the correction for the number of candidates tested that night (Step 12). This is the project's own rule (docs/VERDICT.md); the public speedrun records use no such pairwise test.

The rules are shown to each agent in a different order so nobody fixates on the first one. Under them, every agent also sees a computed cost card: where the recipe's parameters and compute go by component, and the exact headroom the rules leave in parameters, step time and memory, so "spend the headroom" is a number, not a feeling.

## Before anything else: the original is measured, and the obvious answers are locked away

- The original recipe is timed on the card today, and trained for 45 and 240 steps from three different random starts. The spread between those starts, step by step, is the noise floor every later comparison is measured against.
- Instrumented runs of the original, from three random starts, record how it actually behaves: the loss curve and where it bends, loss by position in the window, loss by how common each word is, and per layer the gradient size, the activation size and how sharp the attention is. This one-page table goes to the map-maker, to the idea agents, and to the questioning stage, so nobody theorises blind. Any cell that sits off the trend of its family on every start, after a filter for false discoveries, is listed separately as an anomaly for the agents to start from.

## Three control recipes go first

- Before any idea is tested, three known recipes go up the same ladder: a placebo (the original with a different data order, which must never win), a known small winner (which should pass), and a known loser (which must fail). Their outcomes are the run's own measure of false alarms and of blindness, and they are reported with the results. The overnight verdict can run them too.

## The constants are tuned by script, every run

- Invention is not the only road: at this size many real gains hide in the recipe's constants. So at round one a script, not a model, makes eleven single-knob moves around the current values (both learning rates up and down, weight decay, warmup, cooldown, gradient clipping, the rotary base) and sends each up the same ladder as every idea. The three that beat the original at the learning check go on to the long comparison and the night; the rest are dropped so the card is not spent on them. Because the values are read from the recipe as it is, the sweep follows it when a winner is promoted.
- The idea agents may also propose a tuning change, marked as such, when they have a reason (a warmup too short for the optimiser, an inherited constant from another scale); those are built like any idea. And when the night judges an optimiser idea, it re-tunes the original's learning rates first, so a tuning gain is never mistaken for a mechanism.

## The obvious answers are locked away

- The first thing the script does is ask the AI once: "what are the first five changes that come to mind?"
- Those five are saved in a private folder and never shown to any agent.
- At the end we can compare what the process produced against them. If the process only rediscovers the obvious, we will know.

---

## Step 1. Split the recipe into parts

- Before the map is drawn, one reading call asks the cheaper research model how the field splits this problem and where it is weak (never fixes). The map-maker reads that summary next to the measurements. A run with `--no-preread` skips it, as a control.
- An agent draws a map of the recipe as seven parts, each with:
  - a short description of how it works today;
  - three to five hidden assumptions, the things everyone takes for granted;
  - the exact region of the script it owns.
- A part may have sub-parts, and the map may grow to four levels during the run: parts, sub-parts, questions (a failed check with a reason becomes a question under its part, with the test that would answer it) and helper questions.
- The seven parts: how text enters and leaves the model; how it mixes information along a sentence; how it processes each word; how its layers are stacked; how it learns; how text is fed to it; what it is told to aim for.
- An eighth part is the whole recipe: ideas that only make sense across two parts have a home there.
- Above the parts sits the whole problem itself, so someone can also question the framing.
- The map is drawn by the strongest model, because it decides what the search can see at all. It is drawn through a lens: by default the parts of the recipe, for every run. The other lenses (the path of one token, the phases of training, where capacity is wasted, how small models fail) are used only when a run names one, or in a lens experiment (`--lens-by-replicate`), so the lens is never confounded with the replicate. The part's list of design assumptions does not grow during the run. What the questioning stage discovers an idea silently assumes is kept on the part as a separate list, shown to later agents as context only, never as a rule to break.
- If the agent's map is unusable, the script falls back to a built-in default map.

## Step 2. Research each part on the web

- For every part (not the whole problem, the off-map node or a question), one agent is sent to the web with a question: what has been tried here, what worked, what failed, what is untested at our small size.
- It comes back with a brief: 4 to 10 known techniques with their measured effect, up to 5 that did not help, up to 5 open directions, and the searches it ran.
- Every line must carry a real link. The script deletes any line without one, so the brief cannot contain invented facts.
- Briefs are kept for a week so a repeated run does not pay for the same research twice. The cache key holds the profile, the lens, the original's version and the part's description, so a changed part is researched again.
- A second search per part looks outside the field: five problems in other areas (biology, control, logistics, physics, economics) with the same structure, each with the mechanism used there, what corresponds to what, and a documented case with a link. These feed a dedicated analogy angle in the next step.
- Results of earlier runs are added to the briefs automatically: anything that won or failed the overnight verdict before appears as known or failed, so no run repeats a verdict it already has.
- A brief is reading material and a reference list. It never decides which ideas are good.

## Step 3. Many agents, many angles, short idea sketches

This is the heart of the run. Around thirty agents work, up to six at a time, and none of them can see the others.

**Each agent is assigned one part and one direction:**
- *Improve from inside*: keep the part's assumptions and make it better.
- *Step outside*: every idea must drop or flip at least one of the part's assumptions, and say which. Mere tuning does not count.
- *Question the whole thing* (whole-problem level only): propose a different measure of success. These are recorded as proposals for the humans, never built.

**Each agent is also given one of several ways in:**
- the problem and the script as they are;
- the script with every explanatory comment removed, so habit has less to hold on to;
- a digest of how the newest big models are built, scaled down to our size;
- the research brief for its part, with the instruction to go beyond what is listed as known or to test what is listed as open;
- an unrelated word, as a forced detour. The word is not drawn purely at random: each such agent on a part gets a different abstract function (flow, storage, feedback, timing, and so on), and the distances are mixed, about half far (everyday objects, nature), a quarter mid and a quarter near, because far analogies raise variance rather than the average. `--seeds random` keeps the old uniform draw as a control;
- the problem and the script read formally. In the map's parts this replaces the old "drop one assumption" card, because the step-outside direction already hands the agent the part's assumptions;
- the analogues from other fields, with the rule that every sketch must state the mapping from their structure to a concrete change here, transferring structure, never vocabulary;
- the measurements of how the original behaves, with the instruction to aim at the weakest point they show and to say which measurement each idea should move;
- three known techniques for the part with their measured effects, with the instruction not to copy them but to adapt them the way the public speedrun adapts ports: zero-initialise, last layers only, fewer channels, a learned gate;
- in later rounds, a measured trade-off from this run, an idea that learned better but paid in time, memory or size, with the instruction to keep the gain and remove the cost.

One extra agent per part and direction gets the research brief, when the brief has literature in it; the others do not. That way every run contains its own comparison of ideas with and without research.

Besides its own way in, every agent sees a short digest of what the strongest open models do right now: facts with sources, written by the research assistant from the newest technical reports, including the Chinese labs, and refreshed by a script before a run. The agent may port a component down to our size or deliberately go past it; a component counts only if it should lower the exam score at the fixed budget. The digest's hash is recorded with the run's commitments.

Every agent on a part also reads that part's memory, when it has one: what the team already knows about the part from earlier runs (facts, what was tried, calibrated priors, cues, open questions, framings that failed), as evidence it may dispute, never as rules. The memory is one file per part, read whole. After each round's checks one curator call per part proposes additions; a script keeps an entry only if it cites a record that exists and is not a near-duplicate, and never lets a model rewrite the file. One context per part and round ignores the memory, as a guard against fixation and an in-run comparison. `--no-memory` is the control arm.

**Every idea agent gets the web through a research assistant.** It first lists the questions it would want answered (the newest techniques for its part and their measured effects, what failed, facts it is unsure of), a cheaper research agent searches the web and answers them with sources, and the idea agent then writes its sketches with those findings in front of it. The expensive model never spends its turns searching. At least half of its ideas must be its own, and any borrowed idea must name where it came from.

**Each agent writes five to eight sketches, no code.** A sketch has these lines:
1. the idea, in a few words;
2. the mechanism: what changes and why it should help;
3. a prediction: what we expect to see in the measurements;
4. the cheapest experiment that would prove it wrong;
5. the source: "own", or a link;
6. the measurement it should move, and whether its benefit would even show in this exam;
7. its kind: a small trick adapted from somewhere, a tuning of existing constants, or a leap; a leap adds the rule it breaks, the core it keeps, its own chance of working and the number that would kill it.

An idea without a prediction and a test is not accepted as an idea.

**Two kinds of idea, by quota.** Every idea agent must deliver both: small tricks, which are known techniques adapted to this recipe and must say where they come from, and leaps, which drop or flip a rule the recipe takes for granted (what a loss is, what a layer computes, which tokens see which, how an update is made), keep the rest as it is, and might well fail. At least a quarter of each agent's sketches, never fewer than two, must be leaps, and a leap states the rule it breaks, the core it keeps, its own chance of working and the number that would kill it at the first learning check. The agent is not told to be bold; it is handed one of eight operators drawn from how breakthroughs actually arose (break one rule, subtract a part and reinvest, take a loose analogy literally, re-measure an inherited constant, re-represent the step, push a quantity to its limit, import one mechanism from a far field, assume a better recipe exists and name what it must be) and the two agents on the same part get different operators. **Three more sources of leaps.** The measurements of the original are taken on three seeds, and any cell that sits off the trend of the rest of its family on every seed, after a filter for false discoveries, is shown to the measurement-reading agents as a short list of concrete rows; those agents must start at least two sketches from a row, restate it, name three rival causes including a measurement artifact, and name the five-minute probe that would separate them. One run in ten carries a fabricated row, recorded privately, so the report can say how often agents chase noise. A leap that passes the first checks is a near miss or better, and the next round builds two variants of it, narrower and relaxed, outside the quota. And you can seed the lane yourself: a file of mechanisms, one per part, becomes an extra context each, and the agent must instantiate your mechanism three ways before it may depart from it.

Leaps are protected in selection by the long-shot lane, which takes about a fifth of the build slots (`--longshot-share 0.2`) and never fewer than two per round, with at least half of those slots going to leap groups whenever any exist, and they are counted separately in the report by operator, because the evidence says such ideas pay about one to three times in a hundred and must be judged by their best outcome over many runs, never by their average or by a dry spell. Each sketch also names the measurement it should move, so the build can later be checked against it, and says whether its benefit would even show in this exam; ideas about long context or inference cost are marked as outside the exam and ranked down.

Two measurements guard the ideation itself. The discovery curve counts how many new idea groups each round and each way in produced; a way in whose sketches keep landing in the same few groups is retired for the next round. And before any idea is built, a cheap text comparison against everything already built in this run and in earlier runs stops near-duplicates, building a random tenth of them anyway so the gate's own error rate is known.

## Step 4. Group the sketches, blind

- All sketches for one part and direction go to a separate agent that sees only the text. It does not know which agent wrote which, or which way in they were given.
- It groups sketches that describe the same mechanism, even in different words. Different settings of one mechanism belong together.
- Anything it drops becomes its own group. If it fails, the script groups by word overlap instead.
- One more call looks across all parts and merges the same change filed under two different parts, so nothing is built twice.
- The sketch that speaks for a group is the one with the cheapest test, never the longest text.
- Ten agents proposing the same thing become one group, not ten votes.

## Step 5. Tag each group against the research

- Each group is compared with the research brief for its part and tagged: *new*, *already known*, or *known to fail*.
- A cheap model does the matching, mechanism against mechanism, with word overlap as the fallback.
- Each group is also compared with the locked-away obvious answers from the start and marked "obvious" if it is one of them. That is the run's measure of getting beyond the first thing that came to mind.
- The tags are hints for the next step, never verdicts.

## Step 6. Choose what to build

- Round one has ten build slots: eight go by score, split about sixty-forty between improve-from-inside and step-outside ideas, and two form the long-shot lane described below. Testing is cheap here, so more ideas get real tests.
- Within each direction, groups get a score that adds up: how many *different* ways in produced the idea (for an idea born in the questioning stage, the idea it came from counts as a way in), a bonus for *new*, a strong penalty for *known to fail*, a smaller penalty for *obvious*, a little for a departure angle and for a cheap test, and a little against sheer size, because many agents agreeing is convergence, not evidence.
- A score that adds up, rather than a strict order, means a genuinely new idea from one angle can beat an old idea from two.
- Novelty is protected, not enforced. About a fifth of the build slots form a long-shot lane, never fewer than two per round, drawn at random, weighted by score, from the leap, step-outside, analogy, adapted, owner-seeded and new groups, with at least half of the lane going to leap groups whenever any exist; they get a lenient first learning check and their yield is reported on its own. The main slots go by score with only a small bonus for novelty, because the evidence says most real gains are adapted known techniques and recombinations, and that forcing novelty produces nothing. Once the record holds about a hundred builds, the weights can be learned from it.
- Slots are handed out in turns across the parts, so one part cannot take them all. Each turn starts with the parts that have had the fewest builds so far, so when there are fewer slots than parts the parts at the end of the map still get their turn in the next round. The questioning picks are spread the same way.
- How well a sketch is written plays no part. Only its spread across angles, its novelty and its testability.

## Step 7. Interrogate each chosen idea

Before anything is built, the best ideas are taken apart by questioning: not only the six that won slots but the top dozen or so, spread across the parts. This is where ideas get deep, and where many new ones appear on the way.

- A fresh agent receives the idea, the part it belongs to, the rules, the actual script the idea will be built into, the part's research brief, and the record of what this run has already built and what happened to it. It first writes the idea as a chain of three to six links from the change to the loss, each naming the quantity it moves, its measured value today, the expected direction, and the observation that would refute it, and marks the link it is least sure of. Then it asks itself as many questions as it takes, at least six and with no upper limit, aimed at the weakest links first, and only questions whose answer would change how the idea is built: each question says which two build choices it decides. The questions cover the exact mechanism, how it interacts with each other part of the recipe, how much compute, memory and time it costs, what settings and starting values it needs, what it silently assumes, how it could fail or do nothing, and what is already known about it.
- It lists the questions it would look up, the cheaper research agent answers them from the web with sources, and it then answers every question with facts, writing "unknown" where it does not know. Hopes do not count as answers.
- It then writes three lists:
  - *what the builder must know*: the concrete facts that came out of the answers, each tagged with where it came from: read from the script, taken from the measurements, found on a page with its link, or the agent's own belief. A measured claim without a source is dropped, and a belief never reaches the builder as a fact; it travels separately, marked as unverified. Before an idea is built, the numeric claims taken from the web are checked by the cheaper research agent against the very page they cite; a claim the page does not support becomes a belief;
  - *what the idea assumes*: these are kept on the part as what tested ideas assumed, apart from the part's design assumptions; later agents see them as context only, not as rules to break;
  - *new ideas that came up on the way*: four to six of them, one per slot: drop one of the idea's assumptions and build what follows, strengthen the mechanism, specialise it to fewer layers or one kind of token or one phase, port it to another part, combine it with a named known technique; each written as a proper sketch, each different in mechanism from the idea being questioned, each naming the part it belongs to so an idea for another part is filed there, and at least one of them a leap, marked with the rule it breaks;
  - *still open*: the questions it could not answer, each marked whether its answer would change how the idea is built.
- A separate agent then runs a pre-mortem: assume the idea was built and did not beat the original, and explain why, as concretely as possible, in terms of the actual script. It is given what the builder did not have, the measured results of earlier runs for this part, the measurements of the original and its anomaly rows, because dissent only helps when the critic knows something the builder does not. Each objection is typed (a broken rule, a hidden cost, an interaction that cancels the effect, an early-only gain, an effect below the noise, an implementation slip, something the exam cannot see, something only scale would show) and names the measurement that would confirm it: the parameter ratio, the step-time ratio, the loss gap at 45 or 240 steps, the trend, or whether the named measurement moved. The critic's default pack also holds the research brief's published failures for the part, each with its link. With `--premortem-web` the critic may first ask up to three questions of one shape ("has this mechanism been reported to fail or fade at small scale or under this condition?"), answered by the research model in one call with links. Then the idea's author gets one anchored reply round: for each objection it may only concede and change the idea, rebut with a quoted fact tagged with its source, or propose the measurement that would settle it; the critic marks each objection resolved, revised or standing. A belief cannot resolve an objection, and nothing is dropped. `--no-dialogue` skips the reply round as a control. The objections travel with the idea to the builder as things to address, and once the build goes up the ladder each one is marked confirmed or refuted by what was measured. Later builders of the same idea see the resolutions instead of the raw list, and the report counts how often the critic was right, so its weight can be earned rather than assumed. An objection class the critic raises against most ideas in a run (the effect is below the noise, the gain fades early, the builder will slip) is collapsed into one standing line that the ladder checks for every build anyway, so the builder's attention goes to the objections specific to its idea. The critic itself is measured once per version of the original: five copies of the recipe with a planted flaw, the known winners and the placebo go through the pre-mortem blind, and the record says how often it named the planted flaw and whether its severity tells a flawed idea from a good one. The first measurement found that it sees the flaw four times in five but objects to good ideas just as hard, which is why its objections are a checklist and never a gate.
- The open question that bears on the weakest link is handed to another fresh agent, together with the facts gathered so far and the chain, and that agent must also say which links its answers confirmed or refuted. Questions that are only curiosity are not followed. The chain stops going deeper when it would add nothing: when half the answers were "unknown", or when a level settled no link and produced no new fact. Otherwise this repeats two levels deep, so each chosen idea ends up with a chain of three interrogations, and the builder and the critic both receive the mechanism chain with the status of every link.
- Every new idea from these chains goes back into the pool of sketches, is grouped and tagged like any other, and competes for the build slots. The selection of Step 6 is then run again. An idea discovered while questioning another idea can take a slot from it.
- Then it happens again, one generation on: the best of the ideas that were born in the questioning are themselves interrogated the same way, producing their own facts, their own offshoots and their own open questions. Ideas therefore come recursively: an idea leads to questions, the questions lead to new ideas, and those get questioned in turn. The number of ideas questioned per generation and the number of generations are settings of the run. No idea is ever questioned twice, in any round.
- The facts from the whole chain travel with the idea to its builder. The questions and answers never rank the idea. They only make the build better informed.

## Step 8. Build each chosen idea

- For each chosen group, one agent receives the problem, the full script, the region its part owns, the chosen sketch, up to three variants of the same idea from other agents, and everything the interrogation established about it, with the instruction to pick the version most likely to work.
- It must return: one sentence saying what it changes and why, one line naming what it touched, a fidelity line (exact, partial, substituted, or cannot, with the reason), and the complete modified script. A build declared substituted or partial is recorded as such, so a failure of a watered-down build is never counted against the idea; a cannot records what blocked it on the part, beside what tested ideas assumed (context only).
- A builder that is missing one specific fact may ask for it on a NEED line instead of writing code (at most two). The loop looks each one up with a source and asks the builder once more. `--no-fetch-on-demand` is the control; it is on by default when the web is on.
- Everything outside its part's region must stay identical, so any difference in the exam can be attributed to the change. The builder is told exactly what the checker will enforce: it may add new functions, add settings, and wire a new component into the model, but it may not touch the exam, the data loader, or other parts.
- Two builds that turn out to be the same script after ignoring comments and spacing are merged. A script identical to one already judged in an earlier run reuses that verdict instead of being tested again.
- A build that fails the boundary check or does not start is handed straight back for one repair in the same round, with the exact violations, instead of waiting a round.
- Every builder also sees the few pitfalls recorded for its part in earlier runs: short lessons a script derives from the cheap checks (code written outside the boundary, a touched protected function, a crash on start), each with how often it was seen and whether a repair fixed it. A second kind of lesson records what the overnight verdicts settled. Lessons are written and merged by the script from the records, never by an agent, and a lesson gains standing only as more runs confirm it.
- After each round, pairs of checked builds that changed different parts of the script are spliced together by script, with no model involved, and the combination climbs the ladder as a candidate with two parents. This is the cheapest new candidate the run can make, and it tests directly whether improvements add up.

## Step 9. The ladder of cheap checks

A plain script, not an AI, checks every build. The checks get more expensive as they go, and stop at the first failure.

0. **Did it stay inside its part?** Free. Every function and class is compared with the original. A change outside the part's region, any touch of the exam or the data loader, or a forbidden import fails here, with the exact list of what went wrong.
1. **Does it start?** The script must run and report its size, which must be within one tenth of the original.
   **Does the change reach the computation?** Then one short forward and backward pass on the processor, no card time: every parameter the change added must receive a gradient, and if the model code changed but the output is identical to the original's with no parameter added, the change does nothing and fails here. This is the check for the silent no-op that the learning rung cannot see on this card. Three refinements came from the first real hand-built files: a parameter that gets no gradient only because another new parameter starts at zero is given one tiny step and checked again; a change that is identical at the start but acts once a shared value moves (a gain that starts at one) is caught by nudging every shared parameter of both models the same way and comparing again; and the probe text contains an end-of-text token, so document-aware changes have something to act on.
2. **Does it run?** Three real training steps. Memory must stay inside the graphics card, and each step must take at most twice as long as the original, measured on the same card at the start of this run, so a slow day never fails a good script. If the first timing is slow, it is measured once more.
3. **Does it learn?** Forty-five training steps from the same random start as the original. The error must fall, and at the same step the loss must not be behind the original's recorded curve by more than a few times the noise floor measured at the start. A candidate whose curve is identical to the original's at every step changed code that training never reads, and fails here.
4. **The long comparison**, after the round: every script that passed gets two hundred and forty steps, about five minutes, again from the same start. Its gap to the original's curve is read at the half and at the end, in units of the noise floor, and the trend between the two is projected forward. A lead that is shrinking is an early-training artefact; a lead that is growing goes first overnight.

A build that passes the first four checks is "checked": it works and learns about as well as the original over five minutes. That says nothing yet about the full exam.

Every checked build is also diagnosed the way the original was, and the measurement its sketch named is compared: did it move, in the stated direction? The answer travels with the build into the report. A predicted gain smaller than the noise between seeds cannot be checked at this stage and is not counted as held; the report says so.

Every build is also held to its own prediction. The sketch it came from said what would happen to the size, the speed and the loss; the measurements say what did. Whether the prediction held is recorded with the build, shown to the agents of later rounds, and counted in the final report, so the run learns which kinds of idea and which angles are trustworthy.

## Step 10. Fix the near misses

- A build that at least started but failed later gets a precise failure record: which check, why, and the exact error.
- It goes to a revision queue, closest misses first. In the next round, up to two of these are handed to a fresh agent with the previous script, the idea's full specification (the sketch, its target, its mechanism chain, the verified facts and the objections), a short post-mortem card (which check failed, why, where, and the cause tag) instead of a raw record, and a move chosen from the failure: a build or boundary failure gets fixed, a memory or speed failure gets the idea applied to a smaller piece.
- The revised build climbs the same ladder. It remembers its parent, so ideas have a family tree.
- A build from the long-shot lane that passed the ladder is a near miss or better, not a failure: two variants of it, one narrower and one relaxed, are built in the next round outside the quota, because the evidence says exploring around a promising long shot is where the hits come from.

## Step 11. Rounds and the budget

- A run has two rounds by default. Round two has a third of the build slots, uses the revision queue first, skips groups already built, and questions only ideas not questioned before.
- Round two knows what happened in round one. Every sketch and interrogation agent gets the record: what was built, whether it passed, why it failed, how it compared with the original. Noticing failure and switching is the point of a second round.
- From round two the team also picks its next question. Open questions on the map (each with a test, a threshold and a failure condition) are scored by the chance of resolving them, what the answer would unblock, how new they are and what they cost; every few rounds the most novel one takes the slot instead. The chosen question's part gets two extra contexts. A person sees the top three and may veto or choose one through the control file. `--no-pick-questions` is the control arm.
- Every call of the inventing model is charged against a fixed budget, split into envelopes per stage (research, ideation, judging, interrogation, building, a reserve). The cheap model's calls, web research and clerical work, are metered apart and do not count against that budget: a web-research call reads its pages again on every search turn and so counts about half a million tokens, which would otherwise have emptied the budget before a single build. They have their own, much looser cap (ten times the budget unless set); past it the run stops searching the web and goes on with what it has, instead of stopping. The dashboard and the report show both meters. Before each call the script estimates its cost; a call that would go over is skipped and logged, and a call from any stage but building is also refused when it would eat into the builds' floor, so a round can never spend its budget on ideas and then build nothing. A round only gets the build slots the remaining budget can pay for.
- The run ends when the rounds are done or the budget is spent.
- A small run can cap the number of idea contexts per round. The cap is dealt round-robin across the parts, each part's richest context first (an owner seed, then the research brief, the diagnosis, the analogy), so every part is still seen before any part is seen twice.
- The owner can steer without stopping: a small control file in the run folder, read at every stage boundary, can pause the run, stop it cleanly after the current stage, exclude a part or an idea, add budget, change the number of build slots, rounds or lane shares, or leave a note that every later agent reads. Every change to the file is logged with the stage it took effect at.
- A run that crashed or was stopped can be resumed: everything already on disk is reloaded and the interrupted round continues from its first incomplete stage, without paying for the stages that were done.
- Before any idea exists the run writes its commitments to a file, hashed into its state: the rules, the win margin and level, the baseline's hash, the selection weights and whether they were learned, the slots, the models, the budget and its envelopes. The report prints them with the number of control-file changes, so a reader can tell a pre-registered result from a tuned one. Every build also records a manifest of what its builder saw (the sketches, the facts, the objections, the chain, the lane and its selection probability), and every selection round records why each group was chosen or dropped: picked by score, picked by the lane, below the cut, or at the cut but the turn went to another part.
- The output is a pool of checked scripts, ranked by their projected five-minute gap in units of the noise floor, plus a complete record of every decision, the proposals for new framings of the whole problem, sourced facts from the questioning stage saved into the research briefs for the next run, and a written report: the funnel from sketches to verified wins with conversion rates, costs, idea sources, how many ideas were obvious, how predictions fared, and for each verified winner the closest known technique.

## Step 12. The overnight verdict

- Every full training run happens under the same watchdog, from the training text only, with a time cap set from the original's own full-run time and the candidate's measured speed. When it ends, the run's own exam script grades the saved weights. A candidate whose self-reported score disagrees with the exam fails.
- The original recipe's own wobble is measured once and shared: six full runs from different random starts by default, kept in one place and reused by every run after, so the noise estimate gets better over time instead of being redone each night. The noise the verdict uses is fixed from those runs alone before the first candidate, as an upper bound on their spread, and candidate run s is paired with the original's run s.
- Candidates are trained in stages, best five-minute gap first, with one slot in every five reserved for the ambitious lanes (long shot, family variants, hedge), so a long shot is examined even when it ranks below the safe ones. Every candidate gets one full run. A candidate worse than the original's worst run stops there; one whose first two runs are both worse than that stops for futility; the rest get more runs while they are still promising or a close call, up to five.
- Each run adds evidence to an e-value, a statistic that stays honest whatever is decided from it: seeds can be added or stopped on the evidence so far without inflating the chance of a false win. A script *wins* when the evidence that it beats the pooled original by at least 0.005 reaches the one-percent level over at least three runs, and survives the correction for the number of candidates tested that night.
- A smaller but real gain, at least 0.002 with the five-percent level and the same sign at every rung, is *stackable*: not a win on its own, but real enough to be combined with others. Stackable changes are composed by script and the combinations are tested the next night, so small wins add up instead of being thrown away.
- Optionally the original is also trained with proportionally more text, to answer whether a slower candidate earned its gain or bought it with extra compute; winners can be re-trained at double the budget to see whether the gain holds; and optimiser ideas can face an original whose settings were tuned the same way as theirs.
- Better but inside that margin is a *close call*. Everything else fails. Nothing that failed is ever counted.
- A time limit stops the night cleanly; everything finished is kept and the rest resumes next time.
- A winner can then be promoted: it becomes the new original, the old one is archived with the verdict it lost to, and every later run measures against the new recipe. Winners compound instead of being rediscovered.
- Every result goes into a permanent log with the idea, its family tree and the numbers.

---

## Building by hand, reference rows, and tests without training

- The loop can be stopped cleanly at the end of any stage through its control file. Stopping after interrogation leaves everything a builder needs on disk, and two files render it for people: the chosen ideas with their sketches, chains, facts, open questions and objections, and the full catalogue of sketches by part and kind. With them go the baseline script, the problem statement with its rules, a prompt for a coding agent to build one idea as a complete script, and a step-by-step course from idea to write-up. Hand-built scripts climb the same ladder and go to the same night; nothing about the verdict changes.
- Reference rows are models compared for context rather than judged as candidates: the strongest open models' dense architecture scaled to this size, built from their published configurations, and that skeleton with our changes added. They may run outside the step-time cap, since the question is the architecture at equal tokens, and the write-up says so next to their numbers; the compute-matched comparison is the honest companion for anything slower than the original.
- Some questions need no training at all, only saved weights and held-out text. Premise tests check whether an idea has the lever it assumes: whether the final norm's gain really drifts from one, whether a token's residual magnitude really predicts how hard the token is. A post-hoc fit tests a mechanism with a few parameters after training. Lesion tests switch one mechanism off inside a trained model and measure the loss it costs: how much the model came to rely on each part, which is not the same as what each part contributed, so the single-idea runs remain the final word. These run in minutes on the processor while the card trains.

## How we know the method matters

- The same run can be made with the thinking removed. The `plain` arm asks the same strong model for a change and a complete script, with no map, no research, no questioning and no selection, and puts the results through the same ladder, the same controls and tuning sweep, and the same overnight exam. It builds until the same token budget is spent (`--n-builds` 0 by default) and shows the rules in the same canonical order as the scaffold's builders. The `climb` arm does what the public autoresearch loop does: one build at a time, each starting from the current best script, keep or discard.
- Each stage of the thinking can also be switched off on its own, and every feature added on 2026-10-17 has its own control arm: `--no-preread`, `--no-memory`, `--no-dialogue`, `--no-pick-questions`, `--no-fetch-on-demand`, `--seeds random`; `--premortem-web` is off by default. The report compares arms and ablations side by side: verified wins per unit of cost, and the share of ideas that were new.
- Without this comparison a win would show that the model is good. With it, a win shows what the method added.

## What the card is used for, and when

The graphics card trains the real small model, but almost always for seconds or minutes, never to completion except overnight. In order of appearance:

- **Measuring the original, once per version of the original.** Three steps to time it on the card today; forty-five and two hundred and forty steps from three different random starts, to get the noise floor every later comparison is measured against; and one hundred instrumented steps from the same three starts, to get the measurements of how it behaves and the rows that stand out from seed noise. All of it is cached, so a later run pays nothing unless the original changed.
- **The three control recipes**, through the same ladder as the ideas, at the start of each run: a few minutes.
- **The ladder, for every built idea.** Three steps for timing and memory; forty-five steps for the learning check, about a minute; two hundred and forty steps for the long comparison, about five minutes. A round of ten builds is roughly an hour of card time.
- **The overnight exam**, the only full training: fifty million tokens per run, about thirty-one minutes each, three to five runs per candidate plus the original's own runs. This is where a result becomes a result, and it starts only when you start it.
- **Test runs of the machinery.** A dry run uses fake agents that cost no model calls and write dummy changes, but the training side is real, shortened to twelve and thirty steps, so the code around the ideas is exercised end to end in about ten minutes of card time. A run that stops before anything is built, for instance to look at ideas only, never touches the card.

## What you see while it runs

A local page in the browser, refreshed every two seconds:
- the budget bar (the inventing model's tokens) with the cheap model's meter beside it, and what the run is doing right now;
- every agent: running or finished, its part, its angle, its cost, and what came out;
- the map of parts, each with its research summary and links, and per direction how many sketches, groups, builds and checked scripts;
- the idea map: every group with its score, its tags (new, known, known failure, obvious), how many angles produced it, its mechanism, prediction and test, and whether it is being built; plus the counts that measure the run: how many ideas came from the agents themselves versus the web, how many groups match the obvious answers, how many cross-part duplicates were merged, and per generation of questioning how many calls, new ideas, facts, and unsourced numbers dropped;
- the interrogation of each chosen idea: the questions and answers level by level, the facts for the builder, the new ideas that came up, and what is still open;
- each build's position on the ladder and the reason if it failed, including the exact boundary violations;
- the pool with each script's five-minute and one-minute gaps to the original, and the full decision log;
- the controls' verdicts, the discovery curve, the long-shot lane's yield, the leaps by operator, the tuning table, the anomaly rows and whether the fabricated one was chased, the critic's hit rate, the commitments, the selection reasons, a reproduction card for every winner (script hash, what changed, the closest known technique, the command to rerun it), the fidelity checks and the near-duplicate gate's record, in the written report. The report opens with a page for a newcomer: the result, whether to trust it and why, what it needs from you with the command and its cost, and a six-term glossary.

## The rules the run never breaks

- No idea is ranked by how good it sounds.
- No fact enters without a link. No result enters without a measurement.
- Agents proposing ideas never see each other, so one loud idea cannot silence the rest.
- The agent that groups ideas never knows who wrote them.
- The first obvious answers stay locked away until the end.
- A failed check is never skipped to save money.
- No idea is questioned twice, and no verdict is repeated: what earlier runs settled is in the briefs.
- Every call is recorded, so any result can be traced to the exact call that produced it.

## Who does the work

- The strongest available model proposes ideas and writes the code, with its reasoning effort set by role: high when it builds or repairs, medium when it questions, low when a cheaper model does clerical work. Weaker models recall; they do not invent.
- A cheaper model does the mechanical jobs: the web research, the searches the idea agents ask for, drawing the map, grouping the sketches.
- A plain script makes every decision, runs every check and does all the training. The models never grade their own work.
