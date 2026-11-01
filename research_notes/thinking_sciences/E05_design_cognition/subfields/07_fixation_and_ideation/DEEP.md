# Fixation and ideation: deep document

*Subfield E05.07. Key work: Jansson and Smith 1991 ("examples fix ideas"). Why it matters: schema state S3 (fresh contexts). Sources: evidence_a-d.jsonl (ids a01-d22), claims.jsonl (K01-K33), critique.md in this folder. Honest warning up front: the founding numbers of Jansson and Smith 1991 and the effect sizes of the Sio 2015 meta-analysis were never read from the primary papers. Everything about them is second-hand. The strongest evidence here is on LLMs, and most of it comes from GPT-4o-class models, not Claude.*

## 1. What it is

Design fixation is the habit of staying close to something you already have in mind. The "something" can be a pictured example, an early idea of your own, or the way you solved the last few problems. The result is ideas that copy features of the source, cover fewer categories, or repeat one approach when a cheaper or better one exists.

Three related things are often mixed under this name. Keep them apart.

- **Example fixation** (Jansson and Smith 1991). A designer sees one example. Later designs reuse its features, even flawed ones. The source is an outside stimulus.
- **Mental set / Einstellung** (Luchins 1942; Duncker 1945 for functional fixedness). A run of problems solved one way makes a person keep that way when a better one exists. The source is the person's own recent history. Neroni et al. 2017 argue design fixation is closer to this (a13).
- **Within-session ideation fixation.** Early ideas in one session make later ideas fall in the same categories. Measured as how fast new categories accumulate across a sequence of ideas (Deng et al. 2026, a20).

For an LLM agent there are two more things that look like fixation and are not the same:

- **Cross-session sameness.** Many runs of the same model give the same ideas ("hivemind"). This is not fixation inside a run. It is missing spread between runs (a21, b24).
- **Anchoring on context.** Numbers, hints, early guesses and earlier outputs in the prompt pull later answers (c21, c22, c25).

The most useful result of this folder: for LLMs, the cross-session problem dominates. Within one session GPT-4o fixates about as much as people (a20). Across sessions it is far narrower (a21). That changes what S3 should do.

## 2. History and theories in depth

**Roots.** Duncker 1945 (functional fixedness: seeing an object only in its usual role). Luchins 1942 (water jars): after several problems solved by one long method, most people kept the long method on a problem with a one-step solution. A control group that saw only the critical problem solved it fast (b07, a13; both second-hand through Neroni 2017).

**Founding study.** Jansson and Smith 1991, Design Studies 12(1):3-11 (a01). Four experiments. A treatment group got a design brief plus a picture of an example. A control group got the brief alone. Tasks included a car-mounted bicycle rack, a measuring cup for the blind and a spill-proof coffee cup (a02). Example pictures carried deliberate flaws (features that broke the brief). Reported pattern, second-hand (a04, a18, b02):
- Both groups made a similar number of designs.
- The treatment group's designs reused example features, including the flawed ones, at an abnormal rate.
- Copying also appeared in experienced designers (Exp 4 used professional engineers, d02).
- A later experiment found lower flexibility and originality in the fixated group.
- Telling people to avoid the example's problems did not stop copying (a03, b08). This is second-hand and contested (see section 5).

Exact N and copy counts: not read. Treat the effect as "reported", not "measured by us".

**Extensions and doubts (1990s).**
- Smith, Ward and Schumacher 1993: three experiments in which examples constrained features of new toys and imaginary creatures (b03, second-hand).
- Purcell, Williams and Gero 1993, "Fixation effects: do they exist in design problem solving?" (a07, b04). Snippet only. Reported as a weak replication: fixation seen mainly when the example matched the designer's expertise or domain familiarity. Unverified.
- Purcell and Gero 1996 place design fixation among other fixation types (a06, not read).
- Perttula and Liikkanen 2006 (b01, read): see section 5.

**Reviews.** Youmans and Arciszewski 2014 (concepts); Sio, Kotovsky and Cagan 2015 (meta-analysis, 43 studies, a09/d03, search summary only); Vasconcelos and Crilly 2016 (methods; 25 studies using the same basic example-exposure design, 14 manipulated variables, a08, abstract only). Neroni et al. 2017 add that the field leans on open-ended early ideation and subjective metrics (b09). Over half the studies in Vasconcelos and Crilly score fixation as presence or absence of repeated example features (d02).

**Competing explanations.**
1. *Associative networks and lateral inhibition* (Howard et al. 2013, a15). Typical examples activate related concepts and suppress distant ones. Authors' account, not tested directly.
2. *Unconscious plagiarism / part-list cueing* (Marsh et al. 1999; Deng et al. a24). Examples leak features even when told to avoid them.
3. *Sampling probability* (Perttula and Liikkanen, b01). Examples use up the easy ideas, so fewer new categories are left to explore. Not conformity.
4. *Selective forgetting of redundant ideas* (Smith and Blankenship 1991; the 2019 dyad study, d05). Exposure hurts late, and breaks undo it.
5. *Mental set* (Neroni, a13). Own earlier solutions, not only outside examples.
6. *LLM-specific*: autoregressive decoding means early output conditions later output (a24), and a shared training distribution means no spread across runs (b24). Post-training shrinks the distribution further (c14, c15, c16, c19).

