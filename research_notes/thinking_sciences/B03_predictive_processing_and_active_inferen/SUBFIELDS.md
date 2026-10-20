# Predictive processing and active inference: subfields

Predictive processing says the brain keeps a model of the world, predicts its inputs and learns from errors. Active inference adds action: an agent acts to make predictions come true and to reduce uncertainty. The field divides into predictive coding (a testable process theory), the free energy principle (a general mathematical principle), the decision theory built on it, applications in AI, and philosophy. The free energy principle is contested as unfalsifiable. Only the decision-theory part gives a clear procedure for an agent, and much of that overlaps with older ideas such as Bayesian experimental design.

## Subfields

| Subfield | What it studies | Key people or works | Useful for our agent | How |
|---|---|---|---|---|
| Hierarchical predictive coding | Predictions flow down, errors flow up; a process theory that can be tested | Mumford; Rao and Ballard; Wikipedia FEP page [V] | Low | Background only |
| Free energy principle | A normative principle: systems act as if minimising surprise | Friston; criticism by Aguilera, Colombo and Palacios [V] | Low | Background; Friston calls it unfalsifiable, only process theories are tested |
| Active inference decision theory | Pick policies by expected free energy: pragmatic plus epistemic value | Friston et al. 2015 (not opened); arXiv 1909.10863 abstract [V] | Med | S7 select: choose the test that most separates hypotheses (equals expected information gain) |
| Active inference versus reinforcement learning | Reward treated as another observation; compared with Q-learning and Bayesian model-based RL on OpenAI Gym, including reward-free tasks | Sajid et al., arXiv 1909.10863 [V] | Med | Background for exploration without reward (open mode) |
| Epistemic value and curiosity | Explore until information gain runs out, then exploit | Friston et al. 2015 and 2017 (search snippets) | Med | S3 open mode and the explore-to-exploit switch; unconfirmed by opened source |
| Structure learning and model reduction | Learning model structure; pruning redundant parameters | Friston et al. 2017 (snippet) | Low | Memory pruning idea; see B04 |
| Precision weighting and attention | Weighting errors by reliability; dopamine as precision | Wikipedia Active inference [V] | Low | Code-side evidence weighting only |
| Link to variational methods | Negative free energy equals the evidence lower bound used for variational autoencoders | Wikipedia Active inference [V]; Dayan, Hinton, Neal, Zemel | Low | Background |
| Philosophy and interoception | What predictive models imply for mind and emotion | Clark; Hohwy; Seth | Low | Not relevant |

## Dig into next

**1. Expected-information-gain test selection.**
- Can S7 compute, for each candidate input, how evenly it splits the live hypotheses by their executable outputs, and pick the best?
- Is the free energy language needed, or is plain experimental design enough?
- Evidence needed: Friston 2015 (open the paper), Bayesian experimental design texts, ARC items where two programs fit.

**2. Explore-to-exploit switch.**
- Is there a code rule that moves from open exploration to exploitation when new attempts stop adding information?
- Evidence needed: the 2015 epistemic value paper, bandit results, our diversity-versus-accuracy logs.

**3. Reward-free exploration.**
- Do the Gym comparisons show an advantage in tasks without a reward signal, as open mode has none?
- Evidence needed: full text of arXiv 1909.10863 (the PDF fetch was unreadable).

## Does not transfer

Cortical layers, dopamine and precision, the claim that living systems minimise free energy, interoception and emotion are about brains or are physics claims. The Wikipedia pages did not discuss expected free energy or epistemic value at all, and flagged the claim that all Bayesian inference is free energy minimisation as failing verification. An LLM already predicts, so "the brain predicts" adds little.

## Sources

[V] means the page was actually opened (fetched and read) this session. [M] means seen only in search results or from memory.

1. [V] Free energy principle, Wikipedia https://en.wikipedia.org/wiki/Free_energy_principle
2. [V] Active inference, Wikipedia https://en.wikipedia.org/wiki/Active_inference
3. [V] arXiv 1909.10863 abstract page https://arxiv.org/abs/1909.10863
4. [M] Active inference and epistemic value, Friston et al. 2015 (search result) https://www.fil.ion.ucl.ac.uk/~karl/Active%20inference%20and%20epistemic%20value.pdf
5. [M] Friston et al., Active inference, curiosity and insight (search result) https://discovery-pp.ucl.ac.uk/id/eprint/1570070/1/Friston_Active%20Inference%20Curiosity%20and%20Insight.pdf
6. [M] arXiv 2602.06029, curiosity coefficient (search snippet) https://arxiv.org/abs/2602.06029v1
