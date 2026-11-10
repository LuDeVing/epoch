# Formal argumentation frameworks (AI): deep document

*Subfield D04.06. Evidence ids (a01..d18) are in evidence_a-d.jsonl; claim ids (D04.06-K01..K36) are in claims.jsonl; checks are in critique.md. Status marks: [E] established, [S] single-source, [C] contested. Cautions from critique.md are applied: Dung 1995 and Prakken 2010 were not opened (definitions come from the Modgil and Prakken tutorial); all human data on grounded match come from one lab and student samples; the ArgLLM family is one research group; no study equates tokens; most LLM work uses trees, not cyclic Dung graphs.*

*Neighbours (not repeated here): argument evaluation criteria (D04.05), argument schemes and critical questions (D04.02), debate versus voting (SCHEMA guardrail G9).*

## 1. What it is

A formal argumentation framework (AF) is a very small object. It is a set of arguments and one relation: "A attacks B". Nothing else. Dung (1995) showed that you can decide which arguments are acceptable from this graph alone. You never look inside the arguments.

Core vocabulary.
- Conflict-free set: no member attacks another member.
- Defence: set S defends argument a if every attacker of a is attacked by some member of S.
- Admissible set: conflict-free and defends all its members.
- Semantics: a rule that picks sets of arguments ("extensions") from the graph. Main ones: grounded, complete, preferred, stable, semi-stable, stage, CF2.
- Grounded extension: unique, the most cautious. Accept arguments nobody attacks. Remove what they attack. Repeat until nothing changes. It is the least fixed point and takes polynomial time.
- Preferred extension: a maximal admissible set. There may be several.
- Stable extension: attacks every argument outside it. May not exist (odd cycle).
- Sceptical acceptance: in every extension. Credulous: in at least one.
- Structured argumentation (ASPIC+, Prakken 2010; Modgil and Prakken 2013): arguments are built from premises and strict or defeasible rules. Three attack types: undermine a premise, undercut a defeasible step, rebut a conclusion. Preferences turn attacks into defeats. The abstract graph is computed from this.
- Gradual (weighted) semantics: arguments carry numeric strengths. Attackers lower, supporters raise. Examples: DF-QuAD, quadratic energy. Used in most LLM work (the "ArgLLM" family).

Why it matters for our agent. S7 (Select) must choose among candidates. If candidates plus the tests or counterexamples that knock them out form an attack graph, code can compute which survive. This fits G5 (code selects) and G2/G3 (revise on real output). The open questions: does it beat plain voting at equal tokens, and are LLM-judged edges reliable enough?

## 2. History and theories in depth

**Founding (1995).** Dung's paper (a01, a24) defined AFs and the grounded, preferred and stable semantics. It showed that many nonmonotonic logics (default logic, logic programming) are special cases. Pure theory, no experiments. Lasting effect: a clean split between building arguments and evaluating them. Not opened this session; definitions checked against the tutorial (a02).

**Structured arguments (2010 to 2013).** Prakken (2010) (a26, b24) and Modgil and Prakken (2013) (a02, a03, a04) built ASPIC+ on Dung. Four rationality postulates: sub-argument closure, closure under strict rules, direct consistency, indirect consistency. A naive instantiation can accept two contradictory conclusions. The postulates hold only under conditions (closure under transposition or contraposition, a reasonable preference ordering). For CF2, which fits humans well, closure under strict rules fails (b05). Structure is not free; it is where errors enter.

**Complexity and solvers.** Reasoning is intractable in general (stated from memory, not opened: a25). Grounded is polynomial. ICCMA 2021 (a09) ran 9 solvers (7 exact, 2 approximate) on 165 old and 422 new instances. Solvers cope in practice, but only two were fully correct in one subtrack, so even exact tools need a check. Benchmark graphs are far larger than a candidate set (4 to 10 nodes).