**Fixation versus inspiration.** Examples are not only harmful. Sio et al. 2015 (search summary): examples narrow the range of ideas but raise novelty. Quality rose with degree of copying. A single uncommon example helped most (d03). Perttula and Liikkanen saw 13 cases where an example triggered a new sub-function solution, 27% of 47 extra solutions (b05). So the question is not "do examples fix ideas" but "when does the narrowing cost more than the lift".

## 3. Core findings with exact numbers

Status key: **E** established (2+ independent sources), **S** single source, **C** contested, **H** human-only, **G4** GPT-4/4o-era model only.

| Finding | Numbers | Source (ids) | Status |
|---|---|---|---|
| Humans copy features of a shown example | Founding numbers not read. Similar idea counts, more similarity to example, lower flexibility and originality | Jansson and Smith 1991 (a01, a04, a18; second-hand) | S, H, unverified numbers |
| Example fixation does not always show | N=16 (8/group). Ideas 9.38 vs 8.75 (p=.75). Categories 12.88 vs 13.00. Example-feature reuse not different (e.g. .55 vs .47, p=.50). Non-redundant categories 6.00 vs 13.00 (t=3.74, p=.01) | Perttula and Liikkanen 2006 (b01) | C, H |
| Warning to avoid the example's flaws | J&S: copying persisted (second-hand). Chrysikou and Weisberg 2005: defixation instruction diminished the effect (Exp 1 N=89 in 3 conditions, Exp 2 N=60). Copy counts unread | a03, b08, d01 | C, H |
| Mental-set fixation in design | After 5 single-approach trials: 83% (15/18) vs 44% (8/18) used the costly approach on dual-approach trials (chi2=5.90, p=.01). Trials 47% vs 18%. Cost $30,077 vs $27,461, d=1.10. Time 102.5 vs 74.4 s, d=.70. Parts 26.5 vs 19.6, d=.85. 9/18 (50%) vs 2/18 (11%) said they were on autopilot | Neroni et al. 2017 (a10, a11, a12, b06) | S, H |
| Debiasing lecture lowers fixation | Ratio 0.88 to 0.53 (76 to 48 elements), 12 teams, no control, p=.026 | Howard et al. 2013 (a14) | S, H, weak |
| Examples: narrow range, raise novelty; few and uncommon best | 43 studies. No effect sizes obtained | Sio et al. 2015 (a09, d03) | S, snippet |
| Harm from exposure is late harm | Idea count in last 10 min: exposed-immediate vs exposed-relax -3.21 (p=.003); vs exposed-task -2.38 (p=.029). Harm absent in first 10 min | Dyad study 2019 (d05) | S, H |
| Incubation helps divergent tasks most | Positive overall; divergent > insight; long preparation helps; high-demand filler hurts. No effect size read | Sio and Ormerod 2009 (d04) | S, H |
| Human fixation on AI images | GenAI +.32 (89% CI .11-.55, BF 124); image search +.27 (BF 42). Log-link coefficients. N=60 | Wadinambiarachchi et al. 2024 (a16, c01, c02) | S, H |
| Fluency loss with image tools | Image search -.49 (CI -.9 to -.10, BF 46.6); GenAI total effect -.21 (CI crosses zero) | same (c02) | S, H |
| LLM within-session fixation equals humans | Slope 1.013 vs 1.035 (p=.51). Categories 12.46 vs 12.68. 99 vs 99 | Deng et al. 2026 (a20, b10) | S, G4 |
| LLM cross-session gap | First-idea categories (groups of 10) 8.37 vs 14.51. Pairwise distance 1.51 vs 2.41 | Deng (a21, b10) | E (with c05, c07) |
| Seeding with a human first idea | Categories 18.34 vs 18.35 (p=.95) | Deng (a22, b11) | S, G4 |
| Chain of thought (list 10 titles, revise bolder) | Slope 1.013 to 1.363 (main); 1.095 (robustness). Human unchanged 1.035. Totals: LLM 22 cat / 83 combos; +CoT 27/152; persona+CoT 27/248 vs human 28/197 | Deng (a23, b12, b13) | E (with Meincke) |
| Ordinary personas | Totals 27 cat, 193 combos vs human 28/197. Persona lowers within-session slope (.876) | Deng (b12) | S, G4 |
| Prompt strategy changes pool spread | Cosine: human .243; GPT-4 prompts .255-.432; base .377-.386; CoT best. Unique ideas ~3700 vs ~4700 | Meincke et al. 2024 (a25, b14) | S, G4 |
| Mixed strategies beat repeating one | Little overlap in first 50 ideas across strategies. Prior top ideas as seeds: .403 vs .386 | Meincke (b15) | S |
| Same-model repetition | Pairwise similarity >0.8 in 79% of cases. Min-p, temp 2.0: 61.2% >0.8, 81% >0.7. Cross-model 71-82% | Jiang et al. Hivemind (b21, c07, c08, c09) | E |
| Population variability | AUT cosine distance LLM .459 vs human .738; FF .534 vs .835; DAT .665 vs .819. System prompt does not fix | Wenger and Kenett 2025 (c05, c06) | E |
| Fewer than 3 distinct answers in 10 samples | 1,100 prompts, 20 models; larger models worse | NoveltyBench (c19) | E |
| Show-previous regeneration | Claude 3 Opus, GPT-4o, Gemini 2.0 Pro reach about human diversity over 8 generations. Reasoning effort: no help or worse (o-series) | NoveltyBench (c20, d09) | E for regeneration; S for reasoning effort |
| Independent fresh single-idea sessions are least diverse | GPT-4o: 0.452 (independent) vs 0.679 (one session lists many) vs 0.698 (CoT) vs human 0.773. Claude Opus 4.8: 0.24 vs 0.80 | Terwiesch et al. 2026 (d06); Wadhwa et al. 2026 (d08) | E |
| Per-idea quality cost of a list | Claude Opus 4.8 win rate 0.33 vs 0.21; utility 0.34 vs 0.38 | d08 | S |
| Random persona or constraint per session | 0.757 and 0.735 vs plain 0.679, human 0.773. Eccentric personas no better. Industry paper +4.76 on a judge score (d=2.88, 7 tasks, vendor) | d07, d22 | S |
| Repeated "bolder" refinement | Two passes 0.575 vs 0.679 plain | d07 | S |
| Pool saturation | 4000 seeds per topic: about 200 (5%) non-duplicates at cosine 0.8, even with earlier titles shown | Si et al. (a26, b22, c11, d10) | E that it saturates in that task |
| No saturation in another task | Coverage of human ideas, mean nearest-neighbour distance .546 (N=100) to .478 (N=1,000) | d07 | C against the row above |
| Co-writing homogenises groups, not individuals | Group-level t(32)=3.21, d=.67; individual .65 vs .66 (p=.35). Categories 8.58 vs 6.77 (d=.54) | Anderson et al. 2024 (a28, b16) | S, H |
| AI story ideas: novelty up, similarity up | Novelty +5.4% (1 idea), +8.1% (5); similarity to AI idea +5.2%; low-creativity writers gain up to +10.7% | Doshi and Hauser 2024 (a27, b17, b18, c13) | S, H |
| Feedback-tuned model homogenises; base does not | N=38. InstructGPT lower diversity; GPT-3 not | Padmakumar and He (b19, c14) | E with c15, c16 |
| Post-training shrinks diversity | Verbalized sampling recovers 66.8% of base diversity; 1.6-2.1x over direct | Zhang et al. 2025 (c16-c18); Mohammadi 2024 (c15) | E |
| Anchoring in LLMs | CoT, reflection, "ignore the anchor" did not reduce it. 9 of 11 exceptions from GPT-3.5 | Lou and Sun 2024 (c25) | S |
| Early commitment in multi-turn | Average drop 35-39% (200,000+ conversations, 15 models). Recap recovers part | Laban et al. 2025 (c22, c23) | S |
| Label/order bias in few-shot | "P P P N" gave ~90% Negative. SST-2 accuracy 54.3-93.4% by order. Calibration up to +30 points | Zhao et al. 2021 (c21) | E (analogue) |
| Coverage with many samples plus a verifier | 15.9% to 56% from 1 to 250 samples (SWE-bench Lite). Plateau without verifier | Brown et al. 2024 (c24) | E |
| Sequential vs parallel with verifier | Sequential narrowly better overall (MATH); hard items need a mix | Snell et al. 2024 (d11) | S |
| Strategy-mode coverage beats one mixed distribution | Pass@k math; up to 4x efficiency, up to 10% | Wu et al. 2025 (d21) | S, small models |
| Personas cost accuracy on correctness tasks | MMLU 71.6 to 68.0 (long persona 66.3). CSQA -2.1 to -4.4. Temperature spread -0.11 to -0.41 | d18, d19 | E |
| Mechanism-shift failure in agents | Claude Sonnet 4.6 path discovery 53.6% to 73.2% with switch operator; GPT-5.4 48.2% to 67.9%; Self-Refine 44.6% | MUTATE (d14) | S |
| Context rot, summary trigger | 32K: 57.7% / 2.4% inconclusive; 48K 50.6% / 7.2%; 64K 41.7% / 20.2% | Xia et al. 2026 (d12) | S |
| Drop give-up trajectories before voting | +2.6 to +4.9 points | d13 | S |
| Einstellung probe, older models | o1 48%, Gemini 1.5 Pro 50% vs physicians 66%. GPT-4 solved 3-6 of 494 red-herring walls vs 285 human | d15, d16 | E |
| Einstellung probe, newer models | Claude 4.1 Opus 0.751 vs physicians 0.66. On the 20 physician-missed items: 55.0% decisively correct | Shidara et al. 2026 (d17) | S (same 100 items) |
| Method prompts for defixation | Simple "think wild" beats elaborate TRIZ/SCAMPER prompts. Novelty +10 to 24%. Cross-model distance only .206-.341 | IDEAFix (d20) | S |

