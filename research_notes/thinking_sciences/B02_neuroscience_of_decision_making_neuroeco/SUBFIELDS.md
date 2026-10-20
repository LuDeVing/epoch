# Neuroscience of decision making (neuroeconomics): subfields

Neuroeconomics joins economics, psychology and neuroscience to ask how brains assign value, choose and learn. It divides by process: valuation, learning from reward, the choice rule, control between cached habit and planning, the trade-off between exploring and exploiting, the cost of mental effort, and confidence. Much of it is already written as algorithms (reinforcement learning, evidence accumulation, cost-benefit allocation), so several parts imply a procedure directly. The anatomy and drugs do not transfer.

## Subfields

| Subfield | What it studies | Key people or works | Useful for our agent | How |
|---|---|---|---|---|
| Valuation and common currency | One value scale for different options (ventromedial prefrontal cortex) | Montague, King-Casas and Cohen 2006; Sharot and Dolan 2011 | Low | Background only |
| Reward prediction error learning | Dopamine as a prediction-error signal in model-free learning | Doll, Simon and Daw 2012 [V] | Low | Background; learning is outside the loop |
| Model-based versus model-free control | Planned versus cached choice; arbitration by uncertainty or by time cost | Daw, Niv and Dayan 2005; Keramati, Dezfouli and Piray 2011; two-step task, Daw 2011 [V] | High | S0 gate: use planning only when its expected gain exceeds its cost |
| Habits versus goal-directed action | Devaluation tests; striatal lesions | Yin, Balleine, O'Doherty [V via review] | Low | Background only |
| Exploration and exploitation | Directed (information bonus) versus random exploration | Daw et al. 2006; Wilson et al. 2014; Sayfulina et al. 2020 (page returned 404) | High | S3 open mode, S6: assign untried directions as an information bonus |
| Expected value of control | Choosing whether, which and how strongly to apply effortful control: payoff minus effort cost, maximised | Shenhav, Botvinick and Cohen 2013 [V] | High | S0 and G11, G12: allocate thinking by expected payoff minus token cost |
| Evidence accumulation | Sample until a bound is reached | Ratcliff; Gold and Shadlen 2007 | High | Stopping rule for the number of attempts |
| Foraging and patch leaving | When to leave a depleting source | Kolling et al. 2012 | High | S6 trigger: leave an operator when yield falls below the average |
| Pruning of decision trees | Pavlovian bias cuts branches after losses | Huys et al. 2012 (cited in Doll [V]) | Med | Tree rules: prune after a bad first step |
| Confidence and metacognition | Reading one's own certainty | Fleming | Med | Use sample consistency, not self-report (SCHEMA 4b) |
| Risk, loss and social choice | Prospect theory in the brain | Tom et al. 2007 | Low | Background only |

## Dig into next

**1. Expected value of control (S0 gate).**
- EVC is: probability-weighted outcome value minus an effort cost that rises with intensity; the optimum is "just strong enough". Can the gate use pass probability by mode times reward minus tokens?
- Evidence needed: Shenhav et al. formal model [V], plain pass rate by class from our logs.

**2. Arbitration between direct and planned modes.**
- Daw 2005 gives control to the system with less uncertainty; Keramati 2011 uses a speed and accuracy trade-off, planning only if expected gain exceeds time cost. Which rule suits S0?
- Evidence needed: Doll review [V], our equal-token mode comparisons.

**3. Exploration, foraging and stopping.**
- What is the model-side analogue of the average reward rate for abandoning an operator?
- Does a directed bonus beat random re-sampling?
- Evidence needed: Wilson et al. horizon-task results, operator yield logs.

## Does not transfer

Dopamine, norepinephrine and acetylcholine roles, striatal and cingulate anatomy, lesion findings, stress effects and human risk attitudes are about brains. The Doll review itself says it identifies no specific neural arbitration mechanism and that many model-based signals may reflect fMRI limits. The algorithms transfer; the anatomy does not.

## Sources

[V] means the page was actually opened (fetched and read) this session. [M] means seen only in search results or from memory.

1. [V] Doll, Simon and Daw 2012, Current Opinion in Neurobiology https://pmc.ncbi.nlm.nih.gov/articles/PMC3513648
2. [V] Shenhav, Botvinick and Cohen 2013, expected value of control https://pmc.ncbi.nlm.nih.gov/articles/PMC3767969
3. [M] Sayfulina et al. 2020 (fetch returned 404) https://psyjournals.ru/en/jmfp/2020/n2/Sayfulina_et_al.shtml
4. [M] Montague, King-Casas and Cohen 2006 (search result) https://beam.vt.edu/content/dam/fbri_vtc_vt_edu/publications/montague-publications/2006_AnnualReviewofNeuroscience.pdf
5. [M] Sharot and Dolan review (secondhand blog) https://lesswrong.com/lw/8a7/review_of_sharot_dolan_neuroscience_of_preference
6. [M] Wilson et al. 2014 and Daw et al. 2006, exploration (no URL)
7. [M] Kolling et al. 2012, Science, foraging (no URL)