**Human behaviour experiments.**
- Rahwan, Madakkatel, Bonnefon, Awan and Abdallah (2010) (a07, b23, d04; abstract only): people do not follow reinstatement fully. On floating reinstatement, preferred beat grounded.
- Cramer and Guillaume (2019) (a05, b01 to b05): 61 students, 12 small AFs. Grounded about 75% match, CF2 about 75%, preferred 68%. The same group's earlier 3-AF study found CF2 and preferred beating grounded (b04). The authors explain the change with an untested guess: fictional content pushed people to the simple "undecided when in doubt" strategy.
- Cramer and van der Torre (2019, 2023) (a06, b06, d06): SCF2 fits slightly better than CF2, not significantly. Partly post hoc on the same data.
- Polberg and Hunter (2018) (a08, d03): non-student online sample. People use graded beliefs, not three states.
- Guillaume et al. (2022) (d01) and Cramer and Guillaume 2018 (d02): same lab; grounded is worst on floating reinstatement and 3-cycles.
- 2024 gradual-semantics experiment (d05; abstract only): replicates that a reinstated argument is rated lower than one presented alone.

**LLM era (2020 to 2026).** Three lines.
1. Can the model compute semantics? Zero-shot poorly; fine-tuned well; graph neural networks nearly perfectly (a12, b17).
2. Argumentative LLMs: the model writes pro and con arguments and base scores, code propagates strengths on a tree (ArgLLMs a10; MArgE a16; ARGORA d08; ART a18). Aim: explainability and contestability, not raw accuracy.
3. Dung-style survival inside a pipeline: Castagna et al. 2024 (d07) with ASPARTIX; ArgMed-Agents (d13) with generator, verifier and symbolic solver; ArgRE (a22) for requirements.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Grounded extension is unique and computed by iteration | Polynomial time; preferred may be several; stable may not exist | a01, a02, a24 | [E] |
| Naive structured instantiation can break rationality postulates | Two contradictory conclusions accepted in examples; needs transposition and a reasonable preference order | a03, a04, b24 | [E] |
| Humans match grounded and CF2 about equally on 12 small AFs | Grounded 74.97, CF2 75.46, preferred 68.42, stage2 68.36, semi-stable 62.84, stage 62.79; chance 33%; 86.7% coherent responses (49 of 61); coherent-only grounded 82.79, preferred 75.17; grounded vs CF2 p=.212 | a05, b01 | [C] |
| Grounded is worst on floating reinstatement and 3-cycles | Floating: preferred/CF2 predict 100% and 97.5% (science, maths), grounded 0% and 2.5%; news context 67.5% vs 27.5% (p<.001). 3-cycle: CF2 56%, grounded and preferred 12%, none 32%. Group data: CF2 59.6% first answer, 73.6% group, 72.4% final | d01, d02 | [C] |
| Humans split into strategies | 49 coherent: 22 grounded-like, 27 not; most of the 27 fit CF2 on 11 of 12 AFs; six-cycle: CF2 33%, preferred/semi-stable 60% | d06 | [S] |
| Humans read attacks as intended about 80% of the time | Good items 74% (students), 84% (experts); Rahwan items 56% and 73%; intended one-way attacks seen as one-way 17% (students), 44% (experts); drawing accuracy 77% to 89% by set | d01, d02 | [S] |
| People hold graded beliefs | 69 AMT users, 80 valid responses; most used 4 to 6 belief values; chance of 3 or fewer 0.0000015 | d03 | [S] |
| Frozen LLMs compute grounded poorly | Zero-shot: Llama3-8B 0.18, Llama3-70B 0.37, Qwen2.5-7B 0.31, GPT-3.5 0.15, GPT-4o 0.54 (AFs of 6 to 25 args) | a12, b14 | [S] |
| Fine-tuning fixes it | SFT grounded Qwen 0.97, Llama 0.95; conflict-free 1.00; above 25 arguments Qwen 0.85 grounded with explanation, about 30% without | a12, b15, c08, c09 | [S] |
| Graph neural networks learn semantics | MCC 0.997 to 1.0 up to 25 args; plain GCN 0.16 to 0.39; complete recall 0.41 before verification, 0.91 after | b17, b18 | [E] |
| ArgLLM (tree, DF-QuAD) vs CoT | 0.5 base scores trail CoT by 0.03 to 0.17 (Mixtral 0.56 vs 0.72); estimated base scores within about 0.03 in most cells (Gemma 2 9B 0.53 vs 0.61); GPT-4o MedClaim: direct 0.54, CoT 0.58, ArgLLM 0.51 to 0.53 | a10, b08, b10, c01, c02 | [S] |
| Depth 2 vs depth 1 trees | No reliable gain; differences go both ways | b09, c02 | [S] |
| Argumentative UQ vs direct prompting | Direct up to 0.130 better accuracy; 180 intervals, 74 significant: 44 direct, 24 LUQ, 6 Semantic Entropy | a15, c04 | [S] |
| ArgRAG | PubHealth GPT-4.1-mini 0.898 vs 0.838 no retriever; plain RAG 0.647 to 0.670; RAGuard GPT-3.5 0.804 vs 0.768; GPT-4o-mini 0.855 vs 0.840 | a14 | [S] |
| MArgE | Up to 8.4 points over debate, at worst 2.6 below; up to about 20 with stronger scorer; 3.5 and 1.0 over CoT on two datasets | a16, c05 | [S] |
| ARGORA vs compute-matched vote of 3 | MMLU-Pro (N=500): direct 0.604, MV3 0.604, CoT-like MV3 0.618, ARGORA 0.638; MedQA 0.812 both; significant paired tests on 3 of 7 sets (p=.026, .032, .039); best-semantics numbers are an oracle | d08 | [S] |
| LLM base scores vs constant 0.5 | MMLU-Pro 0.638 vs 0.618; GPQA 0.523 vs 0.419; calibration never measured | d09, d12, b12 | [E] that calibration is unmeasured; gain [S] |
| Voting beats debate | Qwen2.5-7B avg: vote 0.7691, best debate 0.7377, single 0.7205; GSM8K vote 0.9400 vs debate 0.8867 | d10 | [S] (fits G9) |
| Verifier-attack loop | ArgMed GPT-4 MedQA direct 67.8, CoT 71.4, ArgMed 83.3 (n=300); PubMedQA 72.9, 77.2, 81.6; GPT-3.5 MedQA 52.7, 48.0, 62.1; no vote baseline, several times the tokens | d13 | [S] |
| Castagna et al. pipeline | MT-Bench +2.18% average; 5 of 8 categories better, math tie, writing 8.15 to 8.05; one run, scrambled table | d07 | [S] |
| Argument mining by LLMs is weak | Best open model macro F1 75 (RoBERTa about 68); attack F1 below support F1; ArgBench mining 0.31 to 0.60 across 11 LLMs | a17, b21, c14, d15 | [E] |
| LLM judging of debates | DebatePedia Spearman about 0.11 vanilla vs 0.46 CoT few-shot; 12AngryMen 0.11 to 0.35; graph-order effect MCC +8.14 (GPT-4o), -16.48 (Claude-3.5-sonnet) | c10, c11, c12 | [S] |
| Position bias in LLM judges | Pairwise consistency 0.57 to 0.82; list-wise 0.34 to 0.68; worse when quality is close | d11 | [S] |
| Cycles depend on protocol | Pairwise protocol cyclicity 0; cross-pair arbitration 0.20 to 0.29; grounded and preferred diverge from about 0.25 | b20 | [S] |
| Random-graph simulation (ours, not LLM output) | n=4: cycles 5.8/24.5/48.3/86.2% at edge prob 0.1/0.2/0.3/0.5; grounded empty 0.6/5.6/18.7/57.8%. n=6: cycles 16.8/55.6/85.2/99.6%; grounded empty 0.5/9.1/32.5/81.9%; skeptical preferred differs from grounded 0.6/8.5/22.5/41.0% | d17 | simulation only |
| LLM review of graph structure is flaky | Objects to 9.8% of correct graphs (11 of 112); verdict changes on 6.2% of identical calls; 2,758 ms vs 1 ms for a validator; recall 0.96 to 1.00 on injected defects; 21% of graphs have an invalid scheme field | d12 | [S] |
| Forecasting with argumentative agents | Metaculus 68% to 81%; GJOpen 63% to 75% in best variants | a21 | [S] |
| Requirements negotiation | Compliance coverage 84.7% vs 47.6 to 47.8%; trace completeness 40.9% | a22, b19, c06 | [S] |
| Legal tasks (ACAL) | Learned Hands Courts 70.8 vs CoT 69.3, RAG 70.3; gains 0.5 to 1.5 points, single runs | a19, d18 | [S] |
| Graph shape predicts persuasion barely | AUC about 0.56; logistic 0.587; n=384 | c16 | [S] |
| Structured reasoning can collapse on small inputs | AAM-CBR 10 factors 1.00/0.96 vs 0.90; 6 factors small model 0.28 vs 0.76 | c17 | [S] |
| Debate lowers diversity | Creative-MAD restores 26.2% semantic and 24.0% lexical diversity (Qwen3-8B), quality within 1.2% | d14 | [S] |

