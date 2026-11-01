# Combinational creativity: deep document

*Subfield C04.03. Source files in this folder: evidence_a-d.jsonl (ids a01-a28, b01-b28, c01-c28, d01-d16), claims.jsonl (K01-K29), critique.md. Evidence count is not source count: the same 8 papers appear 2 to 4 times. Claims count independent papers.*

## 1. What it is

Combinational creativity is making something new by joining existing ideas that were not joined before. Boden (2004) named it as the first of three kinds, next to exploratory and transformational creativity. It is the easiest kind to model, because it needs only a pool of ideas and a way to pick two or more and join them.

"Joining distant concepts across domains" hides four steps. Each has its own evidence and its own failure.

1. **Source choice.** Find a second idea from another domain that could matter. Humans and models both do this badly when the source is far.
2. **Shared structure.** Find what the two ideas have in common at an abstract level (Gentner's mapped relations, Fauconnier and Turner's generic space).
3. **Blend or map.** Project parts of both into one new thing and let new structure emerge.
4. **Check.** Decide whether the result is valid, novel and useful. Model judges are weak here.

Where it sits in our schema: operator O7, "map an analogue: a distant problem and a typed mapping, checked by code". SCHEMA already says unaided analogy rarely transfers and that distant sources lower the average and raise the spread. The new evidence agrees, and adds one correction: for models the weak steps are 1 and 2 (find the source, find the shared abstraction), not step 3.

Short answer to "does it work for LLMs?": models invent a new combination readily, and ratings of novelty come out high. They do not reliably pick far sources, they converge on the same combinations, and the novelty edge shrinks when the idea is executed. The one open-ended benchmark (KOMBINE) says a valid shared abstraction is found 43.4% of the time, but a blend follows from a valid one 97.1% of the time.

## 2. History and theories in depth

**Association (Mednick 1962).** Creativity is forming associative elements into new combinations that meet requirements. The more remote the elements, the more creative the result. The Remote Associates Test (RAT): 30 items, 40 minutes, find the fourth word linking three words. Mednick reported Spearman-Brown reliability 0.92 and 0.91. Validity is weak: no data that high scorers excel in any field, Worthen and Clark (1971) said it measures language sensitivity, and it is now read as a convergent or insight task (a25, secondary source). Lesson: remoteness alone is not value. Any distance measure needs a validity gate.

**Bisociation (Koestler 1964).** Every creative act joins two frames ("matrices") that habit keeps apart. Covers humour, science and art. Only case histories; no empirical test (a26). Hadamard (1954) and Einstein's "combinatory play" are the same kind of introspective report (a27). Motivation, not evidence.

**Structure-mapping (Gentner 1983; SME by Falkenhainer, Forbus, Gentner 1989).** Analogy transfers relations, not attributes. Systematicity: a predicate inside a connected relational system is more likely to be mapped. Three steps: align, infer, evaluate. Time pressure and high working-memory load push people toward surface matches (a24). Competitor: Tversky's contrast theory, which counts shared attributes. MAC/FAC splits the job into a cheap many-are-called retrieval and a costly few-are-chosen mapping. This split is the right shape for an agent: cheap retrieval in code, costly mapping by the model.

**Conceptual blending (Fauconnier and Turner).** Two input spaces, a generic space of shared structure, a blend with emergent structure built by composition, completion and elaboration. Critics: Gibbs (2000) says it lacks testable hypotheses; Ritchie (2004) says many blends reduce to simpler processes; the theory does not say where the inputs come from (a23). Computational versions: Veale and O'Donoghue 2007, Pereira 2006 (a22). KOMBINE (2025) turned blending into a scored task for the first time.

**Conceptual combination in the lab (Wisniewski 1997; Wilkenfeld and Ward 2001; Mobley, Doares, Mumford 1992; Baughman and Mumford 1995).** Far pairs make more novel combined concepts. Two lab studies found lower quality for far combinations, one found no effect (b03). All seen second-hand through Chan and Schunn (2015); do not quote their sizes (b24, b25). The proposed mechanism: people find alignable conflicts by analogical mapping, reason causally to reconcile them, and think more abstractly about distant pairs (b04). So the useful work is the reconciling inference, not the juxtaposition.

**Field and citation data.** Uzzi et al. (2013, Science): top papers mix mostly conventional prior work with a small tail of atypical combinations. Chan and Schunn (2015): in 4,557 inspirations on OpenIDEO, distance alone had zero effect; only iteration on distant ideas helped. Shi and Evans (2023, Nature Communications) reported that impactful work includes more distant combinations of ideas, methods and concepts. Known only via citation in Schapiro et al.; it seems to pull against Uzzi, so the distance optimum is unsettled (a28).