## 4. Mechanisms and models

Written so that an engineer can build or test each one.

**4.1 Slope-of-accumulation fixation metric (Deng).** Ask a source (human or LLM session) for 10 ideas in order. Label each idea with a category set. Plot cumulative distinct categories against idea number. Fit the slope. A high slope means ideas keep opening new categories. Compare to the human slope (1.035). Category labelling needs a labeller model, which is a weak point (a28: best embedding agrees with human coders 59%).

**4.2 Cross-session spread metric.** Run N sessions with the same prompt. Take the first idea of each. Compute mean pairwise embedding distance (or count distinct categories and distinct category combinations). Humans: distance 2.41, 14.51 categories per group of 10. GPT-4o: 1.51, 8.37. Alternative: 1 minus mean pairwise cosine (Terwiesch: human 0.773). Always report the embedding model. Hivemind uses text-embedding-3-small; Si uses MiniLM at cosine 0.8 for a duplicate.

**4.3 Two-cause model of LLM narrowness.** Cause A: within-session fixation (early output constrains later output). Cause B: no knowledge partitioning (every run draws from the same distribution). A is measured by the slope, B by cross-session first-idea spread. Result (a20, a21): A about equal to humans, B very different. Fixes: A is moved by chain-of-thought list-then-revise (slope 1.013 to 1.363). B is moved by random personas or constraints per session (0.679 to 0.757). They interact: ordinary personas lower the within-session slope (.876) while raising cross-session spread. Use both and log each separately.

