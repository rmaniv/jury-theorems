# jury-theorems

> Jury theorems are interested in the probability of correctness - the probability that the majority decision coincides with the objective truth. Typical jury theorems make two kinds of claims on this probability:
>
> 1. *Growing Reliability*: the probability of correctness is larger when the group is larger.
> 2. *Crowd Infallibility*: the probability of correctness goes to 1 when the group size goes to infinity.
>
> Claim 1 is often called the non-asymptotic part and claim 2 is often called the asymptotic part of the jury theorem.
>
>Obviously, these claims are not always true, but they are true under certain assumptions on the voters. Different jury theorems make different assumptions. 

[Source: Wikipedia](https://en.wikipedia.org/wiki/Jury_theorem)

## Condorcet's Jury Theorem (CJT)

> Condorcet's jury theorem makes the following three assumptions:
>
> 1. *Unconditional Independence*: the voters make up their minds independently. In other words, their opinions are independent random variables.
> 2. *Unconditional Competence*: the probability that the opinion of a single voter coincides with the objective truth is larger than 1/2 (i.e., the voter is smarter than a random coin-toss).
> 3. *Uniformity*: all voters have the same probability of being correct.
>
>The jury theorem of Condorcet says that these three assumptions imply Growing Reliability and Crowd Infallibility.

[Source: Wikipedia](https://en.wikipedia.org/wiki/Jury_theorem)

In the `theorems` package, `condorcet.py` simulates the CJT.

- The `montecalro` function estimates the probability of reaching a majority decision that is correct using a vectorized implementation of the Monte Carlo simulation. It performs 1 million trials and counts the of trials in which the majority reached the correct decision.

- The `deterministic` function performs a summation of binomial probabilities for all combinations in which more voters are making the correct decision than not.

<table>
  <tr>
    
$$ P = \sum_{r = \left\lfloor \frac{n}{2} \right\rfloor + 1}^{n} \binom{n}{r} p^r (1 - p)^{n-r} $$
  
  In this equation:
  
  - $P$ is the total probability of a correct majority decision.
  -  $n$ is the total number of voters.
  -  $p$ is the probability of an individual voter making a correct decision.
  -  $r$ is the number of voters making a correct decision, ranging from the majority $\left\lfloor \frac{n}{2} \right\rfloor + 1$, the smallest integer greater than half of $n$, to $n$ (all voters).
  -  $\binom{n}{r}$ is the binomial coefficient, representing the number of ways to choose $r$ successes out of $n$ trials.
  -  $p^r$ and $(1 - p)^{n-r}$ represent the probabilities of $r$ voters making a correct decision and $n-r$ voters making an incorrect decision, respectively.
  </tr>
</table>
  
- The `plot` function generates a graph of the probability of a correct majority decision as a function of an independent voter's probability of being correct. Users have the option to employ either the Monte Carlo simulation or the deterministic approach.

<p align="center">
  <img src="https://github.com/vinamrsachdeva/jury-theorems/blob/main/sim_results/condorcet/condorcet_montecarlo.png" width="48%" />
  <img src="https://github.com/vinamrsachdeva/jury-theorems/blob/main/sim_results/condorcet/condorcet.png" width="48%" /> 
</p>
<p align="center" style="color: gray; font-weight: lighter;">
  Figure: Condorcet Jury Theorem plots with the Monte Carlo simulation (left) and the deterministic approach (right).
</p>

[View `condorcet.py`](https://github.com/vinamrsachdeva/jury-theorems/blob/main/theorems/condorcet.py)

A summary of other jury theorems which mainly differ on the independence and uniformity assumptions (from [Wikipedia](https://en.wikipedia.org/wiki/Jury_theorem)):

## Correlated votes

- Growing infallibility might not hold if votes are correlated (weakening the unconditional independence claim). https://doi.org/10.1007%2Fs11238-009-9170-2
- Growing reliability and crowd infallibility hold under conditional independence, competence and uniformity. https://plato.stanford.edu/entries/jury-theorems/#PartSoluCondJuryTheo
- Crowd infallibility holds if the probability of following the opinion leader is less than 1-1/2p (where p is the competence level of all voters). https://doi.org/10.2307%2F3214318
- Growing reliability holds but the asymptote is below a probability of 1 under conditional independence, "tendency to competence," and conditional uniformity. Tendency to competence: "for each voter, and for each r>0, the probability that p(x) = 1/2+r is at least as large as the probability that p(x) = 1/2-r." (from wiki) https://doi.org/10.1017%2FS0266267113000096
- Crowd infallibility holds because the average covariance between voters becomes small as the population becomes large. https://doi.org/10.1016%2Fj.jmateco.2017.06.001

## Diverse Capabilities

to be added...

*Stay tuned! I'm actively working on expanding this repository with more jury theorems.*