**Computational models, in order.** SME and ACME (1980s-90s); blending via analogy mapping (2000s); Hope et al. analogy mining by purpose and mechanism (2017, KDD); link prediction on concept graphs (Krenn et al. 2022); LLM pipelines for idea generation (SciMON 2023; Si et al. 2024; Gu et al. 2024/25; Scideator 2024-26; Nova 2024; Chain of Ideas 2024); evolutionary recombination with LLMs as crossover (LMX 2023; AlphaEvolve 2025; ShinkaEvolve 2025); and the first open-ended benchmark (KOMBINE 2025).

## 3. Core findings with exact numbers

Status: **E** established, **S** single-source, **C** contested, **H** human-only, **O** older models only.

| Finding | Numbers | Source (evidence ids) | Status |
|---|---|---|---|
| Top-cited papers combine conventional with a small atypical tail | Top-5% hit rate per 100: high conventionality plus high tail novelty 9.11; conventional only 5.82; novel only 5.33; neither 2.05; background 5. P<0.00001. 17.9M WoS papers. Teams 37.7% more likely than solo authors to insert novel combinations | Uzzi et al. 2013 (d01, a20) | S, H, observational |
| Distance alone has zero effect on shortlisting in field data | 2,341 concepts, 4,557 inspirations, 12 problems. Direct distance: chi2(1)=0.00, p=.92 (456 concepts). Per-problem slopes 6 positive, 6 negative | Chan and Schunn 2015 (b01) | S, H |
| Iteration on distant-sourced ideas helps | Indirect distance (522 concepts): chi2(1)=3.26, p=.07. +0.10 distance = +0.45 log-odds; Pr(shortlist) 0.13 to 0.19. Authors: 2 to 4 iterations seemed enough | Chan and Schunn 2015 (b02) | S, H, marginal |
| Lab work: far combos raise novelty, quality mixed or lower | 2 lab studies lower quality, 1 no effect | via Chan and Schunn (b03, b24, b25) | C, H, second-hand |
| Purpose-and-mechanism retrieval roughly doubles good human ideas | Pr(good) k=2: 0.71 [0.48,0.87] vs TF-IDF 0.28 vs random 0.27. k=3: 0.56 vs 0.16 vs 0.14. 38 workers, 749 ideas, kappa 0.51. B=-1.81 (k=2 vs TF-IDF), -1.94 (k=3) | Hope et al. 2017 (a14, b14, d08) | S, H |
| Learned extractor repeats it | 51% of inspirations useful (at least 2 of 10 raters) vs under 30% best baseline; 62% of boxes vs 39%. Same group | Hope et al. 2022 (d09) | S, not independent |
| Blending is the hardest combination task; the shared abstraction is the bottleneck | Mean over 35 LLMs: association 59.0%, valid analogy 53.4%, valid blend 43.4%. Given a valid generic space, coherent blend 97.1%. Every pair had at least one model find a valid blend | Schapiro et al. 2025 KOMBINE (a05) | S (one benchmark, LLM judges) |
| Humans fail the validity gate more often | Humans valid: association 22.1%, analogy 32.9%, blend 12.8%. Overall 13.7 vs best LLM 55.2. 75 Prolific adults | KOMBINE (a07) | S |
| Far association predicts analogy and blend skill across models | Association vs analogy originality r=0.73; analogy surprise r=0.63; blend originality 0.42; valid blends 0.48 | KOMBINE (a08) | S, correlational |
| Different LLMs invent the same concepts | 412 of 2,070 concepts (19.9%) share 2 or more properties with another model's. Same-family excess: DeepSeek +12.2 pp, Anthropic +11.1, xAI +7.4, Meta +4.2, Qwen +2.6, Z.ai +1.2, Google +0.4, OpenAI -1.4 | KOMBINE (a06) | S |
| Outputs converge across and within models | Pairwise similarity above 0.8 for one prompt (vs 0.1-0.2 random); 79% still above 0.8 at temperature 2.0, min-p 0.1; cross-model 71-82%; 22 LLMs more alike than humans | Jiang et al. 2025; Wenger and Kenett 2025 (c07, c06) | E |
| LLM ideas rated more novel than expert ideas, before execution | Novelty human 4.84 (n=119 reviews) vs AI 5.64 (n=109, p<.01) vs AI plus human rerank 5.81 (p<.001). Feasibility 6.61/6.34/6.44 n.s.; overall 4.68 vs 4.85 n.s. vs 5.34 (p=.04). 49 ideas per condition, 79 reviewers | Si et al. 2024 (a10, b07, c03) | S |
| The novelty edge disappears on execution | Change after execution, human vs AI: novelty -0.010 vs -1.049; excitement 0.078 vs -1.760; effectiveness -0.052 vs -1.879; overall -0.628 vs -1.976. 43 experts, 100+ hours each, 58 reviewers. After execution the novelty means were 4.903 vs 4.729 (n.s.) | Si et al. 2025 (a12, c05, d14) | S |
| Mass generation hits a duplicate wall | 4,000 seed ideas gave about 200 non-duplicates (cosine above 0.8); appending earlier titles did not fix it | Si et al. 2024 (a11, b08, c04) | S |
| LLM judges of ideas are near chance | Best judge 71.4% pairwise (Claude-3.5-Sonnet), GPT-4o 61.1, Claude-3-Opus 63.5; human agreement 56.1%. Research-contribution LLM-human r=0.159 (best 0.234) | Si 2024; arXiv 2508.05470 (b09, b21) | E |
| Webb: GPT-3 matched students on text analogies | Digit matrices OR 1.88 [1.21,2.91] p=.005 (humans N=40); letter strings OR 1.76 p=6.3e-5 (N=57); stories humans better, OR 0.37, p=.0003 (N=54) | Webb, Holyoak, Lu 2023 (a15, c10) | C, O |
| Counterfactual alphabets break it | Accuracy: humans 0.753, GPT-3 0.488, GPT-3.5 0.350, GPT-4 0.452. GPT-3.5 by number of generalisations 0 to 3: 0.488, 0.358, 0.317, 0.160. Alternate-rule share of errors 5.81% GPT-3, 22% GPT-4, 38.59% humans (critique attributes 38.59% to GPT-3.5; sources disagree, see section 10) | Lewis and Mitchell 2024 (a16, d02, d03) | C, O |
| Synthetic alphabet collapse | GPT-3 accuracy below 0.1 on extend-sequence, successor/predecessor, fix-alphabet | Hodel and West 2023 (c13) | C, O |
| Story-analogy answers depend on answer order | GPT-4, 18 story problems: 89% (16/18) when story A correct, 61% (11/18) when B correct | Lewis and Mitchell 2024b (d03) | S, O |
| Far narrative analogy is below chance | Binary choice, chance 50%. Models overall 57% vs humans 96%. Near: 75.0% vs 97.9%. Far: 39.6% vs 94.1%. GPT-4 below random on far | ARN, Sourati et al. 2024 (d04) | S, O |
| Retrieving the analogue is the weak step | Accuracy at 1/10/30 sentences: GPT-4 89.1/66.5/60.7, human 96.0/72.5/73.3. Gap 6.9 to 28.8 points. GPT-3.5 65.3/46.4/30.8; Claude 68.2/30.2/25.9; chance 25%. Full bank: near random | AnaloBench 2024 (b16, c14) | E (with ARN), O |
| Self-generated near analogues help a little | GSM8K GPT-3.5 77.8 vs 5-shot CoT 76.7 vs 0-shot 75.8; MATH 37.3 vs 34.9 vs 33.9; Codeforces GPT-4 Acc@1 19% vs 16%, Acc@10 37% vs 30% | Yasunaga et al. 2024 (b17, c09) | S, near only |
| Users skip far facets | Near and input facets chosen far more than far ones; main reason low perceived relevance. CSI median 70.5 vs 61.0 (p<.01), N=22 | Scideator (b10, b11, c19) | S, self-report |
| Facet decomposition improves prior-art detection | Overlap retrieval 89.66% vs 13.79, 10.34, 8.62, 5.17 for weaker variants; 43 held-out ideas | Scideator (b12) | S |
| Retrieve-and-iterate raises novelty | SciMON: first iteration raised novelty in 55.6% of ideas, second in 57.8%; real paper idea still better in 85% of comparisons. Nova: 3.4x unique novel ideas, gains stop after about 3 rounds | SciMON; Nova (a13, b13, d06) | S, LLM or small human judges |
| Recombination from an archive beats fresh sampling at equal compute, when execution scores it | AlphaEvolve "no evolution" ablation worse; ShinkaEvolve rejection of near-duplicates (embedding similarity above 0.95) beats no filter; LMX more parents give more diverse offspring | d10, d11, d12 | E, in-task sources only |
| Medium distance can do as well as farthest | 26 novice teams, 136 ideas. Selection: biological 45.5%, cross-domain 29.4%, within 25%. Novelty bio vs within p=0.012; bio vs cross p=0.088 | Keshwani and Casakin 2024 (b18) | S, H |
| Gu et al.: multi-level retrieval beats no retrieval on similarity | SPECTER cosine 0.85 vs 0.78 (design rationale), 0.83 vs 0.75, 0.87 vs 0.77; 87 papers; Claude-3.5-Sonnet. No ablation, no judge, no variance | Gu et al. 2024/25 (a02, c01, d16) | S, weak |
| Word-level far association is easy | GPT-4 above human mean on DAT; GPT-4 at temperature 1.5 scored 85.6, above 72% of humans; top human decile wins; "microscope" in 70% of GPT-4 sets | Bellemare-Pepin et al. (a18, b22, c08) | E, weak proxy |
| Chatbots beat humans on AUT mean, not on max with time and instruction | Original humans n=256 vs AI N=33; replication humans n=50, AI N=93; no significant difference on maximum score in the modified task | Koch et al. 2025 (b23) | S |
| Few-shot examples pull LLM designs toward the crowd | Qualitative; numbers not extracted | Ma et al. 2023 (c20) | S |
| Chain organisation of sources helps in an LLM-judged ablation | Without chain: average 42.4 (50 = tie); without trend 46.2; without entities 45.4 | Chain of Ideas (d13) | S, LLM judge |