## 4. Mechanisms and models

**4.1 Grounded extension, implementable in a few lines.**
```
def grounded(args, attacks):          # attacks: set of (a, b): a attacks b
    IN, OUT = set(), set()
    changed = True
    while changed:
        changed = False
        for a in args:
            if a in IN or a in OUT: continue
            attackers = {x for (x, y) in attacks if y == a}
            if attackers <= OUT:           # all attackers defeated, or none
                IN.add(a); changed = True
        for a in args:
            if a not in OUT and any(x in IN for (x, y) in attacks if y == a):
                OUT.add(a); changed = True
    return IN, OUT, set(args) - IN - OUT   # accepted, rejected, undecided
```
Undecided arguments are those in cycles or attacked by undecided ones. A self-attacking argument is never accepted (the loop above handles it, since it is its own attacker and never in OUT first).

**4.2 Preferred and stable.** For 4 to 10 candidates, brute force over subsets (at most 1024) is fine. Keep admissible sets, take maximal ones. Sceptical preferred = intersection of all preferred extensions. Use an exact solver (ASPARTIX, clingo) if n grows. ICCMA solvers (a09) are the reference.

**4.3 CF2.** Split the graph into strongly connected components, process them in topological order, and in each component keep maximal conflict-free sets under the attacks left after earlier components are fixed. Most non-grounded humans follow it (d06). It does not need admissibility. Build only if the test on cyclic graphs shows it matters.

