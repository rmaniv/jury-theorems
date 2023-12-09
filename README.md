# jury-theorems

## jury.py

It implements the following equation:

$$ P = \sum_{r = \left\lceil \frac{n}{2} \right\rceil + 1}^{n} \binom{n}{r} p^r (1 - p)^{n-r} $$

In this equation:

- $P$ is the total probability of a correct majority decision.
- $n$ is the total number of voters.
- $p$ is the probability of an individual voter making a correct decision.
- $r$ is the number of voters making a correct decision, ranging from the majority $\left\lceil \frac{n}{2} \right\rceil + 1$, the smallest integer greater than half of $n$, to $n$ (all voters).
- $\binom{n}{r}$ is the binomial coefficient, representing the number of ways to choose $r$ successes out of $n$ trials.
- $p^r$ and $(1 - p)^{n-r}$ represent the probabilities of $r$ voters making a correct decision and $n-r$ voters making an incorrect decision, respectively.