## 4. Mechanisms and models

Written so an engineer can build each piece.

### 4.1 Two-stage retrieval then mapping (MAC/FAC)

- **Stage 1, many are called (cheap, code).** Index each stored problem or solution by a short typed record: purpose (what it is for), mechanism (how it works), universal principle (domain-free wording). Retrieve by embedding of the purpose or principle field, not the surface text. Hope et al. 2017 used purpose and mechanism vectors learned from 8,500 products. Gu et al. stored problem structure, design rationale, universal principle and key mechanism, with levels L1 (domain-specific) to L4 (universal), and retrieved per level with text-embedding-3-large, keeping one top item per level after a similarity filter.
- **Stage 2, few are chosen (costly, model).** For each shortlisted source the model writes a typed mapping: object to object, relation to relation, plus a list of conflicts (things that do not map). Chan and Schunn's mechanism says the value comes from reconciling alignable conflicts, so require the conflict list and a repair for each.
- **Retrieval rule worth copying (Hope et al.).** Same purpose, different mechanism. Gave 0.71 vs 0.28 good-idea share in humans. Note that random (0.14) sat close to surface similarity (0.16) at k=3, so surface match gave no advantage over chance.

### 4.2 Abstraction-first (the KOMBINE bottleneck)

1. Given inputs A and B, the model lists candidate shared properties (the generic space).
2. Code checks each: is it stated as a relation (not a shared surface word)? Does it hold in both inputs under a restatement test?
3. Only a verified generic space goes to the blend step. KOMBINE: 43.4% find rate, then 97.1% blend rate. So spend tokens on step 1.
4. Blend checklist (Xi et al. 2026 poster, b19; no data): both frames present, roles preserved, an emergent element present in neither input, coherence.