**4.4 Why bare fresh contexts fail.** A fresh context with an identical prompt resets A but not B. Each run draws the same typical idea. The result is the least diverse arm (0.452, d06; 0.24 for Claude Opus 4.8, d08). One session that lists several ideas spreads them because the model avoids repeating itself in the visible list. Implementation: ask each fresh context for a list of k (3 to 10) ideas, not one.

**4.5 Persona or constraint injection.** Per fresh context, draw one short persona (an ordinary person: a nurse, a teenager) or one constraint (a random design rule) from a list in code. Add to the prompt. Keep ideation lists inside the context. GPT-4o: random persona 0.757, constraint 0.735. Over-eccentric personas add nothing (d07). On correctness tasks personas cost accuracy (d18, d19), so use only in open mode.

**4.6 Generate-then-revise (CoT ideation).** Step 1: list k short titles. Step 2: revise to be bolder and more different. One context. Works for LLMs (slope 1.013 to 1.363), not for humans. Caution: repeating "make it bolder" on its own output twice reduced set diversity (0.575 vs 0.679, d07). One revision pass, not iterated.

**4.7 Show-previous regeneration.** Keep earlier answers visible and ask for something different (NoveltyBench). Lifts three frontier models to about human diversity. Seeing earlier ideas without that instruction is a different case: Deng's human seed (b11) did nothing, Si's earlier titles slowed but did not stop repeats (d10).

**4.8 Strategy-mode conditioning (for correctness tasks).** Split samples across named approaches (induction, contradiction, brute force, invariant) rather than persona voices. Argument: with success rates p1, p2 on two modes, spending k/2 on each beats k from the mixture when the modes are complementary (d21). Verified only on small trained models.

**4.9 Switch trigger on repeated same-mechanism failure (MUTATE).** Code tracks the mechanism label of each failed attempt. When failures on one target pass a threshold, force a divergent step: generate candidates with no convergence pressure, then select by check. Claude Sonnet 4.6 path discovery 53.6% to 73.2% (d14). Generic Self-Refine lowered it (44.6%). This matches G1/G2: switch on a signal, not on a schedule.

**4.10 Context length triggers.** Summarise and restart when context passes a length (32K was best in one open-model test, d12). The gain came from fewer give-ups (2.4% vs 20.2% inconclusive), not from less fixation. Filtering out give-up trajectories before voting added 2.6 to 4.9 points (d13).

**4.11 Pool saturation stop rule.** Count new non-duplicates per batch of samples (dedupe by embedding cosine at 0.8). Stop when a batch adds less than a set share. No tested threshold exists. Si: about 5% survive at 4000 samples. Terwiesch: no plateau to 1,000 (d07). Task and measure decide.

**4.12 Example-copy scorer for the agent.** For an in-context flawed example, list K features of the example (14 in Wadinambiarachchi, a16). Have two scorers (code or blind raters) count shared features in each output. Fixation = shared features / K. Not yet run on LLMs.

## 5. What holds up

**Replication record for human example fixation: mixed and under-documented.**
- Original (Jansson and Smith): not re-read; second-hand reports say copying in four experiments, in professionals too.
- Purcell 1993: weak replication (snippet only, a07/b04).
- Perttula and Liikkanen 2006: no rise in example-feature reuse, no rise in idea count; fewer non-redundant categories (6.00 vs 13.00). N=16. The non-redundant row looks asymmetric (control equals its total), so the metric is odd.
- Chrysikou and Weisberg 2005: fixation present, reduced by an avoid-instruction. N=89 and N=60 (abstract only).
- Wadinambiarachchi 2024: fixation on an example with AI or image help, N=60, BF > 40. Not a clean Jansson-Smith replication: three arms with tool help.
- Neroni 2017: fixation as mental set, clear effects (d=.70 to 1.10, N=36).
- No pre-registered multi-lab replication was found.

