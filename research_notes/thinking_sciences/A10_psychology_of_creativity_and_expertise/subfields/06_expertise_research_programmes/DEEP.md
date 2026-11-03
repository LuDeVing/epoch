# Expertise research programmes: deep document

*Subfield A10.06. Based on evidence_a-d.jsonl (ids a01-a28, b01-b27, c01-c25, d01-d16), claims.jsonl (A10.06-K01 to K24) and critique.md in this folder. Evidence ids are cited in brackets. [V] = full text or page opened, [M] = abstract or snippet only.*

## 1. What it is

"Expertise research programmes" is the label Campitelli, Connors, Bilalic and Hambrick (2015) used for the main strands of modern expertise research in their editorial for a 35-article Frontiers collection [a01, b17]. They sort the field into five programmes:

1. Cognitive processes of experts (memory, perception, eye movements, problem solving).
2. Development of expertise (practice, learning curves, talent).
3. Expertise and general cognition (does expertise go with general ability, and does it change it?).
4. Transfer of skills between domains.
5. Methods and frameworks.

Domains in the collection: chess, music, perception, teaching, ICU diagnosis, video games, sports, dance, maths, climbing, fingerprints [a01].

This document concentrates on the strands that matter most for our agent: the cognitive-process strand (chunks, templates, expert eye movements) and the transfer strand (training in one area rarely helps another). The editorial's headline for us is a warning: transfer of skill across domains is often absent. Video-game expertise showed no transfer to selective attention or working memory. Teaching experience was a very poor predictor of teacher effectiveness. Perceptual expertise with cars interfered with face processing. Dance and climbing expertise were domain-bound [a04, b17].

Why it matters. We are building one language-model agent that thinks well through a scaffold (a thinking schema), not by training. Three questions follow from this field:

- If the scaffold is tuned on some problem types, will it help on others? Human history says be suspicious [K01, K12].
- Does an "expert" framing or an expert-style template give skill? Human history says skill is stored knowledge in narrow chunks, not a general mode [K06, K09].
- What can we copy from expert cognition that is cheap and domain-light, such as fast triage of relevant parts? [K07]

Related subfields run in parallel (not covered here): Expertise as chunking, Computational chunk models, Expert flexibility and adaptive expertise, Surface-cue heuristics, Program comprehension, Working-memory limits and chunking.

## 2. History and theories in depth

### 2.1 Common elements and the old transfer debate

Thorndike and Woodworth's common-elements theory predicts that transfer is common between similar tasks and rare between dissimilar ones [a06]. A century later the same pattern shows in meta-analyses: near transfer exists, far transfer does not [a08, b05].

### 2.2 Chunking and template theory (cognitive-process programme)

Chase and Simon (1973) showed that chess masters recall real game positions far better than random ones, and explained it by chunks: familiar piece groups held in long-term memory. Gobet and Simon (1998) ran a computerised replication with 26 players [a15, V]:

- Masters (n=5, mean Elo 2453), Experts (n=9, 2148), Class A (n=12, 1869).
- Recall of game positions: 92.0%, 57.1%, 32.2%.
- Recall of random positions: 19.0%, 13.8%, 12.4%.
- Skill x position type interaction: F(2,23) = 34.17.
- The 2-second inter-piece interval still marks chunk boundaries, so chunks are real.
- Masters used far larger chunks than reported in 1973. This led to template theory [a15, a16].

The famous "50,000 chunks" figure is an extrapolation from the MAPP simulation (Simon and Gilmartin 1973; range 10,000 to 100,000). Holding argued that about 2,500 might do if chunks coded relations, not locations [a16]. In the 1973 data the first chunk replaced had 3.8 pieces for a Master, 2.6 for Class A, 2.4 for a beginner; median largest Master chunk 5. In the new data the Master vs Class A difference in chunk number in recall is under one chunk [a16].

Template theory (CHREST lineage) adds slots to frequently met chunks, so new information can be written to long-term memory in seconds (normal chunk learning is 5 to 10 s). Slots hold piece locations and pointers to plans, moves and other templates [a17].

Counter-evidence. Holding and Reynolds (1982), via Gobet and Simon: skill (Elo 1000 to 2200) did not correlate with recall of briefly shown random positions, yet it did correlate with finding the best move in them. Gobet and Simon explain this by pattern recognition applied recursively during look-ahead [a18]. So the chunk story is not a pure memory story. Skill also shows in search.

### 2.3 Expert perception and eye movements