### 4.3 Bounded far insert (Uzzi)

Build the candidate from a mostly conventional base (near sources, known structure) and add one atypical element. All-far is no better than background (5.33 vs 5), while base plus a small atypical tail gives 9.11.

### 4.4 Iterate the far combination

Chan and Schunn: a far combination is raw material. Build on it 2 to 4 times, each time with a critique of the real failing part. SciMON and Nova show retrieve-iterate loops raise rated novelty and saturate near 3 rounds. Neither is at equal tokens and both use LLM or small human judges.

### 4.5 Evolutionary recombination with an execution check

LMX: put several parent programs in a prompt, ask for a new one, validate by parsing and by fitness. More parents give more diverse offspring. AlphaEvolve: keep an archive of scored programs, sample parents and inspirations, mutate, score with an automatic evaluator; feeding the same program repeatedly ("no evolution") is worse. ShinkaEvolve: reject offspring whose code embedding similarity to an existing one is above 0.95; weighted parent selection beats best-of-N and hill climbing; default 2 inspirations. This is the only family where validity is checked by running, which fits G8.

### 4.6 Diversity control

- Seed conditioning (Nagarajan et al. 2025, a09): randomness at the input matched or beat temperature for diversity (toy tasks, small fine-tuned model). In an agent: code draws the source domain at random and puts it in the prompt.
- Embedding dedup in code (Si: cosine above 0.8 on all-MiniLM-L6-v2; Shinka: 0.95 on code embeddings).
- Fresh context per candidate (already in S3).
- KOMBINE scoring recipe (a04): validity gate first (0/1), then surprise as semantic distance, then originality as mean embedding distance to the 5 nearest answers other responders gave for the same item.

### 4.7 Link prediction framing

Krenn et al. 2022: concept graph from papers; predict which pairs will be joined later. Hand-built network features beat learned features; popular concepts gain edges over time, so popularity bias dominates. Sourati and Evans 2023: adding who researches what raises discovery prediction by up to 400%, and the model can be steered to propose "alien" hypotheses the crowd would not try. For an agent: keep a counted list of pairs already tried and avoid them (a19).

## 5. What holds up

**Holds up (two or more sources, or a clean design).**
- LLM output converges across samples and across models (Jiang, Wenger and Kenett, KOMBINE: three papers, different measures).
- Model judges are unreliable for idea quality (Si, 2508.05470, Vibe Spaces: LLM judge top-1 agreement with humans 35.7% vs chance 25 in one visual test).
- Finding the analogue is the hard step (AnaloBench and ARN: near-random on long or far items).
- Execution-scored recombination beats fresh sampling at equal compute (AlphaEvolve, ShinkaEvolve, LMX).
- Word-level distance (DAT) is easy and is not value.