**Boundary conditions suggested by the sources.**
- Number of examples: one versus several varied (Perttula; Sio: fewer is better for facilitation).
- Commonness: uncommon examples help most (Sio). Common ideas get reproduced more (b03).
- Domain match: effects strongest when example and designer expertise match (Purcell; snippet).
- Timing: harm appears late; breaks remove it (d05). Up-front vs delayed examples: up-front covered fewer categories (b05, second-hand).
- Ideas per person: the original had about 3 to 4 ideas per subject; Perttula's subjects gave about 9 (b25).
- Measure: copying, categories, novelty and quality disagree. Sio: range narrows, novelty rises. Perttula: total categories flat, non-redundant halved.

**Interventions in humans.**
- Worked: defixation instruction (Chrysikou, abstract); relax or unrelated-task break after exposure (d05); lecture training (Howard, no control, so weak).
- Did not work or unclear: warnings in the original (second-hand); chain-of-thought listing for humans (1.035 vs 1.035, b13); Oblique Strategies vs ChatGPT: no individual difference (b16).
- Strategy cards: no fixation control, exclude (a29).

**Interventions in LLMs.**

| Intervention | Result | Verdict |
|---|---|---|
| Temperature up | Garbled at 1.5-2.0 (Deng footnote); min-p at 2.0 still 61.2% > 0.8 | Not a lever [E] |
| Creative system prompt | No change in population variability (c06) | No [E] |
| Paraphrase, "be unique" system prompt | Marginal (c20, d09) | No |
| CoT list then revise | Slope +0.35 in main set; direction holds in robustness | Yes [E] |
| Persona per session | 0.679 to 0.757 | Yes [S], open ideation only |
| Verbalized sampling | 1.6-2.1x, 66.8% of base | Yes [S] |
| Show-previous regeneration | To human level on 3 models | Yes [E] |
| List in one context vs independent singles | 0.80 vs 0.24 (Claude Opus 4.8) | Yes [E] |
| Iterated "bolder" | 0.575 vs 0.679 | No |
| Human seed idea | No change | No [S] |
| Prior top ideas as seeds | .403 vs .386 | No |
| CoT, reflection, ignore-hint vs numeric anchors | No reduction (c25) | No [S] |
| More reasoning effort | Fewer distinct outputs (o-series), none (Gemini 2.5 Flash) | Not a lever [S]; no Claude test |
| Named defixation methods (TRIZ, SCAMPER) | Simple "think wild" better (d20) | Keep prompts simple [S] |
| Self-Refine on stuck agent | Lowered Claude 53.6% to 44.6% (d14) | No |

**Competing results to keep in view.**
- Deng: LLM within-session fixation equals human. Wadinambiarachchi and Doshi: humans fixate on AI output. Different directions, different units.
- Saturation: Si (plateau near 200) vs Terwiesch (no plateau). Different tasks, measures, prompts.
- Laban 2025 (one long thread degrades) and Brown 2024 (many samples help) agree on fresh samples, but Brown needs a verifier. Snell 2024: with a verifier, sequential revision narrowly wins on MATH. Those test accuracy, not diversity.

**Corrections from the cross-check (critique.md).**
- Wadinambiarachchi coefficients are log-link model coefficients, not proportions. Originality there is the share of other participants without the same idea cluster, so low originality means convergence across people.
- Deng persona+CoT robustly raises combinations; the category slope in the robustness setup was not significant (p=.19).
- Deng CoT slope in robustness is 1.095, not 1.363.
- Only 2 of 10 target numbers (Deng, Wadinambiarachchi) were re-verified by the cross-check. The rest rely on the agents' opened flags.

## 6. Language models

**Where LLMs stand.**
1. *Within one session* GPT-4o accumulates idea categories at the human rate (slope 1.013 vs 1.035, p=.51; 12.46 vs 12.68 categories; 99 vs 99 simulated participants, fitness products; a20, b10). One model, one task, labels from GPT-4o.
2. *Across sessions* the spread is far below human: pairwise distance 1.51 vs 2.41; first-idea categories 8.37 vs 14.51 (a21). AUT population variability .459 vs .738 across 22 LLMs vs 102 humans (c05). Mean originality is comparable, so single-run quality looks fine while the set is narrow.
3. *Within a model* 79% of response pairs exceed 0.8 cosine (c07). Across vendors 71-82% (c09). Frontier models give under 3 distinct answers per 10 samples; larger models are worse (c19).
4. *Post-training causes part of it.* Llama-2 chat forms tight clusters vs base (c15). Verbalized sampling recovers 66.8% of base diversity, and baseline diversity drops after SFT, DPO and RLVR (c16, c18). Feedback-tuned InstructGPT homogenises human co-writers; base GPT-3 does not (c14, b19).
5. *Fresh contexts with an identical prompt are the least diverse arm.* GPT-4o: 0.452 vs 0.679 for one session listing ideas (d06). Claude Opus 4.8: 0.24 vs 0.80, but win rate vs gold fell 0.33 to 0.21 and utility moved 0.34 to 0.38 (d08). Tokens were not matched in either study, and the tasks differ (product ideas; NLP research ideas).

**What changed the behaviour, and by how much.**
- List then revise bolder: slope +0.35 (1.013 to 1.363), combinations 83 to 152 (b13).
- Ordinary persona plus CoT: 248 combinations vs 197 human, +26%.
- Random persona: 0.679 to 0.757; constraint: 0.735 (d07).
- Prompt strategy mixing: little overlap between strategies' first 50 ideas, so mixed pools spread more than repeated ones (b15).
- Show-previous regeneration: to roughly human diversity on Claude 3 Opus, GPT-4o, Gemini 2.0 Pro (c20).
- Verbalized sampling: 1.6 to 2.1x; human raters agreed (poem 1.90 to 2.39; story 2.74 to 3.06; joke 1.83 to 3.01; c17).
- No effect: seeding with a human idea (18.34 vs 18.35), prior top ideas, system-prompt creativity, temperature, more reasoning effort.