**4.4 Candidate attack graph for S7 (proposed).**
- Nodes: distinct candidates from the S4 harvest.
- Edge a to b if a test input exists where a passes and b fails, or where they disagree and code verifies a. This keeps edges tied to code output (G2, G3), not model opinion.
- An LLM-proposed edge is a "claim edge" and counts only after a check runs.
- Compute grounded. Survivors are the accepted set. If grounded is empty, fall back to sceptical preferred, then to group size and shortness (the existing S7 rule). Log the fallback (as d07 does).
- Validate in code: dangling ids, duplicate ids, cycles, self-attacks (d12: exact, 1 ms).

**4.5 Gradual semantics on a tree (DF-QuAD).** Each node has base score tau in [0,1]. For a node, combine attacker strengths as v_a = 1 - prod(1 - s_i) over attackers, and v_s likewise over supporters. If v_a >= v_s, final = tau - tau*(v_a - v_s); else final = tau + (1 - tau)*(v_s - v_a). Compute bottom-up. This is the cheap scoring layer in ArgLLMs, MArgE and ARGORA. It needs a tree, or an iteration that converges, for cycles.

**4.6 ArgLLM pipeline (a10).** For claim c: ask the model for pro and con arguments (depth 1) and again for each (depth 2). Ask for a base score for each, or set 0.5. Run DF-QuAD. Output true if the final score of c exceeds 0.5. Depth 2 costs about 7 LLM calls per claim against 1 for CoT.

**4.7 Verifier-attack loop (d13).** Generator proposes a decision. Verifier proposes an attack. Solver computes acceptability. Loop to a dialogue limit of 8. An empty acceptable set signals knowledge limits: in 63% of empty cases identifiable reasoning errors existed, 76% of those from conflicting knowledge.

## 5. What holds up

**Holds up.**
- The computation is exact and cheap: grounded in polynomial time; learned solvers near perfect (K01, K10).
- Simple reinstatement cannot separate semantics; only floating reinstatement and cycles do (b04, K05). Two lines (Rahwan 2010 and the Luxembourg lab) agree people do not follow grounded there.
- LLM edge extraction is weak: macro F1 75 best; ArgBench 0.31 to 0.60 (K18).
- At equal model, graph scoring does not beat CoT in the ArgLLM family; the value is explainability (K11, K13).
- Voting is the baseline to beat (d10, d08).