**Replications and failures.**
- Webb et al. (GPT-3 analogy) was contested within months. Hodel and West (2023) and Lewis and Mitchell (2024, two papers) found sharp drops on counterfactual or permuted items while humans held. Comprehension checks showed the models read the new alphabets. Contested, not refuted: only letter-string, digit-matrix and story families on GPT-3, 3.5 and 4 were re-tested. No Claude-class or reasoning-model test was found (d15).
- Koch et al. (2025) partly replicated chatbot-beats-humans on the Alternate Uses Task, but the human deficit vanished on maximum scores with instruction and time.
- Hope et al. 2017: no independent replication. The authors warn a replication may show a smaller effect.
- Gu et al.: no replication found, no matched-reference baseline, no ablation (d16).
- Uzzi 2013: original numbers read (d01); no replication on newer data found.

**Boundary conditions.**
- Distance alone: zero effect (field, chi2=0.00); novelty up and quality mixed (lab).
- Iteration is the moderator (Chan and Schunn), marginal at p=.07.
- Time and load push humans to surface matching; instruction and time close human-AI gaps on creativity maxima (Koch).
- Models are sensitive to prompt format and answer order (best GPT-4 prompt was Hodel and West's format; story answer position 89% vs 61%).
- Task type: association easiest, blending hardest for models (59.0 / 53.4 / 43.4).

**Interventions that worked.**
- Purpose-mechanism retrieval (humans).
- Facet split plus recombination for researchers' self-reported support (Scideator).
- Retrieve-compare-update loop: novelty raised in 55.6% then 57.8% of ideas (SciMON).
- Planned iterative retrieval, 3.4x unique novel ideas, saturating near 3 rounds (Nova).
- Self-generated near analogues: +1 to +3 points on math, +3 points Acc@1 on Codeforces with GPT-4.
- Etymology strategy prompt raises DAT for GPT-3.5 and GPT-4; higher temperature raises DAT.
- Embedding near-duplicate filter at equal proposals (Shinka).
- Seed conditioning (Nagarajan, toy tasks).
- Chain-ordered sources over flat dumps (LLM-judged only).

**Interventions that did not work, or backfired.**
- Mass generation: 4,000 ideas, about 200 distinct.
- Giving earlier titles to avoid: still plateaued.
- Few-shot examples: pulled design ideas toward the crowd.
- LLM self-evaluation of ideas.
- Scale on long-story analogue retrieval: little help.
- Offering far facets: users ignored them.

## 6. Language models

**Behavior by step.**

| Step | What models do | Size | Evidence |
|---|---|---|---|
| Name far words | Beat human mean | GPT-4 DAT above human mean; top human decile still wins | a18, c08 |
| Find the analogue in a bank | Weak, near random for long stories | Gap to human 6.9 to 28.8 points; full-bank retrieval near random | b16, c14 |
| Detect far narrative analogy | Below chance | 39.6% vs 94.1% human | d04 |
| Map with unfamiliar structure | Brittle | 0.35 to 0.49 vs human 0.753 on counterfactual letters | a16, d02 |
| Find shared abstraction (generic space) | About half the time | 43.4% | a05 |
| Build blend given the abstraction | Almost always | 97.1% | a05 |
| Rate own idea quality | Unreliable | Best judge 71.4% vs 56.1% human agreement; r=0.159 | b09, b21 |
| Produce ideas judged novel before execution | Better than experts | 5.64 vs 4.84 | a10 |
| Survive execution | Lose the novelty edge | -1.049 vs -0.010 | a12 |
| Diverge from other models | Do not | 19.9% shared concepts; similarity above 0.8 | a06, c07 |

**What changed behavior, and by how much.**
- Paper retrieval into the prompt plus mass generation and ranking: novelty 4.84 to 5.64 (human rerank 5.81). Overall n.s. unless humans rerank (5.34, p=.04).
- Multi-level abstraction retrieval with decomposition: similarity to target 0.78 to 0.85 (design rationale). Confounded: the framework gets the true references.
- Planned iterative retrieval: 3.4x unique novel ideas, gains stop near 3 rounds.
- Self-generated exemplars: +1 to +3 points on math with GPT-3.5; larger on weaker models (text-davinci-003 GSM8K 61.0 vs 54.0).
- Higher temperature: DAT up, but repeated words persist.
- Execution scoring plus archive: better than resampling at equal compute (in-task sources).
- Model size: a bigger LLM gives more valid offspring in LMX (about 30% valid with the 6B model on Sodarace).
- Multi-token training objective (toy tasks, Gemma 2B): about 5x algorithmic creativity (a09). A training result, not a prompting one.
- Model age: GPT-4 beats GPT-3 and 3.5 on near analogies (ARN near: GPT-4 close to human) but not on far ones. GPT-4-turbo was worse than GPT-4 on DAT. Newer is not always better.

**Gaps.** Most analogy and counterfactual tests used GPT-3 to GPT-4 (2022-2024). KOMBINE (2025) covers newer models but uses LLM judges and one run per item. No clean far-versus-near test at equal tokens for any LLM was found.

## 7. What our agent should take

Tags: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, M memory.

### Add now (established)

1. **Never accept a combination on a model's own novelty rating.** G8 already says it; strengthen with numbers: best judge 71.4%, LLM-human r=0.159, novelty edge -1.049 after execution. [E] a11, b09, b21 (three sources on judges); execution gap a12 is single-source. Schema: G8, S7.
2. **Check a mapping on a variant before trusting it.** Run the mapping on a permuted, renamed or order-swapped twin; require the same answer. [E for brittleness] a16, d02, d03, c13, d04: three independent groups, older models only. Schema: G3 applied to O7, S4.
3. **Dedup candidates in code before selection.** Cosine above 0.8 on sentence embeddings for ideas; above 0.95 for code. [E] a11, d12, c07. Schema: S4 harvest, S7.
4. **Score a recombination by execution or a held-out check whenever one exists.** Archive recombination with an executable scorer beats resampling at equal compute. [E] d10, d11, d12. Schema: O7 plus S4. Only for classes with a check.
5. **Do not use word distance (DAT or RAT) as a pass signal for O7.** [E] a18, a25, b22. Schema: G8.
6. **Keep O7 wording: far sources are raw material, used at impasses and in open mode.** Matches b01 (zero direct effect) and b03 (lab line second-hand). [E] that distance alone does not help. Schema: O7, no change.
7. **Convergence is real; do not count agreement between models as validation of a novel combination.** [E] c06, c07, a06. Schema: G4 (already present).

### Test first (single-source or contested)

1. **Abstraction-first before blending.** [S] a05. Schema: O7, S2. Test U1.
2. **Far vs near vs none sources at equal tokens, executable score.** [no evidence] critique gap 1. Schema: O7. Test U2.
3. **Bounded far insert (mostly near plus one far).** [S] d01. Schema: O7. Test U3.
4. **Iterate the far combination 2 to 4 times.** [S] b02, d06, a13. Schema: S5 on O7 children. Test U4.
5. **Typed purpose/mechanism index for memory.** [S] a14, d08, d09. Schema: M subgoal library. Test U5.
6. **Code-drawn source per branch for diversity.** [S] a09. Schema: S3, O7. Test U6.
7. **Variant-consistency guard as a standard step.** [C] a16, d02, d03 (contested whether the original ability exists at all). Schema: G3, O7. Test U7.
8. **Conflict list plus repair in the mapping.** [S] b04, cited theory. Schema: O7. Test U8.
9. **Facet decomposition for novelty check.** [S] b12. Schema: S7 open mode. Test U9.
10. **Self-recall of related solved problems.** [S] b17, c09. Schema: O7 near variant, M. Test U10.
11. **Medium distance first, far only at impasses.** [S] b18, novices. Schema: O7. Covered by U2 and U3.
12. **Counted list of combinations already tried.** [S] a19. Schema: M. Test U11.

Full list with thresholds: UNKNOWNS.md.

## 8. Concrete tests on our bench

All arms use equal total tokens (setup, retrieval and iteration counted, G7). At least 3 seeds per arm; pair by item.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Abstraction-first | Pairs needing a valid blend; puzzle items where a principle from another field applies | A direct; B extract generic space, code-check, then combine; C direct with samples matched to B's tokens | Valid-blend rate by fixed rubric plus blind check; on puzzles pass@1 of an executable check | B above A by 10 or more points; B above C (the real test) 0 to 8 points |
| T2 Far/near/none | Coding or ARC-like items with unit tests, where a named other-domain source can be supplied | A none; B near; C far; D random | Pass rate; held-out pass rate | Far no better than near on pass rate (zero direct effect); gain on diversity and at impasses |
| T3 Bounded insert | Same items as T2 | A all-near; B all-far; C near base plus one far element | Pass rate; distinct passing solutions | C above A and B by 2 to 5 points |
| T4 Iteration depth | Same items, a far source in every arm | 1, 2, 3, 4 rounds with the failing output shown | Pass rate per token | Gain from 1 to 3, flat after 3 |
| T5 Typed memory index | Subgoal library; new problems sharing mechanism but not wording | A full-text embedding; B purpose plus mechanism fields; C none | Top-3 retrieval hit; downstream pass rate | B above A by 10 or more points on hit rate |
| T6 Source forcing | Open-mode generation, 8 candidates per item | A temperature only; B code-drawn source domain per branch; C B plus dedup | Unique ideas per 1,000 tokens (cosine 0.8); best-of-8 pass under a check | B and C raise unique yield; pass rate flat or small change |
| T7 Variant guard | Mapping items with permuted and renamed twins | A trust first mapping; B accept only if the twin answer is consistent | Wrong-mapping acceptance rate; final accuracy | B cuts wrong acceptances sharply for one extra call |
| T8 Conflict list | Cross-domain design items scored by execution or hidden-reference rubric | A map; B map plus conflict list and repair | Pass rate; rubric score | B above A by a few points |
| T9 Self-recall | Reasoning items with exact answers | A plain CoT; B recall 2 related solved problems then solve | Accuracy | +1 to +3 points on a mid-strength backbone; about 0 on strong ones |
| T10 Tried-pair list | Repeated open-mode runs on one class | A none; B counted list shown after the first attempt | Distinct pairs per run; pass rate | More distinct pairs; pass rate flat |

## 9. What does not transfer, and why

- **Citation-based hits (Uzzi, Shi and Evans) to a single-run agent.** Citations measure reception over years. A run needs a check now. Use the pattern (conventional base plus one atypical part), not the numbers.
- **OpenIDEO chi2=0.00.** Human contributors filter what they post; distance was coded by text similarity (r=0.39 to 0.48 with human coding). An agent that posts every candidate faces different selection.
- **Purpose-mechanism gains in crowd workers.** Graders were grad students (kappa 0.51), corpus was consumer products, baselines were weak. A model with a code check does not need a human "good idea" rating.
- **Human execution as a validity test (Si 2025).** 100+ hours per idea. Not an agent-loop tool. A unit test or held-out example is a stand-in, not the same measure.
- **KOMBINE scores.** LLM judges, pool-relative originality, one run per item. Use as a scoring recipe, not as truth.
- **Gu et al. similarity.** SPECTER similarity to the real paper rewards re-deriving known work, and the framework got the true references. It supports "right ingredients plus decompose and recombine recovers an idea", not "far retrieval adds value".
- **Facet-use data (Scideator).** Humans ignore far facets because they look irrelevant. An agent can be forced; what to log is whether it used them.
- **DAT and RAT.** Single words, no validity.
- **Multi-token training (Nagarajan).** A training change on toy tasks. Only the seed-conditioning idea transfers.
- **Evolution loops (AlphaEvolve).** Need an automatic evaluator and hundreds of evaluations. Only the archive-plus-check pattern transfers.
- **Link prediction on concept graphs.** Predicts what will be combined (popular pairs), not what is valuable.

## 10. Open questions

1. At equal tokens, do far-domain sources beat near-domain or none when scored by execution? (No study.)
2. Does abstraction-first beat simply sampling more? (No study.)
3. Which abstraction level L1 to L4 is best; is there an inverted U? Gu et al. never ablate the levels.
4. Does a matched-baseline replication of Gu et al. keep the 0.85 vs 0.78 gap?
5. How large is the Hope et al. effect under independent replication, and does an LLM-built purpose/mechanism index reproduce it?
6. Does the Chan and Schunn iteration effect hold for LLM agents, and at how many rounds?
7. Does Uzzi's pattern replicate on newer data, and how does it square with Shi and Evans (2023)? The Shi and Evans primary was not opened.
8. How to measure validity of an open idea cheaply without an LLM judge? Execution works for code; nothing equivalent for open ideas.
9. Do Webb-style results survive counterfactual items on Claude-class and reasoning models?
10. Does source forcing raise diversity at equal tokens without lowering validity?
11. Is the far-association probe (r=0.73 to analogy originality across 35 models) usable to predict O7 skill on one backbone?
12. KOMBINE found homogeneity strongest within model families (DeepSeek +12.2 pp, Anthropic +11.1) and absent for OpenAI (-1.4). Matters if we mix backbones.
13. Data discrepancy: the alternate-rule error share of 38.59% is attributed to GPT-3.5 in one evidence line (c12) and to humans in another (d02), with GPT-3 5.81% and GPT-4 22%. Re-check in Lewis and Mitchell before quoting.

## 11. Sources

[V] opened and read this series; [M] snippet or second-hand only.

- [V] Gu, Wang, Zhang, Li (2025) LLMs can realize combinatorial creativity. https://arxiv.org/abs/2412.14141
- [V] Schapiro et al. (2025) Measuring combinatorial creativity in LLMs and humans (KOMBINE). https://arxiv.org/abs/2509.21043
- [V] Si, Yang, Hashimoto (2024) Can LLMs generate novel research ideas? https://arxiv.org/abs/2409.04109
- [V] Si, Hashimoto, Yang (2025) The ideation-execution gap. https://arxiv.org/abs/2506.20803
- [V] Wang, Downey, Ji, Hope (2023/24) SciMON. https://arxiv.org/abs/2305.14259
- [V] Hope, Chan, Kittur, Shahaf (2017) Accelerating innovation through analogy mining. https://arxiv.org/abs/1706.05585
- [V] Hope et al. (2022) Scaling creative inspiration with fine-grained functional aspects of ideas. https://arxiv.org/abs/2102.09761
- [V] Webb, Holyoak, Lu (2023) Emergent analogical reasoning in LLMs. https://arxiv.org/abs/2212.09196
- [V] Lewis and Mitchell (2024) Counterfactual tasks for analogical reasoning. https://arxiv.org/abs/2402.08955
- [V] Lewis and Mitchell (2024) Robustness of analogical reasoning in LLMs. https://arxiv.org/abs/2411.14215
- [V] Hodel and West (2023) Response: Emergent analogical reasoning in LLMs. https://arxiv.org/abs/2308.16118
- [V] Choi et al. (2024) AnaloBench. https://arxiv.org/abs/2402.12370
- [V] Sourati et al. (2024) ARN: Analogical reasoning on narratives. https://arxiv.org/abs/2310.00996
- [V] Stevenson et al. (2023) Do LLMs solve verbal analogies like children do? https://arxiv.org/abs/2310.20384
- [V] Yasunaga et al. (2024) LLMs as analogical reasoners. https://arxiv.org/abs/2310.01714
- [V, abstract and intro only] Yuan et al. (2023) AnalogyKB. https://arxiv.org/abs/2305.05994
- [V] Chan and Schunn (2015) The importance of iteration in creative conceptual combination. https://joelchan.github.io/files/2015-cognition-openideo-diversity-manuscript.pdf
- [V] Uzzi, Mukherjee, Stringer, Jones (2013) Atypical combinations and scientific impact. https://www.kellogg.northwestern.edu/faculty/uzzi/htm/papers/Science-2013-Uzzi-468-72.pdf
- [V] Radensky et al. (2024-26) Scideator. https://arxiv.org/abs/2409.14634
- [V] Keshwani and Casakin (2024) Bio-inspiration and engineering-domain inspiration. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11201427/
- [V] Bellemare-Pepin et al. (2024/26) Divergent creativity in humans and LLMs. https://arxiv.org/abs/2405.13012 ; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12824279/
- [V] Koch et al. (2025) Time-on-task and instructions help humans keep up with AI. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12181282/
- [V] Wenger and Kenett (2025) We're different, we're the same. https://arxiv.org/abs/2501.19361
- [V] Jiang et al. (2025) Artificial Hivemind. https://arxiv.org/abs/2510.22954
- [V] Nagarajan et al. (2025) Roll the dice and look before you leap. https://arxiv.org/abs/2504.15266
- [V] Sourati and Evans (2023) Accelerating science with human-aware AI. https://arxiv.org/abs/2306.01495
- [V] Krenn et al. (2022) Predicting the future of AI with AI. https://arxiv.org/abs/2210.00881
- [V] Li et al. (2024) Chain of Ideas. https://arxiv.org/abs/2410.13185
- [V] Hu et al. (2024) Nova. https://arxiv.org/abs/2410.14255
- [V] Kumar et al. (2024) Can LLMs unlock novel scientific research ideas? https://arxiv.org/abs/2409.06185
- [V] Ma et al. (2023) Conceptual design generation using LLMs. https://arxiv.org/abs/2306.01779
- [V] Meyerson, Lehman et al. (2023) Language model crossover. https://arxiv.org/abs/2302.12170
- [V] Novikov et al. (2025) AlphaEvolve. https://arxiv.org/abs/2506.13131
- [V] Lange et al. (2025) ShinkaEvolve. https://arxiv.org/abs/2509.19349
- [V] Rethinking creativity evaluation (2025). https://arxiv.org/abs/2508.05470
- [V] Yang et al. (2025) Vibe Spaces. https://arxiv.org/abs/2512.14884
- [V] Xi, Cheng, Soni, Turner (2026) Evaluating creative generative AI with conceptual blending (poster, no data). https://markturner.org/ACL2026_Conceptual_Blending_Poster_compressed.pdf
- [V, secondary] Wikipedia: Computational creativity, Conceptual blending, Structure-mapping theory, Remote Associates Test, Bisociation. https://en.wikipedia.org/wiki/Computational_creativity (sibling pages)
- [M] Shi and Evans (2023) Surprising combinations of research contents and contexts, Nature Communications (via Schapiro et al.).
- [M] Baughman and Mumford (1995); Mobley, Doares, Mumford (1992); Wilkenfeld and Ward (2001) (via Chan and Schunn 2015).
- [M] Koivisto and Grassini (2023) (via Koch et al. 2025).
- [M] Gentner et al. story-analogy materials (via Webb et al.).
- [M] Boden (2004); Mednick (1962); Koestler (1964); Hadamard (1954); Gentner (1983); Fauconnier and Turner (2002); Gibbs (2000); Ritchie (2004) (secondary pages and citations only).