**Agent-side evidence (not ideation).**
- Same-mechanism repetition when blocked, on every model tested; a switch rule lifted Claude Sonnet 4.6 by 19.6 points (d14).
- Einstellung probe: earlier models failed badly (d15, d16); Claude 4.1 Opus reached 0.751 vs physicians 0.66 (d17). The trap is now largely avoided on that probe, so mental set may matter less for current Claude-class models than the older literature suggests. Same 100 items, so contamination is possible.
- Long contexts end early with give-up answers (d12). This is a different failure from fixation, but a restart cures it.
- Early commitments in multi-turn chats cost 35-39% (c22).

**Not found.** An in-context flawed-example replication on any LLM. A Jansson-Smith-style test on Claude. A Claude extended-thinking diversity test. A delayed-vs-up-front example test on agents. The share of agent errors due to mental set. An equal-token test of N fresh contexts vs one long context on a Claude-class model for a non-product task.

**Humans with AI (indirect for an agent).** Fixation on AI images +.32 (BF 124); novelty +5.4 to +8.1% but similarity to the AI idea +5.2% (Doshi); group-level homogenisation with unchanged individual diversity (Anderson, d=.67). Lesson for a multi-run agent: sharing outputs among runs may lift weak runs but narrows the pool.

## 7. What our agent should take

Schema key: G guardrail, S state, O operator, M memory. Status: [E] established, [S] single source, [C] contested.

### Add now (established)

1. **S3 change: each fresh context writes a list of ideas, not one idea.** Bare identical single-idea fresh contexts are the least diverse arm. This contradicts the current S3 wording only if "fresh context" is read as "one idea per context". Keep isolation between contexts; change what each context produces. S3. [E]. Evidence: d06, d08, c07, c19, b21.
2. **S3: do not use temperature or a "be creative" system prompt as the diversity lever.** S3/G. [E]. Evidence: b21, c08, c06, a24 footnote, d19.
3. **S3 / O: generate-then-revise as one step inside a context (list titles, one revision pass for bolder and different).** [E] for LLMs (Deng plus Meincke, CoT best of 35). Do not iterate a second time (d07, [S]). Evidence: a23, b12, b13, a25, b14.
4. **S3: in-context "give a different one" with earlier answers visible, for list generation inside a context.** S3/O. [E]. Evidence: c20, d09, d08. Do not show earlier answers without the instruction.
5. **S3/G: judge diversity across runs, not within a run.** Log pairwise distance of first ideas over runs. [E]. Evidence: a21, b16, a28, c05, c14.
6. **G4 / 4b: no persona or strategy voters on single-answer problems.** Already in G4. New support: MMLU 71.6 to 68.0, CSQA -2.1 to -4.4, temperature spread nil. [E]. Evidence: d18, d19.
7. **S1 input hygiene stays; CoT and reflection do not remove anchoring.** G/S1. [E]. Evidence: c25, c21, c22. Remove suggestive cues; do not argue the model out of them.
8. **Verifier plus many samples where a check exists; without a checker, do not expect gains.** S3/S4. [E]. Evidence: c24, d11, d13.

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Persona or constraint per fresh context, open ideation, Claude | S3 | [S] | d07, b12, d22 |
| T2 | Fresh contexts each writing a list of k vs one long list vs N single-idea contexts, equal tokens | S3 | [E] direction; Claude equal-token untested | d06, d08 |
| T3 | Strategy-prefix samples (named approaches) on proofs and code with a checker | S3/G4 | [S] | d21, d18, d19 |
| T4 | Switch trigger: repeated same-mechanism failures pass a threshold, force divergent-then-select | O (switch), S6 | [S] | d14 |
| T5 | Restart with a summary of rejected directions after a context-length trigger | S3/S6 | [S] | d12, c22 |
| T6 | Avoid-X line naming the example's flaw in S1/S3 | S1/G | [C] | a03, d01 |
| T7 | Delayed vs up-front exposure of retrieved analogues or prior attempts | S3, O7 | [C] | b05, d05 |
| T8 | Saturation stop rule (new non-duplicates per batch) vs fixed N | S3 stop | [C] | a26, d10, d07 |
| T9 | Verbalized sampling inside one context vs separate contexts | O | [S] | c16-c18 |
| T10 | Mental-set probe to gate restart operators by model | S0/S6 | [E] that old models fail, new pass | d15-d17 |
| T11 | Cross-context sharing of ideas: help weak runs, narrow the pool? | S3 | [S] | a27, a28 |
| T12 | Drop give-up and low-confidence runs before voting | S7 | [S] | d13 |
| T13 | Forbid iterated "make it bolder" (add to 4b if a second source appears) | 4b | [S] | d07 |

Do not add: AI-image-fixation findings (K16) as agent rules; the lecture result (K06); strategy cards (K24).

## 8. Concrete tests on our bench