**Failed or weak.**
- "Grounded models humans well" is unstable. The earlier 3-AF study had CF2 and preferred beating grounded (b04); the 12-AF study had a tie; later studies had grounded worst on discriminating cases (d01, d02). Status [C].
- ArgLLM with 0.5 base scores trails CoT by up to 0.17.
- Deeper trees do not reliably help (b09).
- Argumentative confidence loses to direct prompting in 44 of 74 significant intervals (a15).
- GPT-4o on MedClaim: variants 0.51 to 0.53 against CoT 0.58 (b10).
- Graph shape alone predicts persuasion at AUC about 0.56 (c16).
- LLM structure review objects to 9.8% of correct graphs (d12).

**Moderators.**
- Content: fictional content pushes toward the cautious strategy; real-world content lets world knowledge shift answers (grounded 67.5% vs 27.5% in news context) (b04, d02).
- Group discussion before individual answers raises match (CF2 59.6% to 73.6%) (d01). Answers within a group are not independent.
- Strength of base model: gains shrink for stronger models (a14, a21, b10).
- Graph shape: grounded and preferred coincide on acyclic graphs; only cycles split them (b20, d17).
- Explanations in training help generalisation to larger AFs (b15).
- Cost: the largest gain (ArgMed 71.4 to 83.3) comes with several times the tokens and no vote baseline (d13).

**Interventions that worked (with caveats).**
- Code validation of graphs (exact, 1 ms) (d12).
- Retrieval plus graph (a14); estimated base scores over 0.5 (d09).
- ARGORA vs MV3: +2 points on MMLU-Pro, zero on MedQA (d08). Small.
- Falling back from grounded to preferred; +2.18% MT-Bench, no token matching (d07).

**Did not work or not shown.**
- Debate vs vote: debate lost (d10).
- Relation labels from LLM mining (d15).
- ASPIC+ structure: no measured benefit (K35).
- Creative tasks: no study; debate lowers diversity (d14).

## 6. Language models

**Computing semantics.** Zero-shot grounded accuracy runs from 0.15 (GPT-3.5) to 0.54 (GPT-4o) on AFs of 6 to 25 arguments (a12). Open models: Llama3-8B 0.18, Llama3-70B 0.37, Qwen2.5-7B 0.31. Scale helps but not enough. SFT lifts to 0.95 to 0.97 and conflict-free to 1.00. Careful: 0.97 is on the paper's test distribution; above 25 arguments Qwen reaches 0.85 grounded with explanations and about 30% without (critique correction 3). A GNN reaches MCC 0.997 to 1.0 (b17). Lesson: give survival to code, not the model.

**Reasoning on attack graphs in words.** In witness-testimony puzzles (c10) models fail even on linear chains (parity of "Alice lies"). o1-preview scored 100% on chains (subset); others fell toward 50% as chains grew. In 2,540 non-linear prompts only 8.85% had answer "yes", and models over-answered yes. Graph order in the prompt moves results: MCC +8.14 for GPT-4o, -16.48 for Claude-3.5-sonnet (c11).

**Judging debates.** Vanilla Spearman about 0.11 against QuAD gold on DebatePedia; CoT few-shot 0.46 (c12). Position bias: pairwise consistency 0.57 to 0.82 (d11). Nobody measured it on attack-edge labels.

**Building the graph.** Relation mining F1 75 for the best open model (a17); attack F1 trails support F1. ArgBench mining 0.31 to 0.60 (d15). A demo (c15) extracted 45.60% attack and 34.72% support relations in one corpus with no accuracy check. Human edge drawing is itself about 80% accurate (d01), and only 17% to 44% see intended one-way attacks as one-way (d02), so the label ceiling is below 100% even for people.

**Argumentative scoring vs CoT.** At equal model, graph scoring is usually at or below CoT: 0.03 to 0.17 below with 0.5 base scores; about 0.03 with estimated scores (a10, c02). MArgE: +1.0 and +3.5 over CoT on two of three sets (a16). ARGORA +2 points over MV3 on MMLU-Pro, tie on MedQA (d08). ACAL +0.5 to 1.5 on legal sets (a19). ArgMed +11.9 on MedQA (GPT-4) with a multi-round loop (d13). Forecasting +13 and +12 points (a21). Only ARGORA has a token-matched vote.

**Calibration.** Argumentative confidence loses to direct prompting in 44 of 74 significant cases (a15). LLM base scores were never checked for Brier or ECE (d12, d09).

