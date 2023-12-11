# jury-theorems

## Majority Vote

_jury.py_ can estimate the probability of reaching to a majority decision that is correct using a Monte Carlo simulation or the equivalent deterministic approach which does a summation of binomial probabilities for all combinations in which more voters are making the correct decision than not.

$$ P = \sum_{r = \left\lfloor \frac{n}{2} \right\rfloor + 1}^{n} \binom{n}{r} p^r (1 - p)^{n-r} $$

In this equation:

- $P$ is the total probability of a correct majority decision.
- $n$ is the total number of voters.
- $p$ is the probability of an individual voter making a correct decision.
- $r$ is the number of voters making a correct decision, ranging from the majority $\left\lfloor \frac{n}{2} \right\rfloor + 1$, the smallest integer greater than half of $n$, to $n$ (all voters).
- $\binom{n}{r}$ is the binomial coefficient, representing the number of ways to choose $r$ successes out of $n$ trials.
- $p^r$ and $(1 - p)^{n-r}$ represent the probabilities of $r$ voters making a correct decision and $n-r$ voters making an incorrect decision, respectively.

## Theorems

> Jury theorems are interested in the probability of correctness - the probability that the majority decision coincides with the objective truth. Typical jury theorems make two kinds of claims on this probability:
>
> 1. *Growing Reliability*: the probability of correctness is larger when the group is larger.
> 2. *Crowd Infallibility*: the probability of correctness goes to 1 when the group size goes to infinity.
>
> Claim 1 is often called the non-asymptotic part and claim 2 is often called the asymptotic part of the jury theorem.
>
>Obviously, these claims are not always true, but they are true under certain assumptions on the voters. Different jury theorems make different assumptions. 

[Source: Wikipedia](https://en.wikipedia.org/wiki/Jury_theorem)

### Condorcet's Jury Theorem

> Condorcet's jury theorem makes the following three assumptions:
>
> 1. *Unconditional Independence*: the voters make up their minds independently. In other words, their opinions are independent random variables.
> 2. *Unconditional Competence*: the probability that the opinion of a single voter coincides with the objective truth is larger than 1/2 (i.e., the voter is smarter than a random coin-toss).
> 3. *Uniformity*: all voters have the same probability of being correct.
>
>The jury theorem of Condorcet says that these three assumptions imply Growing Reliability and Crowd Infallibility.

[Source: Wikipedia](https://en.wikipedia.org/wiki/Jury_theorem)

The `condorcet` function in _theorems.py_ plots probability of correct majority decision against the probability of correctness for an indedependent voter. One can use either the deterministic approach or the Monte Carlo simulation. The Monte Carlo simulation is, for obvious reasons, is always slower than the deterministic approach for any reasonable accuracy and increasingly slow for more accurate plots.

<p align="center">
  <img src="https://github.com/vinamrsachdeva/jury-theorems/blob/main/condorcet.png" width="48%" />
  <img src="https://github.com/vinamrsachdeva/jury-theorems/blob/main/condorcet_montecarlo.png" width="48%" /> 
</p>
<p align="center" style="color: gray; font-weight: lighter;">
  Figure: Condorcet Jury Theorem plots with the deterministic approach (left) and Monte Carlo Simulation (right).
</p>