All arms get equal total tokens, setup cost counted (G7). Every test logs pairwise first-idea distance (state the embedding model), distinct category count, and best-idea quality by a check, not by the generating model (G8).

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 (T2) | Open ideation: NoveltyBench-type open prompts; BRAINTEASER-style prompts asking for novel solutions | (a) N single-idea fresh contexts; (b) one context lists N; (c) N/3 contexts each listing 3 | Mean pairwise distance; distinct@k; best-of-set quality by check | (b) and (c) beat (a) by 0.3+ distance (Claude Opus 4.8 saw 0.24 vs 0.80); quality loss under 0.1 win rate |
| B2 (T1) | Same items | (a) identical prompt; (b) random ordinary persona per context; (c) random constraint per context; (d) strategy prefix | Pairwise distance; distinct categories | (b),(c) +0.05 to 0.08 over (a) (GPT-4o 0.679 to 0.757); smaller if Claude is already broad |
| B3 (T3) | Items with a checker: ARC puzzles, short proofs, code | (a) plain independent samples; (b) persona per sample; (c) strategy-prefix samples | Pass@k with checker | (b) -2 to -4 points; (c) equal or better than (a) on hard items only |
| B4 (T4) | ARC items where the first mechanism is blocked | (a) plain retries; (b) generic self-critique; (c) switch after 2 same-mechanism failures then divergent-then-select | Solve rate; repeated-mechanism count | (c) +10 to +19 points over (a); (b) no better or worse |
| B5 (T5) | Long multi-step items (over 32K tokens) | (a) one long context; (b) summary-and-restart at fixed length; (c) restart carrying a list of rejected directions | Solve rate; give-up and "unsure" endings; new-category yield after reset | (b),(c) cut premature endings; (c) adds new categories |
| B6 (T6) | Brief plus flawed in-context example (clone Jansson-Smith: rack, cup, coffee cup) | (a) no example; (b) example; (c) example + generic avoid line; (d) example + named-flaw avoid line | Share of K example features reused; flawed features reused; idea quality | (b) copying above (a); (d) copying lower than (b) by 20%+; (c) small |
| B7 (T7) | Same | (a) example up front; (b) example after k own ideas; (c) none | Categories; copying | (b) more categories than (a) |
| B8 (T8) | Open generation | (a) fixed N; (b) stop when a batch adds under 10% new non-duplicates | Best-idea quality per token | (b) saves 30%+ tokens at the same quality |
| B9 (T10) | Misleading-cue plus flexible-override items (Luchins-style, mARC-style) | (a) same context; (b) fresh context on the transfer trial | Share using the costly familiar approach | Probably null for Claude (d17); if null, restart operators earn their cost only at impasse |
| B10 (T11) | Open ideation | (a) isolated contexts; (b) contexts see one peer idea | Pool distance; weak-run quality | (b) lifts weak runs, narrows pool |

## 9. What does not transfer, and why

- **The Jansson-Smith flawed picture example.** A person sees a picture once and cannot un-see it. An agent can be given or denied an example exactly. No in-context LLM replication exists and the human effect size is unread. Do not assume numbers.
- **Human debiasing results** (lecture, 12 teams, no control). Practice effects, no control, and agents do not attend lectures.
- **AI-image fixation** (+.32 log-link). Humans copying generated images in a human-AI loop. The agent meets this only if its own outputs are shown back to it.
- **Incubation by distraction.** Already in 4b (does not replicate). The human incubation benefit (d04, d05) comes from forgetting; a restart is the nearest analogue, but it is untested.
- **"Chain of thought does not help humans."** True for humans (1.035 vs 1.035) and irrelevant to the agent.
- **Persona gains on correctness tasks.** The gains are for open ideation only. On exact-answer tasks the cost is real (MMLU -3.6).
- **Single-run quality comparisons with humans.** Mean originality is comparable (c05), so judging single outputs hides the problem.
- **Verbalized sampling and NoveltyBench numbers.** Authors' own benchmarks; creative writing, not design ideas.
- **Saturation numbers.** Task and prompt specific: NLP research ideas vs student products.
- **Results on small trained or open models** (d21, d19). Claude untested.
- **Context-rot results** (d12). Open models only; the failure is premature stopping, not fixation.

## 10. Open questions

1. What are the exact Jansson-Smith 1991 numbers, and what did the warning condition show? Same for Chrysikou and Weisberg copy counts.
2. What are the Sio 2015 effect sizes and moderator coefficients (number, commonness, timing, domain match)?
3. Do LLMs copy flawed in-context examples? Does an avoid line reduce it, and does naming the flaw matter?
4. Do N fresh contexts beat one long context at equal tokens on a Claude-class model, with and without a verifier, on a non-product task?
5. Does the persona effect hold on Claude and on proofs and code?
6. Does extended thinking change cross-sample diversity on Claude? (NoveltyBench: no help or worse on o-series.)
7. Does delayed example exposure reduce fixation in agents?
8. What share of agent errors in multi-step reasoning is mental set, and does restart-with-summary cut it?
9. What new-non-duplicate rate should stop spawning samples?
10. Does context truncation act like human incubation for fixation?
11. Are embedding distances what a judge or a human would call different ideas? (Best embedding agreed with human coders 59%, a28.)
12. Does Claude's apparent robustness on the Einstellung probe (d17) generalise beyond medical multiple choice?