**What changed behaviour.** Supervised training with explanations; CoT few-shot for debate judging (0.11 to 0.46); estimated base scores over 0.5 (up to 0.10 on GPQA, d09); retrieval (a14); code validators instead of LLM review (d12). What did not: depth (b09), debate rounds (d10).

**Cyclic graphs.** The ArgLLM family never tests them (trees). Only Castagna et al. (d07) used Dung semantics on an LLM-flagged conflict graph, falling back from grounded to preferred. That implies empty grounded sets occur, but no rate is reported.

## 7. What our agent should take

### Add now (established)

1. **Compute survival in code, never in the model.** Part: S7, G5. [E]. Ids: a01, a02, a12 (model zero-shot 0.15 to 0.54), K01, K10. Already consistent with S7 and G5; the addition is the exact grounded routine with a preferred fallback, and logging the fallback.
2. **Edge labels are the weak link; count only code-checked edges.** Part: S7, G2, G3. [E]. Ids: a17, b21, c14, d15 (F1 75 best, 0.31 to 0.60), d01, d02 (human edge reading about 80%).
3. **Validate the graph in code before computing** (cycles, dangling ids, duplicates, self-attacks); never ask an LLM to review structure. Part: S7. Numbers [S] (d12), but zero cost; adopt as hygiene.
4. **Keep majority vote as the baseline for any S7 variant.** Part: G7, G9. [S] numbers (d10, d08); rule already in schema.
5. **Do not treat argumentative confidence as a free calibration source.** Part: G5. [S] (a15).
6. **Do not use graph shape alone as a quality signal.** Part: S7. [S] (c16).
7. **Log in every S7 run:** candidate count, edge count, cyclic yes/no, grounded empty yes/no, fallback used. Part: S9. Needed to answer K32 (instrumentation, not a behaviour change).

### Test first (not established)

1. Grounded survival on code-derived edges vs current S7 and vote (K28, d08) [S].
2. Edge judge accuracy, both orders (K18, K26) [S].
3. Real cycle and empty-grounded rate (K32) [simulation only].
4. CF2 or preferred fallback vs grounded on cyclic graphs (K03, K04) [C].
5. Numeric score next to survive flag (K31) [S].
6. LLM-estimated base scores vs uniform, with calibration (K25).
7. Verifier-attack loop vs vote at equal tokens (K29) [S].
8. Graph filtering of retrieved notes (K15) [S].
9. Undercut edges vs plain (K35, no data).
10. Open-ended tasks, objective-test filter only (K34, no data).

## 8. Concrete tests on our bench

All arms use the same total token budget, counting setup and edge-judge calls. At least 100 items per arm, paired, McNemar test.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 survival vs vote | ARC-like or BrainTeaser items with 4 to 8 harvested candidates and code tests | (a) majority vote; (b) current S7; (c) grounded on test-derived edges; (d) grounded with preferred fallback | Accuracy, paired difference | 0 to +2 points over (b); if (c) equals (b) the graph adds nothing. ARGORA's +2 is the benchmark (d08) |
| T2 edge judge | 50 to 100 hand-labelled candidate pairs | LLM edge judge in order AB, order BA, agree-only | Edge precision and recall; survivor-set change from order | Precision below 0.8 expected (a17, d15); order disagreement 20 to 40% (d11) |
| T3 cycle statistics | All S7 runs | Instrumentation only | Cycle share, empty-grounded share, share where preferred differs from grounded | Cycles below 25% with test-derived edges; above that, semantics matter (d17, b20) |
| T4 cycle handling | Cyclic items from T3 | grounded; sceptical preferred; CF2; size-then-shortness | Accuracy on cyclic subset | CF2 or preferred a few points better; unknown (K03, K04, d02) |
| T5 score plus flag | T1 items | flag only vs flag plus score as tiebreak | Accuracy; Brier on confidence | Small gain (d03) |
| T6 base scores | Claim set (MedClaim-like, StrategyQA) | uniform 0.5; estimated; CoT; vote | Accuracy, Brier, ECE | Estimated beats uniform by 0.01 to 0.10 (d09); Brier unknown |
| T7 verifier loop | Medical or hard reasoning set | CoT; vote; ArgMed-style loop, equal tokens | Accuracy | Most of ArgMed's gain disappears at equal tokens; gain over vote under 3 points |
| T8 memory filter | Items with conflicting retrieved notes | concatenate; graph filter; none | Accuracy | Gain for weaker models only (a14) |
| T9 undercut edges | Items with defeasible rules | plain attack; attack plus undercut | Accuracy and invalid-graph rate | Unknown; invalid-field rate 21% (d12) |
| T10 open-ended | NoveltyBench-like | no filter; objective-test filter | Diversity and quality | Neutral; risk of lower diversity (d14) |