- Sheridan and Reingold (2014) [a19, V]: 41 players; experts (n=17) chose the best move on 93% of trials (SE 2) vs 52% (SE 5) for novices, t(39) = 7.12. Move quality 9.5 vs 6.9 out of 10. Reaction time 28.9 s vs 41.9 s. Experts fixate relevant board regions earlier. The advantage is in the first dwell and first five fixations, not total time: fast detection, not more looking.
- Earlier work: experts (mean Elo 2238) put more fixations on best-move pieces than intermediates (Elo 1786) within the first five fixations. Radiologists detect abnormalities in X-rays shown for 200 ms [a20].
- Reingold et al. (2001): chess experts have a larger visual span than weaker players, but only for meaningful positions, not random ones [b16].
- Sheridan and Reingold (2017) review [b15, V]: radiologists detected 70% of abnormalities at 200 ms (Kundel and Nodine 1975). Mammography: experts found 71% of lesions in 25 s, novices 46% in 40 s. Experts use foveal vision on about 15-20% of the image. The holistic skill is narrow and does not carry to control tasks or neighbouring modalities.
- Editorial strand [a02]: expert ICU doctors looked at more relevant parts of a case than competent non-experts. Arithmetic experts spontaneously use shortcuts. Einstellung (set effect) was studied with eye movements and linked to expert flexibility.

### 2.4 Development: deliberate practice and its limits

- Macnamara, Hambrick and Oswald (2014) meta-analysis, variance explained: games 26%, music 21%, sports 18%, education 4%, professions under 1% [b10, V]. A 2018 corrigendum changed values slightly; the 2020 review cites games 24, music 23, sports 20, education 5, professions 1, overall 14% [b10, b11].
- Hambrick, Macnamara and Oswald (2020) [b11, V]: Macnamara 2014: k=157, r=.38, 14.4% uncorrected. Platz 2014 music: r=.61 (37.2%). Sports: r=.45 (20.3%); among elite athletes only about 1%. Ericsson and Harwell 2019: r=.56 (8 effects). Corrected figures depend heavily on assumed reliability (about a factor of two between uncorrected and corrected, per critique).
- Hambrick et al. (2014) [b13]: practice accounts for about a third of reliable variance in chess and music. Jabusch 2009: lifetime practice predicted only 17% of pianists' baseline variance.
- Gullich 2017 [b12]: 83 international medalists vs 83 non-medalists; medalists had about 948 fewer organised training hours by age 18 and started about 1.5 years later. Early specialisation does not predict elite status. Intelligence explained about 30% of piano learning-rate differences.
- Macnamara and Maitra (2019) [b14, V]: preregistered double-blind replication of the classic violinist study. N=39 (13 per group) vs original N=30. The skill-practice correspondence was substantial but considerably smaller than in the original. Teacher-designed practice did not explain more than practice alone.
- Gaschler et al.: 1,383 chess players tracked over 10 years; learning curves are exponential, not power-law [a03, b17].

### 2.5 Expertise and general cognition

Chess players are about half an SD better than non-players on cognitive ability, and chess skill correlates with fluid intelligence, speed, working memory and knowledge [a05]. This is correlation. The training studies in section 5 do not show that chess causes it.

### 2.6 The transfer programme and the "brain training" fight

Owen et al. (2010) [d03, V]: N=11,430 online, six weeks of training on reasoning, memory, planning, visuospatial and attention tasks. Every trained task improved. No transfer, even to closely related tasks. Simons et al. (2016) [d04, b09] reviewed every study cited by brain-training companies against best-practice standards after two conflicting open letters (70+ scientists sceptical, 133 supportive). Training improves trained tasks and sometimes close ones; evidence for broad transfer is weak; many studies fell short of best practice [a10].

## 3. Core findings with exact numbers

