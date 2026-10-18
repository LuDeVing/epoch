# task text pinning: keep the goal in the live window

The task text is the oldest message and the harness trims oldest first once the window passes 100k tokens, so after about 25 steps the agent often works without its goal [F4, F9, F22]. Nothing re-injects the goal, and the tried summariser shortened or dropped it in 6 of 10 cases [F14].

## Results

- Task moved into system prompt: preferred
- Agent restatement handshake: not_preferred