## 9. What does not transfer, and why

- **Human match percentages.** They come from 61 students on 12 small AFs (3 to 8 arguments), fictional content, group talk first. Our graphs differ in size, content and origin. They say how people reason, not how correct a survivor set is.
- **ArgLLM accuracy results.** Trees, where grounded, preferred and stable coincide; claims with pro and con text and DF-QuAD. Our S7 graphs are cyclic candidate graphs.
- **Fine-tuned solver results (0.95 to 0.97, MCC 1.0).** We do not train, and exact code is better anyway.
- **Requirements, forecasting, medical and legal gains.** Domain-specific, mostly single-group preprints, no token matching.
- **Debate-style loops.** G9 already rules out debate. ArgMed-like loops are debate in structure with a symbolic judge. Test only against votes.
- **ASPIC+ guarantees.** They hold for logic-based rule systems under conditions. LLM-built arguments have no closure guarantee.
- **ICCMA benchmarks.** Large synthetic graphs; ours are 4 to 10 nodes.
- **Creative tasks.** "Fails the test the other passes" is undefined; convergence cuts diversity.
- **Gradual scores as probabilities.** They are not calibrated (d12).

## 10. Open questions

1. Does code-computed grounded survival beat voting at equal tokens when edges come from code tests? No token-matched study exists (nearest: d08, trees).
2. How accurate are LLM attack judgments between candidate answers? Only corpus-level and human edge studies exist.
3. How often do real candidate graphs contain cycles? The 25% to 56% figure is simulation (d17).
4. Do LLM base scores beat uniform, and are they calibrated?
5. Does the 75% grounded match replicate with non-students or AFs above 6 arguments? Nothing found.
6. Order and position bias for edge labels.
7. Cost-benefit of ASPIC+ structure.
8. Any use on creative or open-ended tasks.
9. Rahwan 2010 and the 2024 reinstatement paper were read as abstracts only. Dung 1995 and Prakken 2010 were not opened.
10. Does the 2.18% MT-Bench gain (d07) survive token matching?

## 11. Sources

[V] opened, [M] snippet or abstract only.