Status: established = two or more independent sources; contested = credible conflict; single = one source.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Masters recall real positions far better than random ones | 92.0 / 57.1 / 32.2% real vs 19.0 / 13.8 / 12.4% random (Master / Expert / Class A); N=26; F(2,23)=34.17 | Gobet and Simon 1998 [a15] | established (K06) |
| Expert advantage is in early fixations, not total looking | best move 93% vs 52%; RT 28.9 vs 41.9 s; N=41 (17 experts) | Sheridan and Reingold 2014 [a19] | established (K07) |
| Radiologists spot abnormalities in 200 ms | 70% detected | Kundel and Nodine via [b15] | established |
| Expert visual span larger only for meaningful positions | not given | Reingold et al. 2001 [b16] | established |
| Chess/music/WM training: overall far transfer small | g: chess 0.34 [0.24,0.44]; music 0.16 [0.09,0.22]; WM 0.12 [0.06,0.18] | Sala and Gobet 2017 [a05] | established, one group |
| Effects shrink with active controls | music 0.25 (k=64, passive) to 0.03 [-0.07,0.12] (k=54, active); WM 0.18 (k=34) to 0.05 [-0.05,0.15] (k=40) | [a05] | established (K02) |
| Music training, updated | N=6,984, k=254, m=54; g=0.184 overall; non-active 0.228; active 0.056 (SE 0.058) | Sala and Gobet 2020 [a07] | established |
| Second-order meta-analysis of cognitive training | 332 samples, 1,555 effects, 21,968 people; uncorrected far g=0.12; corrected, active controls g=0.00; tau2=0 | Gobet and Sala 2023 [a08, d05] | established, one group |
| WM training, active controls, far transfer | m=41, k=393, N=2,375; g=0.001 (SE 0.055, p=.982) | Sala and Gobet 2019 [d06] | established |
| WM training transfer is directional | 55 studies, 208 effects, N=3,492; within-WM g=0.146; updating to span 0.176; span to updating 0.048 (ns); updating to non-WM 0.120; span to non-WM 0.008 (ns) | 2026 meta-analysis [b18] | established |
| WM training vs treated controls | 87 publications, 145 comparisons; no evidential value after bias analysis | Melby-Lervag et al. 2016 [a09, b08] [M] | established |
| Large online brain-training trial | N=11,430; no transfer | Owen et al. 2010 [d03] | established |
| Chess instruction meta-analysis | 24 studies, 40 effects; d maths 0.38, cognitive 0.34, literacy 0.25; almost no active controls | Sala and Gobet 2016 [b02] | contested (K03) |
| Chess instruction randomised trial | 1,965 chess vs 1,900 control (Year 5); 25-30 h; no outcome differed | Jerrim et al. 2016 [b03] | contested; arm sizes from one reading |
| Action games: cross-sectional vs intervention | g=0.55 vs 0.34; 30% publication-bias inflation | Bediou et al. 2018 [a12] [M] | contested (K04) |
| Action games, null meta-analysis | k=310 / 315 / 359 for three models; small or null | Sala et al. 2018 [a13] [M] | contested |
| Action-game replication | Exp 1 N=20 (10 per group); Exp 2 N=45 (15 per group); RT speed-up 51 ms (action) vs 59 ms (cognitive game) | van Ravenzwaaij et al. 2014 [d01] | contested (K24) |
| Gamer advantage vanishes at latent level | near-zero relations over full range; N not read | Unsworth et al. 2015 [d02] [M] | contested |
| Demand characteristics in game studies | only 2 covert-recruiting expert-novice studies, both found advantage | Boot et al. 2011 [a11] | single review |
| Placebo effect in cognitive training | suggestive flyer: 5-10 IQ points after 1 h; neutral flyer none; induced expectancy in n-back: no effect | Foroughi 2016 [d07]; [d08] | contested |
| Deliberate practice share of variance | games 26, music 21, sports 18, education 4, professions <1 (%); overall 14.4% (r=.38, k=157) | Macnamara et al. 2014 [b10, b11] | established (K05) |
| Violinist study replication | N=39 vs 30; effect smaller | Macnamara and Maitra 2019 [b14] | established |
| Teaching experience predicts effectiveness poorly; car expertise interferes with faces | no pooled numbers | editorial [a04] | single (K18) |

## 4. Mechanisms and models

### 4.1 Chunks and templates (implementable as a retrieval store)

- Store: a long-term memory of patterns. A chunk is a small group of items that co-occur (median largest master chunk 5 pieces) [a16].
- Template: a frequently met large pattern with slots (variables). Slots take values (locations) and pointers (plans, moves, other templates). Slot filling takes seconds; learning a new chunk takes 5 to 10 s [a17].
- Recognition: match input against chunks; a match cues plans. Applied recursively during look-ahead, it also guides search [a18].
- Engineering consequence: a pattern store helps when input has the learned structure and gives no help when structure is scrambled (random chess positions 19% vs 92%). A retrieval store for an LLM must be evaluated on both structured and novel items (critique gap 6).
- In LLM terms a template is a stored solved problem with variable slots (a parameterised rule or helper program) offered by similarity. This matches the schema's planned subgoal library.

### 4.2 Early relevance triage

- Human mechanism: a fast parallel perceptual pass (about 200 ms for radiographs) finds the relevant regions; later fixations go there [a19, a20, b15].
- Implementable form: a first cheap pass scores parts of the input for relevance (by code where possible, not model opinion) and passes only the top parts to the expensive step. Success criterion: same accuracy, fewer tokens. No LLM study found (gap 7).

### 4.3 Common elements and near transfer

Transfer scales with task similarity [a06, d06]. Rule for us: a scaffold element tuned on task type A should help type B only to the degree they share operators and structure. Measure on held-out types.

### 4.4 Why RL transfers and SFT forgets (machine side)

