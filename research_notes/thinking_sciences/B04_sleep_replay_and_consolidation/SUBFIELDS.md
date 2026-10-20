# Sleep, replay and consolidation: subfields

This field studies how memories are strengthened, moved, abstracted and pruned offline, mostly in sleep. It divides into accounts of consolidation (active systems consolidation and synaptic downscaling), methods that cue replay (targeted memory reactivation), sleep-stage roles (slow-wave versus REM), the neurochemistry of sleep, and computational theories linking replay to learning. For our agent only the computational idea transfers: an offline pass over stored experience can extract general rules and remove weak or irrelevant items. Sleep biology does not.

## Subfields

| Subfield | What it studies | Key people or works | Useful for our agent | How |
|---|---|---|---|---|
| Active systems consolidation | Hippocampus replays traces in slow-wave sleep and trains the cortex; memories become more schema-like | Diekelmann and Born 2010; Feld and Diekelmann 2015 [V] | High | Memory: an offline job turning episodes into rules |
| Synaptic homeostasis / downselection | Learning raises synaptic strength; sleep scales it down | Tononi and Cirelli [V] | Med | Memory: prune lessons |
| Relevance-based fate of memories | Whether a memory is strengthened or erased depends on its future relevance; reconciles the two accounts | Feld and Born 2019 [V] | High | Memory: keep or drop a lesson by expected future use |
| Targeted memory reactivation | Cues during sleep bias replay; effect depends on sleep state; mixed results for fear | Rasch et al. 2007 [V] | Low | Background; shows replay is causal |
| Slow-wave and REM roles | SWS strongest for declarative memory; REM less settled, more emotional | Marshall 2006; Ngo 2013; Payne 2008 [V] | Low | Background |
| Sleep and insight | Sleep roughly doubled insight performance in one study | Wagner et al. 2004 (cited in Wikipedia Insight [V]) | Low | Background; single study |
| Neurochemistry of sleep and memory | Glutamate, GABA, dopamine tagging, acetylcholine, cortisol | Feld and Born 2019 [V] | Low | Not relevant |
| Complementary learning systems | Fast hippocampal and slow cortical learners; interleaved replay prevents interference | McClelland, McNaughton and O'Reilly 1995 | High | Memory: test new lessons against old problems |
| Gist extraction by overlapping replay | Replay of overlapping memories extracts shared structure | Lewis and Durrant 2011 | High | Subgoal library: merge overlapping rules |
| Replay and wake-sleep learning in AI | Wake: solve tasks. Abstraction sleep: grow the library from solutions. Dreaming: train the search net on replays and fantasies | Ellis et al., DreamCoder [V abstract]; PLDI 2021 refactoring (search snippet) | High | Memory: a wake and sleep cycle for the subgoal library |

## Dig into next

**1. Wake and abstraction cycle for the subgoal library.**
- DreamCoder grows its library by finding fragments shared across solved tasks. Can a batch job do this for our logged solved subgoals and verify the merged rule on all of them?
- Evidence needed: full DreamCoder paper (only the abstract was opened), our subgoal records.

**2. Relevance-based keep and prune.**
- Feld and Born say future relevance decides strengthening versus erasure. What is a computable proxy (retrievals, successes in new problems)?
- Evidence needed: the Tononi and Cirelli papers, cache-eviction policies, retrieval logs.

**3. Interleaving.**
- Does testing a new lesson against old problems stop it from breaking earlier ones?
- Evidence needed: McClelland 1995 and Kumaran 2016 (not opened).

## Does not transfer

Sleep stages, spindles, ripples, odour and sound cueing, hormones, drugs, age effects and dreams are about brains. A model has no state between calls, so "sleeping on it" is not a mechanism; incubation by distraction failed to replicate in people too. The reviews note that REM evidence is conflicting, and that much of the human pharmacology comes from one lab and needs replication.

## Sources

[V] means the page was actually opened (fetched and read) this session. [M] means seen only in search results or from memory.

1. [V] Feld and Diekelmann 2015, Sleep smart https://pmc.ncbi.nlm.nih.gov/articles/PMC4428077/
2. [V] Feld and Born 2019, Neuropsychopharmacology https://pmc.ncbi.nlm.nih.gov/articles/PMC6879745
3. [V] DreamCoder, arXiv abstract page https://arxiv.org/abs/2006.08381
4. [M] DreamCoder PLDI 2021 paper (search result) https://people.csail.mit.edu/asolar/papers/EllisWNSMHCST21.pdf
5. [M] Lutz, Harkotte and Born 2025 review (search snippet only; no URL)
6. [M] McClelland et al. 1995; Lewis and Durrant 2011; Wagner et al. 2004 (no URL)