- [M] Dung (1995) On the acceptability of arguments... https://doi.org/10.1016/0004-3702(94)00041-X (a01, a24, b07, c26)
- [V] Modgil and Prakken (2013) The ASPIC+ framework: a tutorial. https://webspace.science.uu.nl/~prakk101/pubs/ASPICtutorial.pdf (a02, a03, a04)
- [M] Prakken (2010) An abstract framework for argumentation with structured arguments. https://doi.org/10.1080/19462160903564592 (a26, b24)
- [M] Dunne and Wooldridge; Dvorak and Dunne, complexity. https://doi.org/10.1007/978-3-319-67582-4_4 (a25)
- [M] Rahwan et al. (2010) Behavioral experiments for assessing the abstract argumentation semantics of reinstatement. https://doi.org/10.1111/j.1551-6709.2010.01123.x (a07, b23, d04)
- [M] Polberg and Hunter (2018), journal version. https://doi.org/10.1016/j.ijar.2018.01.005 (a08)
- [V] Polberg and Hunter (2018) arXiv. https://arxiv.org/abs/1707.09324 (d03)
- [V] Cramer and Guillaume (2019) Empirical study on human evaluation of complex argumentation frameworks. https://arxiv.org/abs/1902.10552 (a05, b01 to b05)
- [V] Cramer and van der Torre (2019) SCF2. https://arxiv.org/abs/1908.08406 (a06, b06)
- [V] Cramer and van der Torre (2023). https://doi.org/10.3389/frai.2023.1045663 (d06)
- [V] Cramer and Guillaume (2018) Empirical cognitive study. https://orbilu.uni.lu/handle/10993/37025 (d02)
- [V] Guillaume, Cramer, van der Torre, Schiltz (2022). https://doi.org/10.1371/journal.pone.0273225 (d01)
- [M] Experimental evaluation of gradual argument acceptability semantics (2024). https://doi.org/10.3233/aac-230016 (d05)
- [V] Amgoud (2019) survey. https://www.ijcai.org/proceedings/2019/0874.pdf (d16)
- [V] Lagniez et al. (2021) ICCMA 2021. https://arxiv.org/abs/2109.08884 (a09)
- [V] Freedman et al. (2025) Argumentative LLMs. https://arxiv.org/abs/2405.02079 (a10, a11, b08 to b12, b29, c01 to c03)
- [V] Li et al. (2025) Enhancing conflict resolution in language models. https://arxiv.org/abs/2412.16725 (a12, a13, b14 to b16, c08, c09)
- [V] Craandijk and Bex (2020). https://arxiv.org/abs/2007.07629 (b17, b18)
- [V] Zhu et al. (2025) ArgRAG. https://arxiv.org/abs/2508.20131 (a14)
- [V] Zhou et al. (2025) UQ. https://arxiv.org/abs/2510.02339 (a15, c04)
- [V] Ng et al. (2025) MArgE. https://arxiv.org/abs/2508.02584 (a16, c05)
- [V] Gorur, Rago, Toni (2024). https://arxiv.org/abs/2402.11243 (a17, b21, c14)
- [V] ART (2026). https://arxiv.org/abs/2601.05455 (a18)
- [V] Nguyen et al. (2026) arena-based. https://arxiv.org/abs/2602.18916 (a19, d18)
- [V] Freedman et al. (2026) neurosymbolic. https://arxiv.org/abs/2605.20098 (a20)
- [V] Forecasting multi-agent (2025). https://arxiv.org/abs/2510.24303 (a21)
- [V] ArgRE (2026). https://arxiv.org/abs/2604.23124 (a22, b19, b20, c06)
- [V] QUARE (2026). https://arxiv.org/abs/2603.11890 (c07)
- [V] Fungwacharakorn et al. (2025). https://arxiv.org/abs/2512.12656 (a23, c17)
- [V] Dejl et al. (2026) ArgLLM-App. https://arxiv.org/abs/2602.24172 (b13, c20)
- [V] Chen et al. (2024). https://arxiv.org/abs/2311.09022 (b22; per-dataset numbers not extracted)
- [V] Steging, Renooij, Verheij (2025). https://arxiv.org/abs/2505.01539 (c10, c11)
- [V] Sanayei et al. (2025). https://arxiv.org/abs/2509.15739 (c12, c13)
- [V] Alfano et al. (2026). https://arxiv.org/abs/2603.02858 (c15)
- [V] Bhargava et al. (2026). https://arxiv.org/abs/2610.15091 (c16)
- [V] Li and Russo (2026). https://arxiv.org/abs/2602.16481 (c18)
- [V] Mileva et al. (2025). https://arxiv.org/abs/2310.12309 (c19, c27)
- [M] https://arxiv.org/abs/2602.06260 (c21); https://arxiv.org/abs/2508.09759 (c22); https://arxiv.org/abs/2610.30349 (c23); https://arxiv.org/abs/2506.16383 (c24); https://arxiv.org/abs/2411.05639 (c25)
- [V] Castagna, Sassoon, Parsons (2024). https://arxiv.org/abs/2405.13036 (d07)
- [V] Jin et al. (2026) ARGORA. https://arxiv.org/abs/2601.21533 (d08, d09)
- [V] Choi, Zhu, Li (2025) Debate or Vote. https://arxiv.org/abs/2508.17536 (d10)
- [V] Shi et al. (2025) Judging the Judges. https://arxiv.org/abs/2406.07791 (d11)
- [V] Baba and Chudziak (2026). https://arxiv.org/abs/2610.27361 (d12)
- [V] ArgMed-Agents (2024). https://arxiv.org/abs/2403.06294 (d13)
- [V] Nguyen et al. (2026) Creative-MAD. https://aclanthology.org/2026.emnlp-main.2298 (d14)
- [V] Ajjour et al. (2026) ArgBench. https://aclanthology.org/2026.findings-acl.1099 (d15)
- [V] Own Monte Carlo simulation (this run). D:/research_scratch/D04.06/tmp/D04.06_sim.py (d17)