- Forgetting after fine-tuning is predicted by forward KL from the base policy: R2 = 0.961 (toy ParityMNIST), 0.71 (LLM experiments). On-policy RL stays near the base; SFT can land far away [d11, V].
- Huan et al. latent-shift data [b20]: PCA shift on non-reasoning tasks, as listed: Qwen3-14B no-think 129.8, SFT no-think 113.7, SFT think 38.2, RL 36.9 (the paper's own table; the reading of which row is baseline is not settled here). KL on MATH-500: SFT no-think 0.372 vs RL 0.084. Token-rank shift for the RL model: 0.98 positions [c07] (a different metric, not a conflict).
- Prompt scaffolds change no weights, so they avoid this route [K20]. Whether prompts shift behaviour on unrelated inputs is a separate question (6.3).

### 4.5 Counterfactual twin method

To separate reasoning from reciting, build a twin of each test item with the same abstract reasoning but unfamiliar rules, then measure the gap [c08]. A control task (CCC) checks whether the model knows the new rule [c09]. Implementable: per bench item type, write a rule-swapped twin plus a one-line rule check.

## 5. What holds up

### 5.1 Holds up

- Domain-specific chunk knowledge as the basis of expert memory and perception. Replicated over decades; the 1998 replication kept the chunk-boundary result and revised chunk size [a15].
- Fast early detection of relevant regions by experts (chess, radiology, ICU) [a19, a20, b15, a02].
- Near transfer exists, scaled to task similarity. Far transfer is near zero with active controls: music 0.03, WM 0.05 or 0.001, corrected grand mean 0.00 [a05, a07, a08, d06]. Independent large-N support: Owen 2010, N=11,430 [d03].
- Deliberate practice is necessary but not sufficient; its share depends on domain (26% games to under 1% professions) [b10, b11, b13].

### 5.2 Failures, conflicts, replications

- Chess instruction: the meta-analysis (d 0.34-0.38) came from designs with almost no active controls. The randomised trial (about 1,900 per arm) found nothing [b02, b03]. The trial is the better design.
- Video games: cross-sectional g=0.55 falls to 0.34 in interventions; the null meta-analysis and replications find nothing with active controls [a12, a13, d01, d02]. Differences come from control choice, inclusion rules and extreme-group designs.
- Violinist deliberate-practice study: replicated in direction, smaller in size [b14].
- Persona prompts: see section 6.

### 5.3 Moderators

- Control type (passive vs active) is the biggest: music 0.25 to 0.03, WM 0.18 to 0.05 [a05].
- Direction of WM transfer: updating to span 0.176; span to updating 0.048 (ns) [b18].
- Random allocation: non-random designs gave 0.246 in music, active controls near zero [a07].
- Expectation: a suggestive flyer gave 5-10 IQ points in one hour [d07]; an attempt to induce expectancy in n-back training found none [d08]. Placebo effects are possible but not stable.
- Hours: 25-30 h suggested minimum in chess instruction [b02]; Bediou asked for studies over 30 h [a12].

### 5.4 What worked and what did not (human)

- Worked: practice on the trained task; near-transfer tasks that share structure; machine-derived concepts taught to 4 grandmasters (gains 6 to 42 percentage points, uneven, not tested out of domain) [c16].
- Did not work: brain-training programs for broad cognition [d03, d04]; chess lessons for school results in the best trial [b03]; action games for general attention under active controls [d01].

### 5.5 Dependence on one group

Sala and Gobet (with colleagues) wrote a05, a07, a08, b02, b05, d05, d06. Independent support: Melby-Lervag 2016 [M], Owen 2010, Simons 2016 [abstract], the 2026 WM meta-analysis [b18]. No newly preregistered large replication from another group was found (gap 10). "Established" for far-transfer-null rests on one group plus independent large-N and review support.

## 6. Language models

### 6.1 Persona ("you are an expert") prompts

- Zheng et al. 2024 [c01-c04, V]: 162 roles, 4 model families, 2,410 MMLU questions in 26 subjects. Most personas did not differ from no persona. In-domain persona coefficient 0.004 (p<0.01): real but negligible. Oracle choice of the best persona per question beats control, but automatic selection (random, most-similar role, RoBERTa domain classifier at 78.1% domain accuracy, best-on-train) does no better than random. Audience style ("you are talking to a lawyer") was slightly better than speaker style. Llama3-70B had more personas with negative effects; Qwen2.5-7B and 72B were insensitive to all 162 [c24].
- Xu et al. 2025 ExpertPrompting [c15]: GPT-4 reviewer preferred expert answers 48.5% vs 23% vanilla (rest ties). Open-ended answers, model judge that may favour length [c21].
- Kim et al. 2024 [d09, V]: GPT-4 persona average on arithmetic 91.06 to 92.28; other tasks 61.37 to 77.08 (Letter 19.80 to 92.80, Date 66.93 to 75.93; some sets down: Strategy 76.42 to 75.71). Persona could flip right answers to wrong. Llama3-8B was worse on 7 of 12 sets. No Claude or Gemini data. Status: contested (K09).

### 6.2 Counterfactual twins: skill tied to seen conditions

Wu et al. 2024 [c08, c09, c25, V], 11 tasks. GPT-4 chess opening legality (100 items each): 100% default vs 21% with swapped knight/bishop start; with zero-shot CoT 100% vs 61%. Control task CCC: 89% vs 74% without CoT; 100% vs 96% with CoT. GPT-3.5: 73% vs 4%. The task is balanced yes/no (chance 50%), so 21% is far below chance: the model applies the standard rule systematically (critique). The failure is in using a known rule, not in knowing it. CoT narrows the gap but never closes it.

Reversal curse [c11]: GPT-4 gives "Tom Cruise's mother" correctly 79% of the time, the reverse 33%. Fine-tuned GPT-3 and Llama-1: reverse likelihood no higher than random; not fixed by augmentation. Direction-bound learning.

### 6.3 Transfer from training (machine analogue of the transfer programme)

- Huan et al. 2025 [a21, b19, b20, c05-c07, V]: over 20 open-weight reasoning models; most that succeed in math fail to transfer. Qwen3-14B, 47K math problems: non-reasoning average 45.7 base, 21.1 SFT(think), 29.0 SFT(no-think) (transferability index -104.1), 53.2 RL. IFEval 69.2 base vs 41.4 SFT no-think vs 70.0 RL. Other-reasoning 30.2 base, 45.3 SFT, 60.0 RL. Math 27.7 base, 49.8 SFT, 53.8 RL. Qwen3-8B ablation: off-policy SFT TI_non -40.5, on-policy RL +32.4.
- Chu et al. 2025 [b24, d10, V]: rule shift V-IRL-L: RL 80.8 to 91.8, SFT 80.8 to 1.3. GP-L: RL 11.5 to 15.0, SFT 11.5 to 3.4. Visual shift V-IRL-VL: RL 16.7 to 77.8, SFT 16.7 to 11.1. SFT still helps RL by stabilising output format.
- Game to reasoning. SPIRAL [a22, d12, V]: Qwen3-4B-Base average over 8 benchmarks 34.0 to 44.5 (+10.5); RLVR on maths gives 46.0. Qwen3-8B 39.5 to 49.6; Octothinker-8B 25.8 to 33.8. But SFT on the same game data gave 39.7 (4B) and 46.1 (8B): 5.7 of 10.5 and 6.6 of 10.1 points. No non-game synthetic control. ViGaL [b21, b22, V]: Qwen2.5-VL-7B math average 47.7 to 49.4 (Snake) to 50.6 (Snake+Rotation), vs math-trained MM-Eureka 50.1. Logic-RL [b23]: under 5,000 puzzles, Knights and Knaves 0.19 to 0.89; AIME +125%, AMC +38% relative.
- Code to language. Aryabumi et al. 2024 [c10, b25]: code in pretraining adds up to 8.2% relative NL reasoning, 4.2% world knowledge, 6.6% generation win-rate (470M-2.8B models). Opposite of the human null.
- Narrow harm. Emergent misalignment [b26, V]: 6,000 insecure-code examples gave 19.8% misaligned answers (+-7.1, interval not re-verified) in GPT-4o vs about 0% for secure and educational controls; backdoor model under 0.1% without trigger, about 50% with it. In-context version [d14]: 1 to 24% with 16 examples, from as few as 2 examples, in Gemini, Kimi-K2, Grok, Qwen; larger models more susceptible.

Reading: machines transfer when trained with RL or mixed pretraining, and lose generality under narrow SFT. The human null is not a prediction for LLM training.

### 6.4 Narrow expert machines

A 270M transformer trained on 10M games with Stockfish labels: Lichess blitz Elo 2895 vs humans (174 games), 2299 vs bots (228 games); puzzles 95.4% (9M model 88.9%, 136M 94.5%); GPT-3.5-turbo-instruct 1755 vs bots, puzzles 66.5% [a26, b27, c12]. Chess-GPT (25M, 50M) forms board-state and skill representations; a skill vector raised win rate up to 2.6x; a board-state edit raised legal-move rate 41% to 92% [c13]. Othello-GPT builds an editable board model [c14]. None test transfer out of the domain [c23]. Machine-to-human concept teaching: 4 grandmasters, 36 puzzles each (48 for GM4): GM1 0 to 42%, GM2 33 to 58, GM3 25 to 42, GM4 38 to 44; 97.6% of concepts were removed by a teachability filter [c16].

### 6.5 Scaffold-adjacent results

- Generic self-verification without new information hurts: GPT-3.5 CommonSenseQA 75.8 to 38.1 after self-correction; GPT-4 GSM8K 95.5 to 91.5 to 89.0; with oracle labels 97.5 [d15].
- Placebo computation: in small transformers trained for it, filler tokens replaced chain of thought: 3SUM-type 95.1 (CoT), 93.6 (filler), 78.7 (none), majority baseline 63% [d16]. So part of a scaffold's gain can be extra computation. Trained-from-scratch models; not shown for prompted frontier models.
- Experience retrieval: ExpeL [d13]: HotpotQA to FEVER success ReAct 58 vs about 63-70 for ExpeL variants (table assignment uncertain); retrieve-only with Reflexion 40.3 to 54.4 on the main benchmark. Cross-task carry-over occurred; no test of harm on novel problems.
- Expert gaze as training signal: EyeMulator [c17]: 27 programmers, 6 backbones, 36/36 cells positive, +6.8 to +9.7% in examples, some only +1.4%; EyeLayer up to +13.17% BLEU-4 [c18]; +7.16 CodeBLEU [c19]. Needs fine-tuning; single group.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Sharpen G7: compare against a length-matched placebo scaffold, not only the bare prompt.** Part: G7 (evaluation rule). [E] K02, K01. Evidence a05, a07, a08, d06; d16 [S] supports. Human effects shrink by 80-90% once the control is active (music 0.25 to 0.03).
2. **Report scaffold gain separately in-domain and on held-out types.** Part: G7 logging (SCHEMA section 6). [E] K12, K20. Evidence a21, b19, b24, d10, d11. Do not assume a tuning-set gain transfers.
3. **Any verification or check step must add information (rule text, tool output, held-out example).** Part: G2/G3 (already present; this confirms them). [E] K22. Evidence d15.
4. **Do not use accumulated context length or "experience" as a proxy for competence.** Part: G10/G11 design note. [S] K18, consistent with [E] K05 (more practice alone does not make skill). Evidence a04, b10, b11. Not a new rule.
5. **Log cross-domain side effects whenever a domain module is loaded.** Part: logging. [E] for weights (K14: b26, c10); [S] for prompts (K21: d14). Logging is cheap; the active check goes to tests.
6. **Keep the expert-persona line out of the schema (no change).** Part: none; consistent with G4 and 4b. [C] K09: no gain on 2,410 MMLU items, GPT-4 mixed. Not adding is the default.

### Test first

7. **Counterfactual-twin check per item type** (G/O): log default-vs-twin gap with and without scaffold. [S] K11 (Wu only). Evidence c08, c09, c25.
8. **Rule-restating guardrail before applying a rule** (G2 variant): restate the active rule and compare it with the standard rule by code. [S], open. Evidence c09 (knowing is not using), d15 (generic checks hurt).
9. **Early relevance triage in S0/S1** (S): cheap first pass keeps only relevant parts. [E] for humans (K07), no LLM evidence. Evidence a19, a20, b15.
10. **Chunk/template retrieval store** (memory): solved patterns with slots, shown after the first attempt (schema rule). [E] for humans (K06); [S] for LLM agents (d13). Test structured vs novel.
11. **Domain-module contamination check** (G): [S] K21, d14.
12. **Persona on larger closed models, verifiable vs judged benchmarks**: [C] K09, K10. Only to close the question.

## 8. Concrete tests on our bench

All arms at equal total tokens including setup (G7). Fixed seeds, items shuffled once, graders blinded to arm.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Held-out transfer: tune wording on item type A (e.g. ARC), test on type B (BrainTeaser, others) | bare; scaffold; length-matched placebo scaffold with no content | accuracy on B; gain(scaffold) minus gain(placebo) | Gain on B smaller than on A; placebo recovers part (d16 hints at this). |
| T2 | Counterfactual twins: per item type, one rule-swapped twin plus rule check | bare; scaffold; scaffold + rule-restating guardrail | accuracy on default, on twin, gap | Gap shrinks with restating; Wu saw 100 to 61 with CoT, never closed. |
| T3 | Persona vs none on verifiable items and a judged set | none; "expert X" speaker; audience style | accuracy (verifiable); preference by a judge from another family | Near zero on verifiable (Zheng); possible lift on judged. |
| T4 | Long inputs with distractors | full-context solve; triage then solve | accuracy; tokens | Same accuracy, fewer tokens (size unknown, no source). |
| T5 | Pattern store: items matching stored patterns vs scrambled/novel items | no store; store shown after first attempt | accuracy on both sets | Gain on matched, zero or negative on novel (chess analogy 92% vs 19%). |
| T6 | Contamination: unrelated benign queries after loading each module | no module; each module | change in answer quality and style; flagged outputs | Small; grows with number of examples (d14). |
| T7 | Verification with vs without information | plain re-ask; rule-restating; tool-backed check | accuracy change; right-to-wrong flips | Plain re-ask lowers accuracy (d15); informative checks help. |
| T8 | Practice vs choice: more O-operator rounds vs better-chosen operators | N random rounds; N rounds chosen by S6; fewer chosen rounds | accuracy | More rounds alone give weak return (deliberate-practice analogy; weak). |

## 9. What does not transfer, and why

- **The human far-transfer null as a prediction for LLM training.** Humans: near zero with active controls. LLMs: RL and code pretraining transfer (+10.5 SPIRAL, +8.2% code), while narrow SFT loses (TI -104.1). Different learning mechanism. Import the control discipline, not the null.
- **Training-time findings (SFT/RL, gaze fine-tuning, grandmaster concept teaching).** Our agent is scaffolded, not trained. They warn that narrow tuning can hurt; they offer no operators.
- **Chess-specific chunk numbers (50,000 chunks, 2-second boundary).** Tied to board positions and human working memory. The principle (domain pattern store) may carry; the numbers do not.
- **Eye movements as such.** An LLM has no fovea. Only the idea of an early relevance pass could carry, and it is untested.
- **Deliberate practice hours.** An agent has no accumulating practice. Its closest analogue is the lesson store, already gated by two-problem trust.
- **Expertise labels.** Calling the agent an expert adds nothing reliable on facts (Zheng).

## 10. Open questions

1. Does a thinking scaffold improve held-out domains at equal tokens against a length-matched placebo? (gap 1; no study found)
2. Do personas help larger closed models such as Claude or Gemini on verifiable items? (d09 covers only GPT-4, GPT-3.5, Llama3-8B)
3. Does a rule-restating guardrail close the counterfactual gap, and at what token cost? (gap 3)
4. Do prompt scaffolds behave like RL (little drift) or SFT (large drift) on unrelated tasks? Prompts show contamination in d14, but only for misalignment.
5. How much of SPIRAL's gain is format exposure vs game skill? (needs a non-game synthetic control)
6. Do chunk stores help structured problems and hurt novel ones? (gap 6)
7. Does early-fixation triage save tokens without losing accuracy? (gap 7)
8. Exact N and effect sizes of Jerrim 2016, Unsworth 2015, Melby-Lervag 2016 (only abstracts or an earlier reading).
9. Is the human far-transfer null stable in new preregistered large-N work from groups other than Sala and Gobet? (gap 10)
10. Do counterfactual-twin gaps hold for current frontier models? Wu et al. tested GPT-4 and GPT-3.5 era models.

## 11. Sources

[V] opened, [M] abstract or snippet only.

- [V] Campitelli, Connors, Bilalic, Hambrick (2015) editorial: https://europepmc.org/article/PMC/PMC4354238 ; https://www.frontiersin.org/articles/10.3389/fpsyg.2015.00258/full
- [V] Sala and Gobet (2017) Does far transfer exist?: https://europepmc.org/article/PMC/PMC5724589 ; [M] https://journals.sagepub.com/doi/10.1177/0963721417712760
- [V] Sala and Gobet (2020) music training: https://europepmc.org/article/PMC/PMC7683441
- [V] Sala, Gobet et al. (2023) cognitive training: https://europepmc.org/article/PMC/PMC9903001 ; Gobet and Sala (2023): https://doi.org/10.1177/17456916221091830
- [V] Sala and Gobet (2019 preprint) WM training in children: https://doi.org/10.31234/osf.io/p3vku
- [M] Sala et al. (2019) Near and far transfer: https://doi.org/10.1525/collabra.203
- [M] Melby-Lervag, Redick, Hulme (2016): https://doi.org/10.1177/1745691616635612
- [M] Simons et al. (2016) brain training (abstract; [d04] listed opened): https://doi.org/10.1177/1529100616661983
- [V] Owen et al. (2010): https://doi.org/10.1038/nature09042
- [V] 2026 WM asymmetry meta-analysis: https://pmc.ncbi.nlm.nih.gov/articles/PMC13553679/
- [V] Boot, Blakely, Simons (2011): https://europepmc.org/article/PMC/PMC3171788
- [M] Bediou et al. (2018): https://doi.org/10.1037/bul0000130
- [M] Sala, Tatlidil, Gobet (2018): https://doi.org/10.1037/bul0000139
- [V] van Ravenzwaaij et al. (2014): https://pmc.ncbi.nlm.nih.gov/articles/PMC4447196/
- [M] Unsworth et al. (2015): https://doi.org/10.1177/0956797615570367
- [V] Sala and Gobet (2016) chess instruction and Jerrim et al. (2016): https://www.frontiersin.org/articles/10.3389/fpsyg.2017.00238/full ; [M] https://pubmed.ncbi.nlm.nih.gov/28646322/
- [V] Gobet and Simon (1998): https://bura.brunel.ac.uk/bitstream/2438/1343/1/Copy-Task-NEW-BJP.pdf
- [V] Sheridan and Reingold (2014): https://europepmc.org/article/PMC/PMC4142462
- [V] Sheridan and Reingold (2017), Reingold et al. (2001): https://www.frontiersin.org/articles/10.3389/fpsyg.2017.01620/full
- [V] Macnamara, Hambrick, Oswald (2014): https://pubmed.ncbi.nlm.nih.gov/24986855/
- [V] Hambrick, Macnamara, Oswald (2020): https://www.frontiersin.org/articles/10.3389/fpsyg.2020.01134/full
- [V] Hambrick et al. (2014): https://www.frontiersin.org/articles/10.3389/fpsyg.2014.00751/full
- [V] Macnamara and Maitra (2019): https://doi.org/10.1098/rsos.190327
- [V] Foroughi et al. (2016): https://doi.org/10.1073/pnas.1601243113 ; placebo n-back (2018): https://doi.org/10.1016/j.jarmac.2018.06.001
- [V] Zheng et al. (2024): https://arxiv.org/abs/2311.10054
- [V] Xu et al. ExpertPrompting: https://arxiv.org/abs/2305.14688
- [V] Kim, Yang, Jung (2024): https://arxiv.org/abs/2408.08631
- [V] Wu et al. (2024): https://arxiv.org/abs/2307.02477
- [V] Berglund et al. (2024): https://arxiv.org/abs/2309.12288
- [V] Huan et al. (2025): https://arxiv.org/abs/2507.00432 ; https://arxiv.org/html/2507.00432v2
- [V] Liu et al. SPIRAL: https://arxiv.org/abs/2506.24119
- [V] Xie et al. ViGaL: https://arxiv.org/html/2506.08011v4 ; [M] https://arxiv.org/abs/2506.08011
- [V] Logic-RL: https://arxiv.org/html/2502.14768
- [V] Chu et al. SFT memorizes, RL generalizes: https://arxiv.org/abs/2501.17161
- [V] Shenfeld et al. RL's Razor: https://arxiv.org/abs/2509.04259
- [V in c10, M in a24] Aryabumi et al.: https://arxiv.org/abs/2408.10914
- [V] Betley et al.: https://arxiv.org/html/2502.17424 ; Afonin et al.: https://arxiv.org/abs/2510.11288
- [V] Ruoss et al.: https://arxiv.org/html/2402.04494 ; Karvonen: https://arxiv.org/abs/2403.15498 ; Li et al. Othello-GPT: https://arxiv.org/abs/2210.13382
- [V] Schut et al.: https://arxiv.org/abs/2310.16410
- [V] Zhang et al. EyeMulator, EyeLayer, programmer attention: https://arxiv.org/abs/2508.16771 ; https://arxiv.org/abs/2602.22368 ; https://arxiv.org/abs/2503.14936
- [V] Zhao et al. ExpeL: https://arxiv.org/abs/2308.10144
- [V] Huang et al. self-correction: https://arxiv.org/abs/2310.01798
- [V] Pfau et al. filler tokens: https://arxiv.org/abs/2404.15758

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 10 established claims: 7 confirmed as written, 3 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A10.06-K02** (now single-source: the sources are not independent). Numbers match (music 0.25 to 0.03, WM 0.18 to 0.05, chess one active-control study at 0.10) but they come from one Sala and Gobet paper; the other listed sources are the same authors' follow-up or a coauthor's editorial, so there is no independent confirmation.
- **A10.06-K06** (reworded: the sources support less). The 92%/19% recall figures could not be checked (Brunel PDF returned 503; PubMed abstract has no numbers), and 'the advantage vanishes' conflicts with the Sala and Gobet 2017 meta-analysis (r = .41, experts better in 49 of 55 samples) showing a reduced but real expert advantage on random material; in the single study the skill effect on random recall was just non-significant (N = 26). Corrected claim: Expert chess skill rests on large stores of chunks and templates; in Gobet and Simon (1998, N = 26) masters recalled about 92% of game positions but only about 19% of random ones (experts 13.8%, class A 12.4%, skill effect on random positions not significant), so the advantage largely shrinks, though not entirely, for structure that does not match learned patterns.
- **A10.06-K07** (now single-source: the sources are not independent). Sheridan and Reingold 2014 (experts distinguish relevant from irrelevant regions earlier, 'early part of the trial') is supported, but the only other source is the same authors' 2017 review of that and related work, so one lab; 'first fixations' is a loose paraphrase of 'early part of the trial'.
- **A10.06-K22** (now single-source: only one opened source, code check).