## 11. Sources

[V] opened; [M] snippet or second-hand only. Full URLs per evidence id are in the url field of evidence_a-d.jsonl.

- [M] Jansson and Smith 1991, Design fixation, Design Studies 12(1):3-11. https://doi.org/10.1016/0142-694X(91)90003-F (a01-a04, b02, c04, d02)
- [V] Chrysikou and Weisberg 2005, Following the wrong footsteps, JEP:LMC 31(5):1134-1148. https://doi.org/10.1037/0278-7393.31.5.1134 (abstract only; a05, d01)
- [M] Purcell and Gero 1996, Design Studies 17(4):363-383. https://doi.org/10.1016/S0142-694X(96)00023-3 (a06)
- [M] Purcell, Williams and Gero 1993, Fixation effects, Environment and Planning B 20. https://doi.org/10.1068/b200333 (a07, b04)
- [M] Vasconcelos and Crilly 2016, Design Studies 42. https://doi.org/10.1016/j.destud.2015.11.001 (a08, abstract)
- [M] Sio, Kotovsky and Cagan 2015, Fixation or inspiration? A meta-analytic review (a09, d03, search summary)
- [V] Neroni, Vasconcelos and Crilly 2017, Studying design fixation with a computer-based task (a10-a13, b06-b09)
- [V] Howard et al. 2013, Applying the neuroscience of creativity to creativity training, Frontiers in Human Neuroscience (a14, a15)
- [V] Wadinambiarachchi, Kelly, Pareek, Zhou and Velloso 2024, Effects of generative AI on design fixation and divergent thinking, arXiv 2403.11164 (a16-a18, c01-c03)
- [V] Chen et al. 2025, Understanding design fixation in generative AI, arXiv 2502.05870 (a19, b23)
- [V] Deng, Brucks and Toubia 2026, Examining and addressing barriers to diversity in LLM-generated ideas, arXiv 2602.20408 (a20-a24, b10-b13, b24)
- [V] Meincke, Mollick and Terwiesch 2024, Prompting diverse ideas (a25, b14, b15)
- [V] Si, Yang and Hashimoto 2024, Can LLMs generate novel research ideas? arXiv 2409.04109 (a26, b22, b26, c11, c12, d10)
- [V] Doshi and Hauser 2024, Generative AI enhances creativity but reduces diversity (a27, b17, b18, c13)
- [V] Anderson, Shah and Kreminski 2024, Homogenization effects of LLMs on human creative ideation (a28, b16, b27)
- [V] Microfluidic design-strategy cards study 2018 (a29)
- [V] Perttula and Liikkanen 2006, Exposure effects in design idea generation (b01-b05, b25)
- [V] Padmakumar and He 2024, Does writing with language models reduce content diversity? ICLR (b19, b20, c14)
- [V] Jiang et al. 2025, Artificial Hivemind (b21, c07-c10)
- [V] Wenger and Kenett 2025, We're different, we're the same (c05, c06)
- [V] Mohammadi 2024, Creativity has left the chat (c15)
- [V] Zhang et al. 2025, Verbalized Sampling (c16-c18)
- [V] NoveltyBench, 2025 (c19, c20, d09)
- [V] Zhao et al. 2021, Calibrate before use (c21)
- [V] Laban et al. 2025, LLMs get lost in multi-turn conversation (c22, c23)
- [V] Brown et al. 2024, Large Language Monkeys (c24)
- [V] Lou and Sun 2024, Anchoring bias in LLMs (c25)
- [V] Bellemare-Pepin et al. 2024, Divergent creativity in humans and LLMs (c26, c27)
- [M] Davis et al., Creative Sketching Partner (c28); Hoggenmueller et al. (c29)
- [V] Sio and Ormerod 2009, Does incubation enhance problem solving? (d04, abstract)
- [V] Exposure to ideas, evaluation apprehension and incubation intervals in collaborative idea generation, 2019 (d05)
- [V] Terwiesch, Meincke, Girotra, Mollick, Nave and Ulrich 2026, AI and its impact on creativity, arXiv 2607.27553 (d06, d07)
- [V] Wadhwa et al. 2026, Training reasoning models for ideas (d08)
- [V] Snell, Lee, Xu and Kumar 2024, Scaling LLM test-time compute (d11)
- [V] Xia, Wang, Huang and Liu 2026, Diagnosing and mitigating context rot, arXiv 2606.29718 (d12, d13)
- [V] MUTATE authors 2026, Beyond one path (d14)
- [V] Alavi Naeini et al. 2023, LLMs are fixated by red herrings (d15)
- [V] Kim et al. 2025, Limitations of LLMs in clinical problem-solving (d16); Shidara et al. 2026, Advances in LLM reasoning (d17)
- [V] Hu, Rostami and Thomason 2026, Expert personas (d18)
- [V] Ferreira et al. 2026, Beyond symmetric agents (d19)
- [V] Carichon et al. 2026, IDEAFix (d20)
- [V] Wu, Goyal and Raghunathan 2025, Mode-conditioning (d21)
- [V] Doudkin, Voelker and von Borries 2025, The Spark Effect (d22, vendor paper)
